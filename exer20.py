idade = int(input("Informe sua idade: "))
membro = input("Você é membro do clube? (s/n): ").lower()
acompanhado_por_membro = input("Você está acompanhado por um membro? (s/n): ").lower()
if idade > 18:
    if membro == 's':
        print("Acesso permitido. Bem-vindo ao clube!")
    else:
        if acompanhado_por_membro == 's':
            print("Acesso permitido. Você deve pagar meia entrada.")
        else:
            print("Acesso permitido. Você deve pagar o ingresso completo.")
else:
    print("Acesso negado. Você deve ter mais de 18 anos para entrar no clube.")