"""Crie um programa que leia e escreva arquivos no formato JSON, que salve 
em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia
o mesmo arquivo exibindo os dados, caso o arquivo
não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha. """

import json

def salvar_dados_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")

def ler_dados_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print("Conteúdo do arquivo JSON:")
            for chave, valor in dados.items():
                print(f"{chave}: {valor}")
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: o arquivo '{nome_arquivo}' não contém um JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

# Dicionário exemplo
pessoa = {
    "nome": "Maria",
    "idade": 28,
    "cidade": "São Paulo"
}

nome_arquivo = "pessoa.json"

salvar_dados_json(nome_arquivo, pessoa)
ler_dados_json(nome_arquivo)