import redes

print("Amigos em comum de Joao e Maria ", redes.amigos_em_comum("Joao","Maria"))

print("Aurora segue: ",", ".join(redes.rede_social["Aurora"]["seguindo"]))
redes.seguir("Aurora","Guilherme")

print("Aurora segue: ",redes.rede_social["Aurora"]["seguindo"])

print(redes.rede_social.keys())


print(redes.seguir("Vitor","Joao"))
print("Agora Vitor segue o Joao")

seguidor = input("Digite o nome do Usuario que você quer ver quem ele está seguindo: ")
if seguidor in redes.rede_social and "seguindo" in redes.rede_social[seguidor]:
    print(redes.rede_social[seguidor]["seguindo"])

seguindo = input("Digite o nome do Usuario que você quer ver os seguidores: ")
if seguindo in redes.rede_social and "seguidores" in redes.rede_social[seguindo]:
    print(redes.rede_social[seguindo]["seguidores"])

