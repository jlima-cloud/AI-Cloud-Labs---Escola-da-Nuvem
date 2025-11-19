"""1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada
    """

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):

    if not isinstance(valor_conta, (int, float)) or not isinstance(porcentagem_gorjeta, (int, float)):
        raise TypeError("Os parâmetros devem ser números.")
    if valor_conta < 0 or porcentagem_gorjeta < 0:
        raise ValueError("Os parâmetros não podem ser negativos.")

    gorjeta = (valor_conta / 100) * porcentagem_gorjeta
    return gorjeta


def main():
    try:
        valor_conta = float(input("Digite o valor total da conta: R$ "))
        porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (%): "))
        gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
        print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
        print(f"Total a pagar: R$ {valor_conta + gorjeta:.2f}")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()