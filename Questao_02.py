import os
os.system("cls || clear")

def academia():

    nome = input("Digite seu nome: ")
    pesos = []

    for i in range(3):
        peso = float(input(f"Digite o {i +1}° peso levantado em kg: "))
        pesos.append(peso)

    media = sum(pesos) / len(pesos)

    if media < 40:
        mensagem = "Continue Firme!\n O importante é a constância!"
    elif 40 <= media <= 80:
        mensagem = "Ótimo Trabalho!\n Você está evoluindo bem!"
    else:
        mensagem = "Incrível!\n Seu desempenho está excelente!"
    
    print()
    print("\n === RESULTADOS ACADEMIA ===")
    print(f"Nome: {nome}")
    print(f"Média de pesos levantados {media} em kg")
    print(f"Mensagem: {mensagem}")

academia()