from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from Model import WeatherModel  # Asegúrate de que el archivo se llame Model.py

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar Flask usando las variables de entorno
app.config['DEBUG'] = os.getenv('FLASK_DEBUG') == 'True'

# Instanciar el modelo del clima
weather_model = WeatherModel()

# Definir rutas (endpoints)
@app.route("/")
def home():
    """Ruta principal que retorna un mensaje de bienvenida"""
    return jsonify({
        "mensaje": "¡Bienvenido a mi primer servicio web con Flask!",
        "status": "success"
    })

@app.route("/saludo/<nombre>")
def saludo(nombre):
    """
    Ruta que retorna un saludo personalizado
    
    Args:
        nombre (str): Nombre de la persona a saludar
    """
    return jsonify({
        "mensaje": f"¡Hola, {nombre}! Bienvenido al servicio web con Flask.",
        "status": "success"
    })

@app.route("/clima/<ciudad>")
def clima(ciudad):
    """
    Ruta que retorna los datos del clima para una ciudad específica
    
    Args:
        ciudad (str): Nombre de la ciudad
    """
    weather_data = weather_model.get_weather(ciudad)
    if weather_data:
        return jsonify({
            "mensaje": "Datos del clima obtenidos exitosamente.",
            "status": "success",
            "data": weather_data
        })
    else:
        return jsonify({
            "mensaje": "No se pudo obtener datos del clima para la ciudad especificada.",
            "status": "error"
        }), 404

@app.errorhandler(404)
def not_found(error):
    """Manejador para errores 404"""
    return jsonify({
        "mensaje": "Ruta no encontrada",
        "status": "error"
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Manejador para errores 500"""
    return jsonify({
        "mensaje": "Error interno del servidor",
        "status": "error"
    }), 500

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run()
