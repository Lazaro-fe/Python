import os
# CÓDIGO USADO PARA LIMPAR O TERMINAL
os.system('cls' if os.name == 'nt' else 'clear') # Limpar o Terminal


print(" ====== GERADOR DE INTERVALOS =====")
numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))

maior = max(numero_1, numero_2)
menor = min(numero_1, numero_2)

for numero in range(menor +1, maior):
    print(numero, end="")

print("\n")