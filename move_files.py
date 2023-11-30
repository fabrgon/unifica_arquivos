import os
import shutil

# Função para mover arquivos de múltiplas fontes para uma pasta de destino
def copy_files_from_multiple_sources(source_folders, destination_folder, file_extension):
    for source_folder in source_folders:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith(file_extension):
                    file_path = os.path.join(root, file)
                    shutil.copy(file_path, destination_folder)

# Exemplo de uso
source_folders = ['/Users/fabrgon/Desktop/teste/Bases/Bases/Base1', '/Users/fabrgon/Desktop/teste/Bases/Bases/Base2', '/Users/fabrgon/Desktop/teste/Bases/Bases/Base3']  # Lista de pastas de origem
destination_folder = '/Users/fabrgon/Desktop/teste/Bases/Bases/Consolidada'
file_extension = '.csv'  # Substitua pela extensão desejada

# Chamada da função
copy_files_from_multiple_sources(source_folders, destination_folder, file_extension)
copy_files_from_multiple_sources(source_folders, destination_folder, file_extension)

import pandas as pd
import os

# Função para combinar múltiplos arquivos CSV em um único arquivo CSV
def combine_csv_files(source_folder, output_file):
    # Lista para armazenar os dataframes
    dfs = []

    # Percorre todos os arquivos no diretório
    for filename in os.listdir(source_folder):
        if filename.endswith('.csv'):
            filepath = os.path.join(source_folder, filename)
            df = pd.read_csv(filepath, index_col=None, header=None)
            dfs.append(df)

    # Combina todos os dataframes em um único dataframe
    combined_df = pd.concat(dfs, axis=0, ignore_index=True)

    # Salva o dataframe combinado em um novo arquivo CSV
    combined_df.to_csv(output_file, index=False)

# Exemplo de uso
source_folder = '/Users/fabrgon/Desktop/teste/Bases/Bases/Consolidada'
output_file = '/Users/fabrgon/Desktop/teste/Bases/Bases/Consolidada2/Consolidada2.csv'

combine_csv_files(source_folder, output_file)
# Passo 1: Ler os Arquivos CSV
for filename in os.listdir(source_folder):
    if filename.endswith('.csv'):
        filepath = os.path.join(source_folder, filename)
        df = pd.read_csv(filepath, index_col=None, header=0)
        print(f"Conteúdo do arquivo {filename}:")
        print(df.head())  # Imprime as primeiras linhas do dataframe
        dfs = []  # Define the dfs variable as an empty list

# Passo 2: Ler os Arquivos CSV
# Lendo o arquivo Consolidada2.csv
df_consolidada = pd.read_csv('/Users/fabrgon/Desktop/teste/Bases/Bases/Consolidada2/Consolidada2.csv')

# Lendo o OutroArquivo.csv
df_outro = pd.read_csv('/Users/fabrgon/Desktop/teste/Bases/Bases/Consolidada2/Consolidada3.csv')

#Passo 3: Realizar a Operação de Merge (PROCV)
# Supondo que 'coluna_comum' é a coluna que você deseja usar para o PROCV
df_merged = pd.merge(df_consolidada, df_outro, on='0', how='left')

#Passo 4: Salvar o Resultado (Opcional)
df_merged.to_csv('/Users/fabrgon/Desktop/teste/Bases/Bases/Consolidada2/Consolidada4.csv', index=False)
