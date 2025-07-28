from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://quizbucket.netlify.app"}})

# Supabase client
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

        supabase.table("Web_db").insert({"name": name}).execute()
        return jsonify({"message": "Name Saved successfully!"})
    except Exception as e:
        print("ERROR in sendname:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/sendcppmarks', methods=['POST'])
def send_c_marks():
    try:
        data = request.get_json()
        name = data.get("name")
        marks = data.get("marks")

        if not all([name, isinstance(marks, int)]):
            return jsonify({"error": "Invalid name or marks"}), 400

        supabase.table("Web_db").update({"C_Cpp": marks}).eq("name", name).execute()
        return jsonify({"message": f"C&Cpp marks updated for {name}!"})
    except Exception as e:
        print("ERROR in sendmarks:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/sendpythonmarks', methods=['POST'])
def send_python_marks():
    try:
        data = request.get_json()
        name = data.get("name")
        marks = data.get("marks_py")

        print("Received data:", data)
        print("Name:", name, "| Marks:", marks, "| Type of marks:", type(marks))

        if isinstance(marks, str) and marks.isdigit():
            marks = int(marks)

        if not all([name, isinstance(marks, int)]):
            return jsonify({"error":"Invalid name or marks"}), 400
        
        supabase.table("Web_db").update({"Python":marks}).eq("name",name).execute()
        return jsonify({"message": f"Python marks updated for {name}!"})
    
    except Exception as e:
        print("Error in send marks", e)
        return jsonify({"error":str(e)}), 500

@app.route('/sendWebdevmarks', methods=['POST'])
def send_webdev_marks():
    try:
        data = request.get_json()
        name = data.get("name")
        marks = data.get("marks")

        print("Received data:", data)
        print("Name:", name, "| Marks:", marks, "| Type of marks:", type(marks))


        if not all([name, isinstance(marks, int)]):
            return jsonify({"error":"Invalid name or marks"}), 400
        
        supabase.table("Web_db").update({"Web - Dev":marks}).eq("name",name).execute()
        return jsonify({"message": f"Python marks updated for {name}!"})
    
    except Exception as e:
        print("Error in send marks", e)
        return jsonify({"error":str(e)}), 500
    
@app.route('/sendassemblymarks', methods=['POST'])
def send_assembly_marks():
    try:
        data = request.get_json()
        name = data.get("name")
        marks = data.get("marks")

        print("Received data:", data)
        print("Name:", name, "| Marks:", marks, "| Type of marks:", type(marks))


        if not all([name, isinstance(marks, int)]):
            return jsonify({"error":"Invalid name or marks"}), 400
        
        supabase.table("Web_db").update({"Assembly":marks}).eq("name",name).execute()
        return jsonify({"message": f"Python marks updated for {name}!"})
    
    except Exception as e:
        print("Error in send marks", e)
        return jsonify({"error":str(e)}), 500
    
@app.route('/sendffmarks', methods=['POST'])
def send_ff_marks():
    try:
        data = request.get_json()
        name = data.get("name")
        marks = data.get("marks")

        print("Received data:", data)
        print("Name:", name, "| Marks:", marks, "| Type of marks:", type(marks))


        if not all([name, isinstance(marks, int)]):
            return jsonify({"error":"Invalid name or marks"}), 400
        
        supabase.table("Web_db").update({"Full - Form":marks}).eq("name",name).execute()
        return jsonify({"message": f"Python marks updated for {name}!"})
    
    except Exception as e:
        print("Error in send marks", e)
        return jsonify({"error":str(e)}), 500



@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        return '', 200

if __name__ == "__main__":
    app.run(debug=True)
