
pares = 0
impares = 0
for i in range(10):
    numero = int(input(f"selecione o {(i + 1)} numero: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"sao pares: {pares}, impares: {impares}")