velocidade = 61 #velocidade atual do carro 
local_carro = 99 #local que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 # local do radar 1 está na estrada 
RADAR_RANGER = 1 #a distância onde o radar pega

#FORMA MAIS EXTENSA DE FAZER:
if velocidade > RADAR_1:
    print("Velocidade do carro passou do permitido")

if local_carro <=(LOCAL_1+RADAR_RANGER) and local_carro >=(LOCAL_1-RADAR_RANGER) and velocidade>RADAR_1:
    print('O carro foi multado no radar 1')

#FORMA MAIS LEVE DE FAZER:
velocidade_carro_maior_radar = velocidade>RADAR_1
carro_multado_radar_1 = local_carro>=(LOCAL_1-RADAR_RANGER) and local_carro<=(LOCAL_1+RADAR_RANGER)

if velocidade_carro_maior_radar:
    print("Velocidade do carro passou do permitido")

if carro_multado_radar_1 and velocidade_carro_maior_radar:
    print('O carro foi multado no radar 1')

#FORMA AINDA MAIS ENXUTA DO CÓDIGO
velocidade_carro_maior_radar = velocidade>RADAR_1
carro_passou_radar_1 = local_carro>=(LOCAL_1-RADAR_RANGER) and local_carro<=(LOCAL_1+RADAR_RANGER)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_maior_radar

if velocidade_carro_maior_radar:
    print("Velocidade do carro passou do permitido")

if carro_passou_radar_1:
    print("Carro passou no radar 1")

if carro_multado_radar_1:
    print('O carro foi multado no radar 1')