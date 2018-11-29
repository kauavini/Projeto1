suspeita = 0
lista = []
for i in range(5):
    if i == 0:
        lista.append(str(input('Telefonou para a vítima? ')))
    if i == 1:
        lista.append(str(input('Esteve no local do crime? ')))
    if i == 2:
        lista.append(str(input('Mora perto da vítima? ')))
    if i == 3:
        lista.append(str(input('Devia para a vítima? ')))
    if i == 4:
        lista.append(str(input('Já trabalhou com a vítima? ')))
for i in range(0, 5):
    if lista[i] in 'SimsimSs':
        suspeita += 1
if suspeita == 2:
    print('Suspeita')
if suspeita == 3 or suspeita == 4:
    print('Cúmplice')
if suspeita == 5:
    print('Assassino')
if suspeita == 1 or suspeita == 0:
    print('Inocente')

