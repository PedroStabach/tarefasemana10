idades = int(input("quantas idades voce deseja? "))
totalIdades = []
media = 0
for i in range(idades):
    idade = int(input("escreva a idade desejada"))
    totalIdades.append(idade) 
    media += totalIdades[i]
media = media / idades
print(f"a media 'e {media}")