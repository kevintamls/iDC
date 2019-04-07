# Import Flask
from flask import Flask, jsonify
from flask_cors import CORS

# Configuration
DEBUG = True

# Initialise Flask app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
        return jsonify('pong!')


if __name__ == '__main__':
    app.run(host='192.168.1.140')
