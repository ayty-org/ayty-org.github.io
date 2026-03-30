---
layout: page
title: Equipe
permalink: /equipe/
description: Conheça os alunos, professores e colaboradores que fazem parte dos projetos do AYTY.
nav: true
nav_order: 4
display_categories: [Professores, Colaboradores externos, Alunos]
horizontal: false
---

<!-- pages/equipe.md -->
<div class="equipe">
{%- if site.enable_project_categories and page.display_categories %}

  <!-- Contador de membros ativos -->
  {%- assign total_alunos = 0 %}
  {%- assign total_professores = 0 %}
  {%- assign total_colaboradores = 0 %}
  {%- for member in site.equipe %}
    {%- assign has_active = false %}
    {%- for p in member.projetos %}
      {%- unless p.saiu %}{%- assign has_active = true %}{%- endunless %}
    {%- endfor %}
    {%- if has_active %}
      {%- if member.category contains "Alunos" %}
        {%- assign total_alunos = total_alunos | plus: 1 %}
      {%- elsif member.category contains "Professores" %}
        {%- assign total_professores = total_professores | plus: 1 %}
      {%- elsif member.category contains "Colaboradores" %}
        {%- assign total_colaboradores = total_colaboradores | plus: 1 %}
      {%- endif %}
    {%- endif %}
  {%- endfor %}
  <div class="projetos-contador">
    <span><i class="fas fa-user-graduate"></i> {{ total_alunos }} alunos ativos</span>
    <span><i class="fas fa-chalkboard-teacher"></i> {{ total_professores }} professores</span>
    {%- if total_colaboradores > 0 %}
    <span><i class="fas fa-handshake"></i> {{ total_colaboradores }} colaboradores</span>
    {%- endif %}
  </div>

  <!-- Display categorized team (only members with at least one active project) -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_equipe = site.equipe | where: "category", category -%}
  {%- assign sorted_equipe = categorized_equipe | sort: "name" | sort: "importance" %}
  <div class="grid">
    {%- for member in sorted_equipe -%}
      {%- assign has_active = false -%}
      {%- for p in member.projetos -%}
        {%- unless p.saiu -%}{%- assign has_active = true -%}{%- endunless -%}
      {%- endfor -%}
      {%- if has_active or member.category contains "Colaboradores externos" -%}
        {% include equipe.html %}
      {%- endif -%}
    {%- endfor %}
  </div>
  {%- endfor %}

{%- else -%}
<!-- Display members without categories (only members with at least one active project) -->
  {%- assign sorted_members = site.equipe | sort: "name"  | sort: "importance" -%}
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-4">
    {%- for member in sorted_members -%}
      {%- assign has_active = false -%}
      {%- for p in member.projetos -%}
        {%- unless p.saiu -%}{%- assign has_active = true -%}{%- endunless -%}
      {%- endfor -%}
      {%- if has_active -%}
        {% include equipe_horizontal.html %}
      {%- endif -%}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for member in sorted_members -%}
      {%- assign has_active = false -%}
      {%- for p in member.projetos -%}
        {%- unless p.saiu -%}{%- assign has_active = true -%}{%- endunless -%}
      {%- endfor -%}
      {%- if has_active -%}
        {% include equipe.html %}
      {%- endif -%}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}

<h2 class="category">Antigos integrantes da equipe</h2>
<div class="grid grid-encerrados">
  {%- assign equipe_sorted = site.equipe | sort: "name"  | sort: "importance" -%}
  {%- for member in equipe_sorted -%}
    {%- assign has_active = false -%}
    {%- for p in member.projetos -%}
      {%- unless p.saiu -%}{%- assign has_active = true -%}{%- endunless -%}
    {%- endfor -%}
    {%- unless has_active or member.category contains "Colaboradores externos" -%}
      {% include equipe.html %}
    {%- endunless -%}
  {%- endfor %}
</div>

</div>
