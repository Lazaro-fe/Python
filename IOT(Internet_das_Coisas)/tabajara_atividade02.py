import os
# CÓDIGO USADO PARA LIMPAR O TERMINAL
os.system('cls' if os.name == 'nt' else 'clear') # Limpar o Terminal

nome_do_colaborador = input("Digite o nome do colaborador:")
salario_do_colaborador = float(input("Digite o salário do colaborador:"))

if (salario_do_colaborador <= 280): # Aumento salarial de 20%
    aumento_salarial = salario_do_colaborador * 0.20
elif (salario_do_colaborador > 281 and salario_do_colaborador <= 700): # Aumento salarial de 15%
    aumento_salarial = salario_do_colaborador * 0.15
elif (salario_do_colaborador > 701 and salario_do_colaborador <= 1500): # Aumento salarial de 10%
    aumento_salarial = salario_do_colaborador * 0.10
else: # Aumento salarial de 5%
    aumento_salarial = salario_do_colaborador * 0.05

novo_salario = salario_do_colaborador + aumento_salarial

print()
print(" ===== ORGANIZAÇÕES TABAJARA ======")
print(f"Nome do colaborador: {nome_do_colaborador}")
print(f"Salário do colaborador sem o aumento: R$ {salario_do_colaborador} reais")
print(f"Salário do colaborador com o aumento: R$ {novo_salario} reais")