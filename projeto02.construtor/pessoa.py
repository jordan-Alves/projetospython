class Pessoa:

    #Método construtor do Python é o __init__
    #o parametro self é obrigatorio 
    def __init__(self,nome,idade,nascimento):

        #criando os atributos dentro do construtor
        self.nome = nome
        self.idade = idade
        self.nascimento = nascimento
    def __str__(self):
        return f'''
        Nome: {self.nome}
        Data de Nascimento: {self.nascimento}
        Idade: {self.idade} anos. '''
        