import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
    def reiniciaPartida(self):
        self.vidas = self.numeroDeVidas
    def actualizaRecord(self):
        if self.vidas > self.record:
            self.record = self.vidas
    def quitaVida(self):
        self.vidas -= 1
        if self.vidas > 0:
            return True
        else:
            return False        
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un numero entre 0 y 10")
        while True:
            num = int(input("Ingrese numero: "))
            if num == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if num < self.numeroAAdivinar:
                        print("El numero es MAYOR")
                    else:
                        print("El numero es MENOR")
                else:
                    print("Ya no tienes vidas")
                    break
if __name__ == "__main__":
    juego = JuegoAdivinaNumero(3)
    juego.juega()

