x1 = int(input('x do primeiro ponto: '))
y1 = int(input('y do primeiro ponto: '))
x2 = int(input('x do segundo ponto: '))
y2 = int(input('y do segundo ponto: '))

distancia = ((x1 - x2) ** 2 + (x2 - y2) ** 2) ** 0.5

if distancia >= 10:
    print('longe')
else:
    print('perto')