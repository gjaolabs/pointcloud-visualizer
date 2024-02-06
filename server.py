from flask import Flask, request, jsonify
from utils import functions, visualize
import threading

app = Flask(__name__)


def run_visualizer(point_cloud_data, point_data):
    visualize.visualizer_function(point_cloud_data, point_data)


@app.route("/test", methods=["POST"])
def test_endpoint():
    if request.method == "POST":
        try:
            # Get JSON data from the POST request
            data = request.get_json()

            # Process JSON
            # Unpack data
            point_cloud_data, point_data = functions.load_data(data["cloud_path"], data["points_path"])

            # Get flag
            returned_flag = functions.check_matching_points(point_cloud_data, point_data)

            if data["flag"]:
                response = {"message": "JSON data received successfully", "data": {"var": 1, "flag": returned_flag}}
            else:
                response = {"message": "JSON data received successfully", "data": {"var": None, "flag": returned_flag}}

            # Run the visualization function in a separate thread
            threading.Thread(target=run_visualizer, args=(point_cloud_data, point_data)).start()

            # Return response
            return jsonify(response), 202

        except Exception as e:
            # Handle exception
            error_response = {"error": str(e)}
            return jsonify(error_response), 400


if __name__ == "__main__":
    app.run(port=5050, debug=True)
