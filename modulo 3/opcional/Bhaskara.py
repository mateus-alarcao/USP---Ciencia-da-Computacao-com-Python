a = int(input())
b = int(input())
c = int(input())

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    x = -b / (2 * a)
    print(f'a raiz desta equação é {x}')
else:
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    raiz1 = min(x1, x2)
    raiz2 = max(x1, x2)
    print(f'as raízes da equação são {raiz1} e {raiz2}')
