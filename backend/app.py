from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS  # Asegúrate de que CORS está importado

app = Flask(__name__)

# Habilitar CORS para permitir solicitudes desde el frontend (localhost:3000)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Configuración de MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/urban_insight_data"
mongo = PyMongo(app)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    # Recuperar los restaurantes desde MongoDB
    restaurants = mongo.db.restaurants.find()
    response = []
    for restaurant in restaurants:
        response.append({
            'Nombre': restaurant.get('Nombre'),
            'Tipo': restaurant.get('Tipo'),
            'Nota': restaurant.get('Nota'),
            'Nº Reseñas': restaurant.get('Nº Reseñas'),
            'Accesibilidad': restaurant.get('Accesibilidad'),
            'Barrio': restaurant.get('Barrio'),
            'Dirección': restaurant.get('Dirección'),
            'Coordinates': restaurant.get('Geometry', {}).get('coordinates', [])
        })
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
