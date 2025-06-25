import os

def lt():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
    

def linha():
    print('-' * 50)
    
    
def header(msg):
  print("=" * 50)
  print(f"{msg:^50}")
  print("=" * 50)
  
 
lt() 
header("Sistema Bancário EOS")

saldo = 0.0
extrato = []
limite_saque = 500.0
saques_diarios = 0
LIMITE_SAQUES = 3

while True:
    linha()
    print("Escolha uma operação:")
    print("[1] - Depositar")
    print("[2] - Sacar")
    print("[3] - Extrato")
    print("[4] - Sair")
    linha()
    
    opcao = input("Opção: ")
    linha()

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("\nDepósito realizado com sucesso!")
            
        else:
            print("\nValor inválido para depósito.")

    elif opcao == "2":
        if saques_diarios >= LIMITE_SAQUES:
            print("\nLimite diário de saques atingido.")
            continue
        valor = float(input("Informe o valor do saque: "))
        if valor > limite_saque:
            print("\nValor do saque excede o limite por operação.")
            
        elif valor > saldo:
            print("\nSaldo insuficiente para saque.")
            
        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque:    R$ {valor:.2f}")
            saques_diarios += 1
            print("\nSaque realizado com sucesso!")
            
        else:
            print("\nValor inválido para saque.")

    elif opcao == "3":
        print("\n==================== EXTRATO ====================")
        
        if not extrato:
            print("\nNão foram realizadas movimentações.")
            
        else:
            for operacao in extrato:
                print(operacao)
                
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=================================================")

    elif opcao == "4":
        print("Obrigado por utilizar o banco EOS!")
        linha()
        break

    else:
        print("Opção inválida. Tente novamente.")