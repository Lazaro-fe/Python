vetor_de_notas = []
vetor_de_nomes = []
notas_acima_da_media_calculada = []

# O enunciado pedia 8 alunos
for i in range(8):
    # Usando i+1 para perguntar sobre o 1º aluno, 2º aluno, etc.
    nome = input(f"Digite o nome do {i+1}° aluno: ")
    valores_notas = float(input(f"Digite a nota de {nome}: "))
    
    if (valores_notas >= 0 and nome != ''):
        vetor_de_notas.append(valores_notas)
        vetor_de_nomes.append(nome)
    else:
        print("Entrada Inválida!!")
        break

if len(vetor_de_notas) > 0:
    media_aritmetica_da_turma = sum(vetor_de_notas) / len(vetor_de_notas)

    # Aqui ele apenas FAZ a verificação
    for valores_notas in vetor_de_notas:
        if valores_notas > media_aritmetica_da_turma:
            notas_acima_da_media_calculada.append(valores_notas)

    # Note que os prints estão alinhados com o 'for', e não dentro dele!
    # Isso garante que eles só rodem depois que o 'for' terminar.
    print("\n--- RESULTADOS ---")
    print(f"O valor da média aritmética da turma é : {media_aritmetica_da_turma:.2f}")
    print(f"Os nomes dos alunos são: {vetor_de_nomes}")
    
    # Se a lista de notas acima da média estiver vazia, avisamos o usuário
    if len(notas_acima_da_media_calculada) > 0:
        print(f"As notas que são acima da média aritmética da turma: {notas_acima_da_media_calculada}")
    else:
        print("Nenhuma nota ficou acima da média da turma!")
        
else:
    print("\nNenhum dado válido foi inserido para calcular a média.")