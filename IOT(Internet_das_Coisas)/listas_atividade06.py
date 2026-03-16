import os
# CÓDIGO USADO PARA LIMPAR O TERMINAL
os.system('cls' if os.name == 'nt' else 'clear') # Limpar o Terminal

# LISTANDO DE FORMA DEFINIDA OS NÚMEROS
lista1 = [2, 4, 5, 6, 7, 5]
lista2 = [2, 5, 7, 9, 7, 9]

# CRINANDO LISTA 3
lista3 = []

for num in lista1:
    if num not in lista3:
        lista3.append(num)

for num in lista2:
    if num not in lista3:
        lista3.append(num)

print()
print(f"Lista 1", lista1)
print(f"Lista 2", lista2)
print(f"Lista 3 (sem repetições)", lista3)