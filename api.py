from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import pytesseract
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'hello world'})

@app.route('/date', methods=['GET'])
def get_date():
    result = subprocess.check_output(['date']).decode('utf-8')
    return jsonify({'message': result.strip()})

@app.route('/languages', methods=['GET'])
def get_languages():
    return jsonify({'message': pytesseract.get_languages(config='')})

@app.route('/itt', methods=['POST'])
def itt():
    file = request.files['file']
    image = Image.open(file.stream)
    result = pytesseract.image_to_string(image, lang='slk')

    return jsonify({'message': result})

if __name__ == '__main__':
    app.run()