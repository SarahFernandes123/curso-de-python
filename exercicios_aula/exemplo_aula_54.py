#None = sem valor
#is e not is = é ou não é (Tipo, valor)
# id = identidade

condição = False
passou_no_if = None

if condição:
    passou_no_if = True
    print('Faça algo')
else:
    print ('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')