# ==============================
# CÓDIGO PARA OPERAÇÕES BÁSICAS
# ==============================

# SOLICITANDO ENTRADA DO USUÁRIO
# Solicita ao usuário que digite um número e armazena na variável 'num1'
# A função input() recebe o valor como texto, então a função int() converte para número inteiro
num1 = int(input("Digite um número: "))  

# Solicita ao usuário outro número e converte para inteiro, armazenando em 'num2'
num2 = int(input("Digite outro número: "))  

# REALIZANDO AS OPERAÇÕES MATEMÁTICAS
# Soma os dois números e armazena o resultado na variável 'soma'
soma = int(num1 + num2)  

# Subtrai 'num2' de 'num1' e armazena o resultado na variável 'subt'
subt = int(num1 - num2)  

# Multiplica 'num1' por 'num2' e armazena o resultado na variável 'mult'
mult = int(num1 * num2)  

# Divide 'num1' por 'num2' e armazena o resultado na variável 'divi'
# OBS: O uso de int() aqui pode arredondar o valor e causar perda de precisão
divi = int(num1 / num2)  

# EXIBINDO OS RESULTADOS NA TELA
# Cada operação será impressa separadamente pelo print()
print(soma)  # Mostra o resultado da soma
print(subt)  # Mostra o resultado da subtração
print(mult)  # Mostra o resultado da multiplicação
print(divi)  # Mostra o resultado da divisão (mas pode perder precisão)
