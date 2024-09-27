num = int(input("Digite um número inteiro para checar se este número pertence a sequência de Fibonacci: "))
sequencia = [0,1]

while num > sequencia[-1]:
    sequencia.append(sequencia[-1]+sequencia[-2])
else:
    if num in sequencia:
        print("Este número pertence a sequência")
    else:
        print("Este número não pertence a sequência")
