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

'''l1 = [1,2,3,4,5,6,7,8,9]
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
print(l3)'''
