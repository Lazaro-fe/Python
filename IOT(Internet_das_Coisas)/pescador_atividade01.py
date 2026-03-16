import os

os.system('cls' if os.name == 'nt' else 'clear') # Limpar o Terminal
peso = float(input("Digite a quantidade de peixe pescado em kg:"))

if (peso > 50):
    calculo_de_quilo_excedente = peso - 50
    multa = calculo_de_quilo_excedente * 4.00
    print()
    print(" --- PESCARIA DE JOÃO ---")
    print(f"Peso de qulio da pesca: {peso:.2f}")
    print(f"Quantidade de quilo excedente: {calculo_de_quilo_excedente:.2f}")
    print(f"Quantos reais devem ser pagos pelo excesso: R$ {multa:.2f} Reais")
else:
    peso_excedente = 0
    multa = 0
    print()
    print("--- PESCARIA DE JOÃO ---")
    print(f"Quantidade de peixe pescado: {peso} kg")
    print(f"Quantidade de peso excedente: {peso_excedente}")
    print(f"Multa à pagar: {multa}")
    print("Limite de peso respeitado!")