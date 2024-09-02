# a simple Flask server

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/status', methods=['GET'])
def hello():
    return "Hello Vue JS!\n"


@app.route('/hello', methods=['GET'])
def hello2():
    return jsonify({'message': 'Hello My Friend!'})

@app.route('/upload', methods=['POST'])
def upload():
    print(request.files)
    file = request.files['file']
    file.save(file.filename)
    return jsonify({'message': 'success'})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)