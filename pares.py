'''
O filter Retorna só os elementos que satisfaçãm a condição da função...
aplicada em cada elemento da lista

'''

valores = [8,99,65,12,0,7,2,12]

pares = list(filter(lambda x: x % 2 == 0,valores))
print('Os números pares da lista são: ',pares)