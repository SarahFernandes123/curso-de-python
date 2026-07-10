'''
Empréstimo
Peça o salário.
Se o salário for maior ou igual a R$2.000, informe "Empréstimo aprovado".
Caso contrário, "Empréstimo negado".

'''
salario = input('Digite o seu salário: ')
salario_certo = float(salario)

if salario_certo >= 2000:
    print('Empréstimo aprovado')
else:
    print('Empréstimo negado')