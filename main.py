from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
import json
app = Flask(__name__)

cors = CORS(app)

from Controladores.ControladorEstudiante import ControladorEstudiante

miControladorEstudiante = ControladorEstudiante()

# Rutas Estudiante
@app.route("/estudiante", methods=["GET"])
def mostrarEstudiante():
    json = miControladorEstudiante.mostrar()
    return jsonify(json)

@app.route("/estudiante", methods=["POST"])
def crearEstudiantes():
    data = request.get_json()
    json = miControladorEstudiante.crear(data)
    return jsonify(json)

@app.route("/estudiante/<string:id>", methods=["GET"])
def consultarEstudiante(id):
    json = miControladorEstudiante.consultar(id)
    return jsonify(json)

@app.route("/estudiante/<string:id>", methods=["PUT"])
def actualizarEstudiante(id):
    data = request.get_json()
    json = miControladorEstudiante.actualizar(id, data)
    return jsonify(json)

@app.route("/estudiante/<string:id>", methods=["DELETE"])
def eliminarEstudiante(id):
    json = miControladorEstudiante.eliminar(id)
    return jsonify(json)



def loadFileConfig():
    with open("config.json") as f:
        data = json.load(f)
    return data

@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"]= "Serve Running ..."
    return jsonify(json)





if __name__ == "__main__":
    dataConfig = loadFileConfig()
    print("Serve: http://{}:{}".format(dataConfig["url-backend"], dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])