primeiro_numero = int(input("Digite um número:"))
segundo_numero = int(input("Digite um número:"))
operacao = input("Digite uma operação:")

match operacao:
    case"+":
        resultado = primeiro_numero + segundo_numero
    case"-":
        resultado = primeiro_numero - segundo_numero
    case"*":
        resultado = primeiro_numero * segundo_numero
    case"/":
        resultado = primeiro_numero / segundo_numero
    case _:
        print("Opção Inválida")
        
print()
print(f"Primeiro número: {primeiro_numero}")
print(f"Operação: {operacao}")
print(f"Segundo número: {segundo_numero}")
print(f"Resultado: {resultado}")