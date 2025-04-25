print("Sistema de Monitoramento de Sustentabilidade")

#Entrada de dia, mês e ano, e validações
#--------------------------------------

digitou_nome=False
while not digitou_nome:
    usuario = input("\nDigite seu nome (até 45 caracteres): ").strip()
    if len(usuario) == 0:
        print("O nome não pode estar vazio!")
    elif len(usuario) > 45:
        print("O nome deve ter no máximo 45 caracteres!")
    else:
        digitou_nome=True
        
while True:
    try:
        dia = int(input("\nDigite o dia: "))
        if dia < 1 or dia > 31:
            print("Valor inválido para dia!")
            continue
        break
    except ValueError:
        print("O dia deve ser um valor inteiro!")

while True:
    try:
        mes = int(input("Digite o mês: "))
        if mes < 1 or mes > 12:
            print("Valor inválido para mês!")
            continue
        break
    except ValueError:
        print("O mês deve ser um valor inteiro!")

while True:
    try:
        ano = int(input("Digite o ano: "))
        if ano < -45:
            print("Este programa não valida datas com anos anteriores a 46ac, antes do calendário juliano!")
            continue
        if ano == 0:
            print("Não existiu ano 0!")
            continue
        break
    except ValueError:
        print("O ano deve ser um valor inteiro!")
    
data = f"{dia:02d}/{mes:02d}/{ano}"

'''----------------\\COMEÇO SUSTENTABILIDADE\\----------------'''

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
        kg_residuos=float(input("\nQuantos kg de resíduos não recicláveis você gerou hoje? Se for em gramas, preencha '0.!!!': "))
    except ValueError:
        print("Digitar apenas números válidos!")
    else:
        digitou_corretamente3=True

        if kg_residuos <= 0.770: #770 gramas
            kg_residuos_susten="Alta Sustentabilidade"
        elif kg_residuos <= 0.770 or kg_residuos <=1.54: 
            kg_residuos_susten="Moderada Sustentabilidade"
        elif kg_residuos > 1.54:
            kg_residuos_susten="Baixa Sustentabilidade"

digitou_corretamente4=False
while not digitou_corretamente4:
    try:
        por_residuos=float(input("\nQual a porcentagem de resíduos reciclados no total (em %)?: "))
    except ValueError:
        print("Apenas números válidos!")
    else:
        digitou_corretamente4=True

        if por_residuos <20 :
            por_residuos_susten="Baixa Sustentabilidade"
        elif por_residuos <=20 or por_residuos <= 50: 
            por_residuos_susten="Moderada Sustentabilidade"
        elif por_residuos > 50: 
            por_residuos_susten="Alta Sustentabilidade"

        
"""----------------------///BANCO DE DADOS///----------------------"""
# Conexão com o banco e gravação dos dados
import pymysql

# Conecta banco de dados
conexao = pymysql.connect(
    host="127.0.0.1",
    user="root",         
    password="Samu25052006*",       
    database="sustentabilidade"
)

#Para enviar comandos sql para banco
cursor = conexao.cursor()

# formato MySQL (yyyy-mm-dd)
data_mysql = f"{ano}-{mes:02d}-{dia:02d}"

sql = """
INSERT INTO sistema (
    usuario, data, l_agua, energia, kg_residuos, por_residuos,
    transporte_publico, bicicleta, caminhada, carro_fossil,
    carro_eletrico, carona_fossil
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""

valores = (
    usuario,
    data_mysql,
    l_agua,
    energia,
    kg_residuos,
    por_residuos,
    'Sim' if transporte_publico else 'Nao',
    'Sim' if bicicleta else 'Nao',
    'Sim' if caminhada else 'Nao',
    'Sim' if carro_fossil else 'Nao',
    'Sim' if carro_eletrico else 'Nao',
    'Sim' if carona_fossil else 'Nao'
)

# Executar e confirmar dados no banco
cursor.execute(sql, valores)
conexao.commit()

print("---------------DADOS INSERIDOS!")

#   Calcula das medias
cursor.execute(""" 
    select 
        AVG(l_agua),
        AVG(energia),
        AVG(kg_residuos),
        AVG(por_residuos)
    from sistema
""")

#Pegando a linha de cada informações no banco para média
#.2f: Deixar o numero decimal com virgula
for row in cursor:
    media_agua = row[0]
    media_energia = row[1]
    media_residuos = row[2]
    media_residuos_reciclaveis = row[3]

    print("\n---------------MÉDIAS DOS DADOS DO BANCO---------------")
    print(f"\nMédia de Consumo de Água: {media_agua:.2f} litros")
    print(f"Média de Consumo de Energia: {media_energia:.2f} KWh")
    print(f"Média de Resíduos Não Recicláveis: {media_residuos:.2f} KG")
    print(f"Média de Resíduos Recicláveis: {media_residuos_reciclaveis:.2f} %")

cursor.close()
conexao.close()