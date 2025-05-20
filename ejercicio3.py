
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

class Carro(Vehiculo):
    def __init__(self, marca, modelo, numero_de_puertas):
        super().__init__(marca, modelo)
        self.numero_de_puertas = numero_de_puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de puertas: {self.numero_de_puertas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_de_motor):
        super().__init__(marca, modelo)
        self.tipo_de_motor = tipo_de_motor

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de motor: {self.tipo_de_motor}")

carro1 = Carro("Toyota", "Corolla", 4)
moto1 = Moto("Yamaha", "MT-07", "4 tiempos")

carro1.mostrar_info()
print()
moto1.mostrar_info()
