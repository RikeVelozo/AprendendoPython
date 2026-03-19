#esse vai ser um sistema para registrar alunos, suas notas e as médias.

lista_alunos = []
for i in range(1):
    aluno_indiv = []
    Nome = input('Digite o nome do aluno: ')
    aluno_indiv.append(Nome)
    for j in range(3):
        Nota = int(input('Digite a nota do aluno: '))
        aluno_indiv.append(Nota)
    media = int((aluno_indiv[1] + aluno_indiv[2] + aluno_indiv[3]) / 3)
    lista_alunos.append(aluno_indiv)
print (lista_alunos)
print (f"A média desse aluno é: {media}, ele foi {'APROVADO :)' if media >= 6 else 'REPROVADO :('}")