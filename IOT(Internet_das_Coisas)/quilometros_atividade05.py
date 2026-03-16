import os
# CÓDIGO USADO PARA LIMPAR O TERMINAL
os.system('cls' if os.name == 'nt' else 'clear') # Limpar o Terminal

km_percorrido = float(input("Digite a quantidade de quilômetros rodados:"))
dia_de_carro_alugado = int(input("Digite a quantidade de dias que o carro foi alugado:"))

custo_de_dias_alugados = dia_de_carro_alugado * 60.00
custo_de_km_percorrido = km_percorrido * 0.15

preco_total_a_pagar = custo_de_dias_alugados + custo_de_km_percorrido

print(f"O valor que deve ser pago a locadora é de: R$ {preco_total_a_pagar:.2f} Reais")