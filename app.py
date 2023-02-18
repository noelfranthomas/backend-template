from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test-data")
def data():

    data = {
    'people': [
        {'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}, 
        {'name': 'Larry', 'website': 'google.com', 'from': 'Michigan'}, 
        {'name': 'Tim', 'website': 'apple.com', 'from': 'Alabama'}
    ]
    }


    print(json.dumps(data, indent = 4))

    return json.dumps(data, indent = 4)