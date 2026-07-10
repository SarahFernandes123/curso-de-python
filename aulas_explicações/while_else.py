nome = "Qualquer valor"
i=0

while i < len(nome):
    letra = nome[i]

    print(letra)

    i+=1
else:
    print('o else foi executado')


## Quando você realiza um comando break dentro do while, o else não é executado.