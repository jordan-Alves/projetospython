from mimetypes import init


class Carro:

    #metodo __inti__ obrigatório (construtor):
    def __init__(self, fabricante, cor, placa,ano):
        self.fabricante = fabricante
        self.cor = cor
        self.placa = placa
        self.ano = ano

        