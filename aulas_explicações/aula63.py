"""
While é um laço de repetição, até que seja verdadeiro continua sendo repetido a condição.

break interrompe o código do while imediatamente
continue faz com que seja "pulado" a condição informada.

"""

contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        continue 

    print(contador)

    if contador == 40:
        break

print("Acabou")