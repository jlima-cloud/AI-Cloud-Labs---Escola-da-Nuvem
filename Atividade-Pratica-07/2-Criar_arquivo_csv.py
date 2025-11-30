"""2 - Crie um programa que cria um arquivo CSV com nome, idade e cidade de algumas pessoas,
 que este programa escreva os dados em formato tabular e salva no arquivo escolhido 
 pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 
"""


import csv

def criar_arquivo_csv(nome_arquivo):
    dados = [
        ["Nome", "Idade", "Cidade"],
        ["Maria", 28, "São Paulo"],
        ["João", 34, "Rio de Janeiro"],
        ["Ana", 22, "Belo Horizonte"],
        ["Carlos", 40, "Curitiba"]
    ]

    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(dados)
        
        print(f"Arquivo '{nome_arquivo}' criado e salvo com sucesso!")
    
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")

nome_arquivo = input("Digite o nome do arquivo CSV (exemplo: pessoas.csv): ")
criar_arquivo_csv(nome_arquivo)