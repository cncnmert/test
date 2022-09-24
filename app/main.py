import os
import string
import pytesseract
from pdf2image import convert_from_path
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Vocab API"

@app.route('/content/<string:file_name>', methods=['GET'])
def File_Content(file_name):
    file_str = ''

    if file_name.endswith('.pdf'):
        pdf_file = convert_from_path(file_name)

        for i in range(len(pdf_file)):
            pdf_file[i].save(f'page{str(i + 1)}.jpg', 'JPEG')
            file = f'page{str(i + 1)}.jpg'
            file_str += pytesseract.image_to_string(file)
    elif file_name.endswith(('.jpg', '.png')):
        file_str = pytesseract.image_to_string(file_name)

    return file_str