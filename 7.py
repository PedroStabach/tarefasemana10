pares = []
soma =0
variavel = int(input("onde quer comecar? "))
variavelFinal = (variavel + 50)
for i in range(variavelFinal):
    j = (i + variavel)
    if j % 2 == 0:
        pares.append(j)
        soma += j
print(f"os primeiros 50 pares apartir do numero {variavel} 'e {pares}, e a soma deles 'e {soma}")