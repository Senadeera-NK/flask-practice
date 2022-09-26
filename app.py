import os
from flask import Flask, render_template, redirect, flash, request, send_from_directory
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = ['txt','pdf','docs','docx']
UPLOADS_FOLDER = 'static/files/'

def file_valid(file):
  return '.' in file and \
    file.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOADS_FOLDER'] = UPLOADS_FOLDER
app.config['SECRET_KEY'] = 'my secret'

@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == "GET":
    return render_template('index.html')
  
  if not 'file' in request.files:
    flash('No file part in request')
    return render_template('failed.html', name=file.filename)

  files = request.files.getlist('file')

  for file in files:
    if file.filename == '':
      flash('No file uploaded')
      return redirect(request.url)

    if file_valid(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
    else:
      flash('Invalid file type')
      return render_template('failed.html', file.filename)

  return render_template('success.html', name=file.filename)


# @app.route('/success', methods=['POST'])
# def success():
#   if request.method == 'POST':
#     f = request.files['file']
#     f.save(f.filename)
#     return render_template('success.html', name=f.filename)