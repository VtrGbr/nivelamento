#Dicionarios de estudantes
#Cada estudante serah identificado pelo seu numero de matricula
#No dicionario irah conter: matricula: periodo,materias que estah pagando, turno
estudantes= {
    "100": {"periodo": 3,"materias": ["ED,LFA,Física 2,C3, Sistemas digitais,Metodologia,Quimica"],"turno": "Integral"},
    "101": {"periodo": 2,"materias": ["ED,C2,Física 1,Circuitos, Lógica,Desenho,Algebra"],"turno": "Matutino"},
    "102": {"periodo": 1,"materias": ["P1,Matemática discreta,C1, GA,IEC"],"turno": "Vespertino"},
    "103":{"periodo": 4,"materias": ["Projeto,Grafos,Física 3,Cálculo 4, OAC,PAA"],"turno": "Integral"}
}

repeticao = int(input("Quantos alunos você quer analisar? "))

while repeticao > 0:
    matricula = input("Digite o número da matrícula do aluno: ")

    if matricula in estudantes:
        print(f"Período: {estudantes[matricula]['periodo']}")
        print(f"Materias: {','  .join(estudantes[matricula]['materias'])}")
        print(f"Turno: {estudantes[matricula]['turno']}")
    else:
        print("Aluno nao encontrado")
    repeticao = repeticao - 1
