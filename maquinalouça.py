import time
ligado = False
tempo = 0
temperatura = 0

def ligar(novotempo, novatemperatura):
    global ligado, tempo, temperatura
    if not ligado:
        ligado = True
        tempo = novotempo
        temperatura = novatemperatura
        print(f"Lava louças ligada por {tempo} segundos na temperatura {temperatura}")
        iniciarCronometro(tempo)
        desligar()
    else:
        print("Lava louças já está ligado")

        def desligar():
            global ligado
            if ligado:
              ligado= False
              print("Lavalouças está desligada")
            else:
                print("Lavalouças já está desligada")
    
def status():
    if ligado:
        print("Tempo: {tempo} segundos \n Temperatura {temperatura}")
    else:
        print("Desligado")

def iniciarCronometro(segundos):
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
    print("\n Louça lavada pode ser retirada")


def VIDRO():
 print("Louça TIPO VIDRO")
 ligar(120, 100)
   
def PLASTICO():
    print("Louça TIPO PLASTICO")
    ligar(60, 21)
    
def METAL():
    print("Louça TIPO METAL")
    ligar(120, 30)

 
escolha=int(input("Escolha uma opção:   1. VIDRO (120s, TEMP 100c -------- 2. PLASTICO (60s, TEMP 21c)  -------- 3. metal (120s, TEMP 30c)"))

if escolha == 1:
    VIDRO()

elif escolha == 2:
    PLASTICO()

else:
    METAL()
   




