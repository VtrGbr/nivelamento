#Lista de estudantes,vai conter: 
#nome, idade, periodo, bolsista,curso

estudantes=[
    ("Joao", 22, 3, "sim", "farmacia"),
    ("Gabriel", 21, 5, "nao", "Educacao fisica"),
    ("Enzo", 20, 7, "nao", "Medicina"),
    ("Tenorio", 20, 4, "sim", "Engenharia de computacao")
]

#Funções: saber quais sao bolsistas, dizer o curso de cada um, a maior idade

def bolsistas(estudantes):
    resultado = ""
    for estudante in estudantes:
        if estudante[3] == "sim":
            resultado+=f"Nome: {estudante[0]}, idade: {estudante[1]} e curso: {estudante[4]}\n"
    return resultado
def cursos(estudantes):
    resultado = ""
    for estudante in estudantes:
        resultado+=f"Nome: {estudante[0]}, curso: {estudante[4]}"
    return resultado

def maior_idade(estudantes):
    maior = 0
    resultado = ""
    nome_mais_velho = ""
    for estudante in estudantes:
        if estudante[1] > maior:
            maior = estudante[1]
            nome_mais_velho = estudante[0]
    

    resultado+=f"Nome: {nome_mais_velho}, idade: {maior}"

#print("Bolsistas: ")
#bolsistas(estudantes)
#print("Cursos: ")
#cursos(estudantes)
#print("Pessoa mais velha: ")
#maior_idade(estudantes)
    