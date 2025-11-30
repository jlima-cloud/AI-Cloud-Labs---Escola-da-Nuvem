"""Crie um programa que leia um arquivo CSV informado pelo usuário, 
percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo
 não seja encontrado, mostre uma mensagem de erro."""

import csv

def ler_arquivo_csv(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

nome_arquivo = input("Digite o nome do arquivo CSV que deseja ler: ")
ler_arquivo_csv(nome_arquivo)