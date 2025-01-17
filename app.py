from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model_path = './saved_models/rf_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

def encode_season(season):
    season_encoding = {'Summer': 0, 'Monsoon': 0, 'Autumn': 0, 'Winter': 0}
    if season.lower() == 'summer':
        season_encoding['Summer'] = 1
    elif season.lower() == 'monsoon':
        season_encoding['Monsoon'] = 1
    elif season.lower() == 'autumn':
        season_encoding['Autumn'] = 1
    elif season.lower() == 'winter':
        season_encoding['Winter'] = 1
    else:
        raise ValueError("Invalid Season. Please choose from 'Summer', 'Monsoon', 'Autumn', or 'Winter'.")
    return season_encoding    

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        season = data['season']
        season_encoded = encode_season(season)
        input_features = [
            data['co'], data['no2'], data['o3'], data['so2'], data['pm2_5'],
            data['pm10'], data['nh3'], data['hour'], data['lag_AQI'], data['lag_pm2_5'],
            int(data['is_weekend']), season_encoded['Summer'], season_encoded['Monsoon'],
            season_encoded['Autumn'], season_encoded['Winter']
        ]

        input_array = np.array(input_features).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        return jsonify({'predicted_aqi': round(prediction, 2)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
