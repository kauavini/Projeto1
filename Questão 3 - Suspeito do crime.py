p1 = str(input('Telefonou para a vítima? ')).split()[0]
p2 = str(input('Esteve no local do crime? ')).split()[0]
p3 = str(input('Mora perto da vítima? ')).split()[0]
p4 = str(input('Devia para a vítima? ')).split()[0]
p5 = str(input('Já trabalhou com a vítima? ')).split()[0]
analisador = 1
suspeita = 0
if p1 in 'Sim':
    suspeita += 1
if p2 in 'Sim':
    suspeita += 1
if p3 in 'Sim':
    suspeita += 1
if p4 in 'Sim':
    suspeita += 1
if p5 in 'Sim':
    suspeita += 1
if suspeita == 2:
    print('Suspeita')
elif suspeita == 5:
    print('Assassino')
elif suspeita == 3 or suspeita == 4:
    print('Cúmplice')
else:
    print('Inocente')










