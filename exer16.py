nun1=int(input("inserir nota 1"))
nun2=int(input("inserir nota 2"))
nun3=int(input("inserir nota 3"))
soma= nun1+nun2+nun3
media= soma/3

if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
else:
    print("Reprovado")

