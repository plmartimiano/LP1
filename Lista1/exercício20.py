# Cadastro de aluno e cálculo da nota final
nome = input("qual é o seu nome? ")
idade = input("qual é a sua idade? ")
nota_1 = input("qual é a sua nota da primeira avaliação na disciplina matemática? ")
nota_2 = input("qual é a sua nota da segunda avaliação na disciplina matemática? ")
Nota_3 = input("qual é a sua nota da terceira avaliação na disciplina matemática? ")
media = (float(nota_1) + float(nota_2) + float(Nota_3)) / 3
print ("nome do aluno:", nome)
print ("idade do aluno:", idade)
print ("Nota final:", media)