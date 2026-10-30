
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Cloud Run!"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Application is running"
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
