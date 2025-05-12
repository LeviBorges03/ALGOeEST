import time
ligado = False
tempo = 0
potencia = 0

def ligar(novotempo, novapotencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True
        tempo = novotempo
        potencia = novapotencia
        print(f"Microondas ligado por {tempo} segundos na potencia {potencia}")
        iniciarCronometro(tempo)
        desligar()
    else:
        print("Microondas já está ligado")

        def desligar():
            global ligado
            if ligado:
              ligado= False
              print("Microondas está desligado")
            else:
                print("Microondas já está desligado")
    
def status():
    if ligado:
        print("Tempo: {tempo} segundos \n Potencia {potencia}")
    else:
        print("Desligado")

def iniciarCronometro(segundos):
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
    print("\n Tempo esgotado")

def pipoca():
    ligar(30, 100)


pipoca()