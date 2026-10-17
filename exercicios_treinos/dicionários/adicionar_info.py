'''
Considere:

carro = {
    "marca": "Toyota",
    "modelo": "Corolla"
}

Adicione uma nova chave chamada "ano" com o valor 2024.

'''

carro = {
    "marca": "Toyota",
    "modelo": "Corolla"
}

carro.update(
    {
        'ano': 2024
    }
)

print(carro)