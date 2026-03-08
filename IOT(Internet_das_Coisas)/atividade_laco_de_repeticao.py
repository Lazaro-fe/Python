# Laço de Repetição - For and While

# Crie um sistema que recebe do usuário 10 números e ao final
# imprime a media dos números digitados pelo usuário

numeros = []

for x in range(10):
    print()
    numer = int(input(f"Digite o {x+1}° numero:"))
    numeros.append(numer)
    
media = sum(numeros) / len(numeros)

print()
print(f"A média dos números é: {media:.0f}")