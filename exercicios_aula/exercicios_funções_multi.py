"""
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""
## Forma maior de resolver
def duplicar(numero):
    return numero *2

def triplicar(numero):
    return numero *3

def quadruplicar(numero):
    return numero *4

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

## Forma menor e mais fácil de resolver

def criar_multiplicador(multiplicador):  #definir o multiplicador
    def multiplicar(numero):  #definir o número
        return numero * multiplicador   #definição do retorno da função
    return multiplicar

duplicar_1 = criar_multiplicador(2)
triplicar_1 = criar_multiplicador(3)
quadruplicar_1 = criar_multiplicador(4)

print(duplicar_1(2))
print(triplicar_1(2))
print(quadruplicar_1(2))