import requests
 
url = "https://api.open-meteo.com/v1/forecast"
 
params = {
    "latitude": -23.55,     # São Paulo
    "longitude": -46.63,
    "current_weather": True
}
 
response = requests.get(url, params=params)
 
if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]
 
    print("Temperatura:", weather["temperature"], "°C")
    print("Vento:", weather["windspeed"], "km/h")
    print("Direção do vento:", weather["winddirection"], "°")
    print("Horário:", weather["time"])
else:
    print("Erro:", response.status_code)