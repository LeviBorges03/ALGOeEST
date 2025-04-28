
def tabuada_personalizada(base, inicio, fim):
    print(f"tabuada do {base} de {inicio} a {fim}:")
    for i in range(1,11):
        print(f"{base} X {i} = {base * i}")

base=int(input("insira numero BASE da tabuada"))
inicio=int(input("insira numero INICIO da tabuada"))
fim=int(input("insira numero FIM da tabuada"))


tabuada_personalizada(base, inicio, fim)
