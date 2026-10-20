import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Permit the published GitHub Pages frontend to call this backend.
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://sunil8656.github.io"]
    }
})

@app.get("/")
def home():
    return jsonify({
        "service": "NIFTY OI Dashboard backend",
        "status": "running",
        "note": "Starter only: live Angel One data is not connected yet."
    })

@app.get("/api/health")
def health():
    return jsonify({"ok": True, "service": "nifty-oi-backend"})

@app.get("/api/status")
def status():
    return jsonify({
        "live_data_connected": False,
        "provider": None,
        "message": "Backend is running, but Angel One SmartAPI integration is not configured."
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
