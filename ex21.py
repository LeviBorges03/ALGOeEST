
nums = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    nums.append(numero)
    
soma = 0

for numero in nums:
    soma = soma+numero

print("A soma de todos os números é:", soma)
