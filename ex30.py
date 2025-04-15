palavras = ["arara", "bola", "radar", "ana", "pato"]
palindromos = []

for p in palavras:
    if p == p[::-1]:
        palindromos.append(p)

print("Palíndromos encontrados:", palindromos)