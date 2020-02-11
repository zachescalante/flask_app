from flask import Flask

UPLOAD_FOLDER = '/mnt/c/Users/NYCZE/Desktop/flask_app/file_uploads'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes
