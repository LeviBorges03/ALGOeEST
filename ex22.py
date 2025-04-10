palavras=[]
for i in range(6):
    palavra = str(input(f"digite a {i+ 1}º palavra"))
    palavras.append(palavra)
soma=0    
for palvras in palavra:
    if (len(palavra))>=5:
        soma=soma+1
        
print(f" na lista(vetor) tem {soma} plavras com mais de 5 caracteres")
        
    
    