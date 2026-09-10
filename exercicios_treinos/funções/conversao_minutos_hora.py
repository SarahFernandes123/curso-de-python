'''
Crie uma função converter_minutos() que receba uma quantidade de minutos e retorne quantas horas e minutos ela representa.

'''

def converter_minutos(minutos):
    horas = minutos //60
    minutos_restantes = minutos %60
    return f'Falta {horas} hora e {minutos_restantes} minutos. '

print(converter_minutos(60))


# Outra forma de resolver 


def conv_min(minutos):
    horas1 = minutos //60
    minutos_restantes1 = minutos%60

    return horas1, minutos_restantes1


tempo = float(input('Digite a quantidade de minutos para converter: '))
horas1, minutos = conv_min(tempo) 

print(f'{horas1} horas e {minutos} minutos')