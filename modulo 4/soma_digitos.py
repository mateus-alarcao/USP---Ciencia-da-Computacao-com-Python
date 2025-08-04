num = int(input("Digite um número inteiro: "))
cont = len(str(num))
soma = 0

while cont != 0:
    cont -= 1
    soma += num % 10
    num //= 10

print(soma)