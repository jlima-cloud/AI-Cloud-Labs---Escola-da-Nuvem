"""3 - Crie um programa que consulte informações de um 
na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não 
existir ou houver erro na requisição, mostre uma mensagem de falha."""


import requests

def consultar_cep():
    print("=== CONSULTA DE CEP ===")
    print()
    
    cep = input("Digite o CEP (apenas números): ").strip()
    cep = cep.replace("-", "").replace(".", "")
    
    if len(cep) != 8 or not cep.isdigit():
        print("\n CEP inválido! Digite 8 números.")
        return consultar_novamente()
    
    try:
        print("\n Consultando CEP...")
        
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url, timeout=5)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            
            if "erro" in dados:
                print("\n CEP não encontrado!")
                print("   Verifique se o CEP está correto.")
            else:
                print("\n CEP ENCONTRADO!")
                print("-" * 40)
                print(f" Logradouro: {dados.get('logradouro', 'N/A')}")
                print(f"  Bairro: {dados.get('bairro', 'N/A')}")
                print(f"  Cidade: {dados.get('localidade', 'N/A')}")
                print(f" Estado: {dados.get('uf', 'N/A')}")
                print("-" * 40)
        else:
            print(f"\n Erro na consulta. Código: {resposta.status_code}")
            
    except requests.ConnectionError:
        print("\n FALHA NA CONEXÃO!")
        print("   Verifique sua conexão com a internet.")
        
    except requests.Timeout:
        print("\n TEMPO ESGOTADO!")
        print("   O servidor demorou muito para responder.")
        
    except Exception as e:
        print(f"\n ERRO: {e}")
        print("   Tente novamente mais tarde.")
    
    return consultar_novamente()

def consultar_novamente():
    print()
    if input("Deseja consultar outro CEP? (s/n): ").lower() == 's':
        print()
        consultar_cep()

if __name__ == "__main__":
    consultar_cep()