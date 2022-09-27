from flask import *
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads/files'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/success', methods=['GET','POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename (f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('success.html', name=f.filename)

if __name__ == '__main__':
    app.run(debug=True)