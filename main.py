# O quadrado de todos os elementos de uma lista

lista = [4,5,2,8,3]
'''
O map aplica uma função a todos os elementos de uma sequencia(lista,Tupla)
Map recebe como parâmetro a função a ser aplicada e a lista em que ele vai aplicar a função
map(função, lista1, lista2, listaN...)
'''

'''O map retorna um objeto de listo por isso usamos o list antes dele...
para que ou retornou sejua uma lista normal'''

print(f'O quadrado dos elmentos: {list(map(lambda x: x**2,lista))}')


'''
É mais rápido usar o lambda doque definir primeiro uma função e usar depois
'''

