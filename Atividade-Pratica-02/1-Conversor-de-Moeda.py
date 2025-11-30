"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar_bruto = valor_reais / taxa_dolar
valor_euro_bruto = valor_reais / taxa_euro

valor_dolar = round(valor_dolar_bruto, 2)
valor_euro = round(valor_euro_bruto, 2)

print("--- Conversor de Moeda ---")
print(f"Valor Inicial (R$): {valor_reais:.2f}")
print(f"Taxa USD: R$ {taxa_dolar:.2f} | Taxa EUR: R$ {taxa_euro:.2f}")
print("###########################################")
print(f"Valor em Dólares (USD): $ {valor_dolar}")
print(f"Valor em Euros (EUR): € {valor_euro}")