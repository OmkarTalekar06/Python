from flask import Flask, request, jsonify
from supabase import create_client
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/sendname', methods=['POST'])
def send_name():
    try:
        data = request.get_json()
        name = data.get("name")
        if not name:
            return jsonify({"message": "No name provided"}), 400

        result = supabase.table("Web_db").insert({"name": name}).execute()
        return jsonify({"message": "Name Saved successfully!"})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
