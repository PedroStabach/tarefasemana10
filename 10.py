vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
contagem = {}

for numero in vetor:
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1

mais_frequente = max(contagem, key=contagem.get)
frequencia = contagem[mais_frequente]

print(f"O número que mais se repete é {mais_frequente}, aparecendo {frequencia} vezes.")