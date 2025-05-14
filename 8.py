total = []
for i in range(10):
    numero = int(input("Escolha um número: "))
    total.append(numero)

 
crescente = sorted(total)
print("Lista em ordem crescente:", crescente)