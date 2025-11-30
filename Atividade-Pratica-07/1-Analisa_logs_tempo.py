"""Crie um programa que lê um arquivo CSV de logs de treinamento com a biblioteca pandas, calcule
 e exiba a média e o desvio padrão da coluna tempo_execucao,
 caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. """


import pandas as pd

def analisar_logs(arquivo_csv):
    try:
        df = pd.read_csv(arquivo_csv)
        
        if 'tempo_execucao' not in df.columns:
            print("Erro: o arquivo não contém a coluna 'tempo_execucao'.")
            return
        
        media = df['tempo_execucao'].mean()
        desvio_padrao = df['tempo_execucao'].std()        
        
        print(f"Média do tempo de execução: {media:.4f}")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.4f}")
    
    except FileNotFoundError:
        print(f"Erro: o arquivo '{arquivo_csv}' não foi encontrado.")
    except pd.errors.EmptyDataError:
        print(f"Erro: o arquivo '{arquivo_csv}' está vazio ou não é um CSV válido.")
    except pd.errors.ParserError:
        print(f"Erro: não foi possível analisar o arquivo '{arquivo_csv}'. Formato inválido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

analisar_logs("Atividade-Pratica-07/logs_treinamento.csv")