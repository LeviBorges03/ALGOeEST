import random
segredo = random.randint(1, 20)
palpites = []

acertou = False
while not acertou:
    chute = int(input("Digite um palpite: "))
    palpites.append(chute)
    if chute == segredo:
        acertou = True
        print("Você acertou!")

print("Seus palpites foram:", palpites)
