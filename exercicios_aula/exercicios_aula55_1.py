"""
Faça um programa que peça ao usuário para digitar um numero inteiro, informe se esse número é impar ou par. 
Caso o usuário digite um número não inteiro, informe que o número não é inteiro.

"""

numero = (input('Digite um número inteiro:  '))

if numero.isdigit():
    numero_int =int(numero)
    par_impar = numero % 2 == 0
    par_impar_texto = "impar"

    if par_impar:
        par_impar_texto: "par"

    print(f"O numero {numero_int} é {par_impar_texto}")
else: 
    print("Você não digitou um numero inteiro")

try:
    numero_int =int(numero)
    par_impar = numero % 2 == 0
    par_impar_texto = "impar"

    if par_impar:
        par_impar_texto: "par"

    print(f"O numero {numero_int} é {par_impar_texto}")
except: 
    print("Você não digitou um numero inteiro")





