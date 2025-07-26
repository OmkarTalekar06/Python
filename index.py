from flask import Flask, request, jsonify
from supabase import Client,create_client
import os

app = Flask(__name__)

url = os.environ.get("https://yhcmkjyhnzpotyhkybaw.supabase.co")
key = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InloY21ranlobnpwb3R5aGt5YmF3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMzNzcwMzUsImV4cCI6MjA2ODk1MzAzNX0.ntDfFrMXQTArpZ8sUQXCvmgd6gMOyWK9h3NaE4GSoNA")
supabase = create_client(url, key)

@app.route('/sendname', methods=['POST'])
def send_name():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"message": "No name provided"}), 400
    
    result = supabase.table("Web_db").insert({"name":name}).execute()
    return jsonify({"message:":"Name Saved sucessfully!"})
