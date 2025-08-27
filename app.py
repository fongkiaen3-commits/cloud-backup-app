from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/upload", methods=["POST"])
def upload():
    return jsonify({"message": "File uploaded (dummy)", "status": "ok"})

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
