#esse vai ser um sistema para registrar alunos, suas notas e as médias.

lista_alunos = []
for i in range(1):
    aluno_indiv = []
    Nome = input('Digite o nome do aluno: ')
    aluno_indiv.append(Nome)
    for j in range(2):
        Nota = int(input('Digite a nota do aluno: '))
        aluno_indiv.append(Nota)
    lista_alunos.append(aluno_indiv)
print (lista_alunos)
