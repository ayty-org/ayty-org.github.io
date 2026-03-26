#!/usr/bin/env python3
"""
Migration script: converts old projeto/ex-projeto/funcao/desde/saiu fields
into a new `projetos` list per member.
"""
import os
import re
import yaml
from pathlib import Path

BASE = Path('/home/user/ayty-org.github.io/_equipe')

# -------------------------------------------------------------------
# Special cases: per-file override for projetos structure
# Key: relative path from BASE
# -------------------------------------------------------------------
SPECIAL = {
    'vivamoveis/pedro_cunha.md': [
        {'nome': 'phoebus',    'ativo': False, 'desde': '2022-07-01', 'saiu': '2023-06-30', 'funcao': 'desenvolvedor full stack', 'ch_semanal': 20},
        {'nome': 'vivamoveis', 'ativo': False, 'desde': '2022-07-01', 'saiu': '2025-09-30', 'funcao': 'UX/UI e testes',          'ch_semanal': 20},
    ],
    'triade/laisa-maria-dos-santos.md': [
        {'nome': 'triade', 'ativo': False, 'desde': '2025-08-01', 'saiu': '2026-01-31', 'funcao': 'bolsista analista de negocios', 'ch_semanal': 20},
    ],
    'phoebus/erick_fernandes.md': [
        {'nome': 'phoebus', 'ativo': False, 'desde': '2023-04-06', 'saiu': '2026-02-28', 'funcao': 'bolsista devops', 'ch_semanal': 20},
    ],
    'administrativo/amanda-cavalcante-rodrigues.md': [
        {'nome': 'cabemais',  'ativo': False, 'desde': '2025-08-01', 'saiu': '2026-02-28', 'funcao': 'suporte administrativo'},
        {'nome': 'phoebus',   'ativo': False, 'desde': '2025-08-01', 'saiu': '2026-02-28', 'funcao': 'suporte administrativo'},
        {'nome': 'portomar',  'ativo': False, 'desde': '2025-08-01', 'saiu': '2026-02-28', 'funcao': 'suporte administrativo'},
        {'nome': 'vivamoveis','ativo': False, 'desde': '2025-08-01', 'saiu': '2026-02-28', 'funcao': 'suporte administrativo'},
        {'nome': 'triade',    'ativo': False, 'desde': '2025-08-01', 'saiu': '2026-02-28', 'funcao': 'suporte administrativo'},
    ],
    'codata/julio_verne.md': [
        {'nome': 'codata',       'ativo': False, 'desde': '2023-08-01', 'saiu': '2025-07-31', 'funcao': 'bolsista dev', 'ch_semanal': 20},
        {'nome': 'apps4society', 'ativo': False, 'desde': '2023-04-01', 'saiu': '2025-07-31', 'funcao': 'bolsista dev', 'ch_semanal': 20},
        {'nome': 'universi.me',  'ativo': False, 'desde': '2023-04-01', 'saiu': '2025-07-31', 'funcao': 'bolsista dev', 'ch_semanal': 20},
    ],
    'codata/mauricio_rodrigues.md': [
        {'nome': 'codata',   'ativo': False, 'desde': '2023-08-01', 'saiu': '2025-07-31', 'funcao': 'bolsista analista de dados', 'ch_semanal': 20},
        {'nome': 'cabemais', 'ativo': False, 'desde': '2023-08-01', 'saiu': '2026-01-31', 'funcao': 'bolsista analista de dados', 'ch_semanal': 20},
    ],
    'old/phoebus/nathan.md': [
        {'nome': 'esig',    'ativo': False, 'desde': '2022-04-01', 'saiu': '2024-06-30', 'funcao': 'bolsista dev', 'ch_semanal': 20},
        {'nome': 'phoebus', 'ativo': False, 'desde': '2024-07-01', 'saiu': '2025-06-30', 'funcao': 'bolsista dev', 'ch_semanal': 20},
    ],
    'old/phoebus/raul_lins.md': [
        {'nome': 'codata',  'ativo': False, 'desde': '2023-08-01', 'saiu': '2024-06-30', 'funcao': 'bolsista analista de requisitos', 'ch_semanal': 20},
        {'nome': 'phoebus', 'ativo': False, 'desde': '2024-07-01', 'saiu': '2025-05-31', 'funcao': 'bolsista analista de testes',    'ch_semanal': 20},
    ],
    'old/phoebus/ronellyson_julio.md': [
        {'nome': 'phoebus', 'ativo': False, 'desde': '2023-04-02', 'saiu': '2024-05-30', 'funcao': 'desenvolvedor Android', 'ch_semanal': 20},
    ],
    'phoebus/ricardo_verissimo.md': [
        {'nome': 'codata',  'ativo': False, 'desde': '2023-07-28', 'saiu': '2025-03-31', 'funcao': 'bolsista analista de testes', 'ch_semanal': 20},
        {'nome': 'phoebus', 'ativo': True,  'desde': '2023-07-28', 'saiu': '',           'funcao': 'bolsista dev',                'ch_semanal': 20},
    ],
    'professores/tacito.md': None,  # handled below via patch
}

# Tácito: active in cabemais + ideal; ex in codata, vivamoveis, universi.me, triade (triade ended 31/01/2026)
TACITO_PROJETOS = [
    {'nome': 'cabemais',    'ativo': True,  'desde': '2023-11-01', 'saiu': '',           'funcao': 'pesquisador'},
    {'nome': 'ideal',       'ativo': True,  'desde': '2023-11-01', 'saiu': '',           'funcao': 'pesquisador'},
    {'nome': 'codata',      'ativo': False, 'desde': '2023-11-01', 'saiu': '',           'funcao': 'pesquisador'},
    {'nome': 'vivamoveis',  'ativo': False, 'desde': '2023-11-01', 'saiu': '',           'funcao': 'pesquisador'},
    {'nome': 'universi.me', 'ativo': False, 'desde': '2023-11-01', 'saiu': '',           'funcao': 'pesquisador'},
    {'nome': 'triade',      'ativo': False, 'desde': '2023-11-01', 'saiu': '2026-01-31', 'funcao': 'pesquisador'},
]
SPECIAL['professores/tacito.md'] = TACITO_PROJETOS


# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def parse_frontmatter(content):
    """Return (fm_dict, fm_raw_text, body). fm_raw_text excludes --- markers."""
    if not content.startswith('---'):
        return None, None, content
    end = content.find('\n---', 3)
    if end == -1:
        return None, None, content
    fm_text = content[4:end]          # skip opening '---\n'
    body = content[end + 4:]          # skip closing '\n---'
    try:
        fm = yaml.safe_load(fm_text)
    except Exception as e:
        print(f"  YAML error: {e}")
        return None, fm_text, body
    return fm, fm_text, body


def clean_value(v):
    """Remove inline YAML comment and strip whitespace."""
    if v is None:
        return ''
    s = re.sub(r'\s*#.*$', '', str(v)).strip()
    return s


def to_list(value):
    """Normalize projeto / ex-projeto field to a Python list of strings."""
    if value is None:
        return []
    if isinstance(value, list):
        return [clean_value(x) for x in value if x is not None and clean_value(x)]
    s = clean_value(str(value))
    if not s:
        return []
    # Handle YAML inline array that wasn't parsed as list
    if s.startswith('[') and s.endswith(']'):
        inner = s[1:-1]
        return [x.strip() for x in inner.split(',') if x.strip()]
    return [x.strip() for x in s.split(',') if x.strip()]


def is_student(category):
    if not category:
        return False
    return 'aluno' in str(category).lower()


def format_date(d):
    """Convert date value to YYYY-MM-DD string or empty."""
    if d is None:
        return ''
    import datetime
    if isinstance(d, (datetime.date, datetime.datetime)):
        return d.strftime('%Y-%m-%d')
    s = clean_value(str(d))
    # Convert DD/MM/YYYY to YYYY-MM-DD
    m = re.match(r'^(\d{2})/(\d{2})/(\d{4})$', s)
    if m:
        return f'{m.group(3)}-{m.group(2)}-{m.group(1)}'
    return s


def build_projetos_yaml(projetos_list):
    """Build the YAML block for the projetos field."""
    if not projetos_list:
        return 'projetos: []'
    lines = ['projetos:']
    for p in projetos_list:
        ativo = p.get('ativo', True)
        lines.append(f"  - nome: {p.get('nome', '')}")
        lines.append(f"    ativo: {'true' if ativo else 'false'}")
        lines.append(f"    desde: {p.get('desde', '')}")
        saiu = p.get('saiu', '')
        lines.append(f"    saiu: {saiu if saiu else ''}")
        lines.append(f"    funcao: {p.get('funcao', '')}")
        if 'ch_semanal' in p:
            lines.append(f"    ch_semanal: {p['ch_semanal']}")
    return '\n'.join(lines)


FIELDS_TO_REMOVE = {'projeto', 'ex-projeto', 'desde', 'saiu', 'funcao'}


def remove_old_fields(fm_text):
    """Remove lines corresponding to old fields."""
    new_lines = []
    for line in fm_text.split('\n'):
        field = re.match(r'^([a-zA-Z_-]+):', line)
        if field and field.group(1) in FIELDS_TO_REMOVE:
            continue
        new_lines.append(line)
    return '\n'.join(new_lines)


def insert_projetos(fm_text, projetos_yaml):
    """Insert projetos block before 'importance:' or at the end."""
    if 'importance:' in fm_text:
        return re.sub(r'(^importance:)', projetos_yaml + '\n\\1', fm_text, flags=re.MULTILINE)
    return fm_text.rstrip() + '\n' + projetos_yaml + '\n'


def build_generic_projetos(fm):
    """Build projetos from old fields for the generic (non-special) case."""
    category = str(fm.get('category', ''))
    student = is_student(category)
    ch = 20 if student else None

    raw_funcao = fm.get('funcao', '')
    funcao = clean_value(str(raw_funcao) if raw_funcao else '')
    if not funcao:
        funcao = 'bolsista dev' if student else 'pesquisador'

    desde = format_date(fm.get('desde'))
    saiu  = format_date(fm.get('saiu'))

    active = to_list(fm.get('projeto'))
    ex     = to_list(fm.get('ex-projeto'))

    # Filter out placeholder values
    active = [p for p in active if not p.startswith('{')]
    ex     = [p for p in ex     if not p.startswith('{')]

    projetos = []
    for nome in active:
        e = {'nome': nome, 'ativo': True, 'desde': desde, 'saiu': '', 'funcao': funcao}
        if ch:
            e['ch_semanal'] = ch
        projetos.append(e)
    for nome in ex:
        e = {'nome': nome, 'ativo': False, 'desde': desde, 'saiu': saiu, 'funcao': funcao}
        if ch:
            e['ch_semanal'] = ch
        projetos.append(e)
    return projetos


# -------------------------------------------------------------------
# Main migration
# -------------------------------------------------------------------
def migrate(filepath):
    rel = str(filepath.relative_to(BASE))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, fm_text, body = parse_frontmatter(content)
    if fm is None:
        print(f'  SKIP (no frontmatter): {rel}')
        return

    if 'projetos' in (fm or {}):
        print(f'  SKIP (already migrated): {rel}')
        return

    # Determine projetos list
    if rel in SPECIAL:
        projetos = SPECIAL[rel]
    else:
        projetos = build_generic_projetos(fm)

    projetos_yaml = build_projetos_yaml(projetos)
    new_fm = remove_old_fields(fm_text)
    new_fm = insert_projetos(new_fm, projetos_yaml)

    new_content = '---\n' + new_fm + '\n---' + body
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'  OK: {rel}')


files = sorted(BASE.rglob('*.md'))
for f in files:
    if f.name == 'phoebus_bolsista.md':
        continue
    migrate(f)

print('\nDone.')
