"""2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório.
 exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha."""

import requests

def buscar_usuario_aleatorio():
    print("=== BUSCADOR DE USUÁRIO ALEATÓRIO ===")
    print()
    
    try:
        print(" Buscando usuário...")
        
        url = "https://randomuser.me/api/"
        resposta = requests.get(url, timeout=5)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            usuario = dados['results'][0]
            
            nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']
            
            print("\n USUÁRIO ENCONTRADO!")
            print("-" * 40)
            print(f" Nome: {nome_completo}")
            print(f" E-mail: {email}")
            print(f" País: {pais}")
            print("-" * 40)
            
        else:
            print(f"\n Erro ao buscar usuário. Código de status: {resposta.status_code}")
            
    except requests.ConnectionError:
        print("\n FALHA NA CONEXÃO!")
        print("   Verifique sua conexão com a internet.")
        
    except requests.Timeout:
        print("\n TEMPO ESGOTADO!")
        print("   O servidor demorou muito para responder.")
        
    except Exception as e:
        print(f"\n ERRO INESPERADO: {e}")
        print("   Tente novamente mais tarde.")
    
    print()
    continuar = input("Deseja buscar outro usuário? (s/n): ").lower()
    if continuar == 's':
        print()
        buscar_usuario_aleatorio()

if __name__ == "__main__":
    buscar_usuario_aleatorio()