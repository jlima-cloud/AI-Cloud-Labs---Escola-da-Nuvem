"""4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais."""


distancia_percorrida = 300
combustivel_gasto = 25

consumo_bruto = distancia_percorrida / combustivel_gasto

consumo_medio = round(consumo_bruto, 2)

print("Relatório de Consumo")
print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print("----------------------------")
print(f"Consumo Médio (km/l): {consumo_medio}")