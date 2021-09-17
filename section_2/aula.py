'''
    DocStrings são utilizada para documentação do meu codigo
    É muito bom para fazer comentários extenso ou ate mesmo a própria 
    documentação do código.
'''

'''# Isso é um comentário
print('Linha 1')    
print('Linha 2')    
# Falando sobre do que se trata essa linha
# Outra Linha
print('Linha 3')  # Isso é um comentário (a pep diz que tenq ter dois espaço antes de um comentário)
print('Linha 4')  # Mais um
# print('Linha 5')  
print('Linha 6')  
# Final
'''
'''print('\n')
#print(123456)

#print('Luiz', 'Otavio', 'Outra coisa')
print('Luiz', 'Otávio', sep='-', end=' #### ')
print('João','e', 'Maria', sep='-')

# Print() # O python é CAP-sense'''

'''
    032.115.349-18
'''
'''print('032', '115', '239', sep='.', end='-' )
print('18')'''
'''
str - string - texto

'''
# print('alguma_coisa')
# print("Aspas Duplas")
# print(123456)

# print("Essa é uma 'string'(str).")
# print('Essa é uma "string"(str).')
# print("Esse é meu \"texto\"(str).")
# print('Esse é meu \'texto\'(str).')

# print(r'Esse é meu texto \n (str)')
# print('Esse é meu texto \n (str)')

# '' "" () {} []

'''
tipos de dados
str- string texto "Assim" "12344"
int - inteiro - 12345, -12344, 10000
float - flutuante  1.390439, 1234,523, 3234,342 -23.342
bool - booleano\lógico- 1 ou 0 True ou False
'''
#if 10 == 10:
#    print('oi')

#if 9 != 10:
#    print('Outro oi')

'''
print(type('Luiz'))
print(type(12234))
print(type(1.23))
print(type(True))
'''
#print(bool('a'))
'''Quando colocamos algo vazio na função bool ele retorna False'''
#print('Luiz', type('Luiz'), bool('Luiz'))

#print('10', type('10'), type(int('10')))

'''print("Fabio Leal Schmitz", type("Fabio Leal Schmitz"))

print(26, type(26))

print(1.79, type(1.79))

print(26 > 18, type(26 > 18))'''
'''
Operadores Aritméticos

+ Adição
- Subtração
* Multiplicação
/ Divisão
//  Inteiro
**  Potenciação
%   Resto
()  Precedencia

'''

'''print(10 * 10)
print(10 + 10)
print(10 - 3)
print(10 ** 3)
print(10 / 2)
print(10 // 10)
print('10 ' * 10)
print('5' + '5')
print(10 % 3)
'''
'''
    Iniciar com letra, pode conter número, separar _, letras minúculas
'''
'''
nome = 'Fabio Leal Schmitz'
idade = 26
altura = 1.80
e_maior = idade > 18
peso = 73
imc = peso / (altura**2)'''
'''
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('é maior:', e_maior)
'''


'''print(nome, 'tem', idade, 'anos de idade e seu imc é: ', imc)'''
'''nome = 'Fabio Leal Schmitz'
idade = 26
altura = 1.80
e_maior = idade > 18
peso = 73
imc = peso / (altura**2)
'''
'''
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos {1} de idade e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e {im} seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
'''
'''
    Entrada de dados
'''
'''
nome = input("Qual seu nome? ")
idade = int(input('Qual sua idade? '))
anoNascimento = 2021 - idade
print()
print(f'O usuário digitou {nome} tem {idade} anos e nasceu em {anoNascimento} e o tipo das variáveis é: ', end='')
print(type(nome), type(idade), type(anoNascimento))
'''

'''n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
print(int(n1)+int(n2))'''
'''
    Condição IF, ELIF e ELSE
'''
'''
    Operadores Relacionais
    
    = é igual
    == Igual? 
    >  Maior que
    >= Maior ou igual a
    <  Menor que
    <= Menor ou igual a
    != Diferente?
'''

'''if False:
    print('\nVerdadeiro')
else:
    print('Num deu')'''

'''n1 = 2
n2 = 2

exp = (n1 >= n2)
print(exp)'''
'''
Operadores Lógicos

and 'e'

or 'ou'

not 'não'
'''

'''if 2 > 1 and 1 == 1:
    print('oi')'''
'''if 1 > 2 or 2 < 3:
    print('oi')'''
'''
    Usando o len
'''

'''user = input('Digite Usuário: ')
qtd_char = len(user)'''


'''print(user, qtd_char, type(qtd_char))'''

'''if qtd_char < 6:
    print('O user tenq ser maior q 6')
else:
    print('Foi cadastrado!')'''  

