taxa_euro = 5.56
taxa_iene = 30.34
print('Conversor de moedas')
valor_real = float(input('Digite o valor em R$: '))
resultado_euro = f'{valor_real / taxa_euro:.2f}'
resultado_iene = f'{valor_real * taxa_iene:.2f}'
print(f'EUR: {resultado_euro} | JPY: {resultado_iene}')