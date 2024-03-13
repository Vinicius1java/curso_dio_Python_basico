saldo = 500

def sacar(valor):

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro")

    print("Obrigado por ser nosso cliente")  

sacar(100)

def depositar(valor):
    saldo = 500
    saldo += valor

    print(f"obrigado pelo deposito saldo")

depositar()