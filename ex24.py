numeros = [4, 9, 2, 7, 5]
maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print("Maior número:", maior)
print("Menor número:", menor)
