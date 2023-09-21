saldo = int(input('Digite o valor de seu saldo:'))
nome = input('Boa tarde, qual o seu nome?')
cliente = input('Do que precisa?')

if saldo>=10000000000:
    print("Você não pode pedir um empréstimo")


if cliente == 'preciso de um empréstimo' or  cliente == 'preciso de um emprestimo' or cliente == 'emprestimo':
    valor_emprestimo=float (input ('Qual é o valor do empréstimo?'))

if valor_emprestimo<1000:
    print(f'{nome}, você tem {valor_emprestimo} e não pode fazer emprestimos.')

else:
    print(f'Olá {nome}! Seu saldo atual é de R${saldo}', 'para você pedir um empréstimo, é necessaro cadastro...')
    

print(nome, 'O senhor quer se cadastrar no nosso banco?')


resposta = input('O senhor quer? (resposta S ou N): ')

if resposta == 'S' or resposta == 's':
    print('Parabéns, bem vindo ao nosso banco')

if resposta == 'N' or resposta == 'n':
    print('Que pena! Você será desconectado!')


valor_emprestimo = int(input('Quanto deseja de empréstimo?'))


if valor_emprestimo <=100000000000000000000:
    print(valor_emprestimo+saldo)
    print(valor_emprestimo,'de empréstimo feito')
    print('Parabés, empréstimo feito')




