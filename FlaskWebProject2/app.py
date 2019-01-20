"""
Routes and views for the flask application.
"""
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/ongrayyi/Documents/GitHub/HackCambridge19/FlaskWebProject2/static/data'
ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY']='secret'

from datetime import datetime
from flask import render_template
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',  methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/upload',  methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        print('No file part')
        flash('No file part')
        return render_template('index.html')
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        print('No selected file')
        flash('No selected file')
        return render_template('index.html')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('index.html')


