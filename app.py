from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init App
app = Flask(__name__)

@app.route("/",methods=['GET'])
def index():
    return jsonify({'msg': "Hello World"})

@app.route("/someroute/<int:pram>")
def someDef(pram):
    return jsonify({'value':pram})

@app.route("/testpost", methods=['GET','POST'])
def testpost():
    if (request.method == 'POST'):
        return jsonify({"about":"The example of REST API as POST req."}),201
    return jsonify({"about":"The example of REST API as GET req."})
    



# Run Server
if (__name__ == "__main__"):
    app.run(debug=True)