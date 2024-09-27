texto = list(input("Digite uma palavra: "))

for posic in range(len(texto)-1,-1,-1):
    texto.append(texto[posic])
    texto.remove(texto[posic])

texto = ''.join(texto)
print(texto)

