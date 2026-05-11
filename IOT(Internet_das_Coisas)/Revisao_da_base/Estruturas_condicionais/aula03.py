nome = input("Qual o seu nome?")
idade = int(input("Qual a sua idade?"))
nota1 = float(input("Qual a sua nota da 1° unidade?"))
nota2 = float(input("Qual a sua nota da 2° unidade?"))
nota3 = float(input("Qual a sua nota da 3° unidade?"))

media = (nota1 + nota2 + nota3) / 3

print()

if media > 6:
    print("Você foi Aprovado!")
    print("Parabéns!! =) ")
else:
    print("Você foi para Recuparação!! =( )")
    print("NÃO DESISTA!!)")
    
print()
print(f"Seu nome é {nome}")
print(f"Você possui {idade} anos")
print(f"Sua média total foi de: {media:.1f}")