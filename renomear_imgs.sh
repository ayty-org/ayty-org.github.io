#!/bin/bash

# Caminho da pasta onde estão os arquivos Markdown
folder_path="/Users/rodrigor/git/AYTY/ayty-org.github.io/_equipe/"

# Caminho fixo das imagens (baseado no campo img do frontmatter)
image_base_path="/Users/rodrigor/git/AYTY/ayty-org.github.io/_equipe/img"

# Função para normalizar nomes de arquivos (remover acentos e ajustar para lowercase)
normalize_filename() {
  local filename="$1"
  # Remove acentos e substitui ç por c, ajusta para lowercase
  echo "$filename" | iconv -f utf8 -t ascii//TRANSLIT | sed 's/[^a-zA-Z0-9._-]//g' | tr '[:upper:]' '[:lower:]'
}

# Função para processar cada arquivo Markdown
process_markdown_file() {
  local md_file="$1"
  
  # Nome base do arquivo Markdown (sem extensão)
  local md_basename=$(basename "$md_file" .md)
  local normalized_md_basename=$(normalize_filename "$md_basename")
  
  # Caminho normalizado do arquivo Markdown
  local normalized_md_file="${folder_path}/${normalized_md_basename}.md"
  
  # Renomeia o arquivo Markdown se necessário
  if [[ "$md_file" != "$normalized_md_file" ]]; then
    mv "$md_file" "$normalized_md_file"
    md_file="$normalized_md_file"
    echo "Renomeado: $md_basename.md -> $normalized_md_basename.md"
  fi
  
  # Lê o conteúdo do arquivo e extrai o valor de "img"
  local img_path=$(grep '^img:' "$md_file" | sed 's/^img:[ ]*//')
  
  # Verifica se o campo "img" foi encontrado
  if [[ -n "$img_path" ]]; then
    # Ajusta o caminho real da imagem no sistema de arquivos
    local img_filename=$(basename "$img_path")
    local img_full_path="${image_base_path}/${img_filename}"
    local normalized_img_name="${normalized_md_basename}.jpg"
    local normalized_img_path="${image_base_path}/${normalized_img_name}"
    local new_img_ref="equipe/img/$normalized_img_name"
    
    # Tenta localizar a imagem no sistema de arquivos
    if [[ -f "$img_full_path" ]]; then
      # Renomeia a imagem para o nome normalizado
      mv "$img_full_path" "$normalized_img_path"
      
      # Atualiza o arquivo Markdown com o novo caminho da imagem
      sed -i '' "s|^img:.*|img: $new_img_ref|" "$md_file"
      
      echo "Atualizado: $normalized_md_file -> img: $new_img_ref"
    else
      echo "Imagem não encontrada para $md_file: $img_full_path"
    fi
  else
    echo "Campo 'img' não encontrado em: $md_file"
  fi
}

# Itera sobre os arquivos Markdown na pasta especificada
for md_file in "$folder_path"/*.md; do
  [[ -f "$md_file" ]] && process_markdown_file "$md_file"
done