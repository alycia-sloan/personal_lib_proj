from flask import Flask, request, jsonify, render_template
import requests

# instance of flask application
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)