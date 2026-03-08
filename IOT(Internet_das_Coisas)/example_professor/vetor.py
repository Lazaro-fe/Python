import random

numeros = [13, 14, 58, 68, 78, 11, 5]
nomes = ["Joana", "Lázaro", "Mohammed", "Ana", "Juliana", "Maria", "Diana"]

# Append - Adiciona um elemento na ultima posição da lista
# Insert  - Adiciona um elemento em uma posição específica na lista
# Pop - Remove a posição do vetor
# Remove - Deleta o valor encontrado no vetor
# Sort - Ordena de forma crescente os valores
# Reverse - Ordena de forma decrescente os valores
# Len - Contagem de valores dentro de um vetor
# Max - Procura o maior valor presente em um valor
# Min - Procura o menor valor presente em um valor
# Sum - Soma todos os valores presentes em um vetor
# Random.choice - Sorteia um valor presente em um vetor


maior = max(numeros)
menor = min(numeros)
total = sum(numeros)
sorteio = random.choice(numeros)


print(numeros)
print(f"O maior valor é : {maior}")
print(f"O menor valor é : {menor}")
print(f"A soma total dos valores é : {total}")
print(f"O número sorteado é : {sorteio}")