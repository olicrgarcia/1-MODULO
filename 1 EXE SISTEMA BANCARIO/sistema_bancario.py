#Criando um sistema bancário básico com Python

#Constantes
VL_LIMITE_DIARIO = 500
QTD_LIMITE_SAQUE = 3
MENU = """~~~~~~~~~~~ SISTEMA BANCÁRIO ~~~~~~~~~~~~

          Selecione uma opção para continuar:  

          [E] - Ver extrato
          [S] - Sacar valores
          [D] - Depositar valores
          [Q] - Sair do sistema

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

#Variaveis
opcao = -1
vl_deposito = 0
vl_deposito_acum = 0
vl_saque = 0
vl_saque_acum = 0
qtd_saque_real = 0
vl_saldo_atual = 500

#Logica do Sistema Bancário

while str(opcao).upper() != 'Q': #Faça o loop enquanto não for 'Q'
    opcao = input(MENU)
    if opcao.upper() == 'E': #Exibindo o extrato bancário

        txt_extrato_1 = f"""
~~~~~~~~~~~ EXTRATO BANCÁRIO ~~~~~~~~~~~~

        Total de Depósitos no Dia: R$ {vl_deposito_acum:.2f}
        Total de Saques no Dia: R$ {vl_saque_acum:.2f}
        Saldo Atual: R$ {vl_saldo_atual:.2f}

        Limite de Saques: {QTD_LIMITE_SAQUE}
        Limite utilizado: {qtd_saque_real}
        Limite de valor por saques: R$ {VL_LIMITE_DIARIO:.2f}

        Obrigado por escolher o nosso banco!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

        txt_extrato_2 = f"""
~~~~~~~~~~~ EXTRATO BANCÁRIO ~~~~~~~~~~~~

        [Não houveram movimentações para esta conta!]

        Saldo Atual: R$ {vl_saldo_atual:.2f}

        Limite de Saques: {QTD_LIMITE_SAQUE}
        Limite utilizado: {qtd_saque_real}
        Limite de valor por saques: R$ {VL_LIMITE_DIARIO:.2f}


        Obrigado por escolher o nosso banco!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
        print(txt_extrato_1) if vl_saque_acum >0 or vl_deposito_acum >0 else print(txt_extrato_2)
        input('Digite para continuar...\n')

    elif opcao.upper() == 'D': #Realizando um deposito na conta e acumulando variavel para a exibição do extrato
        vl_deposito = float(input('Digite o valor desejado a depositar:\n'))
        if vl_deposito < 10:
            print('O sistema permite apenas depósitos maiores que R$ 5,00.')
        elif vl_deposito >= 10:
            vl_saldo_atual += vl_deposito
            vl_deposito_acum += vl_deposito
            print(f'Um depósito de: R$ {vl_deposito:.2f} foi realizado com sucesso!\nSaldo atual: R$ {vl_saldo_atual:.2f}')

    elif opcao.upper() == 'S': #Realizando um saque na conta e acumulando variavel para a exibição do extrato
        vl_saque = float(input('Digite o valor desejado a sacar:\n'))

        if vl_saque > vl_saldo_atual:
            print(f'\nO valor de R$ {vl_saque:.2f} não pode ser sacado devido a falta de saldo na conta!\n')

        elif vl_saque > VL_LIMITE_DIARIO:
            print(f'\nO valor de R$ {vl_saque:.2f} excede o valor diário de R$ {VL_LIMITE_DIARIO:.2f}\n')

        elif qtd_saque_real >= QTD_LIMITE_SAQUE:
            print(f'\nÉ permitido apenas {QTD_LIMITE_SAQUE} saques diários.\n')
            continue

        else:
            if vl_saque < 20:
                print('O sistema permite apenas saques maiores que R$ 20.00.')

            elif vl_saque >= 20:
                vl_saque_acum += vl_saque
                vl_saldo_atual -= vl_saque
                qtd_saque_real += 1
                print(f'Um saque de: R$ {vl_saque:.2f} foi realizado com sucesso!\nSaldo atual: R$ {vl_saldo_atual:.2f}\n')
            else:
                print('\nInsira um valor válido para saque.\n')

    elif opcao.upper() == 'Q': #Saindo do Sistema
       print('\nObrigado por escolher o nosso banco!\nTenha um bom dia!')
       break
            
    else: #Tratativa de erro
        print('Ops! Não conseguimos identificar a opção escolhida.\nSelecione uma opção válida!')

