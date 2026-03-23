# 2°Questão - Crie um Script usando função que recebe um nome de uma pessoa e informa quantas letras tem naquele nome

def contar_numeros_de_um_nome():

    nome_sem_espacos = (" ", "")
    return len(nome_sem_espacos)

nome_de_usuário = input("Digite um nome:")
contar_numeros_de_um_nome(nome_de_usuário)

print(f"O nome é {nome_de_usuário} ---- A quantidade de letras é {contar_numeros_de_um_nome}")