import pandas as pd
import os

# Analisando médias e desvios padrões
def analisar_logs():
    caminho_arquivo = 'treinamento.csv'
    
    try:
        # 1. Lendo o arquivo
        dados = pd.read_csv(caminho_arquivo)
        
        # 2. Fazendo os cálculos
        media = dados['tempo_execucao'].mean()
        desvio = dados['tempo_execucao'].std()
        
        # 3. Exibindo os resultados
        print(f"--- RESULTADOS DOS LOGS ---")
        print(f"Média de Tempo: {media:.2f} segundos")
        print(f"Desvio Padrão:  {desvio:.2f}")
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except KeyError:
        print("Erro: A coluna 'tempo_execucao' não existe no arquivo.")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

#analisar_logs()

# Dados no CSV
import csv

def criação_csv():
    # Imprimindo pastas e arquivos
    pasta_atual = os.getcwd()
    print (f"Pasta {pasta_atual}:")

    arquivos_pasta = os.listdir(pasta_atual)
    for n in arquivos_pasta:
        if n.lower().endswith('csv'):
            print(f"- {n}")
    arquivo = input("Digite o nome do arquivo onde queira salvar: ")
    if not arquivo.endswith('.csv'):
        arquivo = arquivo + ".csv"

    arquivo_existe = os.path.exists(arquivo)

    print("Dados para a tabela")
    nome = input("Insira o nome: ")
    idade = input("Insira a idade: ")
    cidade = input("Insira a cidade: ")

    with open (arquivo, mode='a', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)

        if not arquivo_existe:
            print (f"Arquivo {arquivo} criado com êxito!")
            escritor.writerow (['nome','idade','cidade'])
        escritor.writerow ([nome,idade,cidade])
        
#criação_csv()

# Lendo e imprimindo conteúdo CSV
def imprimindo_csv():
    # Imprimindo pastas e arquivos
    
    pasta_atual = os.getcwd()
    print (f"Pasta {pasta_atual}:")

    arquivos_pasta = os.listdir(pasta_atual)
    for n in arquivos_pasta:
        if n.lower().endswith('csv'):
            print(f"- {n}")
    
    # Validação
    while True:
        entrada = input("Qual arquivo deseja ver o conteúdo: ")
        arquivo_ler = entrada.lower()

        if not arquivo_ler.lower().endswith('.csv'):
            arquivo_ler = arquivo_ler + ".csv"
            
        if os.path.exists(arquivo_ler.lower()):
            break
        else:
            print("Arquivo não encontrado, tente novamente.")

    #Imprimindo o conteúdo
    with open(arquivo_ler, mode='r') as f:
        arquivo_lido = f.read()
    print(f"CONTEÚDO DO ARQUIVO '{arquivo_ler}':\n\n{arquivo_lido}")
#imprimindo_csv()

# Escrevendo e lendo arquivo JSON

import json

def json_arquivos():
    #Exibindo arquivos
    pasta_atual = os.getcwd()
    print (f"Pasta {pasta_atual}:")

    arquivos_pasta = os.listdir(pasta_atual)
    for n in arquivos_pasta:
        if n.lower().endswith('json'):
            print(f"- {n}")
    
    # Imputação de dados
    entrada = input("Qual arquivo deseja escrever: ")
    arquivo_ler = entrada.lower()

    if not arquivo_ler.lower().endswith('.json'):
        arquivo_ler = arquivo_ler + ".json"

    #Conteúdo do arquivo
    print("DADOS A ADICONAR:\n")
    nome = input("Insira o nome: ")
    idade = input("Insira a idade: ")
    cidade = input("Insira a cidade: ")
    dados = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade
    }


    # Escrevendo no arquivo
    
    if os.path.exists(arquivo_ler) and os.path.getsize(arquivo_ler) > 0:
        with open(arquivo_ler, mode="r", encoding="utf-8") as f:
            arquivo_existente = json.load(f)
        arquivo_existente.update(dados)
        with open(arquivo_ler, mode="w", encoding="utf-8") as f:
            json.dump(arquivo_existente, f, indent=4, ensure_ascii=False)
    else:
        with open(arquivo_ler, mode="w", encoding="utf-8") as novo_arquivo:
            json.dump(dados, novo_arquivo, indent=4, ensure_ascii=False)

    #Imprimindo o arquivo
    
    with open(arquivo_ler, mode="r", encoding="utf-8") as f:
        arquivo_imprimir = json.load(f)
    
    print (f"Conteúdo do arquivo:\n {json.dumps(arquivo_imprimir, indent=4, ensure_ascii=False)}")

#json_arquivos()

