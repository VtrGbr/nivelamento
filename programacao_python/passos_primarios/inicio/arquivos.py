import os 
import tuplas_estudantes as te

def escrever_w(arquivo):
    with open(arquivo,'w') as teste:
        teste.write(f"Alunos bolsistas: \n{te.bolsistas(te.estudantes)}")
def escrever_a(arquivo):
    with open(arquivo,'a') as teste:
        teste.write(f"Curso de cada aluno:\n{te.cursos(te.estudantes)}")
def ler(arquivo):
    with open(arquivo,'r') as teste:
        mensagem = teste.read()
        print(mensagem)

arquivo = input("Digite o nome do arquivo: ")
escrever_w(arquivo)
escrever_a(arquivo)
ler(arquivo)