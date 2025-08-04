num = int(input('Digite um número inteiro: '))
contador = 2
primo = True

while contador < num:
    if num % contador == 0:
        primo = False
    contador += 1

if primo == True:
    print('primo')
else:
    print('não primo')