import requests

responseUsd = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
dataUsd = responseUsd.json()
taxa_dolar = float((dataUsd["USDBRL"]["bid"]))

responseEur = requests.get("https://economia.awesomeapi.com.br/json/last/EUR-BRL")
dataEur = responseEur.json()
taxa_euro = float((dataEur["EURBRL"]["bid"]))

print('Conversor de moedas')
valor_real = float(input('Digite o valor em R$: '))

resultado_usd = f'{valor_real / taxa_dolar:.2f}'
resultado_eur = f'{valor_real / taxa_euro:.2f}'

print(f'DLR: {resultado_usd} | EUR: {resultado_eur}')