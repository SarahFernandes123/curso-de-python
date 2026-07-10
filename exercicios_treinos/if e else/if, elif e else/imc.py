"""
 IMC

Peça:

peso;
altura.

Calcule o IMC.

Mostre:

Menor que 18.5 → Abaixo do peso
18.5 até 24.9 → Peso normal
25 até 29.9 → Sobrepeso
30 ou mais → Obesidade

"""

peso = input('Digite o seu peso: ')
altura = input('Digite sua altura: ')

peso_certo = float(peso)
altura_certo = float(altura)
imc = peso_certo / altura_certo ** 2

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso normal')
elif 25 <= imc < 30:
    print('Sobrepeso')
else:
    print('Obesidade')