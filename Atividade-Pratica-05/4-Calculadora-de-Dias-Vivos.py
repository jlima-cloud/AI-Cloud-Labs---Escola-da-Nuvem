"""4 - Crie um programa que calcule a quantos dias 
um individuo está vivo de acordo com a data do dia."""

from datetime import datetime, date

def calcular_idade(data_nascimento):
    hoje = date.today()
    idade = hoje - data_nascimento
    return idade.days


def main():
    try:
        data_nascimento_str = input("Digite a data de nascimento (no formato DD-MM-AAAA): ")
        data_nascimento = datetime.strptime(data_nascimento_str, "%d-%m-%Y").date()
        idade_dias = calcular_idade(data_nascimento)
        print(f"Você está vivo há {idade_dias} dias.")
    except ValueError:
        print("Data de nascimento inválida. Por favor, use o formato DD-MM-AAAA.")
    except KeyboardInterrupt:
        print("\nSaindo...")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()