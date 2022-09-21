from flask import *
import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'statics/uploaded files'
ALLOWED_EXTENTIONS = {'txt', 'pdf', 'docs'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload():
  return render_template('index.html')

# allowed files checking function
def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTIONS


@app.route('/success', methods=['GET','POST'])
def success():
  if request.method == 'POST':
    file = request.files['file']
    # checking if the uploaded file's extension included in 'allowed extensions'
    if not allowed_file(file.filename):
      flash("only .txt, .pdf, .docs files allowed !!!")
    else:
      # saving the file to above mentioned foder
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
      return render_template('success.html', name=file.filename)