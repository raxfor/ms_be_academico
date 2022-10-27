from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve
import json
app = Flask(__name__)

cors = CORS(app)

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