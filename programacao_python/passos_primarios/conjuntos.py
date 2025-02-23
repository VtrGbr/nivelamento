#Transformando uma lista em um conjunto (Retirar numero que sao repetidos)
lista = [ 1,2,2,3,3,4]
conjunto = set(lista)

#Caso eu queira converte o conjunto novamente em lista
lista_sem_duplicata = list(conjunto)

print("Lista com duplicata: ",lista)
print("Conjunto: ",conjunto)
print("Lista sem duplicata: ",lista_sem_duplicata)

#Localizar palavras (mais eficiente que listas, ja que a tabela hash tem busca em O(1))
cidades_turisticas = {"Maceio","Lisboa","Maragogi","Sidney"}

#Palavra que eu quero procurar
cidade = "Maceio"

if cidade in cidades_turisticas: #Operador "in" usado para ver se um elemento esta no conjunto
    print("Cidade encontrada")
else:
    print("Cidade nao encontrada")

#Operacoes matematicas
cidade_numeros = conjunto | cidades_turisticas #uniao

comum = cidade_numeros & conjunto #Intersecao

diferente = cidade_numeros - cidades_turisticas  #diferenca

print("Uniao: ",cidade_numeros)
print("Interseccao: ",comum)
print("Diferentes: ",diferente)


#Verificando se ha emails cadastrados
emails_cadastrados = {"email1@gmail.com", "email2@gmail.com", "email3@gmail.com"}
email_novo = input("Digite o seu email")

if email_novo in emails_cadastrados:
    print("Email ja existente.")
else:
    emails_cadastrados.add(email_novo)
    print("Email cadastrado com sucesso")
print("Emails cadastrados : ", emails_cadastrados)

