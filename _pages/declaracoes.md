---
layout: page
title: Declarações de Participação
permalink: /declaracoes/
description: Declarações de participação dos alunos nos projetos do AYTY
nav: false
---

{% assign alunos_ativos = "" | split: "" %}
{% assign ex_alunos = "" | split: "" %}
{% assign todos_membros = site.equipe | sort: "name" %}
{% for member in todos_membros %}
  {%- assign cat = member.category | downcase | strip -%}
  {%- if cat contains "aluno" -%}
    {%- assign has_active = false -%}
    {%- for p in member.projetos -%}
      {%- unless p.saiu -%}{%- assign has_active = true -%}{%- endunless -%}
    {%- endfor -%}
    {%- if has_active -%}
      {%- assign alunos_ativos = alunos_ativos | push: member -%}
    {%- else -%}
      {%- assign ex_alunos = ex_alunos | push: member -%}
    {%- endif -%}
  {%- endif -%}
{% endfor %}

<h2>Alunos ativos</h2>
<ul>
{% for member in alunos_ativos %}
<li><a href="{{ '/declaracao/' | relative_url }}?membro={{ member.slug }}">{{ member.name }}</a></li>
{% endfor %}
</ul>

<h2>Ex-alunos</h2>
<ul>
{% for member in ex_alunos %}
<li><a href="{{ '/declaracao/' | relative_url }}?membro={{ member.slug }}">{{ member.name }}</a></li>
{% endfor %}
</ul>
