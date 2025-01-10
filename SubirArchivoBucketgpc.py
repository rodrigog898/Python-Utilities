import os
from google.cloud import storage, secretmanager
from flask import Request, make_response, jsonify
from pymongo import MongoClient
from datetime import datetime

def get_secret():
    client = secretmanager.SecretManagerServiceClient()
    name = "projects/{secretro_id}/secrets/{nombre_secreto}/versions/latest"
    response = client.access_secret_version(name=name)
    secret_string = response.payload.data.decode('UTF-8')
    return secret_string

mongos_url = get_secret()

def upload_blob(request: Request):
    print(mongos_url)
    mongo_url = mongos_url
    client = MongoClient(mongo_url)
    db = client['cv_runner']
    coleccion_log = db['log_person_upload']  # Colección donde se guardará la información del upload

    key_provided = request.form.get('mail')

    # Validación del correo
    if key_provided and key_provided.endswith('@api-ux.com'):
        if request.method == 'OPTIONS':
            headers = {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Max-Age': '3600'
            }
            return ('', 204, headers)

        content_type = request.headers.get('Content-Type')

        if not content_type:
            return make_response(jsonify(error='Missing Content-Type header'), 400, {'Access-Control-Allow-Origin': '*'})

        if content_type.startswith('multipart/form-data'):
            file = request.files.get('file')
        else:
            return make_response(jsonify(error='Unsupported Content-Type'), 400, {'Access-Control-Allow-Origin': '*'})

        if not file:
            return make_response(jsonify(error='Missing file'), 400, {'Access-Control-Allow-Origin': '*'})

        # Parámetros fijos
        bucket_name = 'cv_runner'
        # Se genera el nombre del archivo de manera dinámica manteniendo su nombre original dentro de 'cv-origen/'
        destination_blob_name = f'cv-origen/{file.filename}'

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)

        existing_blob = bucket.blob(destination_blob_name)
        if existing_blob.exists():
            return make_response(jsonify(error=f'El archivo {destination_blob_name} ya existe en el bucket {bucket_name}.'), 409, {'Access-Control-Allow-Origin': '*'})

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_string(file.read(), content_type=file.content_type)

        # Guardar información del upload en MongoDB
        upload_data = {
            'correo': key_provided,
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'nombre_documento': destination_blob_name
        }
        coleccion_log.insert_one(upload_data)

        headers = {
            'Access-Control-Allow-Origin': '*'
        }

        response = make_response(jsonify(message=f'File {destination_blob_name} uploaded to {bucket_name}.'), 200, headers)
        return response
    else:
        return make_response(jsonify(error='Clave no encontrada o no coincide'), 404, {'Access-Control-Allow-Origin': '*'})
