from email.errors import InvalidDateDefect


class Agenda:
    lista = []
    dicionario = {}

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone