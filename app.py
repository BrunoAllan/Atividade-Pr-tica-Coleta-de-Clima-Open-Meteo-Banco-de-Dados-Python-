import requests
from sqlalchemy.orm import sessionmaker
from models import Clima, engine

Session = sessionmaker(bind=engine)
session = Session()
api = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,relative_humidity_2m,weather_code'

response = requests.get(api)
data = response.json()
print(data)

if response.status_code != 200:
    print("Não foi possivel conectar com o servidor!")

temperature = data['current']['temperature_2m']
humidity = data['current']['relative_humidity_2m']
wheather = data['current']['weather_code']
timedata = data ['current']['time']

try:
    clima = Clima(
    time=timedata,
    temperature_2m=temperature,
    relative_humidity_2m=humidity,
    weather_code=wheather
)

    session.add(clima)
    session.commit()
    print("sucesso!")

except Exception as e:
    session.rollback()
    print("Erro ", e)
