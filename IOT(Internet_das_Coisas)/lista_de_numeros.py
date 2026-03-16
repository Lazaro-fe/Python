numeros_digitados = []

while True:
    valores = int(input("Digite um números:"))

    if(valores != 0):
        numeros_digitados.append(valores)
    else:
        break

    print(f"Os valores digitados são: {numeros_digitados}")