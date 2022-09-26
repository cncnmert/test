import os
import string
import pytesseract
from pdf2image import convert_from_path
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Vocab API test"

@app.route('/<string:file_name>', methods=['GET'])
def File_Content(file_name):
    return jsonify({'File Content': pytesseract.image_to_string(file_name)})