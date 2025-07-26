from flask import Flask, request, jsonify
from supabase import Client,create_client
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

@app.route('/sendname', methods=['POST'])
def send_name():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"message": "No name provided"}), 400
    
    result = supabase.table("Web_db").insert({"name":name}).execute()
    return jsonify({"message:":"Name Saved sucessfully!"})
