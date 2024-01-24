from flask import Flask, request, jsonify

app = Flask(__name__)


def unpack_list(ls):
    unpacked_list = []
    for i in range(0, len(ls)):
        for item in ls[i]:
            unpacked_list.append(item)

    return unpacked_list


@app.route("/test", methods=["POST"])
def test_endpoint():
    if request.method == "POST":
        try:
            # Get JSON data from the request
            data = request.get_json()

            # Process JSON
            print(unpack_list(data["points"]))
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
