num = int(input("Digite o valor de n: "))
fatorial = 1

while num != 0:
    fatorial *= num
    num -= 1

print(fatorial)