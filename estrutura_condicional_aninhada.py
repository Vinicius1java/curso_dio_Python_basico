conta_normal = True #Alterar para False ele não ira realizar a primeira condição e passara para a de baixo, o mesmo vale para a conta universitaria
conta_universitaria = True

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal :
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else :
        print("Não foi possivel realizar o saque!")

elif conta_universitaria:
    if saldo >= saque :
        print("Saque realizado com sucesso")
    else:
        print("Saldo insufuciente")
