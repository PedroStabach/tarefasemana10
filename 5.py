numeros = []
pares = []
impares = []
for i in range(10):
    numero = int(input(f"selecione o {(i + 1)} numero: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"sao pares: {pares}, impares: {impares}")