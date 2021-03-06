import json
import hashlib
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
    print(num)
    try:
        if int(num) % 2 == 0:
            return jsonify({"resultado":"Par"})
        else:
            return jsonify({"resultado":"Impar"})
    except Exception:
        return jsonify({"resultado":"Solo se aceptan datos numericos"})

    

@app.route('/fibo', methods=['POST'])
@cross_origin()
def fibo():
    num = request.json['fibo']
    if (num > 0 ):
        return {
            "fibo": fibonacci(num)
        }
    return {
        "fibo": 0
    }

@app.route('/alreves/palabra:<string:word>', methods=["GET"])
@cross_origin()
def alreves(word):

    return {'resultado' : word.upper() + ": " + word[::-1] + ": " + hashlib.sha256(word[::-1].encode()).hexdigest()}

@app.route("/raiz", methods=["GET"])
@cross_origin()
def raiz(): 
    numero = (int)(request.args.get("num",0))
    result = 0
    if numero < -1:
        numero = abs(numero)
        result = (numero**(1/3))*-1
    else:
        result = numero**(1/3) 
    return jsonify({"resultado": result})


@app.route("/potencia", methods=["GET"])
@cross_origin()
def potencia(): 
    numero = (int)(request.args.get("num",0))
    result = numero ** 3
    return jsonify({"resultado": result})

@app.route('/multiplicacion', methods=['POST'])
@cross_origin()
def multiplicacion():
    num1 = request.json['num1']
    num2 = request.json['num2']
    try:
        return jsonify({"resultado":num1*num2})
    except Exception:
        return jsonify({"resultados":"Solo se aceptan datos numericos"})

@app.route('/division', methods=['POST'])
@cross_origin()
def division():
    num1 = request.json['num1']
    num2 = request.json['num2']
    try:
        return jsonify({"resultado": int(num1)/int(num2)})
    except Exception:
        return jsonify({"resultados":"Solo se aceptan datos numericos cambio c alificacion"})

if __name__ == '__main__':
    app.run(port=3000, debug=True)