idade = int(input("Digite sua idade: "))
genero = input("Digite seu gênero (masculino/feminino): ").lower()
atleta = input("Você é atleta? (sim/não): ").lower()

if idade < 15:
    print("Anúncios infantis")
elif 15 <= idade <= 21:
    if genero == "feminino":
        print("Anúncios de maquiagem e moda feminina")
    elif genero == "masculino" and atleta == "sim":
        print("Anúncios de artigos esportivos")
    else:
        print("Anúncios de videogames")
elif 22 <= idade <= 32:
    if genero == "masculino" and atleta == "sim":
        print("Anúncios de artigos esportivos")
    elif genero != "masculino" and atleta == "não":
        print("Anúncios de livros, jardinagem e eletrodomésticos")
elif 22 <= idade <= 35 and genero == "feminino":
    print("Anúncios de artigos esportivos e itens de casa")