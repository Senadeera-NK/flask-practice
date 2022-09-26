from pickletools import read_uint1
from flask import *
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = ['txt', 'pdf', 'docs', 'docx']
UPLOADS_FOLDER = 'static/files/'

def file_valid(file):
  return '.' in file and \
    file.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOADS_FOLDER'] = UPLOADS_FOLDER
app.config['SECRET_KEY'] = 'my secret'

@app.route('/', methods=['GET','POST'])
def upload():
  return render_template('index.html')

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/success', methods=['POST'])
def success():
  if request.method == 'POST':
    f = request.files['file']
    f.save(f.filename)
    return render_template('success.html', name=f.filename)