from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "hola, soy grecia. ya ahora si funciona!!! :)"})

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=3000)
