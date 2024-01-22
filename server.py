from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/test", methods=["POST"])
def test_endpoint():
    if request.method == "POST":
        try:
            # Get JSON data from the request
            data = request.get_json()

            # Process JSON
            print(data["flag"])
            if data["flag"]:

                response = {"message": "JSON data received successfully", "data": {"var": 1}}
            else:
                response = {"message": "JSON data received successfully", "data": {"var": None}}

                # Return response

            return jsonify(response), 202

        except Exception as e:
            # Handle exception
            error_response = {"error": str(e)}
            return jsonify(error_response), 400


if __name__ == "__main__":
    app.run(debug=True)