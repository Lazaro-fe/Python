import os
import random

os.system('cls' if os.name == 'nt' else 'clear') # Limpar o Terminal

print("Seja bem-vindo ao jogo da roleta de números!!")
print("Tente sua sorte!!")

sorteado = random.randint(1, 100)

tentativas = 0 # O número de tentativas aumentará a partir da quantidade de tentativas feitas pelo usuário

while True:
    numero = int(input("Advinhe o número sorteado: "))
    os.system('cls' if os.name == 'nt' else 'clear') # Limpando terminal após o usuário digitar o número

    if (numero == sorteado):
        print("Parabéns você acertou o número!!")
        print(f"Foram necessárias {tentativas} para você acertar o número")
        print(f"O número do sorteio foi: {sorteado}")
        break
    elif (numero > sorteado):
        print(f"O número é menor que o número digitado por você!!\nO número digitado por você foi {numero}")
        print(f"Número de tentativas realizadas por você: {tentativas}")
    elif (numero < sorteado):
        print(f"O número é maior que o número digitado por você!!\nO número digitado por você foi {numero}")
        print(f"Número de tentativas realizadas por você: {tentativas}")