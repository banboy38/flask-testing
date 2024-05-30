import time
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def home():
    time.sleep(20)
    return [{'name':"Anirban"}, {'name':"Rahul"}, {'name':"Tanya"}, {'name':"Indresh"}, {'name':"Golu"}], 200

@app.route('/about')
def about():
    return 'About'