from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 🔥 SIMPLE WARANGAL TEST DATA
SPOTS = [
    {"id":1, "lat":18.0005, "lng":79.5800, "type":"park", "host":"Kakatiya University Ground", "dist":0.5, "score":99},
    {"id":2, "lat":18.0042, "lng":79.5751, "type":"stadium", "host":"Warangal Sports Complex", "dist":1.2, "score":100},
    {"id":3, "lat":18.0012, "lng":79.5823, "type":"park", "host":"Bhadrakali Park", "dist":0.3, "score":98},
]

@app.route('/locations')
def get_nearby():
    sport = request.args.get('sport', 'cricket')
    # Return ALL spots for ANY sport (SIMPLE TEST)
    return jsonify([{
        'id': spot['id'], 'lat': spot['lat'], 'lng': spot['lng'],
        'type': spot['type'], 'host': spot['host'], 
        'dist': spot['dist'], 'score': spot['score']
    } for spot in SPOTS])

@app.route('/')
def home():
    return "🚀 PlaySpot API OK! Test: /locations?sport=cricket"

if __name__ == '__main__':
    print("🚀 SIMPLE PlaySpot - http://localhost:5000")
    app.run(debug=True, port=5000)
