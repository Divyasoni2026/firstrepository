from flask import Flask, jsonify

# create flask app
app = Flask(__name__)

# API endpoint
@app.route("/", methods=["GET"])
def message():
    return jsonify({
        "message": "Hello! This is my first Python API from flask",
        "status": "success"
    })


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello! This is my first Python API",
        "status": "success"
    })

# start the server
if __name__ == "__main__":
    app.run(debug=True)
