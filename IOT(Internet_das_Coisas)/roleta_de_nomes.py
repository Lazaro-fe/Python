import random

nomes_sorteados = []

for i in range(10):
    nomes_sorte = input(f"Digite o {i} ° nome: ")
    nomes_sorteados.append(nomes_sorte)

sorteio = random.choice(nomes_sorteados)

print()
print(f"O nome sorteado foi {sorteio}")