import os
# CÓDIGO USADO PARA LIMPAR O TERMINAL
os.system('cls' if os.name == 'nt' else 'clear') # Limpar o Terminal

numeros = []

for x in range(5):
    print()
    numero = int(input(f"Digite o {x+1}° número:"))
    numeros.append(numero)

media = sum(numeros) / len(numeros)

print()
print(f"A média calculada foi de: {media:.2f}")