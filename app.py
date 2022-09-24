from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static/files'
ALLOWED_EXTENSIONS = {'.txt', '.pdf', '.docs', '.docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/success', methods=['GET','POST'])
def upload_files():
  if request.method == 'POST':
    if 'file' not in request.files:
      flash('no file part')
    file = request.files['file']
    if file.filename == '':
      flash('no selected files')
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  return render_template('success.html', name=filename)