notas = []
for i in range(5):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)

soma = 0
for n in notas:
    soma = soma + n

media = soma / 5
print("Média das notas:", media)

