# ==============================
# EXEMPLO DE USO DE VARIÁVEIS E COMANDOS BÁSICOS
# ==============================

# SOLICITANDO ENTRADA DO USUÁRIO
# Pede para o usuário inserir seu nome e armazena o valor em 'nome'
# A função input() retorna o valor como texto
nome = input("Insira seu nome: ")

# Solicita a idade do usuário, convertendo a entrada para inteiro com a função int()
# O valor é armazenado na variável 'idade'
idade = int(input("Insira sua idade: "))

# Solicita o peso do usuário, convertendo para número real (float)
# O valor é armazenado na variável 'peso'
peso = float(input("Insira seu peso: "))

# Exibe os valores inseridos pelo usuário na tela
# A f-string (f"") permite incorporar as variáveis diretamente no texto
print(f"Nome: {nome}, Idade: {idade} anos, Peso: {peso} kg")

# ==============================
# TIPO DE DADOS
# ==============================

# A variável 'pedaco_de_pizza' recebe um valor numérico (5.0) e o tipo é float
pedaco_de_pizza = 5.0

# A variável 'cliente' recebe uma string (texto) com o nome "john"
cliente = "john"

# Exibe o tipo de dados das variáveis 'pedaco_de_pizza' e 'cliente'
print(type(pedaco_de_pizza))  # Exibe o tipo da variável 'pedaco_de_pizza'
print(type(cliente))          # Exibe o tipo da variável 'cliente'

# ==============================
# ENTRADA DE DADOS E TIPOS
# ==============================

# Solicita ao usuário quantos pedaços de pizza ele comeu
# O valor será armazenado em 'pedaco_de_pizza' como string (texto)
pedaco_de_pizza = input("Informe quantos pedaços comeu: ")

# Exibe o tipo da variável 'pedaco_de_pizza' (será string, pois a entrada é sempre texto)
print(type(pedaco_de_pizza))

# Exibe o número de pedaços de pizza que o usuário comeu
# A função print() exibe o valor para o usuário
print(f"Você comeu {pedaco_de_pizza} pedaços de pizza.")  # 'f' permite a formatação de strings

# ==============================
# DECLARAÇÃO DE VÁRIAVEIS E EXIBIÇÃO
# ==============================

# A variável 'a' é do tipo inteiro e recebe o valor 4
a = 4

# A variável 'A' é do tipo string e recebe o valor "Salty"
A = "Salty"

# Exibe os valores das variáveis 'a' e 'A'
print(a)  # Exibe o valor da variável 'a'
print(A)  # Exibe o valor da variável 'A'

# ==============================
# ATRIBUIÇÃO DE VÁRIAS VARIÁVEIS
# ==============================

# Atribui valores a três variáveis de uma vez (fruta1, fruta2, fruta3)
fruta1, fruta2, fruta3 = "Laranja", "Banana", "Maçã"

# Exibe os valores das três variáveis
print(fruta1, fruta2, fruta3)

# ==============================
# OPERAÇÕES ARITMÉTICAS
# ==============================

# Atribui valores aos números
primeiro_numero = 5
segundo_numero = 10

# Exibe a soma dos dois números
print(primeiro_numero + segundo_numero)

# ==============================
# ESTRUTURAS CONDICIONAIS
# ==============================

# Solicita o nome do "vingador mais forte"
nome = input("Qual o nome do vingador mais forte? ")

# Exibe uma mensagem de boas-vindas dependendo do nome inserido
if nome == "hulk":
    print("Bem-vindo, vingador mais forte")
else:
    print("Acesso negado!")

# ==============================
# EXEMPLO DE CONDIÇÃO 'AND'
# ==============================

# Verifica se 'x' está entre 2 e 10, usando o operador 'and'
x = 5
if x > 2 and x < 10:  # Ambas as condições precisam ser verdadeiras
    print("O número está entre 2 e 10")

# ==============================
# EXEMPLO DE CONDIÇÃO 'OR'
# ==============================

# Verifica se 'x' é menor que 2 ou maior que 4, usando o operador 'or'
x = 5
if x < 2 or x > 4:  # Apenas uma das condições precisa ser verdadeira
    print("O número é menor que 2 ou maior que 4")

# ==============================
# EXEMPLO DE CONDIÇÃO 'NOT'
# ==============================

# Inverte a condição e verifica se 'x' não é maior que 10
x = 5
if not x > 10:  # A condição é invertida (x não é maior que 10)
    print("O número não é maior que 10")
