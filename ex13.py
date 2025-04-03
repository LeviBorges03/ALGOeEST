aluno = input("insira seu nome ESTUDANTE:")
idade = int(input("insira sua idade ESTUDANTE:"))
turma = input("insira sua turma ESTUDANTE:")
if idade>=6:
    print(f"Aluno cadastrado com sucesso: {aluno}, {idade}, {turma}.")
else:
    print(f"Aluno nao tem pra estudar conosco: {aluno}, {idade}, {turma}.")
