texto = input("Digite um texto qualquer: ")
vogais = "aeiou"
contagem_vogais = {}

 
for letra in texto.lower():  
    if letra in vogais:
        if letra in contagem_vogais:
            contagem_vogais[letra] += 1
        else:
            contagem_vogais[letra] = 1

total_vogais = sum(contagem_vogais.values())

print(f"\nTotal de vogais: {total_vogais}")
print("Vogais encontradas:")
for vogal, quantidade in contagem_vogais.items():
    print(f"- {vogal}: {quantidade}")