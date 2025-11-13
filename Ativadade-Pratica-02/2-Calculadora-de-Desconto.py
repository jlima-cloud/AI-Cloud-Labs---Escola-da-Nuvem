"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

fator_desconto = porcentagem_desconto / 100
valor_desconto = preco_original * fator_desconto

preco_final = preco_original - valor_desconto

print("--- Detalhes do Desconto ---")
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(".................................")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final com Desconto: R$ {preco_final:.2f}")