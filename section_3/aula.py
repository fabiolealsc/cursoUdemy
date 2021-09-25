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
def func(*args, **kwargs):
    print(args)
    print(kwargs['idade'])
    '''
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    ''''''
    args = list(args)
    args[0] = 20
    print(args)
''''''
    for v in args:
        print(v)'''

lista2 = [23,12,23,54,6,6,80]
lista = [1,2,3,4,5]
func(*lista, *lista2, nome='Fabio', idade=26)

#lista = [1,2,3,4,5]
# desenpacotando
#print(*lista)
