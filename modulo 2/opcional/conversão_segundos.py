segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = segundos // 86400
resto_segundos = segundos % 86400

horas = resto_segundos // 3600
resto_segundos %= 3600

minutos = resto_segundos // 60
resto_segundos %= 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {resto_segundos} segundos.")