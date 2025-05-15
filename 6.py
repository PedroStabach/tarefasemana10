dentro = 0
fora = 0
for i in range(10):
    numero = int(input(f"selecione o {(i + 1)} numero: "))
    if numero >=10 and numero <= 20:
        dentro += 1
    else:
        fora += 1

print(f"estao dentro: {dentro}, fora: {fora}")