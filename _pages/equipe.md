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
      {%- if member.projeto.size > 0 -%}
        {% include equipe.html %}
      {%- endif -%}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display members without categories (only members with at least one active project) -->
  {%- assign sorted_members = site.equipe | sort: "name"  | sort: "importance" -%}
  <!-- Generate cards for each member -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-4">
    {%- for member in sorted_members -%}
      {%- if member.projeto.size > 0 -%}
        {% include equipe_horizontal.html %}
      {%- endif -%}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for member in sorted_members -%}
      {%- if member.projeto.size > 0 -%}
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
    {%- if member.projeto.size == 0 -%}
      {% include equipe.html %}
    {%- endif -%}
  {%- endfor %}
</div>


</div>
