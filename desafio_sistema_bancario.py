menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair 

--> """


saldo = 0
limite_max_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3


while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input('Insiar o valor que deseja depositar: R$'))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
            print('\nDepósito realizado com sucesso!\n')
        else:
            print('Não é possível depositar valores negativos')


    elif opcao == 2:
        saque = float(input('Insira o valor que deseja sacar: R$'))

        saldo_insuficiente = saque > saldo

        limite_excedido = saque > limite_max_saque

        quantidade_saques_excedido = numero_saques > LIMITE_SAQUES_DIARIO

        if saldo_insuficiente:
            print('\nSaldo insuficiente!')

        elif limite_excedido:
            print('\nValor informado excede o valor máximo perimitido! Tente novamente.')

        elif quantidade_saques_excedido:
            print('\nQuantidade de saques diários excedido! Tente novamente amanhã.')

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print('Valor autorizado para saque!')

        else:
            print('\nValor inválido! Tente novamente.')
     

    elif opcao == 3:
        print("\n================ EXTRATO =================")
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nsaldo: R$ {saldo:.2f}')
        print('============================================')

    elif opcao == 4:
        break

    else:
        print('\nOpção inválida! Tente novamente.')
        break