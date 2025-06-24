from flask import Flask, jsonify
from spark_processor import process_health_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/health-data")
def health_data():
    data = process_health_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
