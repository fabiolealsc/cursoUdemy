'''
    * Criar variáveis para nome (str), idade (int),
    * altura (float) e peso (float) de uma pessoa
    * Criar variável com o ano atual (int)
    * Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
    * Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
    * Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
'''

nome = 'Fabio Leal Schmitz'
idade = 27
altura = 1.69
peso = 73.0
anoAtual = 2021
imc = peso / altura**2
print()
print(f'{nome} tem {idade}, {altura} de altura e pesa {peso}Kg.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {anoAtual - idade}')