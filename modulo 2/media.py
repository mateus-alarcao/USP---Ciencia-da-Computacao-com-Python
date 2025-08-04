media = 0

for i in range(4):
    nota = int(input(f"Digite a {i + 1}ª nota: "))
    media += nota

media /= 4
print(f"A média aritmética é {media}")
