# Alô, som!
nome = "Joao"
idade = 21
valor = 29.31

idade = int(input(f"Informe a idade de {nome}: "))

print(f"{nome} tem {idade} anos e possui R$ {valor} na carteira")
if idade < 21:
    print(f"{nome} ainda nao possui idade suficiente para maioridade civil.")
else:
    print(f"{nome} ja pode ser declarado civilmente capaz.")
print("Ate a proxima!")