temper = []

for i in range(5):
    temperatura = float(input(f"Digite a {i+1}° temperatura: "))
    temper.append(temperatura)

maior_temperatura = max(temper)
menor_temperatura = min(temper)
temp_media = sum(temper) / len(temper)

print()
print(f"A maior temperatura é: {maior_temperatura}")
print(f"A menor temperatura é: {menor_temperatura}")
print(f"A média das temperatura é igual a: {temp_media:.2f}")