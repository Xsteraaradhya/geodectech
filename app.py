# backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS # To allow frontend to access
import datetime

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# --- Dummy Data (replace with actual satellite data processing and DB calls) ---
# In a real app, this would come from a database populated by satellite data processing.
dummy_bloom_data = {
    "latest_blooms": [
        {
            "id": "B001",
            "latitude": 27.5,
            "longitude": -82.7,
            "location_name": "Florida Gulf Coast",
            "intensity": "High", # e.g., based on chlorophyll-a
            "chlorophyll_a": 55.2, # ug/L
            "detection_date": "2023-10-26T10:00:00Z",
            "source_satellite": "Aqua/MODIS"
        },
        {
            "id": "B002",
            "latitude": 42.0,
            "longitude": -87.5,
            "location_name": "Lake Michigan",
            "intensity": "Medium",
            "chlorophyll_a": 20.1,
            "detection_date": "2023-10-25T14:30:00Z",
            "source_satellite": "Sentinel-2"
        },
        {
            "id": "B003",
            "latitude": 30.0,
            "longitude": -90.0,
            "location_name": "Mississippi Delta",
            "intensity": "High",
            "chlorophyll_a": 60.5,
            "detection_date": "2023-10-26T08:00:00Z",
            "source_satellite": "Aqua/MODIS"
        }
    ],
    "predicted_blooms": [
        {
            "id": "P001",
            "latitude": 28.0,
            "longitude": -80.0,
            "location_name": "Atlantic Coast (FL)",
            "prediction_intensity": "Medium-High",
            "prediction_date": "2023-10-29T12:00:00Z",
            "confidence": "85%"
        }
    ],
    "chlorophyll_trends": [
        {"date": "2023-10-20", "value": 15},
        {"date": "2023-10-21", "value": 18},
        {"date": "2023-10-22", "value": 25},
        {"date": "2023-10-23", "value": 35},
        {"date": "2023-10-24", "value": 42},
        {"date": "2023-10-25", "value": 48},
        {"date": "2023-10-26", "value": 55}
    ]
}

# --- API Endpoints ---

@app.route('/')
def home():
    return "BloomWatch API is running!"

@app.route('/api/blooms/latest', methods=['GET'])
def get_latest_blooms():
    """
    Returns the latest detected algal blooms.
    In a real app, this would query a database.
    """
    return jsonify({
        "status": "success",
        "data": dummy_bloom_data["latest_blooms"]
    })

@app.route('/api/blooms/predicted', methods=['GET'])
def get_predicted_blooms():
    """
    Returns predicted algal blooms.
    In a real app, this would query a prediction model/database.
    """
    return jsonify({
        "status": "success",
        "data": dummy_bloom_data["predicted_blooms"]
    })

@app.route('/api/trends/chlorophyll_a', methods=['GET'])
def get_chlorophyll_trends():
    """
    Returns historical chlorophyll-a concentration trends for a generic area.
    Can be extended with query params for specific locations.
    """
    return jsonify({
        "status": "success",
        "data": dummy_bloom_data["chlorophyll_trends"]
    })

# --- Error Handling ---
@app.errorhandler(404)
def not_found(error):
    return jsonify({"status": "error", "message": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    # For production, use a WSGI server like Gunicorn
    app.run(debug=True, port=5000)
