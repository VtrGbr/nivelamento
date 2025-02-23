#Vamos simular um exemplo de rede social
#Nesta rede social vamos ter (As pessoas e seus seguidores, funcoes: ver seguidores em comum, adicionar usuario,seguir alguem)

rede_social = {
    "Joao":{"seguidores":{"Maria"},"seguindo":{"Guilherme","Maria"}},
    "Maria":{"seguidores": {"Joao"}, "seguindo":{"Joao","Guilherme"}},
    "Guilherme":{"seguidores":{"Joao"},"seguindo":set()},
    "Aurora":{"seguidores":set(),"seguindo":set()}
}

def adicionar_pessoa(nome):
    rede_social["nome"] = {"seguidores":set(),"seguindo":set()}

def seguir(usuario, alvo):
    valor_usuario = usuario in rede_social #retorna true ou false
    valor_alvo = alvo in rede_social
    if valor_alvo and valor_usuario:
        rede_social[usuario]["seguindo"].add(alvo)
        rede_social[alvo]["seguidores"].add(usuario)
    elif not valor_usuario and not valor_alvo:
        adicionar_pessoa(usuario)
        adicionar_pessoa(alvo)
        rede_social[usuario]["seguindo"].add(alvo)
        rede_social[alvo]["seguidores"].add(usuario)
    elif not valor_usuario:
        adicionar_pessoa(usuario)
        rede_social[usuario]["seguindo"].add(alvo)
        rede_social[alvo]["seguidores"].add(usuario)
    else:
        adicionar_pessoa(alvo)
        rede_social[usuario]["seguindo"].add(alvo)
        rede_social[alvo]["seguidores"].add(usuario)

def amigos_em_comum(pessoa1,pessoa2):
    valor_pessoa1 = pessoa1 in rede_social #retorna true ou false
    valor_pessoa2 = pessoa2 in rede_social

    if valor_pessoa1 and valor_pessoa2:
        return rede_social[pessoa1]["seguindo"] & rede_social[pessoa2]["seguindo"]
    elif not valor_pessoa1 and not valor_pessoa2:
        adicionar_pessoa(pessoa1)
        adicionar_pessoa(pessoa2)
        return rede_social[pessoa1]["seguindo"] & rede_social[pessoa2]["seguindo"]
    elif not valor_pessoa1:
        adicionar_pessoa(pessoa1)
        return rede_social[pessoa1]["seguindo"] & rede_social[pessoa2]["seguindo"]
    else:
        adicionar_pessoa(pessoa2)
        return rede_social[pessoa1]["seguindo"] & rede_social[pessoa2]["seguindo"]
