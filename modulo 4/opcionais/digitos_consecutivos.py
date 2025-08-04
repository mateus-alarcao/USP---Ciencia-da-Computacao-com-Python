num = int(input('Digite um número inteiro: '))
string = str(num)
cont = len(str(num)) - 1

while cont > 0:
    if string[cont] == string[cont - 1]:
        print('sim')
        break
    cont -= 1
else:
    print('não')