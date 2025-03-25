# ==============================
# VERIFICADOR DE NÚMERO PAR OU ÍMPAR
# ==============================

# SOLICITANDO ENTRADA DO USUÁRIO
# Pede para o usuário digitar um número e armazena na variável 'nun'
# A função input() sempre retorna um texto, então usamos int() para converter para número inteiro
nun = int(input("Inserir número: "))  

# VERIFICANDO SE O NÚMERO É PAR OU ÍMPAR
# O operador % (módulo) retorna o resto da divisão de 'nun' por 2
# Se o resto for 0, significa que o número é divisível por 2, logo, é PAR
if nun % 2 == 0:  
    print("Esse número é par")  # Exibe mensagem informando que o número é par
else:  
    print("Esse número é ímpar")  # Exibe mensagem informando que o número é ímpar
