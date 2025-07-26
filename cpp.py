from flask import Flask, request, jsonify
from supabase import create_client
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Get Supabase credentials from environment variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

@app.route('/sendmarks', methods=['POST'])
def send_c_marks():
    try:
        print("Running updated code with C_Cpp key")
        data = request.get_json()
        name = data.get("name")
        marks = data.get("marks")
        if not isinstance(marks, int):
            return jsonify({"error": "Marks must be an integer"}), 400


        # Basic validation
        if not all([name, marks]):
            return jsonify({"error": "Missing name or marks"}), 400

        # Column name is exactly C&Cpp (no quotes or spaces)
        result = supabase.table("Web_db").update({"C_Cpp": marks}).eq("name", name).execute()

        return jsonify({"message": f"C&Cpp marks updated for {name}!"})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
