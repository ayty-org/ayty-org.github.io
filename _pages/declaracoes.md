---
layout: page
title: Declarações de Participação
permalink: /declaracoes/
description: Declarações de participação dos alunos nos projetos do AYTY
nav: false
---

{% assign todos_alunos = site.equipe | where: "category", "Alunos" | sort: "name" %}
{% assign todos_ex = site.equipe | where: "category", "Ex-alunos" | sort: "name" %}

<h2>Alunos ativos</h2>
<ul>
{% for member in todos_alunos %}
  {%- assign has_active = false -%}
  {%- for p in member.projetos -%}
    {%- unless p.saiu -%}{%- assign has_active = true -%}{%- endunless -%}
  {%- endfor -%}
  {%- if has_active -%}
  <li><a href="{{ '/declaracao/' | relative_url }}?membro={{ member.slug }}">{{ member.name }}</a></li>
  {%- endif -%}
{% endfor %}
</ul>

<h2>Ex-alunos</h2>
<ul>
{% for member in todos_ex %}
<li><a href="{{ '/declaracao/' | relative_url }}?membro={{ member.slug }}">{{ member.name }}</a></li>
{% endfor %}
</ul>
