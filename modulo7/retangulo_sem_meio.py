largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

if largura == 2 or altura == 2:
    for x in range(0, altura):
        print('#' * largura)
else:
    for x in range(0, altura):
        if x == 0 or x == altura - 1:
            print('#' * largura)
        else:
            print('#', ' ' * (largura - 4), '#')