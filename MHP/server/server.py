from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_region_mapping', methods=['GET'])
def get_region_mapping():
    try:
        regions = util.get_region_mapping()
        return jsonify({'regions': regions}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    print("hrer we go")
    try:
        total_sqft = float(request.form.get('total_sqft'))
        region = request.form.get('region')
        distance = float(request.form.get('distance'))
        rooms = request.form.get('rooms')
        bathrooms = request.form.get('bathrooms')
        estimated_price = util.get_estimated_price(region, total_sqft, rooms, bathrooms, distance)
        return jsonify({'estimated_price': estimated_price}), 200
    except (TypeError, ValueError, KeyError) as e:
        return jsonify({'error': 'Invalid input data', 'details': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True, host="0.0.0.0", port=3500)