import requests                             # Biblioteca para realizar requisições
from sqlalchemy.orm import sessionmaker     # Importa o sessionmaker para criar sessões no banco de dados
from models import Clima, engine            # Importa o model Clima e a engine de conexão com o banco

Session = sessionmaker(bind=engine)         # Cria uma sessão ligada à engine do banco
session = Session()                         # Abre uma sessão com o banco de dados

api = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,relative_humidity_2m,weather_code'# URL da API Open-Meteo
response = requests.get(api)                # Faz a requisição GET para a API
data = response.json()                      # Converte a resposta da API (JSON) para um dicionário Python
if response.status_code != 200:             # Verifica se a resposta NÃO foi bem-sucedida (status diferente de 200)
    print("Não foi possivel conectar com o servidor!")

temperature = data['current']['temperature_2m']     # Extrai a temperatura atual do JSON
humidity = data['current']['relative_humidity_2m']  # Extrai a umidade relativa do ar
wheather = data['current']['weather_code']          # Extrai o código do clima (weather code)
timedata = data['current']['time']                  # Extrai a data e hora da medição

try:                # Tenta inserir os dados no banco de dados
    clima = Clima(  # Cria um objeto Clima com os dados coletados
        time=timedata,
        temperature_2m=temperature,
        relative_humidity_2m=humidity,
        weather_code=wheather
    )
    session.add(clima)  # Adiciona o objeto à sessão
    session.commit()    # Faz um commit no banco
    print("sucesso!")   # Informa no terminal se deu certo

except Exception as e:  # Caso ocorra qualquer erro durante a inserção
    session.rollback()  # Desfaz qualquer alteração pendente no banco
    print("Erro ", e)   # Exibe no terminal o erro
