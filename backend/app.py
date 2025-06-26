# from flask import Flask, jsonify
# from spark_processor import process_health_data
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route("/api/health-data")
# def health_data():
#     data = process_health_data()
#     return jsonify(data)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, jsonify
from hive_query import query_health_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/health-data")
def get_data():
    data = query_health_data()
    return jsonify(data)

@app.route('/')
def home():
    return "Welcome to my Flask app!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
