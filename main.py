saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_MAX = 500

users = []


def New_User():
    print("==== CADASTRAR NOVO USUÁRIO ====")
    name = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    valido = True

    for dic in users:
        if (cpf == dic.setdefault("cpf", cpf)):
            print("CPF já cadastrado!")
            valido = False

    if valido == True:
        nascimento = input("Data de nascimento do cliente: ")
        endereco = input("Endereço do cliente: ")
        users.append({
            "name": name, "cpf": cpf,
            "nascimento": nascimento,
            "endereco": endereco
        })
        print("Usuário cadastrado com sucesso!")


def List_Users():
    print("==== USUÁRIOS CADASTRADOS ====")
    print(f"{users}")


menu = """
==== MENU ====
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar novo usuário
[l] Listar usuários cadastrados
[q] Sair
=>
"""

while True:
    opcao = input(menu)

    if opcao == "d":
        print("==== DEPÓSITO ====")

        try:
            deposito = float(input("Valor a ser depositado: "))
            saldo += deposito
            print(f"Depósito de R${deposito} realizado com sucesso")
            extrato += (f"Depósito de R${deposito} \n")
        except ValueError:
            print("Digite um valor válido!")

    if opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print(
                f"Quatidade de saques excede o limite diário permitido de {LIMITE_SAQUES}")
            continue
        print("==== SAQUE ====")
        print(f"Saldo atual R${saldo}")
        try:
            saque = float(input("Valor a ser sacado: "))
            if float(saque) > float(LIMITE_MAX):
                print(f"Valor excede o limite permitido de R${LIMITE_MAX}")
            elif float(saque) > float(saldo):
                print(f"Valor excede o saldo de {saldo}")
            else:
                print(f"Saque no valor de R${saque} efetuado com sucesso")
                saldo -= saque
                numero_saques += 1

                extrato += (f"Saque de R${saque} \n")

        except ValueError:
            print("Digite um valor válido!")

    if opcao == "e":
        print("==== EXTRATO ====")
        print(extrato)
        print(f"Saldo atual: R${saldo}")

    if opcao == "c":
        New_User()

    if opcao == "l":
        List_Users()

    if opcao == "q":
        print("==== ENCERRADO ====")
        break
