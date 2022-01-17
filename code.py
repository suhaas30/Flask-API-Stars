from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)
@app.route("/")
def Index():
    return jsonify({
        "data":data,
        "message":"success"
    }), 200

@app.route("/stars")
def Stars():
    name = request.args.get("name")
    stars_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data":stars_data,
        "message":"success"
    }), 200


if __name__ == "__main__":
    app.run()