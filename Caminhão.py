import Veiculo
class Caminhao ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, cambio, tipoCaminhao, capacidadeMaxima ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Caminhão")
        self.cambio = cambio
        self.tipoCaminhao = tipoCaminhao
        self.capacidadeMaxima = capacidadeMaxima
        self.marcha = 0
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 0
""" Aqui comeca o teste """
CaminhaoNovo = Caminhao('5AZKG01Z12A339037', 'DAF', 'CF 85 460', '2020', 'Automático', 'Truck', '30 tn')
print(CaminhaoNovo.get_tipo())
print(CaminhaoNovo.cambio)
print(CaminhaoNovo.tipoCaminhao)
print(CaminhaoNovo.capacidadeMaxima)
print(CaminhaoNovo.ligar())
print(CaminhaoNovo.acelerar())
print(CaminhaoNovo.frear())
print(CaminhaoNovo.desligar())
