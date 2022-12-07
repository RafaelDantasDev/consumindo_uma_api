import requests
import json
from time import sleep



def cotacao_moeda():
    cotacoes = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()
    cotacao_dolar = cotacoes['USDBRL']['bid']
    print(cotacao_dolar)

cotacao_moeda()
    
# Atualiza a cotação do Dolar a cada 15 segundos
while True:
    sleep(15)
    cotacao_moeda()