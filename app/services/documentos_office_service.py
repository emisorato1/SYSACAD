from abc import ABC, abstractmethod
from io import BytesIO
import os
from flask import current_app, render_template
from python_odt_template import ODTTemplate
from weasyprint import HTML
from python_odt_template.jinja import get_odt_renderer
from docxtpl import DocxTemplate
import jinja2


class Document(ABC):
    @staticmethod
    @abstractmethod
    def generar(carpeta: str, plantilla: str, context: dict) -> BytesIO:
        """Generar un documento y devolver un BytesIO"""
        pass


class PDFDocument(Document):
    @staticmethod
    # pyrefly: ignore  # bad-override
    def generar(carpeta: str, plantilla: str, context: dict) -> BytesIO:
        # Construir base_url file:/// para que WeasyPrint pueda abrir archivos locales
        base_path = current_app.root_path.replace('\\', '/')
        base_url = f"file:///{base_path}"

        render_context = dict(context or {})
        render_context.update({"url_base": base_url})

        html_string = render_template(f"{carpeta}/{plantilla}.html", **render_context)
        bytes_data = HTML(string=html_string, base_url=base_url).write_pdf()
        pdf_io = BytesIO(bytes_data)
        return pdf_io


class ODTDocument(Document):
    @staticmethod
    # pyrefly: ignore  # bad-override
    def generar(carpeta: str, plantilla: str, context: dict) -> BytesIO:
        """Genera un ODT usando python-odt-template. Busca plantillas en current_app.template_folder.
        Usa current_app.static_folder como media_path para que las imágenes en static sean accesibles."""
        templates_root = os.path.join(current_app.root_path, current_app.template_folder)
        path_template = os.path.join(templates_root, carpeta, f"{plantilla}.odt")

        # media path para que el renderer encuentre imágenes dentro de static
        media_path = current_app.static_folder
        odt_renderer = get_odt_renderer(media_path=media_path)

        odt_io = BytesIO()
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.odt', delete=False) as temp_file:
            temp_path = temp_file.name

        with ODTTemplate(path_template) as template:
            odt_renderer.render(template, context=context)
            template.pack(temp_path)
            with open(temp_path, 'rb') as f:
                odt_io.write(f.read())

        os.unlink(temp_path)
        odt_io.seek(0)
        return odt_io


class DOCXDocument(Document):
    @staticmethod
    # pyrefly: ignore  # bad-override
    def generar(carpeta: str, plantilla: str, context: dict) -> BytesIO:
        """Genera un DOCX usando docxtpl. Busca plantillas en current_app.template_folder.
        Pone en el contexto url_base file:/// para que plantillas puedan resolver imágenes locales si es necesario."""
        templates_root = os.path.join(current_app.root_path, current_app.template_folder)
        path_template = os.path.join(templates_root, carpeta, f"{plantilla}.docx")

        doc = DocxTemplate(path_template)

        docx_io = BytesIO()
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as temp_file:
            temp_path = temp_file.name

        jinja_env = jinja2.Environment()
        render_context = dict(context or {})
        base_path = current_app.root_path.replace('\\', '/')
        render_context.update({"url_base": "file:///" + base_path})

        doc.render(render_context, jinja_env)
        doc.save(temp_path)
        with open(temp_path, 'rb') as f:
            docx_io.write(f.read())

        os.unlink(temp_path)
        docx_io.seek(0)
        return docx_io


def obtener_tipo_documento(tipo: str) -> Document:
    tipos = {
        'pdf': PDFDocument,
        'odt': ODTDocument,
        'docx': DOCXDocument,
    }
    return tipos.get(tipo)
