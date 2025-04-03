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
        elif l_agua > 200:
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

        if por_residuos >50 :
            por_residuos_susten="Alta Sustentabilidade"
        elif por_residuos <=20 or por_residuos <=50: 
            por_residuos_susten="Moderada Sustentabilidade"
        elif por_residuos <20: 
            por_residuos_susten="Baixa Sustentabilidade"

digitou_corretamente5=False
while not digitou_corretamente5:
    try:
        transporte_publico = input("\nVocê usa transporte público (ônibus, metrô, trem)? (S/N): ").strip().upper()
    except ValueError:
        print("Apenas letras maiúsculas ou S/N")
    else:
        digitou_corretamente5=True

digitou_corretamente6=False
while not digitou_corretamente6:
    try:
        bicicleta = input("Você usa bicicleta? (S/N): ")
    except ValueError:
        print("Apenas letras maiúsculas ou S/N")
    else:
        digitou_corretamente6=True
        
digitou_corretamente7=False
while not digitou_corretamente7:
    try:
        caminhada = input("Você costuma caminhar como meio de transporte? (S/N): ").strip().upper()
    except ValueError: 
        print("Apenas letras maiúsculas ou S/N")
    else:
        digitou_corretamente7=True

digitou_corretamente8=False
while not digitou_corretamente8:
    try:
        carro_fossil = input("Você usa carro com combustível fóssil? (S/N): ").strip().upper()
    except ValueError: 
        print("Apenas letras maiúsculas ou S/N")
    else:
        digitou_corretamente8=True
digitou_corretamente9=False
while not digitou_corretamente9:
    try:
        carro_eletrico = input("Você usa carro elétrico? (S/N): ").strip().upper()
    except ValueError:
        print("Apenas letras maiúsculas ou S/N")
    else:
        digitou_corretamente9=True

digitou_corretamente10=False
while not digitou_corretamente10:
    try:   
        carona_fossil = input("Você usa carona compartilhada com carro a combustíveis fósseis? (S/N): ").strip().upper()
    except ValueError:
        print("Apenas letras maiúsculas ou S/N ")
    else: 
        digitou_corretamente10=True

    usa_transporte_publico = transporte_publico == "S"
    usa_bicicleta = bicicleta == "S"
    usa_caminhada = caminhada == "S"
    usa_carro_fossil = carro_fossil == "S"
    usa_carro_eletrico = carro_eletrico == "S"
    usa_carona_fossil = carona_fossil == "S"

    if (usa_transporte_publico or usa_bicicleta or usa_caminhada) and usa_carro_eletrico:
        sustentabilidade = "Alta sustentabilidade"
    elif usa_transporte_publico or usa_carro_eletrico:
        sustentabilidade = "Moderada sustentabilidade"
    elif usa_carro_fossil or usa_carona_fossil:
        sustentabilidade = "Baixa sustentabilidade"
    else:
        sustentabilidade = "Sustentabilidade não definida"


print("\n---------------SUSTENTABILIDADE---------------")
print("\nConsumo de Água: ",agua_susten,"com ",l_agua,"litros")
print("\nConsumo de Energia: ",energia_susten,"com ",energia,"Kwh")
print("\nGeração de Resíduos Não Recicláveis: ",por_residuos_susten,"com porcentagem de: ",por_residuos)
print("\nUso de transportes foi de: ",sustentabilidade)
print()
print("Uso de Transporte: ",transport)
