nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if (idade >= 0 and idade < 3):
    print("Você é bebê!!")
elif (idade >= 3 and idade < 6):
    print("Você é criança!!")
elif (idade >= 6 and idade < 12):
    print("Você é pré-adolescente")
elif (idade >= 12 and idade < 18):
    print("Você é um adolescente!!")
elif (idade >= 18 and idade < 50):
    print("Você é Adulto!!")
else:
    print("Você é Idoso")
    
print()
print(f"Nome: {nome}")
print(f"Idade: {idade}")