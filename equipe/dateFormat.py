import os
import re
from datetime import datetime

def convert_date(match):
    date_str = match.group(0)
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    return date_obj.strftime('%Y-%m-%d')

# Substituir datas nos arquivos
def process_file(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        file_data = file.read()

    # Procure por datas no formato dd/MM/yyyy
    date_pattern = re.compile(r'\b(\d{2}/\d{2}/\d{4})\b')

    # Substituir todas as datas pelo novo formato
    new_file_data = date_pattern.sub(convert_date, file_data)

    # Escreva os novos dados de volta no arquivo
    with open(file_path, 'w', encoding='utf8') as file:
        file.write(new_file_data)

# Caminho para o diretório com os arquivos .md
directory_path = '.'

# Iterar sobre todos os arquivos no diretório
for filename in os.listdir(directory_path):
    if filename.endswith('.md'):
        process_file(os.path.join(directory_path, filename))
