from audioop import cross
from flask import Flask, jsonify, render_template, Request
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def index():

    return "CI CD Pipeline"


if (__name__ == '__main__'):
    
    app.run(debug=True)





