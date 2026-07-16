# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

multiplica = multiplicar(1,2,3)
print(multiplica)


### Crie uma função que fala se um número é par ou impar.


def par_impar(numero):
    multiplo_dois = numero %2 == 0

    if multiplo_dois:
        return f'{numero} é par'
   
    return f'{numero} é impar'

print(par_impar(5))
print(par_impar(9))