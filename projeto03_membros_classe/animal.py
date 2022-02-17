class Animal:

    #utilizando parametros nomeados:
    def __init__(self,nome = 'Sem nome', raca = 'Labrador', nascimento = 1970):
        self.nome = nome
        self.raca = raca
        self.nascimento = nascimento

        #metodo interno (__str___) para dar saida string
    def __str__(self):
            return f'''
            Nome: {self.nome}
            Data de nascimento = {self.raca}
            Idade: {self.nascimento} anos '''

        