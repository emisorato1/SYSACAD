from flask import Blueprint, jsonify, send_file
from app.services.servicio_ficha_alumno import ServicioFichaAlumno

ficha_alumno_bp = Blueprint('ficha_alumno', __name__)

@ficha_alumno_bp.route('/ficha-alumno/<int:id>/json', methods=['GET'])
def obtener_ficha_json(id: int):
    ficha = ServicioFichaAlumno.obtener_ficha_alumno_json(id)
    if not ficha:
        return jsonify({"error": "Alumno no encontrado"}), 404
    return jsonify(ficha), 200

@ficha_alumno_bp.route('/ficha-alumno/<int:id>/pdf', methods=['GET'])
def obtener_ficha_pdf(id: int):
    pdf_io = ServicioFichaAlumno.generar_ficha_alumno_pdf(id)
    if not pdf_io:
        return jsonify({"error": "Alumno no encontrado"}), 404
    
    return send_file(
        pdf_io,
        mimetype='application/pdf',
        as_attachment=False,
        download_name=f"ficha_alumno_{id}.pdf"
    )
