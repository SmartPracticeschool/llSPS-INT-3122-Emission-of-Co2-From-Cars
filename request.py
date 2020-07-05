import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Fuel':1, 'ENGINESIZE':2.4, 'CYLINDERS':4, 'FUELCONSUMPTION_CITY':11.2, 'FUELCONSUMPTION_HWY':7.7, 'FUELCONSUMPTION_COMB':9.6,'FUELCONSUMPTION_COMB_MPG':29})

print(r.json())
