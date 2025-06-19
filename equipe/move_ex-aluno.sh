#!/bin/bash

DEST_DIR="$1"

if [[ -z "$DEST_DIR" ]]; then
  echo "Uso: $0 <diretório-destino>"
  exit 1
fi

mkdir -p "$DEST_DIR"

for file in *.md; do
  # Extrai o frontmatter entre os dois primeiros ---
  frontmatter=$(awk '/^---$/ {count++} count==1 {print} count==2 {exit}' "$file")

  # Verifica se category é Ex-alunos (ignora espaços extras)
  is_ex_aluno=$(echo "$frontmatter" | grep -iE '^category:\s*Ex-alunos')

  # Verifica se saiu tem valor não vazio, ignorando comentários e espaços
  saiu_valor=$(echo "$frontmatter" | awk -F ':' '/^saiu:/ {
    val = $2;
    sub(/#.*/, "", val); gsub(/[[:space:]]/, "", val);
    if (length(val) > 0) print val
  }')

  if [[ -n "$is_ex_aluno" || -n "$saiu_valor" ]]; then
    echo "Movendo: $file"
    mv "$file" "$DEST_DIR/"
  fi
done