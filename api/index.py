from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return [{'name':"Anirban"}, {'name':"Rahul"}, {'name':"Tanya"}, {'name':"Indresh"}, {'name':"Golu"}], 200

@app.route('/about')
def about():
    return 'About'