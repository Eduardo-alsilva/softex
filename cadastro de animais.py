class cadastro:
    nome=''
    raça=''
    idade=''
    responsavel=''
    telefone=''


def informação():
    cad=cadastro()
    cad.nome=input("Digite o nome do pet:")
    cad.raça=input("Digite o nome da raça:")
    cad.idade=input("Digite a idade do pet:")
    cad.responsavel=input("nome do dono:")
    cad.telefone=input("digite o numero do telefone:")
    return cad