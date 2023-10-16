import Veiculo
class Empilhadeira ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, combustivel, elevacaoMaxima ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Empilhadeira")
        self.combustivel = combustivel
        self.elevacaoMaxima = elevacaoMaxima

""" Aqui comeca o teste """
EmpilhadeiraNova = Empilhadeira('EGF123456789', 'Toyota', '8FGU25', '2022', 'Diesel', '3,5 m')
print(EmpilhadeiraNova.get_tipo())
print(EmpilhadeiraNova.marca)
print(EmpilhadeiraNova.combustivel)
print(EmpilhadeiraNova.elevacaoMaxima)
print(EmpilhadeiraNova.ligar())
print(EmpilhadeiraNova.acelerar())
print(EmpilhadeiraNova.frear())
print(EmpilhadeiraNova.desligar())
