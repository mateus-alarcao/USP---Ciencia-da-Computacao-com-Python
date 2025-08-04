def remove_repetidos(lista):
    lista_ordenada = sorted(lista)
    lista_nova = []

    for elemento in lista_ordenada:
        if elemento not in lista_nova:
            lista_nova.append(elemento)
            
    print(lista_nova)
    return lista_nova
