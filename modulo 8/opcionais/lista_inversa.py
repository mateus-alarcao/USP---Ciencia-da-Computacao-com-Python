lista = []

while True:
    res = int(input('Digite um número: '))
    if res == 0:
        break
    else:
        lista.append(res)

print(lista[::-1])