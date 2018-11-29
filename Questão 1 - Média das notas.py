nota1 = int(input('Digite o valor da sua primeira nota: '))
nota2 = int(input('Digite o valor da sua segunda nota: '))
nota3 = int(input('Digite o valor da sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print('Média = {:.2f}'.format(media))
if media == 10:
    print('Aprovado com distinção!')
elif media < 7:
    print('Reprovado!')
else:
    print('Aprovado!')



