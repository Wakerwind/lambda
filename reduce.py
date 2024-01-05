from functools import reduce

notas = [9.0,6.5,7.8]

media = reduce(lambda x,y: x + y,notas )

print(f'A média é: {media / len(notas):.1f}')