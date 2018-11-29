lista1 = []
lista2 = []
lista3 = []
for i in range(20):
    if i <= 9:
        lista1.append(int(input('Digite um valor (lista1): ')))
    else:
        lista2.append(int(input('Digite um valor (lista2): ')))
indice = 0
while indice <= 9:
    lista3.append(lista1[indice])
    lista3.append(lista2[indice])
    indice += 1
print(lista3)



