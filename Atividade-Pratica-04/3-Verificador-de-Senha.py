"""3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número."""

import re

class SenhaInseguraError(Exception):
    pass

def verificar_senha(senha):
    criterios = [
        lambda s: len(s) >= 8,
        lambda s: any(c.isdigit() for c in s),
    ]

    erros = []
    for criterio in criterios:
        if not criterio(senha):
            if criterio == criterios[0]:
                erros.append("* Deve ter pelo menos 8 caracteres.")
            elif criterio == criterios[1]:
                erros.append("* Deve conter pelo menos um número.")

    if erros:
        raise SenhaInseguraError(erros)


def main():
    while True:
        try:
            senha = input("Digite uma senha: ")
            verificar_senha(senha)
            print("Senha segura!")
            break
        except SenhaInseguraError as e:
            print("Senha não atende aos critérios de segurança:")
            for erro in e.args[0]:
                print(erro)
        except KeyboardInterrupt:
            print("\nSaindo...")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()