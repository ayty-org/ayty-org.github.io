---
layout: page
title: Equipe
permalink: /equipe/
description: Nossa equipe
nav: true
nav_order: 2
display_categories: [Professores, Colaboradores externos, Alunos]
horizontal: false
---

<!-- pages/equipe.md -->
<div class="equipe">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized team -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_equipe = site.equipe | where: "category", category -%}
  {%- assign sorted_equipe = categorized_equipe | sort: "importance" %}
  <!-- Generate cards for each member -->
  <!-- {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for member in sorted_equipe -%}
      {% include equipe_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%} -->
  <div class="grid">
    {%- for member in sorted_equipe -%}
      {% include equipe.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display members without categories -->
  {%- assign sorted_members = site.equipe | sort: "importance" -%}
  <!-- Generate cards for each member -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-4">
    {%- for member in sorted_members -%}
      {% include equipe_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for member in sorted_members -%}
      {% include equipe.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
<h2 class="category">Antigos integrantes da equipe</h2>
<div class="grid">
  {%- assign ex_alunos = site.equipe_old | sort: "importance" -%}
  {%- for member in ex_alunos -%}
    {% include equipe.html %}
  {%- endfor %}
</div>


</div>
