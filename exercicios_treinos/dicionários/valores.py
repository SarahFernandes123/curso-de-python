'''
Considere:

produto = {
    "nome": "Tênis",
    "preco": 150,
    "quantidade": 3
}

Calcule quanto será pago se a pessoa comprar todas as unidades.


'''

produto = {
    "nome": "Tênis",
    "preco": 150,
    "quantidade": 3
}

unidade = int(input('Serão quantos produtos ao total: '))

if unidade == produto["quantidade"]:
    valor_final= produto["preco"]*produto["quantidade"]
    print(valor_final)
elif unidade < produto["quantidade"]:
    valor_final = produto["preco"]*unidade
    print(valor_final)
else:
    print('Quantidade maior do que o estoque do produto.')