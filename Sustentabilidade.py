print("Sistema de Monitoramento de Sustentabilidade")

data=input("\nQual é a Data?: ")

digitou_corretamente=False
while not digitou_corretamente:
    try:
        l_agua=float(input("\nQuantos litros de água você consumiu hoje? (Aprox. em litros): "))
    except ValueError:
        print("Digitar apenas números!")
    else:
        digitou_corretamente=True

        if l_agua <150:
            agua_susten="Alta sustentabilidade"
        elif l_agua <= 150 or l_agua <=200:
            agua_susten="Moderada Sustentabilidade"
        elif l_agua > 220:
            agua_susten="Baixa Sustentabilidade"

digitou_corretamente2=False
while not digitou_corretamente2:
    try:
        energia=float(input("\nQuantos kWh de energia elétrica você consumiu hoje?: "))
    except ValueError:
        print("Digitar apenas números!")
    else: 
        digitou_corretamente2=True

        if energia < 5:
            energia_susten="Alta Sustentabilidade"
        elif energia <=5 or energia<=10:
            energia_susten="Moderada Sustentabilidade"
        elif energia > 10:
            energia_susten="Baixa Sustentabilidade"


print("Sistema de Monitoramento de Sustentabilidade")

data=input("\nQual é a Data?: ")

digitou_corretamente3=False
while not digitou_corretamente3:
    try: 
        kg_residuos=float(input("\nQuantos kg de resíduos não recicláveis você gerou hoje?: "))
    except ValueError:
        print("Digitar apenas números válidos!")
    else:
        digitou_corretamente3=True

digitou_corretamente4=False
while not digitou_corretamente4:
    try:
        por_residuos=float(input("\nQual a porcentagem de resíduos reciclados no total (em %)?: "))
    except ValueError:
        print("Apenas números válidos!")
    else:
        digitou_corretamente4=True
print("\n---------------SUSTENTABILIDADE---------------")
print("\nConsumo de Água: ",agua_susten,"com ",l_agua,"litros")
print("\nConsumo de Energia: ",energia_susten,"com ",energia,"Kwh")
print("\nGeração de Resíduos Não Recicláveis: ",por_residuos_susten,"com porcentagem de: ",por_residuos)
#print("\nUso de transportes foi de: ",sustentabilidade)
print()
#print("Uso de Transporte: ",transport)
