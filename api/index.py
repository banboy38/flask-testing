import time
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    time.sleep(20)
    return [{'name':"Anirban"}, {'name':"Rahul"}, {'name':"Tanya"}, {'name':"Indresh"}, {'name':"Golu"}], 200

@app.route('/about')
def about():
    return 'About'