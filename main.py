# main.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from index import *  # import index routes
from cpp import *    # import sendmarks route

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://quizbucket.netlify.app"}})

# Optional: handle preflight
@app.before_request
def before_request_func():
    if request.method == 'OPTIONS':
        return '', 200

if __name__ == "__main__":
    app.run(debug=True)
