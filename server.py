from flask import Flask, request, jsonify
from utils import functions, visualize
import threading

app = Flask(__name__)


def run_visualizer(cloud_path, points_path):
    visualize.visualizer_function(cloud_path, points_path)


@app.route("/test", methods=["POST"])
def test_endpoint():
    if request.method == "POST":
        try:
            # Get JSON data from the POST request
            data = request.get_json()

            # Process JSON
            # Get flag
            returned_flag = functions.return_flag(data["cloud_path"], data["points_path"])

            if data["flag"]:
                response = {"message": "JSON data received successfully", "data": {"var": 1, "flag": returned_flag}}
            else:
                response = {"message": "JSON data received successfully", "data": {"var": None, "flag": returned_flag}}

            # Run the visualization function in a separate thread
            threading.Thread(target=run_visualizer, args=(data["cloud_path"], data["points_path"])).start()

            # Return response
            return jsonify(response), 202

        except Exception as e:
            # Handle exception
            error_response = {"error": str(e)}
            return jsonify(error_response), 400


if __name__ == "__main__":
    app.run(port=5050, debug=True)
