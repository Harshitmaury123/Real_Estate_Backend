from zipfile import error

from flask import Flask, request, jsonify
from flask_cors import CORS

import util

app = Flask(__name__)
CORS(app)  # This allows all origins

@app.route("/hello")
def hello_world():
    return "Hello World"


@app.route("/get-location-names")
def get_location_names():
    response = jsonify({
        "locations": util.get_locations()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/get-estimated-price", methods=['POST'])
def get_estimated_price():
    try:
        location = request.form.get("location")
        bhk = request.form.get("bhk")
        bath = request.form.get("bath")
        sqft = request.form.get("sqft")
        response=jsonify({
            "estimated_price": util.get_estimated_price(location,sqft,bhk,bath)
        })
        return response
    except:
        response=jsonify({
            "message":"error sending Post request"
        })
        return response


if __name__ == "__main__":
    util.load_locations()
    app.run(debug=True)
