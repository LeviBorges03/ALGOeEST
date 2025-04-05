
usuarioArmazenado = "admin"
senhaArmazenada = "1234"
usuario = input("Insira o nome de usuario: ")
senha = input("Insira a senha: ")
if usuario == usuarioArmazenado and senha == senhaArmazenada:
    print("Login realizado com sucesso!")
else:
    if usuario != usuarioArmazenado:
        print("Nome de usuario incorreto!")
    if senha != senhaArmazenada:
        print("Senha incorreta!")
