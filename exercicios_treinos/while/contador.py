'''
Conte quantos números o usuário digitou até informar 0.

'''

contador = 0

while True:
    numero = input('Digite um número: ')
    num_digitados = int(numero)
    contador +=1

    if num_digitados == 0:
        print('A quantidade total de números digitados foi de:',contador)
        break 
