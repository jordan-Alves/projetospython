#Curso Tecnico de Informatica
#Autor: Sebastiao Marcos
#Data de incio: 16/02/2022
#Termino:16/02/2022
#orientação a objetos

#importando as bibliotecas
from calendar import c
from conta import Conta
from carro import Carro
from pessoa import Pessoa

import os

os.system('cls')

#importando as classes
os.system('cls')

#--------------------------------------------------------------------
print('PROGRAMA PRINCIPAL')
print()

print('Objeto do tipo pessoa------------------------------------------')

#criando objetos pessoa
gerente = Pessoa('Jhon Doe',50)
officeboy = Pessoa('Smith',20)

print(f'\tNome: {officeboy.nome}')
print(f'\tIdade: {officeboy.idade}')
print()

#---------------------------------------------------------------------
print('Objetos do tipo carro-----------------------------------------')

#criando objetos do tipo carro
gol = Carro('Wolkswagen','Branca','BRA3049',1985)
ferrari = Carro('F250','Vermelha','BRA6060',2020)
prios = Carro('Toyota','Marrom','BRA9090',2022)

print(f'\tFabricante:{gol.fabricante}')
print(f'\tCor: {gol.cor}')
print(f'\tPlaca: {gol.placa}')
print(f'\tAno: {gol.ano}')

print()
#----------------------------------------------------------------------
print('Objetos do tipo conta------------------------------------------')

#criando objetos conta
john = Conta('John Doe',123456,1550,13)
jane = Conta('Jane doe',654321,2525,15)

print(f'\tNome do Cliente: {john.cliente}')
print(f'\tAgencia: {john.agencia}')
print(f'\tNumero da Conta: {john.conta}')
print(f'\tDigito: {john.digito}')

#------------------------------------------------------------------------
print('-'*70)