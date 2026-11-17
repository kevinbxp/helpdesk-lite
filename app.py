chamados = []

def listar_chamados():
    if len(chamados) == 0:
        print("Nenhum chamado cadastrado")
        
    else:
        print("--- CHAMADOS CADASTRADOS ---")
        for chamado in chamados:
            print("ID:", chamado["id"])
            print("Solicitante:", chamado["nome"])
            print("Setor:", chamado["setor"])
            print("Problema:", chamado["problema"])
            print("Prioridade:", chamado["prioridade"])
            print("--------------------------")

def cadastrar_chamado():
    global id_chamado
    
    print("Iniciando cadastro de chamado...")
    
    print("\n--- NOVO CHAMADO ---")
        
    nome = input("Nome do solicitante: ")
    nome = nome.strip()
    
    while nome == "":
        print("O nome do solicitante é obrigatório!")
        nome = input("Nome do solicitante: ")
        nome = nome.strip()

    setor = input("Setor: ")
    setor = setor.strip()
    
    while setor == "":
        print("O setor é obrigatório!")
        setor = input("Setor: ")
        setor = setor.strip()

    problema = input("Descreva o problema: ")
    problema = problema.strip()
    
    while problema == "":
        print("A descrição do problema é obrigatória!")
        problema = input("Descreva o problema: ")
        problema = problema.strip()
        
    prioridade = input("Prioridade (Baixa, Média ou Alta): ")
    prioridade = prioridade.strip().lower()
    
    while prioridade not in ["baixa", "média", "alta"]:
        print("Prioridade inválida!")
        prioridade = input("Prioridade (Baixa, Média ou Alta): ")
        prioridade = prioridade.strip().lower()
 
    print("\n--- DADOS DO CHAMADO ---")
    print("ID do chamado:", id_chamado)
    print("Solicitante:", nome)
    print("Setor:", setor)
    print("Problema:", problema)
    print("Prioridade:", prioridade)

    if prioridade == "alta":
        print("ATENÇÃO: Chamado de alta prioridade!")

    elif prioridade == "média": 
        print("Chamado de prioridade média.")

    elif prioridade == "baixa": 
        print("Chamado de baixa prioridade.")
     
    chamado = {
        "id": id_chamado,
        "nome": nome,
        "setor": setor,
        "problema": problema,
        "prioridade": prioridade
    } 
    
    chamados.append(chamado)
    
    id_chamado = id_chamado + 1

def atualizar_chamado():
    
    id_valido = False
    
    while not id_valido:    
        try:
            id_busca = int(input("Digite o ID do chamado: "))
            id_valido = True
        except ValueError:
            print("Você precisa digitar um número válido!") 
        
    encontrado = False
    
    for chamado in chamados:
        if chamado["id"] == id_busca:
            
            encontrado = True
            
            print("Chamado encontrado!")
            print("Solicitante:", chamado["nome"])
            print("Prioridade atual:", chamado["prioridade"])
            
            nova_prioridade = input("Nova prioridade (Baixa, Média ou Alta): ")
            nova_prioridade = nova_prioridade.strip().lower()
            
            while nova_prioridade not in ["baixa", "média", "alta"]:
                print("Prioridade inválida!")
                nova_prioridade = input("Prioridade (Baixa, Média ou Alta): ")
                nova_prioridade = nova_prioridade.strip().lower()
            
            chamado["prioridade"] = nova_prioridade
            
            print("Prioridade atualizada com sucesso!")

    if not encontrado:
        print("Chamado não encontrado!")

def excluir_chamado():
    
    id_valido = False
    
    while not id_valido:
        try:
            id_busca = int(input("Digite o ID do chamado que deseja excluir: "))
            id_valido = True
        except ValueError:
            print("Você precisa digitar um número válido!")
    
    encontrado = False
    
    for chamado in chamados:
        if chamado["id"] == id_busca:
            
            encontrado = True
            
            chamados.remove(chamado)
            print("Chamado excluído com sucesso!")
            
            break
            
    if not encontrado:
        print("Chamado não encontrado!")
    
    

print("====================================")
print("         HELPDESK LITE")
print("         Sistema de chamados de TI")
print("====================================")

print("Bem-vindo ao sistema!")

print("Sistema desenvolvido para gerenciamento de chamados.")
print("Versão 1.0")

executando = True
id_chamado = 1

while executando:
    print("1 - Novo chamado.")
    print('2 - Listar chamados.')
    print("3 - Atualizar chamado.")
    print("4 - Excluir chamado.")
    print("5 - Sair.")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_chamado()
        
    elif opcao == "2":
        listar_chamados()

    elif opcao == "3":
        atualizar_chamado()
        
    elif opcao == "4":
        excluir_chamado()

    elif opcao == "5":
        print("Encerrando o HelpDesk Lite...")
        executando = False

    else:
        print("Opção inválida. Tente novamente.")

