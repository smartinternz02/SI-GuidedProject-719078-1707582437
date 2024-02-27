import pandas as pd
from prophet import Prophet
import pickle

df = pd.read_csv("../model/BTC-USD.csv")
print (df)

prophet_df = df.rename(columns = {'Date':'ds', 'Close':'y'})
print(prophet_df)
      
m = Prophet()
m.fit(prophet_df)

future = m.make_future_dataframe(periods = 30)
forecast = m.predict(future)

print(forecast)
pickle.dump(m, open('fbcrypto.pkl', 'wb'))