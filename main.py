from flask import Flask, render_template, flash, request, redirect, send_from_directory, url_for 
from werkzeug.utils import secure_filename
import os
import subprocess

UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'results'
ALLOWED_EXTENSIONS = {'xls', 'xlsx', 'csv'}
SECRET_KEY = 'simba doggie'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# If the user does not select a file, the browser submits an
		# empty file without a filename.
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			path = os.path.join(app.config['UPLOAD_FOLDER'], filename) 
			file.save(path)
			output = subprocess.check_output(["python", "script.py", path])
			output = output.decode()
			return redirect(url_for('download_file', name=filename))
	return redirect(url_for('index'))

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["DOWNLOAD_FOLDER"], name)
	
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)