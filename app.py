import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route("/")
@cross_origin()
def hello():
    return jsonify({"name":"Analisi y Diseño 1",
                    "estudiante1":"Erick Alexander Alvarado Guerra - 201800546 - Practica 1 - Grupo 2",
                    "estudiante2":"Luis Fernando Culajay Sandoval - 201903838 - Practica 1 - Grupo 2",
                    "estudiante3":"Luis Felipe Delgado Benitez - 201900051 - Practica 1 - Grupo 2"
                    })

if __name__ == '__main__':
    app.run(port=3000, debug=True)