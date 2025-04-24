digitou_corretamente7 = False
while not digitou_corretamente7:
    resposta = input("Você costuma caminhar como meio de transporte? (S/N): ").upper()
    if resposta in ['S', 'N']:
        caminhada = resposta == 'S'
        digitou_corretamente7 = True
    else:
        print("Entrada inválida. Digite apenas 'S' para Sim ou 'N' para Não.")

digitou_corretamente8 = False
while not digitou_corretamente8:
    resposta = input("Você usa carro com combustível fóssil? (S/N): ").upper()
    if resposta in ['S', 'N']:
        carro_fossil = resposta == 'S'
        digitou_corretamente8 = True
    else:
        print("Entrada inválida. Digite apenas 'S' para Sim ou 'N' para Não.")

digitou_corretamente9 = False
while not digitou_corretamente9:
    resposta = input("Você usa carro elétrico? (S/N): ").upper()
    if resposta in ['S', 'N']:
        carro_eletrico = resposta == 'S'
        digitou_corretamente9 = True
    else:
        print("Entrada inválida. Digite apenas 'S' para Sim ou 'N' para Não.")
        
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