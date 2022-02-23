import os
from agenda2 import Agenda
from cores import Cores

os.system('cls')

cor = Cores()

Compromissos = []

Compromissos.append(Agenda('Reunião 13:00'))
Compromissos.append(Agenda('Reunião 14:00'))
Compromissos.append(Agenda('Reunião 15:00'))
Compromissos.append(Agenda('Reunião 16:00'))
Compromissos.append(Agenda('Reunião 17:00'))

for compromisso in Compromissos:
    if compromisso.descricao == 'Reunião 15:00':
        compromisso.concluir()

print(cor.ATENCAO + '-----AGENDA------------------------------------'+cor.RESET)

print(cor.ERRO + 'Compromisso\t\t\tStatus' + cor.RESET)

print(cor.ATENCAO + '='*54 + cor.RESET)

for compromisso in Compromissos:
    print(f'\t• {compromisso}')
print(cor.ATENCAO + '='*54 + cor.RESET)

print()