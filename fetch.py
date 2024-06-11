from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('fetch.html')

@app.route('/randomtext', methods=['GET'])
def randomtext():
    return jsonify({"text": "Hello, World!"})
