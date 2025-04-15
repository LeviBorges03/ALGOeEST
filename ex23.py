n = int(input("Digite um número: "))
tabuada = []

for i in range(1, 11):
    tabuada.append(n * i)

for item in tabuada:
    print(item)