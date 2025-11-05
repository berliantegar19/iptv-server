from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/channels', methods=['POST'])
def get_channels():
    data = request.get_json()
    token = data.get('token')

    if token == "12345":
        return jsonify({
            "status": "success",
            "channels": [
                {"name": "Channel 1", "url": "udp://239.0.0.1:1234"},
                {"name": "Channel 2", "url": "udp://239.0.0.2:1234"},
                {"name": "Channel 3", "url": "udp://239.0.0.3:1234"}
            ]
        })
    else:
        return jsonify({"status": "error", "message": "Invalid token"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
