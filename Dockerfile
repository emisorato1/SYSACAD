FROM python:3.12.10-bookworm

ENV FLASK_CONTEXT=production
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/sysacad/.local/bin

RUN useradd --create-home --home-dir /home/sysacad sysacad
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		python3-dev build-essential libpq-dev python3-psycopg2 \
		curl htop iputils-ping \
		# Dependencias runtime para WeasyPrint/GTK/Cairo/Pango
		libglib2.0-0 libgdk-pixbuf2.0-0 libgtk-3-0 \
		libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libpangoft2-1.0-0 \
		libffi-dev shared-mime-info \
		libxml2 libxslt1.1 \
		libjpeg62-turbo zlib1g \
		libfreetype6 libharfbuzz0b libfribidi0 \
		fonts-liberation fonts-dejavu fonts-freefont-ttf \
		libcairo-gobject2 \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /home/sysacad

USER sysacad
RUN mkdir app

COPY ./app ./app
COPY ./app.py .
COPY ./migrations ./migrations

ADD requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "./app.py" ]