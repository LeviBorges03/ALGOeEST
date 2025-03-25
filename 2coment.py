# ==============================
# MOSTAR AO USUARIO
# ==============================

# Solicita ao usuário que digite seu nome e armazena a entrada na variável 'nome'
# A função input() recebe um texto digitado pelo usuário e retorna como uma string (texto)
nome = input("Digite seu nome: ")  

# Solicita ao usuário que digite sua idade e armazena na variável 'idade'
# A função input() sempre retorna um texto (string), então a função int() é usada para converter esse texto em um número inteiro
idade = int(input("Digite sua idade: "))  

# Exibe uma mensagem personalizada na tela usando a função print()
# A string f"..." é chamada de f-string, permitindo inserir variáveis diretamente dentro das chaves {}
# O texto exibido será: "Olá, [nome]! Você tem [idade] anos." (substituindo [nome] e [idade] pelos valores fornecidos pelo usuário)
print(f"Olá, {nome}! Você tem {idade} anos.")
