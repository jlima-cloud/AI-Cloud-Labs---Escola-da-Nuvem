"""4 - Criar um código que serve para analisar números digitados pelo usuário,
 classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos."""


class AnalisadorNumeros:
    def __init__(self):
        self.pares = 0
        self.impares = 0

    def analisar_numero(self, numero):
        try:
            numero = int(numero)
            if numero % 2 == 0:
                self.pares += 1
                print(f"{numero} é par.")
            else:
                self.impares += 1
                print(f"{numero} é ímpar.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    def relatorio(self):
        print(f"\nTotal de números pares: {self.pares}")
        print(f"Total de números ímpares: {self.impares}")


def main():
    analisador = AnalisadorNumeros()
    while True:
        numero = input("Digite um número (ou 'sair' para parar): ")
        if numero.lower() == 'sair':
            analisador.relatorio()
            break
        analisador.analisar_numero(numero)


if __name__ == "__main__":
    main()