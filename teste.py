# Lista (array) que funcionará como nosso banco de dados em memória
motores = []
proximo_id = 1

def cadastrar_motor():
    global proximo_id
    print("\n--- Cadastrar Novo Motor ---")
    modelo = input("Modelo do motor: ").strip()
    fabricante = input("Fabricante: ").strip()
    
    # Validação simples para garantir que potência e cilindrada sejam números
    try:
        potencia_cv = float(input("Potência (cv): "))
        cilindrada_cc = int(input("Cilindrada (cc): "))
    except ValueError:
        print("Erro: Potência e cilindrada devem ser valores numéricos. Cadastro cancelado.")
        return

    combustivel = input("Tipo de combustível (Gasolina, Etanol, Diesel, Elétrico, Flex): ").strip()

    # Dicionário representando o motor
    motor = {
        "id": proximo_id,
        "modelo": modelo,
        "fabricante": fabricante,
        "potencia_cv": potencia_cv,
        "cilindrada_cc": cilindrada_cc,
        "combustivel": combustivel
    }

    motores.append(motor)
    proximo_id += 1
    print(f"Sucesso: Motor '{modelo}' cadastrado com ID {motor['id']}!")

def listar_motores():
    print("\n--- Lista de Motores Cadastrados ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    for m in motores:
        print(f"ID: {m['id']} | Modelo: {m['modelo']} | Fabricante: {m['fabricante']} | "
              f"Potência: {m['potencia_cv']} cv | Cilindrada: {m['cilindrada_cc']} cc | "
              f"Combustível: {m['combustivel']}")

def buscar_motor():
    print("\n--- Buscar Motor ---")
    termo = input("Digite o ID ou parte do nome do modelo: ").strip().lower()
    encontrados = []

    for m in motores:
        if str(m["id"]) == termo or termo in m["modelo"].lower():
            encontrados.append(m)

    if not encontrados:
        print("Nenhum motor encontrado com esse critério.")
    else:
        for m in encontrados:
            print(f"ID: {m['id']} | Modelo: {m['modelo']} | Fabricante: {m['fabricante']} | "
                  f"Potência: {m['potencia_cv']} cv | Combustível: {m['combustivel']}")

def atualizar_motor():
    print("\n--- Atualizar Motor ---")
    try:
        id_busca = int(input("Digite o ID do motor que deseja atualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    for m in motores:
        if m["id"] == id_busca:
            print(f"Editando '{m['modelo']}' (pressione Enter para manter o valor atual):")
            
            novo_modelo = input(f"Modelo [{m['modelo']}]: ").strip()
            if novo_modelo:
                m["modelo"] = novo_modelo

            novo_fab = input(f"Fabricante [{m['fabricante']}]: ").strip()
            if novo_fab:
                m["fabricante"] = novo_fab

            nova_pot = input(f"Potência em cv [{m['potencia_cv']}]: ").strip()
            if nova_pot:
                try:
                    m["potencia_cv"] = float(nova_pot)
                except ValueError:
                    print("Valor de potência inválido, mantendo o anterior.")

            nova_cil = input(f"Cilindrada em cc [{m['cilindrada_cc']}]: ").strip()
            if nova_cil:
                try:
                    m["cilindrada_cc"] = int(nova_cil)
                except ValueError:
                    print("Valor de cilindrada inválido, mantendo o anterior.")

            novo_comb = input(f"Combustível [{m['combustivel']}]: ").strip()
            if novo_comb:
                m["combustivel"] = novo_comb

            print("Motor atualizado com sucesso!")
            return

    print("Motor não encontrado.")

def remover_motor():
    print("\n--- Remover Motor ---")
    try:
        id_busca = int(input("Digite o ID do motor que deseja remover: "))
    except ValueError:
        print("ID inválido.")
        return

    for i, m in enumerate(motores):
        if m["id"] == id_busca:
            removido = motores.pop(i)
            print(f"Motor '{removido['modelo']}' (ID {removido['id']}) removido com sucesso.")
            return

    print("Motor não encontrado.")

def menu():
    while True:
        print("\n===============================")
        print("   SISTEMA DE MOTORES (TESTE)  ")
        print("===============================")
        print("1. Cadastrar motor")
        print("2. Listar todos os motores")
        print("3. Buscar motor")
        print("4. Atualizar motor")
        print("5. Remover motor")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            buscar_motor()
        elif opcao == "4":
            atualizar_motor()
        elif opcao == "5":
            remover_motor()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    menu()