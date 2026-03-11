#esse vai ser um sistema para registrar alunos, suas notas e as médias.
aluno = [
    ["Henrique", 7, 8],
    ["juninho", 5, 2]
]
for aluno in aluno:
    media = (aluno[1] + aluno[2]) / 2
    print (f"{aluno[0]} Tem a média: {media}")