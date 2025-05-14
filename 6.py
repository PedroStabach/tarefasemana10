dentro = []
fora = []
for i in range(10):
    numero = int(input(f"selecione o {(i + 1)} numero: "))
    if numero >=10 and numero <= 20:
        dentro.append(numero)
    else:
        fora.append(numero)

print(f"estao dentro: {dentro}, fora: {fora}")