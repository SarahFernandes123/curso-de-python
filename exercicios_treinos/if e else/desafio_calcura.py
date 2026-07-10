"""
Calculadora simples
Peça dois números e uma operação (+, -, * ou /).
Se a operação for "+", faça a soma.
Caso contrário, faça a divisão.

"""

numero_1= input("Digite um número: ")
numero_2 = input('Digite um segundo número: ')
operador = input('Escolha qual operador deseja: (+, -, *, /)')

numero_1_certo = float(numero_1)
numero_2_certo = float(numero_2)

if operador == "+":
    print(f'{numero_1_certo}+{numero_2_certo} =', numero_1_certo + numero_2_certo)
elif operador == '-':
    print(f'{numero_1_certo}+{numero_2_certo}=', numero_1_certo - numero_2_certo)
elif operador == '*':
    print(f'{numero_1_certo}*{numero_2_certo}=', numero_1_certo*numero_2_certo)
else:
    print(f'{numero_1_certo}/{numero_2_certo}=', numero_1_certo/numero_2_certo)