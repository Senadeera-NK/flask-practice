from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/static/uploaded files'
app.config['ALLOWED_EXTENSIONS'] = ['.txt','.pdf','docs','docx']

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/success', methods=['GET','POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
  return render_template('success.html', name=file.filename)  
