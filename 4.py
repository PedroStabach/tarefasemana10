idades = [0] * 5
soma = 0

for i in range(5):
    idades[i] = int(input("Digite a idade: "))
    soma += idades[i]
media = soma / 5

print(f"A média das idades é {media}")