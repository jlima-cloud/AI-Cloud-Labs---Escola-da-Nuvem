#1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

def calculadora_simples():
    while True:
        try:
            expressao = input("\nDigite a expressão (ex: 15 + 3 ) ou 'sair': ")
            
            if expressao.lower() == 'sair':
                break
            
            
            if any(op in expressao for op in ['+', '-', '*', '/']):
                resultado = eval(expressao)
                print(f"Resultado: {resultado}")
            else:
                print("Formato inválido! Use: número operador número")
                
        except ZeroDivisionError:
            print("Erro: Divisão por zero!")
        except:
            print("Erro: Expressão inválida!")


calculadora_simples()