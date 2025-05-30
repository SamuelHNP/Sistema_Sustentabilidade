import re

#O PROGRAMA FOI FEITO POR TODOS OS PARTICIPANTES DO GRUPO!#

#Entrada de dia, mês e ano, e validações
#--------------------------------------
def menu():
    print("\n")
    print('+-------------------------------------------------------------+')
    print('|        SISTEMA DE MONITORAMENTO DE SUSTENTABILIDADE         |')
    print('|-------------------------------------------------------------|')
    print('| 1 - Cadastrar parâmetros diários de sustentabilidade        |')
    print('| 2 - Atualizar parâmetros diários de sustentabilidade        |')
    print('| 3 - Excluir parâmetros diários de sustentabilidade          |')
    print('| 4 - Classificar sustentabilidade (Listar Registros)         |')
    print('| 5 - Classificar sustentabilidade (Calcular Médias)          |')
    print('| 0 - Sair do sistema                                         |')
    print('+-------------------------------------------------------------+')

# Conecta banco de dados
def conectar():
    import mysql.connector

    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Samu25052006*",
        database="sustentabilidade"
    )
    cursor = conexao.cursor()
    return conexao

padrao_de_nome = re.compile(r'^[A-Z][a-z]*(?: (?:[A-Z]|[a-z])[a-z]*)*$')

def cadastrar():
    conexao = conectar()
    cursor = conexao.cursor()
    
    while True:
        usuario = input("\nDigite seu nome (até 45 caracteres): ").strip()
        if len(usuario) == 0:
            print("O nome não pode estar vazio!")
        elif len(usuario) > 45:
            print("O nome deve ter no máximo 45 caracteres!")
        elif not padrao_de_nome.match(usuario):
            print("Nome inválido! Use letras com iniciais maiúsculas. Ex: Marcos Felipe")
        else:
            break 
        
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
            elif dia > 30 and mes in [4, 6, 9, 11]:
                    print("Este mês tem apenas 30 dias.")
            elif mes == 2 and dia > 29:
                    print("Fevereiro não possui esse dia.")
            else:
                break
        except ValueError:
            print("O mês deve ser um valor inteiro!")

    while True:
        try:
            ano = int(input("Digite o ano: "))
            if ano < -45:
                print("Este programa não valida datas com anos anteriores a 46ac, antes do calendário juliano!")
            elif ano == 0:
                print("Não existiu ano 0!")
            elif ano >= 2026:
                print("\nAno Inválido")
            elif mes == 2 and dia == 29:
                bissexto = (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0))
                if not bissexto:
                    print("Este ano não é bissexto, fevereiro tem no máximo 28 dias.")
                else:
                    break
            else:
                break
        except ValueError:
            print("O ano deve ser um valor inteiro!")

    data_mysql = f"{ano}-{mes:02d}-{dia:02d}"

#---------------------------------------------\\COMEÇO SUSTENTABILIDADE\\#---------------------------------------------
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

    pergunta_sim_nao(usuario, dia, mes, ano, l_agua, energia, kg_residuos, por_residuos,
                     agua_susten, energia_susten, kg_residuos_susten, por_residuos_susten,
                     data_mysql, conexao, cursor)

#---------------------------------------------SIM/NÃO SUSTENTABILIDADE---------------------------------------------#
   
def pergunta_sim_nao(usuario, dia, mes, ano, l_agua, energia, kg_residuos, por_residuos,
                     agua_susten, energia_susten, kg_residuos_susten, por_residuos_susten,
                     data_mysql, conexao, cursor):
    digitou_corretamente5 = False
    while not digitou_corretamente5:
        resposta = input("\nVocê usa transporte público (ônibus, metrô, trem)? (S/N): ").upper()
        if resposta in ['S', 'N']:
            transporte_publico = resposta == 'S'
            digitou_corretamente5 = True
        else:
            print("Entrada inválida. Digite apenas 'S' para Sim ou 'N' para Não.")

    digitou_corretamente6 = False
    while not digitou_corretamente6:
        resposta = input("Você usa bicicleta? (S/N): ").upper()
        if resposta in ['S', 'N']:
            bicicleta = resposta == 'S'
            digitou_corretamente6 = True
        else:
            print("Entrada inválida. Digite apenas 'S' para Sim ou 'N' para Não.")

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

    digitou_corretamente10 = False
    while not digitou_corretamente10:
        resposta = input("Você usa carona compartilhada com carro a combustíveis fósseis? (S/N): ").upper()
        if resposta in ['S', 'N']:
            carona_fossil = resposta == 'S'
            digitou_corretamente10 = True
        else:
            print("Entrada inválida. Digite apenas 'S' para Sim ou 'N' para Não.")

    sustentavel = 0
    naoSustentavel = 0

#Se usar, irá acrecentar mais 1, para que no final possa ser classificado
    if transporte_publico:
        sustentavel += 1
    if bicicleta:
        sustentavel += 1
    if caminhada:
        sustentavel += 1
    if carro_fossil:
        naoSustentavel += 1
    if carro_eletrico:
        sustentavel += 1
    if carona_fossil:
        naoSustentavel += 1

    print("\n---------------SUSTENTABILIDADE---------------")
    print("\nNome do Usúario: ",usuario)
    print("Data: ",dia,"/",mes,"/",ano)
    print("\nConsumo de Água: ",agua_susten,"com ",l_agua,"litros")
    print("\nConsumo de Energia: ",energia_susten,"com ",energia,"Kwh")
    print("\nGeração de Resíduos não Recicláveis por KG: ", kg_residuos_susten,"com", kg_residuos, "KG")
    print("\nGeração de Resíduos Recicláveis: ",por_residuos_susten,"com porcentagem de ",por_residuos,"%")

    if sustentavel == 0 and naoSustentavel == 0:
        print("\nSustentabilidade Indefinida")
    elif sustentavel >= 1 and naoSustentavel == 0:
        print("\nUso de transporte: Alta sustentabilidade")
    elif sustentavel == 0 and naoSustentavel >= 1:
        print("\nUso de transporte: Baixa sustentabilidade")
    else:
        print("\nUso de transporte: Sustentabilidade moderada")
    print()

    """----------------------------------------//INSERIR NO BANCO DE DADOS///------------------------------------------"""

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

    cursor.close()
    conexao.close()

#---------------------------------------------ALTERAR DADOS---------------------------------------------#

def alterar():
    conexao = conectar()
    cursor = conexao.cursor()

    usuario = input("\nDigite o nome do usuário para alterar os dados: ").strip()
    if len(usuario) == 0:
        print("Nome inválido!")
        return

    cursor.execute("SELECT data FROM sistema WHERE usuario = %s ORDER BY data", (usuario,))
    datas = cursor.fetchall()

    if not datas:
        print(f"\nNenhum registro encontrado para o usuário {usuario}.")
        cursor.close()
        conexao.close()
        return

    print("\nDatas registradas para o usuário:")
    for i, d in enumerate(datas, 1):
        print(f"{i} - {d[0]}")

    while True:
        try:
            opc_data = int(input("Escolha o número da data que deseja alterar: "))
            if 1 <= opc_data <= len(datas):
                data_escolhida = datas[opc_data - 1][0]
                break
            else:
                print("Número inválido, tente novamente.")
        except ValueError:
            print("Digite um número válido.")

    cursor.execute("""
        SELECT l_agua, energia, kg_residuos, por_residuos,
               transporte_publico, bicicleta, caminhada,
               carro_fossil, carro_eletrico, carona_fossil
        FROM sistema
        WHERE usuario = %s AND data = %s
    """, (usuario, data_escolhida))
    dados = cursor.fetchone()

    if not dados:
        print("Erro ao buscar os dados.")
        cursor.close()
        conexao.close()
        return

    print(f"\nAlterando dados para {usuario} na data {data_escolhida} | OU PRESSIONE ENTER PARA PULAR:\n")
    
    #PEDIR SUSTENTABILIDADE - ALTERAR 
    def pedir_float_atual(valor_atual, texto):
        while True:
            entrada = input(f"{texto} (atual: {valor_atual}): ").strip()
            if entrada == '':
                return valor_atual #SE PRESSIONAR ENTER MANTERÁ O VALOR ATUAL
            try:
                val = float(entrada)
                return val
            except ValueError:
                print("Digite um número válido ou deixe vazio para manter o valor atual.")

    def pedir_sim_nao_atual(valor_atual, texto):
        while True:
            entrada = input(f"{texto} (atual: {valor_atual}, S/N): ").strip().upper()
            if entrada == '':
                return valor_atual #SE DER ENTER PULA PARA PROXIMA
            if entrada in ['S', 'N']:
                return 'Sim' if entrada == 'S' else 'Nao'
            print("Digite S para Sim, N para Não, ou deixe vazio para manter o valor atual.")

    l_agua = pedir_float_atual(dados[0], "Quantidade de litros de água consumidos")
    energia = pedir_float_atual(dados[1], "Quantidade de kWh de energia consumida")
    kg_residuos = pedir_float_atual(dados[2], "Quantidade de kg de resíduos não recicláveis")
    por_residuos = pedir_float_atual(dados[3], "Porcentagem de resíduos reciclados (%)")

    transporte_publico = pedir_sim_nao_atual(dados[4], "Usa transporte público?")
    bicicleta = pedir_sim_nao_atual(dados[5], "Usa bicicleta?")
    caminhada = pedir_sim_nao_atual(dados[6], "Costuma caminhar?")
    carro_fossil = pedir_sim_nao_atual(dados[7], "Usa carro com combustível fóssil?")
    carro_eletrico = pedir_sim_nao_atual(dados[8], "Usa carro elétrico?")
    carona_fossil = pedir_sim_nao_atual(dados[9], "Usa carona compartilhada com carro a combustíveis fósseis?")

    cursor.execute("""
        UPDATE sistema SET
            l_agua = %s,
            energia = %s,
            kg_residuos = %s,
            por_residuos = %s,
            transporte_publico = %s,
            bicicleta = %s,
            caminhada = %s,
            carro_fossil = %s,
            carro_eletrico = %s,
            carona_fossil = %s
        WHERE usuario = %s AND data = %s
    """, (
        l_agua, energia, kg_residuos, por_residuos,
        transporte_publico, bicicleta, caminhada,
        carro_fossil, carro_eletrico, carona_fossil,
        usuario, data_escolhida
    ))

    conexao.commit()
    print("\nDados atualizados com sucesso!")

    cursor.close()
    conexao.close()

#---------------------------------------------EXCLUIR---------------------------------------------#

def excluir():
    conexao = conectar()
    cursor = conexao.cursor()
    print("\n--- Excluir dados ---")
    usuario = input("Digite o nome do usuário que deseja excluir registros: ").strip()
    cursor.execute("SELECT data FROM sistema WHERE usuario=%s ORDER BY data", (usuario,))
    registros = cursor.fetchall()

    if not registros:
        print("Usuário não encontrado.")
    else:
        print("\nDatas disponíveis para exclusão:")
        for idx, reg in enumerate(registros):
            print(f"{idx+1} - {reg[0]}")
        try:
            escolha = int(input("\nEscolha a data que deseja excluir (número): "))
            data_escolhida = registros[escolha-1][0]
        except:
            print("Escolha inválida.")
            cursor.close()
            conexao.close()
            return
        
        cursor.execute("DELETE FROM sistema WHERE usuario=%s AND data=%s", (usuario, data_escolhida))
        conexao.commit()
        print("\nRegistro excluído com sucesso.")

    cursor.close()
    conexao.close()

#---------------------------------------------DEF CLASSIFICAR---------------------------------------------#

def classificar():
    conexao = conectar()
    cursor = conexao.cursor()
#---------------------------------------------CLASSIFICAÇÃO INDIVIDUAL (POR REGISTRO)---------------------------------------------#
    print("\n---------------CLASSIFICAÇÃO INDIVIDUAL DIÁRIA---------------")

    cursor.execute("""SELECT usuario, data, l_agua, energia, kg_residuos, por_residuos, 
                   transporte_publico, bicicleta, caminhada,
                   carro_fossil, carro_eletrico, carona_fossil 
                   FROM sistema""")
    registros = cursor.fetchall()

    for row in registros:
        usuario, data, l_agua, energia, kg_residuos, por_residuos, transporte_publico, bicicleta, caminhada, carro_fossil, carro_eletrico, carona_fossil = row

        # Classificação individual
        if l_agua < 150:
            agua_susten = "Alta Sustentabilidade"
        elif l_agua <= 150 or l_agua <=200:
            agua_susten = "Moderada Sustentabilidade"
        elif l_agua > 200:
            agua_susten = "Baixa Sustentabilidade"

        if energia < 5:
            energia_susten = "Alta Sustentabilidade"
        elif energia <=5 or energia<=10:
            energia_susten = "Moderada Sustentabilidade"
        elif energia > 10:
            energia_susten = "Baixa Sustentabilidade"

        if kg_residuos <= 0.770:
            residuos_susten = "Alta Sustentabilidade"
        elif kg_residuos <= 0.770 or kg_residuos <=1.54: 
            residuos_susten = "Moderada Sustentabilidade"
        elif kg_residuos > 1.54:
            residuos_susten = "Baixa Sustentabilidade"

        if por_residuos < 20:
            reciclaveis_susten = "Baixa Sustentabilidade"
        elif por_residuos <=20 or por_residuos <= 50:
            reciclaveis_susten = "Moderada Sustentabilidade"
        elif por_residuos > 50:
            reciclaveis_susten = "Alta Sustentabilidade"

        #---------------------------------------------PARTE DE TRANSPORTES SIM/NÃO (CLASSIFICAÇÃO INDIVIDUAL...)---------------------------------------------#
        #LOCALIZAR NA TABELA 
        transporte_publico = row[6]
        bicicleta = row[7]
        caminhada = row[8]
        carro_fossil = row[9]
        carro_eletrico = row[10]
        carona_fossil = row[11]

        sustentavel = 0
        nao_sustentavel = 0

        if transporte_publico == 'Sim':
            sustentavel += 1
        if bicicleta == 'Sim':
            sustentavel += 1
        if caminhada == 'Sim':
            sustentavel += 1
        if carro_eletrico == 'Sim':
            sustentavel += 1
        if carro_fossil == 'Sim':
            nao_sustentavel += 1
        if carona_fossil == 'Sim':
            nao_sustentavel += 1

        if sustentavel == 0 and nao_sustentavel == 0:
            transporte_susten = "Sustentabilidade Indefinida"
        elif sustentavel >= 1 and nao_sustentavel == 0:
            transporte_susten = "Alta Sustentabilidade"
        elif sustentavel == 0 and nao_sustentavel >= 1:
            transporte_susten = "Baixa Sustentabilidade"
        else:
            transporte_susten = "Moderada Sustentabilidade"

        print(f"\nUsuário: {usuario} | Data: {data}")
        print(f"  Água: {l_agua} L - {agua_susten}")
        print(f"  Energia: {energia} kWh - {energia_susten}")
        print(f"  Resíduos: {kg_residuos} kg - {residuos_susten}")
        print(f"  Recicláveis: {por_residuos}% - {reciclaveis_susten}")
        print(f"  Transportes: {transporte_susten}")

#---------------------------------------------DEF CLASSIFICAR MÉDIAS BANCO DE DADOS - REGISTROS---------------------------------------------#
def classificarMedias():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""SELECT usuario, data, l_agua, energia, kg_residuos, por_residuos, 
                   transporte_publico, bicicleta, caminhada,
                   carro_fossil, carro_eletrico, carona_fossil 
                   FROM sistema""")
    registros = cursor.fetchall()

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

        if media_agua <150:
            agua_susten2="Alta sustentabilidade"
        elif media_agua<= 150 or media_agua <=200:
            agua_susten2="Moderada Sustentabilidade"
        elif media_agua > 200:
            agua_susten2="Baixa Sustentabilidade"

        if media_energia < 5:
            energia_susten2="Alta Sustentabilidade"
        elif media_energia <=5 or media_energia<=10:
            energia_susten2="Moderada Sustentabilidade"
        elif media_energia > 10:
            energia_susten2="Baixa Sustentabilidade"

        if media_residuos <= 0.770: #770 gramas
            kg_residuos_susten2="Alta Sustentabilidade"
        elif media_residuos <= 0.770 or media_residuos <=1.54: 
            kg_residuos_susten2="Moderada Sustentabilidade"
        elif media_residuos > 1.54:
            kg_residuos_susten2="Baixa Sustentabilidade"

        if media_residuos_reciclaveis <20 :
            por_residuos_susten2="Baixa Sustentabilidade"
        elif media_residuos_reciclaveis <=20 or media_residuos_reciclaveis <= 50: 
            por_residuos_susten2="Moderada Sustentabilidade"
        elif media_residuos_reciclaveis > 50: 
            por_residuos_susten2="Alta Sustentabilidade"

    print("\n---------------MÉDIAS DOS DADOS DO BANCO DE DADOS---------------")
    print(f"\nMédia de Consumo de Água: {media_agua:.2f} litros, considerado: ",agua_susten2)
    print(f"Média de Consumo de Energia: {media_energia:.2f} KWh, considerado: ",energia_susten2)
    print(f"Média de Resíduos Não Recicláveis: {media_residuos:.2f} KG, considerado: ",kg_residuos_susten2)
    print(f"Média de Resíduos Recicláveis: {media_residuos_reciclaveis:.2f} %, considerado: ",por_residuos_susten2)

    cursor.close()
    conexao.close()

#---------------------------------------------LOOP - MENU PRINCIPAL---------------------------------------------#
while True:
    menu()
    opcao = input("Escolha uma opção: ").strip()
    if opcao == '1':
        cadastrar()  # sua função de cadastro
    elif opcao == '2':
        alterar()
    elif opcao == '3':
        excluir()
    elif opcao == '4':
        classificar()
    elif opcao == '5':
        classificarMedias()
    elif opcao == '0':
        print("\nSistema Encerrado!")
        break
    else:
        print("Opção inválida. Tente novamente.")