from flask import Flask, request, jsonify
from utils import visualize

app = Flask(__name__)


@app.route("/test", methods=["POST"])
def test_endpoint():
    if request.method == "POST":
        try:
            # Get JSON data from the POST request
            data = request.get_json()

            # Process JSON
            # Execute visualizer function, get flag

            returned_flag = visualize.visualizer_function(data["cloud_path"], data["points_path"])

            if data["flag"]:

                response = {"message": "JSON data received successfully", "data": {"var": 1, "flag": returned_flag}}
            else:
                response = {"message": "JSON data received successfully", "data": {"var": None, "flag": returned_flag}}

            # Return response
            return jsonify(response), 202

        except Exception as e:
            # Handle exception
            error_response = {"error": str(e)}
            return jsonify(error_response), 400


if __name__ == "__main__":
    app.run(debug=True)
