import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n

@app.route("/")
@cross_origin()
def hello():
    return jsonify({"name":"Analisi y Diseño 1",
                    "estudiante1":"Erick Alexander Alvarado Guerra - 201800546 - Practica 1 - Grupo 2",
                    "estudiante2":"Luis Fernando Culajay Sandoval - 201903838 - Practica 1 - Grupo 2",
                    "estudiante3":"Luis Felipe Delgado Benitez - 201900051 - Practica 1 - Grupo 2",
                    "estudiante4":"Joel Estuardo Rodríguez Santos - 201115018 - Practica 1 - Grupo 2",
                    "estudiante5":"Cesar Leonel Chamale Sican - 201700634 - Practica 1 - Grupo 2"
                    })
                    
@app.route('/paroimpar', methods=['POST'])
@cross_origin()
def paroimpar():
    num = request.json['num']
    if num % 2 == 0:
        return jsonify({"resultado":"Par"})
    else:
        return jsonify({"resultado":"Impar"})

@app.route('/fibo', methods=['POST'])
@cross_origin()
def fibo():
    return {
        "fibo": fibonacci(request.json['fibo'])
    }


if __name__ == '__main__':
    app.run(port=3000, debug=True)