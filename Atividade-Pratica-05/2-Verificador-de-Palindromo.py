"""2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação).
 Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”."""

import re

def eh_palindromo(texto):
    texto = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    return texto == texto[::-1]


def main():
    texto = input("Digite uma palavra ou frase: ")
    if eh_palindromo(texto):
        print("Sim")
    else:
        print("Não")


if __name__ == "__main__":
    main()