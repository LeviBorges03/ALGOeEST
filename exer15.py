nome = str(input("digitar o nome do produto"))
qaunt = int(input("digitar a quantidade desejada do poduto"))
preco = float(input("digitar o valor unitario do produto"))
valor = qaunt*preco
if valor >= 100:
    desconto=valor*0.05
    print(f"Parabens vc recebeu 5% de desconto o valor total é: {nome} --> {desconto}")
else:
     print(f"Parabens sua compra foi realizada com sucesso o valor total é: {valor}")