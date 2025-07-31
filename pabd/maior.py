import datetime
import flask

a = float(input("1º número: "))
b = float(input("2º número: "))

if a > b:
    print('O maior número é: ', a)
else:
    print('O maior número é: ', b)

print(f'Agora é {datetime.datetime.now()}')