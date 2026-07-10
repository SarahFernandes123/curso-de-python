"""
Temperatura
Peça a temperatura.
Se for maior ou igual a 30°C, mostre "Está quente".
Caso contrário, "Está agradável ou frio".

"""

temperatura = input('Digite a temperatura em °C: ')
temperatura_certa = float(temperatura)

if temperatura_certa >= 30:
    print('Está quente')
else:
    print('Clima está agradável')
