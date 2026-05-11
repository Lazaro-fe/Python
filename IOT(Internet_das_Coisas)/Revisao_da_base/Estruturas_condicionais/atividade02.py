nome = input("Digite sua nome: ")
idade = int(input("Digite sua idade: "))

if (idade >0 and idade <= 12):
    print()
    print(f"{nome} possuí {idade} anos!")
    print("Você se enquadra como uma criança!")
elif (idade > 13 and idade <= 17):
    print()
    print(f"{nome} possuí {idade} anos!")
    print("Você se enquadra como adolescente!")
elif (idade > 18 and idade <= 59):
    print()
    print(f"{nome} possuí {idade} anos!")
    print("Você se enquadra como Adulto!")
elif idade >= 60:
    print()
    print(f"{nome} possui {idade} anos!")
    print("Você se enquadra como Idoso!")