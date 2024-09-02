# a simple Flask server

from flask import Flask, request, redirect, url_for, render_template, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

    # Limit the allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt', 'docx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/status', methods=['GET'])
def hello():
    return "Hello Vue JS!\n"


@app.route('/hello', methods=['GET'])
def hello2():
    return jsonify({'message': 'Hello My Friend!'})

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files part in the request'}), 400
    
    files = request.files.getlist('files[]')

    saved_files = []
    for file in files:
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            continue
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            saved_files.append(filename)

    if saved_files:
        return jsonify({'message': 'Files successfully uploaded', 'files': saved_files}), 200
    else:
        return jsonify({'error': 'No valid files were uploaded'}), 400

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)