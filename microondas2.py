import time

class Microondas:
    def __init__(self):
        self.ligado = False
        self.tempo = 0
        self.potencia = 0
        self.historico = []

    def ligar(self, novotempo, novapotencia):
        if not self.ligado:
            if novotempo <= 0 or novapotencia <= 0:
                raise ValueError("Tempo e potência devem ser maiores que zero!")
            self.ligado = True
            self.tempo = novotempo
            self.potencia = novapotencia
            print(f"Microondas ligado por {self.tempo} segundos na potência {self.potencia}")
            self.historico.append({"tempo": self.tempo, "potencia": self.potencia})
            self.iniciar_cronometro(self.tempo)
            self.desligar()
        else:
            print("Microondas já está ligado!")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print("Microondas está desligado.")
        else:
            print("Microondas já está desligado!")

    def status(self):
        if self.ligado:
            print(f"Microondas ligado\nTempo restante: {self.tempo} segundos\nPotência: {self.potencia}")
        else:
            print("Microondas está desligado.")

    def iniciar_cronometro(self, segundos):
        while segundos > 0:
            print(f"Tempo restante: {segundos} segundos", end="\r")
            time.sleep(1)
            segundos -= 1
        print("\nTempo esgotado!")

    def menu(self):
        while True:
            print("\n=== MENU DO MICROONDAS ===")
            print("1. Pipoca (30s, Potência 100)")
            print("2. Personalizado")
            print("3. Status")
            print("4. Histórico")
            print("5. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.ligar(30, 100)
            elif escolha == "2":
                try:
                    tempo = int(input("Digite o tempo em segundos: "))
                    potencia = int(input("Digite a potência (1 a 100): "))
                    self.ligar(tempo, potencia)
                except ValueError:
                    print("Valores inválidos! Tente novamente.")
            elif escolha == "3":
                self.status()
            elif escolha == "4":
                print("=== HISTÓRICO DE USO ===")
                for idx, item in enumerate(self.historico):
                    print(f"{idx + 1}: Tempo - {item['tempo']}s, Potência - {item['potencia']}")
            elif escolha == "5":
                print("Desligando microondas. Até mais!")
                break
            else:
                print("Opção inválida! Tente novamente.")

# Criar instância do Microondas
meu_microondas = Microondas()
meu_microondas.menu()