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
        return self.vidas > 0
class JuegoAdivinaNumero(Juego):
    def validaNumero(self, num):
        return 0 <= num <= 10
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un numero entre 0 y 10")
        while True:
            num = int(input("Ingrese numero: "))
            if not self.validaNumero(num):
                print("Numero fuera de rango")
                continue
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
                    print("Sin vidas. El numero era:", self.numeroAAdivinar)
                    break
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if not (0 <= num <= 10):
            print("Numero fuera de rango")
            return False
        if num % 2 != 0:
            print("Error: debe ser PAR")
            return False
        return True
    def juega(self):
        self.reiniciaPartida()
        while True:
            self.numeroAAdivinar = random.randint(0, 10)
            if self.numeroAAdivinar % 2 == 0:
                break
        print("Adivina un numero PAR entre 0 y 10")
        while True:
            num = int(input("Ingrese numero: "))
            if not self.validaNumero(num):
                continue
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
                    print("Sin vidas. El numero era:", self.numeroAAdivinar)
                    break
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if not (0 <= num <= 10):
            print("Numero fuera de rango")
            return False

        if num % 2 == 0:
            print("Error: debe ser IMPAR")
            return False
        return True
    def juega(self):
        self.reiniciaPartida()
        while True:
            self.numeroAAdivinar = random.randint(0, 10)
            if self.numeroAAdivinar % 2 != 0:
                break
        print("Adivina un numero IMPAR entre 0 y 10")
        while True:
            num = int(input("Ingrese numero: "))
            if not self.validaNumero(num):
                continue
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
                    print("Sin vidas. El numero era:", self.numeroAAdivinar)
                    break
if __name__ == "__main__":

    j1 = JuegoAdivinaNumero(3)
    j2 = JuegoAdivinaPar(3)
    j3 = JuegoAdivinaImpar(3)
    print("\nJUEGO 1")
    j1.juega()
    print("\nJUEGO PAR")
    j2.juega()
    print("\nJUEGO IMPAR")
    j3.juega()
