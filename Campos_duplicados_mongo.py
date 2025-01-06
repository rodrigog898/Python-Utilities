from pymongo import MongoClient

# Conectar a la base de datos MongoDB
client = MongoClient("url_mongo")  # Cambia la URL según tu configuración
db = client["DB-NAME"]  # Reemplaza con el nombre de tu base de datos
collection = db["PERSON"]  # Reemplaza con el nombre de tu colección

# Pipeline para agrupar por 'correo_persona' y contar cuántas veces se repite
pipeline = [
    {"$group": {"_id": "$correo_persona", "count": {"$sum": 1}}},
    {"$match": {"count": {"$gt": 1}}}  # Solo mostrar los correos que se repiten
]

# Ejecutar el pipeline
correos_repetidos = list(collection.aggregate(pipeline))

# Mostrar los correos repetidos
for correo in correos_repetidos:
    print(f"Correo: {correo['_id']} - Se repite {correo['count']} veces")
