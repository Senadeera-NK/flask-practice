from flask import *


ALLOWED_EXTENTIONS = {'txt', 'pdf', 'docs'}

app = Flask(__name__)

@app.route('/')
def upload():
  return render_template('index.html')

@app.route('/success', methods=['GET','POST'])
def success():
  if request.method == 'POST':
    file = request.files['file']
    file.save(file.filename)
    return render_template('success.html', name=file.filename)