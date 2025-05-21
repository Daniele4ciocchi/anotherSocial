from flask import Flask, request, jsonify 

app = Flask(__name__)

@app.route('/saluta', methods=['GET'])
def saluta():
    return jsonify({"messaggio": "Ciao dal backend in Python!"})

@app.route('/somma', methods=['POST'])
def somma():
    dati = request.get_json()
    a = dati.get('a', 0)
    b = dati.get('b', 0)
    risultato = a + b
    return jsonify({"somma": risultato})

if __name__ == '__main__':
    app.run(debug=True)
