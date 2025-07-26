from flask import Flask, request, jsonify
from supabase import create_client
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

@app.route('/sendmarks', methods=['POST'])
def send_marks():
    try:
        data = request.get_json()
        name = data.get("name")
        subject = data.get("subject")
        marks = data.get("marks")

        if not all([name, subject, marks]):
            return jsonify({"error": "Missing data"}), 400

        # Check if name exists
        existing = supabase.table("Web_db").select("name").eq("name", name).execute()

        if existing.data:
            # Update existing
            result = supabase.table("Web_db").update({subject: marks}).eq("name", name).execute()
            msg = f"{subject} marks updated for {name}!"
        else:
            # Insert new with subject marks
            result = supabase.table("Web_db").insert({"name": name, subject: marks}).execute()
            msg = f"{name} added with marks in {subject}!"

        return jsonify({"message": msg})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

