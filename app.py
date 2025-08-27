import boto3
import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

s3 = boto3.client("s3")
BUCKET_NAME = os.getenv("BUCKET_NAME")

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    s3.upload_fileobj(file, BUCKET_NAME, file.filename)

    return jsonify({"message": f"{file.filename} uploaded to S3", "status": "ok"})

@app.route("/list", methods=["GET"])
def list_files():
    return jsonify({
        "files": [
            {"filename": "report.pdf", "version": 1, "timestamp": "2025-08-26"},
            {"filename": "photo.png", "version": 2, "timestamp": "2025-08-25"}
        ]
    })

@app.route("/restore/<filename>", methods=["POST"])
def restore(filename):
    return jsonify({"message": f"Restored {filename} (dummy)", "status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
