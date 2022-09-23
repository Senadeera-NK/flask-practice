import os
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.txt','.docs',',docx','.pdf']
app.config['UPLOAD_PATH'] = '/statics/uploaded files'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/success', methods=['GET','POST'])
def upload_files():
  uploaded_file = request.files['file']
  filename = secure_filename(uploaded_file.filename)
  if filename != '':
    file_ext = os.path.splitext(filename)[1]
    if file_ext not in app.config['UPLOAD_EXTENSIONS']:
      abort(400)
    uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
  return render_template('success.html',name=uploaded_file)