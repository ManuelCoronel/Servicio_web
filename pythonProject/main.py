from flask import Flask,jsonify
from flask import request
import json
from  persona import Persona
from personaDatabase import Database

app = Flask(__name__)



@app.route("/",methods=['GET'])
def index():
    personaDb = Database()
    grupoPersonas = personaDb.select_all_user()
    grupo = []
    for p in grupoPersonas :
        grupo.append((Persona(p[0],p[1],p[2],p[3]).__dict__))
    return json.dumps(grupo)


@app.route("/Persona",methods=['GET'])
def index2():
    cedula = request.args.get("cedula")
    personaDb = Database()
    p = personaDb.select_user(cedula)
    return json.dumps(Persona(p[0], p[1], p[2], p[3]).__dict__)

@app.route("/",methods=['POST'])
def index3():
    print(request.get_json())
    json = request.get_json()
    personaDb = Database()
    personaDb.insert_user(json["cedula"],json["nombre"],json["edad"],json["pais"])
    return "Insertado"

@app.route("/",methods=['DELETE'])
def index4():
    
    cedula = request.args.get("cedula")
    personaDb = Database()
    personaDb.delete_user(cedula)
    return "Eliminado"

@app.route("/",methods=['PUT'])
def index5():
    print(request.get_json())
    json = request.get_json()
    personaDb = Database()
    personaDb.update_user(json["cedula"],json["nombre"],json["edad"],json["pais"])
    return "Actualizado"



if __name__=="__main__":
    app.run(debug=True)






