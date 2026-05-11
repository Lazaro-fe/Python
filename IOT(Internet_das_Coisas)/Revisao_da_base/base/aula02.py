nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade?  "))
salario_bruto = float(input("Digite o valor do seu sálario bruto: R$ "))

salario_liquido = salario_bruto * 0.085

print()
print(f"SR(a) {nome}, você tem {idade} anos")
print(f"Seu sálario líquido corresponde a R$ {salario_liquido}")