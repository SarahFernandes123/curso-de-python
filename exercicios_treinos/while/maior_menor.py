'''
Peça números até o usuário digitar 0.

No final informe:

maior número
menor número
'''
# Inicializamos as variáveis como None para saber quando o primeiro número for digitado
maior = None
menor = None

while True:
    numero = input('Digite um número: ')
    num_certo = int(numero)
    
    # Condição de parada
    if num_certo == 0:
        break
    # Se for o primeiro número digitado, ele é tanto o maior quanto o menor
    if maior is None and menor is None:
        maior = num_certo
        menor = num_certo
    else:
        # Verifica se o número atual é maior que o maior guardado
        if num_certo > maior:
            maior = num_certo
        # Verifica se o número atual é menor que o menor guardado
        if num_certo < menor:
            menor = num_certo

print ("-"* 30)

# Verifica se o usuário digitou algum número válido antes do 0
if maior is not None:
    print('O maior número digitado foi:',maior)
    print('O menor número digitado foi:',menor)
else:
    print('Nenhum número válido (diferente de 0) foi digitado.')