# O ERRO DO CÓDIGO ESTAVA NA CONTABILIDADE DOS NÚMEROS POSITIVOS E NEGATIVOS
# QUE SÃO GUARDADOS NA MEMÓRIA DA VETOR

vetor_negativos = []
soma_numeros_positivos = 0
quantidade_positivos = 0
quantidade_negativos = 0


for i in range(10):
    valores = int(input(f"Digite o {i}° número: "))
    
    if (valores >= 0):
        quantidade_positivos += 1
        soma_numeros_positivos += valores
        print(f"O números é positivo")
        print()
    else:
        quantidade_negativos += 1
        vetor_negativos.append(valores)
        print(f"O números é negativo")
        print()

print("\n======== RESULTADOS ========")
print(f"A quantidade de números negativos são : {quantidade_negativos}")
print(f"A quantidade de números positivos são : {quantidade_positivos}")
print(f"A soma dos números são : {soma_numeros_positivos}") 