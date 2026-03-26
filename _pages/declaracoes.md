---
layout: page
title: Declarações de Participação
permalink: /declaracoes/
description: Declarações de participação dos alunos nos projetos do AYTY
nav: false
---

{% assign estudantes_ativos = site.equipe | where: "category", "Alunos" | sort: "name" %}
{% assign estudantes_ex = site.equipe | where: "category", "Ex-alunos" | sort: "name" %}

<h2>Alunos ativos</h2>
<ul>
{% for member in estudantes_ativos %}
<li><a href="{{ '/declaracao/' | relative_url }}?membro={{ member.slug }}">{{ member.name }}</a></li>
{% endfor %}
</ul>

<h2>Ex-alunos</h2>
<ul>
{% for member in estudantes_ex %}
<li><a href="{{ '/declaracao/' | relative_url }}?membro={{ member.slug }}">{{ member.name }}</a></li>
{% endfor %}
</ul>
