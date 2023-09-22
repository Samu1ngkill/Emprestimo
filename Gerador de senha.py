p = input('Deseja criar uma senha segura de 1 a 10?')

if p == 'sim' or p == 's':
    print('\nVocê escolheu a criação de uma senha mais forte.')


import random

sequencia = list(range(1, 10))

quatro_numeros_aleatorios = random.sample(sequencia, 4)

print('Esse podem ser a sua senha... ', quatro_numeros_aleatorios)


