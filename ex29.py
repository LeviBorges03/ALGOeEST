valores = [2, 4, 6, 8]
n = int(input("Digite um número para multiplicar: "))

for i in range(len(valores)):
    valores[i] = valores[i] * n

print("Novos valores:", valores)