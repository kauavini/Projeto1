lista = []
for i in range(4):
    lista.append(int(input(f'Digite sua nota {i + 1}: ')))
print('A sua média é {}'.format(sum(lista) / len(lista)))
