class Veiculo:
    def __init__(self, marca, cor, tipo, modelo):
        self.marca = marca
        self.cor = cor
        self.tipo = tipo
        self.modelo = modelo
    
    def acelerar(self):
        print("Blum Blum Blum")

    def __str__(self):
        return f"Marca: {self.marca}\n Modelo: {self.modelo}\n Cor: {self.cor}"
    
class Bicicleta(Veiculo):
    def __init__(self, marca, cor, tipo, modelo):
        super().__init__(marca, cor, tipo, modelo)
    
    def acelerar(self):
        print("Chiiiii")

class Jetski(Veiculo):
    def __init__(self, marca, cor, tipo, modelo):
        super().__init__(marca, cor, tipo, modelo)
    
    def acelerar(self):
        print("Blooo Blooo Blooo")

class Iate(Veiculo):
    def __init__(self, marca, cor, tipo, modelo):
        super().__init__(marca, cor, tipo, modelo)
        self.__bar = []

    def acelerar(self):
        print("Splech Splech")

    def abastecer_bar(self, bebiba):
        self.__bar.append(bebiba)
    
    def listar_bebidas(self):
        for b in self.__bar:
            print(f"Bebida: {b}")
    



v1 = Bicicleta("Monark", "Vermelha", "Terrestre", "1980")

v2 = Jetski("Seadoo", "Azul", "Aquático", "GTI 750")

v3 = Iate("Sunseeker", "Branco", "Aquático", "BJOA")

for i in [v1, v2, v3]:
    print(i)
    i.acelerar()

v3.abastecer_bar("Refrigerante Coca Cola")
v3.listar_bebidas()


