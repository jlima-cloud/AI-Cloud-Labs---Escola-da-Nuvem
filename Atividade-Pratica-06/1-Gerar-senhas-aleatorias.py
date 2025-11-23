""""1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  
também escolha o tamanho da senha  para criar senhas seguras automaticamente."""

import random
import string

def gerar_senha():
    print("=== GERADOR DE SENHAS SEGURAS ===")
    print()
    
    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha desejada (mínimo 4): "))
            if tamanho < 4:
                print(" A senha deve ter pelo menos 4 caracteres para ser segura!")
                continue
            break
        except ValueError:
            print(" Por favor, digite um número válido!")
    
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation
    
    todos_caracteres = letras_minusculas + letras_maiusculas + numeros + simbolos
    
    senha = []
    senha.append(random.choice(letras_minusculas))
    senha.append(random.choice(letras_maiusculas))
    senha.append(random.choice(numeros))
    senha.append(random.choice(simbolos))
    
    for i in range(tamanho - 4):
        senha.append(random.choice(todos_caracteres))
    
    random.shuffle(senha)
    
    senha_final = ''.join(senha)
    
    print()
    print("Senha gerada com sucesso!")
    print(f"Sua senha: {senha_final}")
    print()
    print(" Dicas de segurança:")
    print("   • Guarde esta senha em um local seguro")
    print("   • Não compartilhe sua senha com ninguém")
    print("   • Use senhas diferentes para cada conta")
    
    print()
    continuar = input("Deseja gerar outra senha? (s/n): ").lower()
    if continuar == 's':
        print()
        gerar_senha()

if __name__ == "__main__":
    gerar_senha()