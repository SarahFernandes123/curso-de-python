nome= input("Digite o seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"O seu nome é {nome}")
    print(f"O seu nome invertido é {nome[::-1]}")
    if " " in nome: 
        print('Seu nome contém espaços')
    else:
        print("Seu nome NÃO contém espaços")

    print(f"O seu nome contém {len(nome)} letras")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")