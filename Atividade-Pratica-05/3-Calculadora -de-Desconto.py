"""3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado."""


def calcular_desconto(preco, porcentagem_desconto):
    if preco < 0 or porcentagem_desconto < 0:
        raise ValueError("Os valores não podem ser negativos.")
    desconto = (preco / 100) * porcentagem_desconto
    preco_final = preco - desconto
    return round(preco_final, 2)


def main():
    try:
        preco = float(input("Digite o preço do produto: R$ "))
        porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))
        preco_final = calcular_desconto(preco, porcentagem_desconto)
        print(f"Preço final após desconto: R$ {preco_final:.2f}")
        print(f"Desconto aplicado: {porcentagem_desconto}%")
        print(f"Valor do desconto: R$ {(preco - preco_final):.2f}")
    except ValueError as e:
        print(f"Erro: {e}")
    except KeyboardInterrupt:
        print("\nSaindo...")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()