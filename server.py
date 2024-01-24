from flask import Flask, request, jsonify
from utils import helpers
from utils import visualize

app = Flask(__name__)


@app.route("/test", methods=["POST"])
def test_endpoint():
    if request.method == "POST":
        try:
            # Get JSON data from the POST request
            data = request.get_json()

            # Process JSON
            if data["flag"]:

                response = {"message": "JSON data received successfully", "data": {"var": 1}}
            else:
                response = {"message": "JSON data received successfully", "data": {"var": None}}
            #
            print(helpers.unpack_list(data["points"]))
            print(data["flag"])
            visualize.visualizer_function(data["path"])

            # Return response
            return jsonify(response), 202

        except Exception as e:
            # Handle exception
            error_response = {"error": str(e)}
            return jsonify(error_response), 400


if __name__ == "__main__":
    app.run(debug=True)
