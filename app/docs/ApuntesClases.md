
# CLASE 30/04/2025

# Base de dato con postgreSQL
services:
    postgresql:

        container_name: postgresql-servidor
        image: postgres:15.4-bullseye
        
        ports:
          - "5432:5432"

        networks:
          - mired
        
        environment:
          - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
          - POSTGRES_DB=${POSTGRES_DB}
          - POSTRGRES_USER=${POSTGRES_USER}
          - PGDATA=/var/lib/postgresql/data/pgdata  ###-esto es donde se va a guardar esta base de datos-###
        
        volumes:  
          - ./data:/var/lib/postgresql/data
          - ./sql:/docker-entrypoint-initdb.d

        restart: always
networks:
    mired:
        external: true


# 12 Factores de una app

Twelve Factors

I. Código base (Codebase)
Un código base sobre el que hacer el control de versiones y multiples despliegues

II. Dependencias
Declarar y aislar explícitamente las dependencias

III. Configuraciones
Guardar la configuración en el entorno

IV. Backing services
Tratar a los “backing services” como recursos conectables

V. Construir, desplegar, ejecutar
Separar completamente la etapa de construcción de la etapa de ejecución

VI. Procesos
Ejecutar la aplicación como uno o más procesos sin estado

VII. Asignación de puertos
Publicar servicios mediante asignación de puertos

VIII. Concurrencia
Escalar mediante el modelo de procesos

IX. Desechabilidad
Hacer el sistema más robusto intentando conseguir inicios rápidos y finalizaciones seguras

X. Paridad en desarrollo y producción
Mantener desarrollo, preproducción y producción tan parecidos como sea posible

XI. Historiales
Tratar los historiales como una transmisión de eventos

XII. Administración de procesos
Ejecutar las tareas de gestión/administración como procesos que solo se ejecutan una vez