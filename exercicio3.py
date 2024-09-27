import json
#exemplo de arquivo json
arquivo = '''
{"dia":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
"faturamento":[1000, 1200, 1100, 1300, 1250, 0, 0, 1600, 1550, 1700, 1650, 1800, 0, 0, 1850, 2000, 1950, 2100, 2050, 0, 0, 2300, 2250, 2400, 2350, 2500, 0, 0, 2550, 2700]}
'''
json = json.loads(arquivo)

lista_faturamento =[]

for faturamento in json["faturamento"]:
    if faturamento != 0:
        lista_faturamento.append(faturamento)

qtd_dias = len(lista_faturamento)

faturamento_total = sum(lista_faturamento)
faturamento_media = faturamento_total/qtd_dias


valor_maiorF = valor_menorF = lista_faturamento[0]

qtd_dias_media = 0

for index in range(len(lista_faturamento)):
    if lista_faturamento[index] < valor_menorF and lista_faturamento[index] != 0: #verifica qual o menor faturamento do mês
        valor_menorF = lista_faturamento[index]
    if lista_faturamento[index] > valor_maiorF: #verifica qual o maior faturamento do mês
        valor_maiorF = lista_faturamento[index]
    if lista_faturamento[index] > faturamento_media: #verifica e contabiliza os dias que possuem media superio a do
        qtd_dias_media +=1

print(f"""
Faturamento Total: R${faturamento_total:.2f}
Quantidade de dias com faturamento: {qtd_dias_media}
Média de faturamento diário no mês: {faturamento_media:.2f}

Maior Faturamento do mês: {valor_maiorF:.2f}
Menor Faturamento do mês: {valor_menorF:.2f}
Quantidade de dias que a ultrapassaram a média do mês: {qtd_dias_media}
""")
