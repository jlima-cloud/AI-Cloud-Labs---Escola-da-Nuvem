"""4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, 
caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro."""


import requests
from datetime import datetime
import json

class ConsultaCotacao:
    def __init__(self):
        self.base_url = "https://api.awesomeapi.com.br/json/last/"
        self.base_url_alt = "https://economia.awesomeapi.com.br/last/"
    
    def formatar_data(self, timestamp):
        try:
            dt = datetime.fromtimestamp(int(timestamp))
            return dt.strftime("%d/%m/%Y %H:%M:%S")
        except:
            return "Data não disponível"
    
    def testar_conexao(self):
        try:
            response = requests.get("https://www.google.com", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def consultar_moeda(self, moeda_origem):
        try:
            if not self.testar_conexao():
                return {"erro": "Sem conexão com a internet"}
            
            moeda_par = f"{moeda_origem}-BRL"
            urls = [
                f"{self.base_url}{moeda_par}",
                f"{self.base_url_alt}{moeda_par}",
                f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
            ]
            
            print(f"\nConsultando cotação de {moeda_origem} para BRL...")
            
            for i, url in enumerate(urls):
                try:
                    print(f"Tentativa {i+1}...")
                    response = requests.get(url, timeout=10, headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                    })
                    
                    if response.status_code == 200:
                        data = response.json()
                        
                        if i < 2:
                            key = f"{moeda_origem}BRL"
                            if key in data:
                                cotacao = data[key]
                                return {
                                    "sucesso": True,
                                    "moeda": cotacao.get("code", moeda_origem),
                                    "nome": cotacao.get("name", ""),
                                    "valor_atual": float(cotacao.get("bid", 0)),
                                    "maxima": float(cotacao.get("high", 0)),
                                    "minima": float(cotacao.get("low", 0)),
                                    "variacao": float(cotacao.get("varBid", 0)),
                                    "pct_variacao": float(cotacao.get("pctChange", 0)),
                                    "data_hora": self.formatar_data(cotacao.get("timestamp", ""))
                                }
                        else:
                            if "rates" in data and "BRL" in data["rates"]:
                                rate = data["rates"]["BRL"]
                                return {
                                    "sucesso": True,
                                    "moeda": moeda_origem,
                                    "nome": f"{moeda_origem}/Real Brasileiro",
                                    "valor_atual": rate,
                                    "maxima": rate,
                                    "minima": rate,
                                    "variacao": 0,
                                    "pct_variacao": 0,
                                    "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                                }
                except:
                    continue
            
            return {"erro": f"Não foi possível obter cotação para {moeda_origem}"}
                
        except Exception as e:
            return {"erro": f"Erro inesperado: {str(e)}"}
    
    def exibir_cotacao(self, resultado):
        print("\n" + "="*50)
        
        if "erro" in resultado:
            print(f"ERRO: {resultado['erro']}")
        else:
            print(f"COTAÇÃO: {resultado['nome']}")
            print(f"Código: {resultado['moeda']}")
            print("-" * 50)
            print(f"Valor Atual: R$ {resultado['valor_atual']:.4f}")
            print(f"Máxima: R$ {resultado['maxima']:.4f}")
            print(f"Mínima: R$ {resultado['minima']:.4f}")
            print(f"Variação: R$ {resultado['variacao']:.4f} ({resultado['pct_variacao']:.2f}%)")
            print(f"Última Atualização: {resultado['data_hora']}")
        
        print("="*50)

def menu_principal():
    consulta = ConsultaCotacao()
    
    moedas_populares = {
        "1": ("USD", "Dólar Americano"),
        "2": ("EUR", "Euro"),
        "3": ("GBP", "Libra Esterlina"),
        "4": ("JPY", "Iene Japonês"),
        "5": ("BTC", "Bitcoin"),
        "6": ("ETH", "Ethereum"),
        "7": ("ARS", "Peso Argentino"),
        "8": ("CAD", "Dólar Canadense"),
        "9": ("AUD", "Dólar Australiano"),
        "10": ("CHF", "Franco Suíço")
    }
    
    while True:
        print("\nCONSULTA DE COTAÇÕES - REAL (BRL)")
        print("-" * 40)
        print("Escolha uma opção:")
        print("\nMoedas Populares:")
        for key, (codigo, nome) in moedas_populares.items():
            print(f"{key}. {nome} ({codigo})")
        print("\nDigitar código da moeda")
        print("1002. Testar conexão")
        print("0. Sair")
        
        opcao = input("\nOpção: ").strip()
        
        if opcao == "0":
            print("\nEncerrando programa...")
            break
        elif opcao == "11":
            moeda = input("\nDigite o código da moeda (ex: USD, EUR, BTC): ").strip().upper()
            if moeda:
                resultado = consulta.consultar_moeda(moeda)
                consulta.exibir_cotacao(resultado)
            else:
                print("Código de moeda inválido!")
        elif opcao == "1002":
            print("\nTestando conexão...")
            if consulta.testar_conexao():
                print("Conexão OK!")
            else:
                print("Sem conexão com a internet!")
        elif opcao in moedas_populares:
            moeda_codigo, _ = moedas_populares[opcao]
            resultado = consulta.consultar_moeda(moeda_codigo)
            consulta.exibir_cotacao(resultado)
        else:
            print("Opção inválida!")
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    menu_principal()