'''
    Funtion- def
'''
'''
def funcao():
    print('Olá Mundo')

for i in range(40):
    funcao()'''

'''def a(msg='Oi', nome='Usuário'):
    nome, msg = nome.replace('e', '3'), msg.replace('e', '3')
    nome, msg = nome.replace('a', '4'), msg.replace('a', '4')
    nome, msg = nome.replace('i', '1'), msg.replace('i', '1')
    nome, msg = nome.replace('o', '0'), msg.replace('o', '0')
    print(msg, nome)

a(nome='Zé', msg='Hi')
a('Oi', 'Marcos')
a('Hello', 'Pedro')
a('Ola', 'Fabio')
a()'''

'''def func(var):
    return var

variavel = func('Ola mundo')

if variavel:
    print(variavel)
else:
    print('nada')'''

'''def div(n1,n2=1):
    if n2 == 0:
        return
    return n1/n2

divid = div(3,4)

if not divid:
    print('Divisão por 0 não eh permitida')
else:
    print(divid)'''

'''def f(var):
    print(var)

def dumb():
    return f

''''''var = dumb()('Ola mundo')
print(dumb(), type(dumb()))'''
'''var = dumb()
var('olaMundo')
print(id(var), id(f))
if var == f:'''
'''   print('var é igual a f')'''

'''
Exercício 1
'''
'''def ola(msg='Oi', nome='Estranho'):
    print(msg, nome)

ola('Hello','Pedro')'''

'''
Exercício 2
'''
'''def soma(n1=0, n2=0, n3=0):
    return n1 + n2 + n3

print(soma(2,4,2))'''

'''
Exercício 3
'''
'''def func(n1, n2=0):
    return n1+(n1*(n2/100))

print(func(500, 50))'''

'''
Exercício 4
'''
'''def func(n):
    if n % 3 == 0:
        if n % 5 == 0:
            return 'FizzBuzz'
        return 'fizz'
    if n % 5 == 0:
        return 'Buzz'    
    return n

print(func(4))'''
'''#sempre que definir um padrão para um argumento os proximos argumentos tenque ser definidos padroes
def func(n1,n2,n3,n4,n5,n6=None, n7=None):
    print(n1,n2,n3,n4,n5, n6, n7)

# se chamar um argumento passando um valor a ele, os proximos argumento tenque ser passados.
func(1,2,3,4,5, n6='Pedro', n7=5)'''
'''
def func(*args, **kwargs):
    print(args)
    print(kwargs['idade'])
   
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    
    args = list(args)
    args[0] = 20
    print(args)

for v in args:
        print(v)
    
'''


'''lista2 = [23,12,23,54,6,6,80]
lista = [1,2,3,4,5]
func(*lista, *lista2, nome='Fabio', idade=26)
'''
#lista = [1,2,3,4,5]
# desenpacotando
#print(*lista)
'''
Escopo global e local
'''
'''def func():
    print(variavel)

def func2(arg=None):
    #global variavel
    arg = arg.replace('v', 'c')
    return arg

func()
outraVariavel = func2(arg=variavel)
print(outraVariavel)
'''
'''def func():
    #print(variavel)
    outraVariavel = 'Valor2'
    variavel = 1234
    print(variavel)
    return outraVariavel

def func2(arg):
    print(arg)

var=func()
func2(var)'''

'''def olaMundo():
    return 'Olá Mundo!'

def mestre(func):
    return func()

exe = mestre(olaMundo)'''
'''
def mestre(func, *args, **kwargs):
    return func(*args, **kwargs)

def falaOi(nome):
    return f'Oi {nome}'

def sauda(nome, saud):
    return f'{saud} {nome}'

exe = mestre(sauda, 'Luiz', saud='olá')
print(exe)'''

'''def func(arg, arg2):
    return arg * arg2

var = func(2,2)
print(var)'''

#a = lambda x, y: x * y
#print(a(2,2))

'''li = [
['P1', 13],
['P2', 6],
['P3', 4],
['P4', 59],
['P5', 9],
]
#li.sort(key=lambda item: item[0], reverse=True)
print(sorted(li, key=lambda i:i[1], reverse=True))
print(li)'''

'''t1 = 1,2,3,4,5,'a', 'Fabio'
t2 = 2,
t3 = t1 + t2
n1,n2,n3, *_, nom = t3
print(t1[0:4], type(t1))
print(t2, type(t2))
print(t3)
print(n3)
print(nom)'''
'''
t1 = (1,2,3,4,5,6)
t1 = list(t1)
t1[1] = 1000
t1 = tuple(t1)
print(t1)
'''
'''perguntas = {
    'Pergunta 1':{
        'pergunta': 'Quando é 2+2?',
        'respostas': {'a':'1','b':'6','c':'4','d':'5',},
        'resposta_certa':'c',
    },
    'Pergunta 2':{
        'pergunta': 'Quando é 25+2?',
        'respostas': {'a':'27','b':'29','c':'30','d':'23',},
        'resposta_certa':'a',
    },
}
resp_certo = 0
for cp, cr in perguntas.items():
    print(f'{cp}: {cr["pergunta"]}')
    print('Resposta: ')
    for rr, rv in cr['respostas'].items():
        print(f'[{rr}]: {rv}')
    resp = input('Sua resposta: ')
    if resp == cr['resposta_certa']:
        print('Acertou á mizeravel')
        resp_certo += 1
    else:
        print('Errouuu!')    
    print()
print(f'Você acertou {resp_certo} perguntas')'''
'''
set1 = {1,2,3,4,5,6}
set1.update((1,2,3,4,4,(213,34,34)))
set1.update('Python')
set1.add(4)
for v in set1:
    print(v)'''

'''
union | une
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^(Elementos que estão nos dois sets, mas não em ambos)
'''
'''s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 ^ s2

print(s3)'''

'''l1=['Luiz', 'João', 'Maria']
l2=['João', 'Luiz','Maria', 'Luiz', 'Luiz', 'Luiz', 'Luiz']

l1 = set(l1)
l2 = set(l2)

print(l1 == l2)'''
'''
l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]
print(ex1)
ex2 = [v * 2 for v in l1]
print(ex2)
ex3 = [(v, v2)for v in l1 for v2 in range(3)]
print(ex3)
l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l2]
print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(y,x)for x,y in tupla]
ex5 = dict(ex5)
print(ex5['valor2'])

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex6)
ex7 = [v if v % 3 == 0 and v % 8 == 0 else "#" for v in l3]
print(ex7)'''
'''
string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
lista = [string[i:i+10] for i in range(0, len(string), 10)]
retorno = '.'.join(lista)
print(lista)
print(retorno)
'''
'''l1 = [1,2,3,4,5]
l2 = [v*2 for v in l1]
print(l2)''''''
lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]
d1 = {f'chave_{x}': x**2 for x in range(5)}
#d1 = dict(lista)
print(d1)'''

'''import sys
import time
def gera():
    variavel  = 'valor1'
    yield variavel
    variavel  = 'valor2'
    yield variavel
    variavel  = 'valor3'
    yield variavel

g = gera()

for v in g:
    print(g)'''
'''import sys

l1 = [x for x in range(1000000)]
l2 = (x for x in range(1000000))
for v in l2:
    print(v)'''
# lists, tuples, str - sequences - iterável
#nome = 'Luiz Otávio'
#itr = iter(nome)

'''carrinho = []

carrinho.append(("produto_1", 30))
carrinho.append(("produto_2", 20))
carrinho.append(("produto_3", 13))


total = sum([float(x) for t,x in carrinho])
print(total)'''
'''
Zip - Unindo iteráveis
Zip_longest - Itertools
'''
'''from itertools import zip_longest, count

#código

ind = count()

cidade = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    ind,
    estados,
    cidade,
    
)

for ind, est, cid in cidades_estados:
    print(ind, est, cid)
'''
'''list_a = [1,2,3,4,5,6,7,8]
list_b = [1,2,3,4]

print([x+y for x,y in list(zip(list_a, list_b))])'''

'''
count - Itertools
'''
'''from itertools import count
'''
#contador = count(start=20, step=-0.5)
'''
for i in contador:
    print(round(i, 2))
    if (i<-20):
        break'''
'''
lista = ['Luiz', 'Maria', 'Pedro', 'João']
cont = count(start=0,step=10)

lista = zip(cont, lista)
print(list(lista))'''

from itertools import combinations, permutations, product, repeat

#pessoas =['Luiz', 'Pedro', 'Augusto', 'Melani', 'Maria', 'Gustavo', 'Pereira']
n = [0,1]
h = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','f']
t = [t for t in product(h, repeat=3)]
c = 0
for grupo in product(n, repeat=8):
    print(f'{grupo} = {c} = {t[c]}')
    c += 1

