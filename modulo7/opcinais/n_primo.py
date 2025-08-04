def e_primo(num):
    if num < 2:
        return False
    else:
        for x in range(2, num):
            if num % x == 0:
                return False
        return True


def n_primos(n):
    cont = 0
    for x in range(2, n):
        if e_primo(x):
            cont += 1
    print(cont)
    return cont

n_primos(4)