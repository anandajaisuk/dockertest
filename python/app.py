import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getuser", methods=["GET"])
def get_name():
    url = "http://localhost:3000/auth/api"
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    app.run(debug=True,host='localhost', port=5000)