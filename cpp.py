from flask import Flask, request, jsonify
from supabase import create_client
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

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
def send_c_marks():
    try:
        data = request.get_json()
        name = data.get("name")
        marks = data.get("marks")

        if not all([name, marks]):
            return jsonify({"error": "Missing name or marks"}), 400

        result = supabase.table("Web_db").update({'"C & Cpp"': marks}).eq("name", name).execute()

        return jsonify({"message": f"C & Cpp marks updated for {name}!"})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


