from flask import Flask, jsonify
import requests

#Levantamiento de API
app = Flask(__name__)

#Endpoint Listar pokemons por su tipo(fuego, agua, hierro...)

@app.route("/pokemon/type/<name>", methods=["GET"])
def pokemon_type(name):
    pokemon_type_url = f"https://pokeapi.co/api/v2/type/{name}"
    response = requests.get(pokemon_type_url)
    
    if response.status_code == 200:
        type_data = response.json()
        return jsonify({"name": type_data["name"], "pokemon": [p["pokemon"]["name"] for p in type_data["pokemon"]]})
    else:
        return jsonify({"error": "Pokemon type not found"}), 404

#Endpoint Listar tipo de Pokemon por su nombre nombre

@app.route("/pokemon/<string:name>")
def get_pokemon_type(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    r = requests.get(url)
    if r.status_code == 200:
        pokemon = r.json()
        types = [pokemon_type["type"]["name"] for pokemon_type in pokemon["types"]]
        return jsonify({"name": pokemon["name"], "types": types})
    else:
        return jsonify({"error": "Pokemon not found"}), 404
    
#Correr la aplicación por puerto 5000 con debug activado
if __name__ == "__main__":
    app.run(debug=True, port=5000)
