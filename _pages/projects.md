---
layout: page
title: Projetos
permalink: /projetos/
description: Atuamos em parceria com empresas, órgãos públicos e iniciativas de pesquisa e extensão. Conheça nossos projetos.
nav: true
nav_order: 3
display_categories: [Empresas, Pesquisa, Extensão, Encerrados]
horizontal: false
---

<!-- pages/projects.md -->
{%- assign ativos = site.projects | where_exp: "p", "p.category != 'Encerrados'" %}
{%- assign encerrados = site.projects | where: "category", "Encerrados" %}
<div class="projetos-contador">
  <span><i class="fas fa-circle" style="color: #28a745;"></i> {{ ativos.size }} projetos ativos</span>
  <span><i class="fas fa-circle" style="color: #aaa;"></i> {{ encerrados.size }} encerrados</span>
</div>

<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_projects = site.projects | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid{% if category == 'Encerrados' %} grid-encerrados{% endif %}">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
  {%- assign sorted_projects = site.projects | sort: "importance" -%}
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>
