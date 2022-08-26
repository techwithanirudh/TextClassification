from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/anjan")
@app.route("/about")
def about():
	return render_template("about.html")

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)