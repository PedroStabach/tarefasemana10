n = int(input("Digite o tamanho dos vetores: "))
A = []
B = []
C = []

print("\nDigite os elementos do vetor A:")
for i in range(n):
    valor = int(input(f"A[{i}]: "))
    A.append(valor)

print("\nDigite os elementos do vetor B:")
for i in range(n):
    valor = int(input(f"B[{i}]: "))
    B.append(valor)

for i in range(n):
    C.append(A[i] + B[i])

print("\nVetor resultante C (A + B):")
print(C)
