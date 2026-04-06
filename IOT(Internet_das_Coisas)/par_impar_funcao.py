# 1° Questão: Crie um Script usando função, que recebe um número e informa se esse número é par ou ímpar

def par_impar(nume):

    if (nume %2 == 0):
        print()
        print(f"O número {nume} é par")
    else:
        print()
        print(f"O número {nume} é ímpar")

print("======= ÍMPAR OU PAR ======")
nume = int(input("Digite um número para conferir se é impar ou par: "))
par_impar(nume)