dados_faturamento = {
    "estados":["sp","rj","mg","es","outros"],
    "faturamento":[67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
    }

lista_estados = dados_faturamento["estados"]
lista_faturamento = dados_faturamento["faturamento"]
faturamento_total = sum(lista_faturamento)

print(f"Faturamento total: R${faturamento_total:.2f}\n")

for i in range(len(lista_estados)):
    print(f"{lista_estados[i]} - \n\t valor: {lista_faturamento[i]} \n\t {lista_faturamento[i]/faturamento_total:.2%}")
