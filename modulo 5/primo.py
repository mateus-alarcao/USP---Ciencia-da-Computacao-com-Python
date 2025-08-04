def maior_primo(k):
    if k <= 2:
        return None

    else:
        while k >= 2:
            cont = 2
            primo = True

            while cont < k:
                if k % cont == 0:
                    primo = False
                cont += 1

            if primo:
                print(k)
                return k
            else:
                k -= 1
