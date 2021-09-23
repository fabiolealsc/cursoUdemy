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
'''
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

if n1.isnumeric():
    n1 = int(n1)
if n2.isnumeric():
    n2 = int(n2)

else:
    print('n')'''

        

'''
Formatando valores com modificadores - aula 5

:s
:d
:f
:.(NÚMERO)f
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''

'''n1 = 10
n2 = 3
divisao = n1 / n2
print('{:.2f}'.format(divisao))

nome = 'Fabio Leal'

print(f'{nome:.4s}')
'''
'''n1 = 1
n2 = 123881

print(f'{n1:0^3}')
print(f'{n2:0<7}')
print(f'{n2:0>10.7f}')'''
'''txt  = 'Python s2'

nova_str = txt[:6]
print(nova_str)'''
'''
while em python
'''
'''while True:
    nome = input('Qual seu nome? ')
    print(f'Olá {nome}')

print('Não')'''

'''x=0
while x <= 5:
    if x == 3:
        x += 1
        continue
    if x == 4:
        break
    print(x)
    x += 1
print('Acabou')'''

'''x =  0

while x < 5:
    y = 0
    while y < 5:
        print(f'x vale {x} e y vale {y}')
        y += 1
    x += 1'''

'''while True:
    print()
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    oper = input('Digite um operador: ')

    if not n1.isnumeric() or not n2.isnumeric():
        print('Valor inválido digite um número!')
        continue

    n1 = int(n1)
    n2 = int(n2)

    if oper == '+':
        print(n1 + n2)
    elif oper == '-':
        print(n1 - n2)
    elif oper == '*':
        print(n1 * n2)
    elif oper == '/':
        print(n1/n2)
    else:
        print('Operador inválido!')
'''
# interando strings
'''
frase = 'O rato roeu a roupa do rei de roma' # Iterável
tam_fra = len(frase)
new = ''

c = 0

input_du = input('Qual letra deseja colocar maiúscula: ')

while c < tam_fra:
    #print(frase[c], c)
    let = frase[c]
    if let == input_du:
        new +=input_du.upper()
    else:
        new += frase[c]
    c += 1
    print(new)'''
'''
FOr in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
'''
'''txt = 'Python'

for c, l in enumerate(txt):
    print(c, l)'''
'''
for n in range(32, 0, -2):
    print(n)'''
'''for n in range(100):
    if n % 8 == 0:
        print(n)'''
# continue - pula pra proxima iteração
# break - quebra o laço
'''
txt = 'Python'
nov = ''
for l in txt:
    if l == 't':
        nov += l.upper()
    elif l == 'h':
        nov += l.upper()
    else:
        nov += l
print(nov)'''
#         0   1   2    3        4    5
'''
lista = [1, 3332, 5, 'Pedro', True, 3.3]
#   -    5    4   3     2       1    0
print(lista[::-1])
lista.append('g')
print(lista)'''
'''
l1 = [1,2,3,4]
l2 = [5,6,7,8]
#l1.pop()
#l2.insert(0, 'cracha')
#l1.append('b')
#l1.extend(l2)
#l3 = l1 + l2
#print(l3)
print(l1)
print(l2)'''

''''l1 = [1,2,3,4]
l2 = [5,6,7,8]

soma = 0
for n in l1:
    soma += n

print(soma)'''
'''
li = ['Fabio', 34, 9.0, True]

for e in li:
    print(f'O tipo do {e} é {type(e)}')'''

'''
secreto = 'perfume'
dig = []
c = 2
while True:
    if c < 0:
        print('Você PERDEU!')
        break
    print(f'Você tem {c+1} chances')
    l = input('Digite um letra: ')
    
    if len(l) > 1:
        print('Não vale digitar mais letras')
        continue
    dig.append(l)
    
    if l in secreto:
        print('Boa, a letra está na palavra secreta!')
    else:
        print('Vish, essa letra não está na palavra secreta!')
        c -= 1
        dig.pop()
    
    sect = ''
    for ls in secreto:
        if ls in dig:
            sect += ls
        else:
            sect += '*'
    
    if sect == secreto:
        print('Legal Você Ganhou')
        break
    else:
        print(f'Você ja chutou: {sect}')
        print()'''

'''
For/Else em python - continue break
'''
'''
variavel = ['Luiz', 'João', 'Maria', 'Manteiga', 'maizena']

c = 0
for v in variavel:
    if v.lower().startswith('m'):
        com_com_m = True
        print('Começa com M', v)
        c += 1
    else:
        print('Não começa com M', v)
    
if c>0:
    print(f'Existe {c} palavra com M')
else:
    print('Não existe palavra que começa com M')'''