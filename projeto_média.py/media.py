class Média:
    def __init__(self,nota1,nota2,nota3,nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
    
    def somanotas(nota1,nota2,nota3,nota4):
        sn = nota1 + nota2 + nota3 + nota4
        print('=-'*40)
        print(f'a soma das suas notas é igual a : {sn}')

    def medianotas(nota1,nota2,nota3,nota4):
        notas = (nota1 + nota2 + nota3 + nota4)/ 4
        print(f'a sua média é : {notas}')
        print('=-'*40)
        if notas >= 6:
            print('voce foi aprovado!')
        else:
            print('voce foi reprovado')



