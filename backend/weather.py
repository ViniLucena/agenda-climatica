from dotenv import load_dotenv
import os
import requests

#carrega variaveis do arquivo ".env" (chave a API do OpenWeather)
load_dotenv()

#pega a chave da variavel de ambiente
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

print("chave da API do OpenWeather:", OPENWEATHER_API_KEY) #apenas para teste, remover depois

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"  #para temperaturas em Celsius
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200: #requisição bem sucedida
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return {"cidade": city_name, "temperatura": temperature, "descricao": weather_desc}
    else:
        return {"error": "nao foi possivel obter o clima para a cidade informada."}