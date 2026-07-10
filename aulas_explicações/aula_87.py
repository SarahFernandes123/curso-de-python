"""
exibir os indices da lista

"""

lista = ["João", 'Maria', 'Antonio']

indices = range (len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))