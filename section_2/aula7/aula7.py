nome = 'Fabio Leal Schmitz'
idade = 26
altura = 1.80
e_maior = idade > 18
peso = 73
imc = peso / (altura**2)

'''
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos {1} de idade e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e {im} seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
'''

