"""Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
unidade_destino = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
if unidade_origem == 'C':
    if unidade_destino == 'F':
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_destino == 'K':
        temperatura_convertida = temperatura + 273.15
    else:
        temperatura_convertida = temperatura
elif unidade_origem == 'F':
    if unidade_destino == 'C':
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_destino == 'K':
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
    else:
        temperatura_convertida = temperatura    
elif unidade_origem == 'K':
    if unidade_destino == 'C':
        temperatura_convertida = temperatura - 273.15
    elif unidade_destino == 'F':
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
    else:
        temperatura_convertida = temperatura
else:
    print("Unidade de origem inválida.")
    temperatura_convertida = None
if temperatura_convertida is not None:
    print(f"A temperatura convertida é: {temperatura_convertida:.2f} {unidade_destino}")
print("\nFim do Programa!")