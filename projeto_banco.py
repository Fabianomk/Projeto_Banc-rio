menu = """"
   ============MENU============
   [1] Depositar
   [2] Sacar
   [3] Extrato
   [0] Sair

   ============================
   
  => """

saldo = 0
limite = 1000
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Informe o valor do deposito:"))

        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito R$ {deposito:.2f}\n"

        else:
            print("Operação invalida! O valor informado não é válido.")

    elif opcao == "2":
        saque = float(input("Informe o valor do saque: "))

        saldo_insuficiente = saque > saldo 

        limite_ultrapassado = saque > limite

        saques_ultrapassado = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Saldo insuficiente, tente outra vez!")
            
            print (f"Seu saldo é de R$ {saldo:.2f}")

        elif limite_ultrapassado:
            print("Ops! Seu saque está acima do seu limite")
            
            print(f"O nosso banco e restrito a um limite diário de: R$ {limite:.2f}")

        elif saques_ultrapassado:
            print("Voce não pode mais realizar essa ação. Voce ja fez o seus 3 saques diários!")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: {saque:.2f}\n"
            numero_saques += 1


    elif opcao == "3":
        print("===============Extrato===============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("===========Banco da Familia==========")
 
    elif opcao == "0":
        break

    else:
        print("Operação invalida, verififique e coloque a opção")
