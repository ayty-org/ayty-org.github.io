---
layout: page
title: Declaração de Participação
permalink: /declaracao/
description: Declaração de participação em projeto do AYTY
nav: false
---

<style>
.declaracao {
  max-width: 720px;
  margin: 0 auto;
  font-family: sans-serif;
  font-size: 1.05em;
  line-height: 1.9;
  color: #111;
}
.declaracao h1.titulo-decl {
  text-align: center;
  font-size: 2em;
  letter-spacing: 0.4em;
  margin-top: 6rem;
  margin-bottom: 2.5rem;
  font-weight: bold;
}
.declaracao .data-local {
  text-align: right;
  margin-bottom: 2rem;
}
.declaracao .paragrafo {
  text-align: justify;
  margin-bottom: 1.5rem;
}
table.projetos-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5rem 0;
  font-size: 0.9em;
}
table.projetos-table th {
  background: #f5f5f5;
  font-weight: bold;
}
table.projetos-table th, table.projetos-table td {
  border: 1px solid #bbb;
  padding: 6px 10px;
  text-align: left;
}
.assinatura {
  margin-top: 5rem;
  text-align: center;
}
.nota-validade {
  margin-top: 2rem;
  text-align: center;
  font-size: 0.85em;
  font-style: italic;
  color: #555;
}
.print-header {
  display: none;
}
@media print {
  .no-print { display: none !important; }
  h1.post-title, .post-description, footer, .footer { display: none !important; }
  .print-header { display: block; width: 100%; margin-bottom: 2rem; }
  .print-header img { width: 100%; }
  .declaracao { font-size: 11pt; font-family: sans-serif; }
  .declaracao h1.titulo-decl { font-size: 18pt; }
  .declaracao .data-local { text-align: right; }
}
</style>

<div class="print-header">
  <img src="{{ '/assets/img/topo_declaracao.png' | relative_url }}" alt="AYTY">
</div>

<div class="no-print mb-3">
  <a href="{{ '/declaracoes/' | relative_url }}" class="btn btn-sm btn-secondary">← Voltar à lista</a>
  <button onclick="window.print()" class="btn btn-sm btn-primary ml-2">Imprimir / Salvar PDF</button>
</div>

<div id="declaracao-content" class="declaracao" style="display:none"></div>
<div id="membro-aviso" class="alert alert-warning mt-3" style="display:none"></div>

<script>
const membros = [
  {%- assign estudantes = site.equipe | where_exp: "m", "m.category contains 'Alunos'" -%}
  {%- for m in estudantes %}
  {
    slug: {{ m.slug | jsonify }},
    name: {{ m.name | jsonify }},
    curso: {{ m.curso | default: "" | jsonify }},
    matricula: {{ m.matricula | default: "" | jsonify }},
    projetos: [
      {%- for p in m.projetos %}
      {
        nome: {{ p.nome | jsonify }},
        funcao: {{ p.funcao | default: "" | jsonify }},
        desde: {%- if p.desde %}"{{ p.desde }}"{%- else %}null{%- endif %},
        saiu: {%- if p.saiu %}"{{ p.saiu }}"{%- else %}null{%- endif %},
        ch_semanal: {{ p.ch_semanal | default: 20 }}
      }{%- unless forloop.last %},{%- endunless %}
      {%- endfor %}
    ]
  }{%- unless forloop.last %},{%- endunless %}
  {%- endfor %}
];

const nomeProjetos = {
  {%- for proj in site.projects %}
  {{ proj.projeto | jsonify }}: {{ proj.title | jsonify }}{%- unless forloop.last %},{%- endunless %}
  {%- endfor %}
};

const meses = ['janeiro','fevereiro','março','abril','maio','junho',
               'julho','agosto','setembro','outubro','novembro','dezembro'];

function formatDatePT(dateStr) {
  if (!dateStr) return 'atual';
  const parts = dateStr.toString().split('-');
  if (parts.length < 3) return dateStr;
  return parseInt(parts[2]) + ' de ' + meses[parseInt(parts[1])-1] + ' de ' + parts[0];
}

function nomeCurso(curso) {
  if (curso === 'SI') return 'Sistemas de Informação';
  if (curso === 'LCC') return 'Licenciatura em Ciências da Computação';
  return curso || '';
}

function nomeProj(slug) {
  return nomeProjetos[slug] || slug;
}

function listaTexto(itens) {
  if (itens.length === 0) return '';
  if (itens.length === 1) return itens[0];
  return itens.slice(0, -1).join(', ') + ' e ' + itens[itens.length - 1];
}

function renderDeclaracao(m) {
  const hoje = new Date();
  const dataHoje = 'Rio Tinto, ' + hoje.getDate() + ' de ' + meses[hoje.getMonth()] + ' de ' + hoje.getFullYear() + '.';

  const ativo = m.projetos.some(function(p){ return !p.saiu; });
  const verboPrincipal = ativo ? 'é bolsista' : 'atuou como bolsista';
  const verboAtividade = ativo ? 'atua' : 'atuou';

  const projReferencia = m.projetos.filter(function(p){ return !p.saiu; });
  const projListar = projReferencia.length > 0 ? projReferencia : m.projetos;

  const nomesProj = projListar.map(function(p){ return '"' + nomeProj(p.nome) + '"'; });
  const funcoes = [];
  projListar.forEach(function(p){ if (p.funcao && funcoes.indexOf(p.funcao) === -1) funcoes.push(p.funcao); });

  const matriculaTexto = m.matricula ? ', com matrícula <strong>' + m.matricula + '</strong>,' : '';
  const cursoTexto = m.curso ? ' do curso <strong>' + nomeCurso(m.curso) + '</strong>' : '';

  const linhasTabela = m.projetos.map(function(p){
    return '<tr><td>' + nomeProj(p.nome) + '</td><td>' + (p.funcao || '–') + '</td><td>' + (p.ch_semanal || 20) + 'h/semana</td><td>' + formatDatePT(p.desde) + '</td><td>' + (p.saiu ? formatDatePT(p.saiu) : 'atual') + '</td></tr>';
  }).join('');

  return '<h1 class="titulo-decl">DECLARAÇÃO</h1>'
    + '<p class="data-local">' + dataHoje + '</p>'
    + '<p class="paragrafo">Declaro para os devidos fins, que <strong>' + m.name + '</strong>, aluno(a)' + cursoTexto + matriculaTexto
    + ' <strong>' + verboPrincipal + '</strong> do projeto de pesquisa e desenvolvimento '
    + listaTexto(nomesProj) + ', sob minha orientação. O(A) aluno(a) ' + verboAtividade
    + ' exercendo atividades de <strong>' + listaTexto(funcoes) + '</strong>.</p>'
    + '<table class="projetos-table"><thead><tr><th>Projeto</th><th>Função</th><th>Carga Horária</th><th>Início</th><th>Término</th></tr></thead>'
    + '<tbody>' + linhasTabela + '</tbody></table>'
    + '<div class="assinatura">'
    + 'Prof. Rodrigo Rebouças de Almeida<br>'
    + 'Coordenador e orientador<br>'
    + 'Professor do Departamento de Ciências Exatas<br>'
    + 'SIAPE: 1799618'
    + '</div>'
    + '<p class="nota-validade">Válido apenas se assinado digitalmente pelo professor.</p>';
}

const params = new URLSearchParams(window.location.search);
const slug = params.get('membro');
const aviso = document.getElementById('membro-aviso');
const content = document.getElementById('declaracao-content');

if (slug) {
  const membro = membros.find(function(m){ return m.slug === slug; });
  if (membro) {
    content.innerHTML = renderDeclaracao(membro);
    content.style.display = 'block';
    document.title = 'Declaração – ' + membro.name;
  } else {
    aviso.innerHTML = 'Membro "' + slug + '" não encontrado. <a href="{{ "/declaracoes/" | relative_url }}">Ver lista de alunos</a>.';
    aviso.style.display = 'block';
  }
} else {
  aviso.innerHTML = 'Nenhum aluno selecionado. <a href="{{ "/declaracoes/" | relative_url }}">Ver lista de alunos</a>.';
  aviso.style.display = 'block';
}
</script>
