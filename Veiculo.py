class Veiculo:
    def __init__( self, chassi, marca, modelo, ano ):
        self.__tipo = None
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self,tipo):
        self.__tipo = tipo
    """ Interfaces """
    def ligar( self ):
        print(f"{self.__tipo} está ligado(a).")
    def acelerar(self):
        print(f"{self.__tipo} está acelerando.")
    def frear(self):
        print(f"{self.__tipo} está freando.")
    def desligar( self ):
        print(f"{self.__tipo} está desligado(a).")
