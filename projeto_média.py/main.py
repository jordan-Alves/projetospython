#curso Técnico de informatica
#Autor: Jordan monteiro
#Data incicio : 22/02/2022
#Término: 22/02/2022
#orientação a objetos


from msilib.schema import Media
from tkinter import N
from media import Média

media1 = Média

print('------------Média de notas dos alunos------------------------')
nota1 = (int(input('Digite a primeira nota: ')))
nota2 = (int(input('Digite a segunda nota: ')))
nota3 = (int(input('Digite a terceira nota: ')))
nota4 = (int(input('Digite a quarta nota:')))

resultado0 = media1.somanotas(nota1,nota2,nota3,nota4)
resultado = media1.medianotas(nota1,nota2,nota3,nota4)



