---
layout: page
title: Equipe
permalink: /equipe/
description: Nossa equipe
nav: true
nav_order: 4
display_categories: [Professores, Colaboradores externos, Alunos]
horizontal: false
---

<!-- pages/equipe.md -->
<div class="equipe">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized team (only members with at least one active project) -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_equipe = site.equipe | where: "category", category -%}
  {%- assign sorted_equipe = categorized_equipe | sort: "name" | sort: "importance" %}
  <div class="grid">
    {%- for member in sorted_equipe -%}
      {%- assign has_active = false -%}
      {%- for p in member.projetos -%}
        {%- if p.ativo -%}{%- assign has_active = true -%}{%- endif -%}
      {%- endfor -%}
      {%- if has_active -%}
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
        {%- if p.ativo -%}{%- assign has_active = true -%}{%- endif -%}
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
        {%- if p.ativo -%}{%- assign has_active = true -%}{%- endif -%}
      {%- endfor -%}
      {%- if has_active -%}
        {% include equipe.html %}
      {%- endif -%}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}

<h2 class="category">Antigos integrantes da equipe</h2>
<div class="grid">
  {%- assign equipe_sorted = site.equipe | sort: "name"  | sort: "importance" -%}
  {%- for member in equipe_sorted -%}
    {%- assign has_active = false -%}
    {%- for p in member.projetos -%}
      {%- if p.ativo -%}{%- assign has_active = true -%}{%- endif -%}
    {%- endfor -%}
    {%- unless has_active -%}
      {% include equipe.html %}
    {%- endunless -%}
  {%- endfor %}
</div>


</div>
