menu = """

[d] Depositar

[s] Sacar

[e] Extrato

[q] Sair



=>"""



saldo = 0

limite = 500

extrato = ""

numero_saques = 0

LIMITE_SAQUES = 3



while True:

    opcao = input(menu)



    if opcao == "d":

        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:

            operacao = f"Operação: Depósito\nValor: R$ {valor:.2f}\n"

            extrato += f"\n{operacao}"

            saldo += valor

            print("Operação realizada!")

        else:

            print("Valor inválido!")



    elif opcao == "s":

        valor = float(input("Digite o valor a ser sacado: "))

        if valor <= 0 or valor > saldo or numero_saques >= LIMITE_SAQUES or valor > limite:

            print("Não foi possível realizar a operação.")

            if valor <= 0:

                print("Valor inválido!")

            elif valor > saldo:

                print("Saldo insuficiente!")

            elif numero_saques >= LIMITE_SAQUES:

                print("Limite de saques diários atingido.")

            elif valor > limite:

                print("O valor excede o limite de R$ 500.00 por operação.")

        else:

            saldo -= valor

            numero_saques += 1

            operacao = f"Operação: Saque\nValor: R$ {valor:.2f}\n"

            extrato += f"\n{operacao}"

            print("Operação realizada!")



    elif opcao == "e":

        print("EXTRATO".center(20,"-"))

        print(extrato)

        print("-"*20)

        print(f"\nSaldo R$ {saldo:.2f}")

    

    elif opcao == "q":

        print("Encerrando sistema!")

        break



    else:

        print("Opção inválida!")

