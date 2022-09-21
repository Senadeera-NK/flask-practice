import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "/uploaded files"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docs', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploaded files"

# functions that check if an extension is valid
def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def upload_file():
  if request.method == 'POST':
    # chech if the post request has the file part
    if 'file' not in request.files:
      flash('no file part')
      return('index.html')
    file = request.files['file']
    # if the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
      flash('no selected file')
      return redirect('index.html')
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return redirect('index.html', name=filename)