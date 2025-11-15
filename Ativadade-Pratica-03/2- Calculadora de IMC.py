# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa solicita peso (kg) e altura (m), calcula o IMC e dá a classificação:
# < 18.5: Abaixo do peso
# < 25:   Peso normal
# < 30:   Sobrepeso
# >= 30:  Obeso

nome = input("Por favor, insira seu nome: ")
peso = float(input("Por favor, insira seu peso em kg: "))
altura = float(input("Por favor, insira sua altura em metros: "))
imc = peso / (altura ** 2)
print (f"{nome}, seu IMC é: {imc:.2f}")

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    imc >= 30
    classificacao = "Obeso"


print("Classificação:", classificacao)
print("\nFim do Programa!")