# CORRIGIR ESSE CÓDIGO E REFAZE-LÓ DE FORMA EXPLICATIVA
# O ERRO DESSE CÓDIGO ENCONTRA-SE NA ÚLTIMA PARTE DO 


vetor_de_notas = []
vetor_de_nomes = []
notas_acima_da_media_calculada = []

for i in range(8):
    nome = input(f"Digite o nome do {i+1}° aluno: ")
    notas = float(input(f"Digite a nota de {nome}: "))
    
    if notas >= 0 and nome != '':
        vetor_de_notas.append(notas)
        vetor_de_nomes.append(nome)
    else:
        print("Entrada Inváida!!")
        break

if len(vetor_de_notas) > 0:
    media_aritmetica_da_turma = sum(vetor_de_notas) / len(vetor_de_notas)

    for notas in vetor_de_notas:
        if notas > media_aritmetica_da_turma:
            notas_acima_da_media_calculada.append(notas)

    print()
    print(f"O valor da media aritmetica da turma é : {media_aritmetica_da_turma:.2f}")
    print(f"O nomes dos alunos {vetor_de_nomes}")
    print(f"As notas que são acima da média aritmética da turma: {notas_acima_da_media_calculada}")
else:
    print("\nNenhum dos processos válidos!!")