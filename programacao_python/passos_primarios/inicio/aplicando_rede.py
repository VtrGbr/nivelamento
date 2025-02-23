import redes

print("Amigos em comum de Joao e Maria ", redes.amigos_em_comum("Joao","Maria"))

print("Aurora segue: ",", ".join(redes.rede_social["Aurora"]["seguindo"]))
redes.seguir("Aurora","Guilherme")

print("Aurora segue: ",redes.rede_social["Aurora"]["seguindo"])