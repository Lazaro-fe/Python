somador_infinito = []

while True:
    numero = float(input("Digite um número:"))

    if numero == 0:
        print("Número 0 inserido! Saindo do programa!!")
        print(f"A soma dos números inseridos é : {sum(somador_infinito)}")
        print(f"Os valores que estavam inseridos nessa soma: {somador_infinito}")
        break
    else:
        somador_infinito.append(numero)