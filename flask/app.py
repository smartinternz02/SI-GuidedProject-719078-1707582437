import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import requests
from datetime import datetime

app = Flask(__name__)

m = pickle.load(open('fbcrypto.pkl','rb'))

def get_current_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        bitcoin_price = data["bitcoin"]["usd"]
        return bitcoin_price
    except Exception as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None


@app.route('/', methods=['GET'])
def index():
    current_bitcoin_price = get_current_bitcoin_price()
    return render_template('index.html', current_bitcoin_price=current_bitcoin_price)


future = m.make_future_dataframe(periods = 10000)
forecast = m.predict(future)

@app.route('/predict', methods=['POST']) 
def y_predict():
    if request.method == "POST": 
        ds = request.form["Date"]
        ds = str(ds)
        next_day = datetime.strptime(ds, "%Y-%m-%d").date()
        forecast_dates = forecast['ds'].dt.date
        print(forecast['ds'].dt.date)
        
        # Check if next_day exists in forecast_dates
        if next_day in forecast_dates.values:
            # Find the corresponding index in forecast_dates
            index = forecast_dates[forecast_dates == next_day].index[0]
            prediction = forecast.loc[index, 'yhat']
            prediction = round(prediction, 2)
        else:
            # Provide a default value or error message if next_day is not found
            prediction = "Date not found in forecast data."

        return jsonify(prediction)
    

if __name__ =="__main__":
    app.run(debug="True")
