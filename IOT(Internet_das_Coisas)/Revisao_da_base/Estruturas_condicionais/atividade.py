desemp_carnaval = int(input("Com quantas pessoas você ficou no CARNAVAL?"))

if (desemp_carnaval >= 1 and desemp_carnaval < 3):
    print("Você foi bem!!")
elif (desemp_carnaval >= 3 and desemp_carnaval < 10):
    print("Você foi muito bem!!")
else:
    print("Você é um mito!!")
    
print()
print(f"Quantas pessoa você pegou: {desemp_carnaval}")