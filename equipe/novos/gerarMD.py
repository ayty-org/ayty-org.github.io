import pandas as pd
import os
from datetime import datetime
import sys

# Verifica se o arquivo CSV foi passado como argumento
if len(sys.argv) < 2:
    print("Por favor, forneça o caminho para o arquivo CSV como argumento.")
    sys.exit(1)

# Caminho do arquivo CSV passado como argumento
file_path = sys.argv[1]

# Ler o arquivo CSV
data = pd.read_csv(file_path)

# Diretório onde os arquivos .md serão salvos (diretório corrente)
output_dir = os.getcwd()

# Função para formatar as datas
def format_date(date_str):
    if pd.isna(date_str):
        return ''
    return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")

# Função para extrair o primeiro e o último nome
def get_first_last_name(full_name):
    names = full_name.split()
    first_name = names[0]
    last_name = names[-1]
    return first_name, last_name

# Função para criar o conteúdo da página .md
def create_markdown(row):
    desde = format_date(row['Data em que iniciou as atividades no AYTY'])
    saiu = format_date(row['Se você já saiu do AYTY, informe a data que saiu'])
    return f"""---
layout: member
name: {row['Nome completo']}
img: {row['Foto do perfil']}
funcao: {row['Escreva a sua função no(s) projetos em que participa']}
projeto: {row['Você está envolvido(a) em que projeto(s)?']}
desde: {desde}
saiu: {saiu}
description: "{row['Descrição']}"
home_page: {row['Home page pessoal (opcional)']}
github: {row['Link do seu github (opcional)']}
linkedin: {row['Link do LinkedIn (obrigatório)']}
instagram: {row['Link do instagram (opcional)']}
twitter: 
importance: 4
category: {row['Marque seu perfil']}
---
"""

# Criar um arquivo .md para cada linha do CSV
for index, row in data.iterrows():
    if pd.isna(row['Nome completo']):
        continue
    
    first_name, last_name = get_first_last_name(row['Nome completo'])
    file_name = f"{first_name}_{last_name}.md".lower()
    file_path = os.path.join(output_dir, file_name)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(create_markdown(row))

print("Páginas .md criadas com sucesso!")