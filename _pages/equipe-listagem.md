---
layout: page
title: Listagem da Equipe
permalink: /listaequipe
description: Nossa equipe
nav: false
projects: [phoebus,codata,vivamoveis,cabemais,portomar,universi.me,ideal,esig,snet,engenharia.software,tracy-td,dobot]
---

<div class="container">
        {% for project_name in page.projects %}
        <h2>{{ site.data.projeto_nome[project_name] }}</h2>
        <table>
            <thead>
                <tr>
                    <th>Ativo?</th>
                    <th>Image</th>
                    <th>Name</th>
                    <th>Website</th>
                    <th>Lattes</th>
                    <th>Joined On</th>
                    <th>Left On</th>
                    <th>Github</th>
                    <th>LinkedIn</th>
                    <th>Instagram</th>
                    <th>Twitter</th>
                    <th>Category</th>
                    <th>Function</th>
                </tr>
            </thead>
            <tbody>
                {% assign filtered_equipe = site.equipe | where: "projeto", project_name  | sort: "name"  | sort: 'importance'  %}
                {% for member in filtered_equipe %}
                    <tr>
                        <td>✅</td>
                        <td><a href="{{ member.img }}" target="_blank"><img src="{{ member.img }}" alt="{{ member.name }}" style="width:40px;height:40px;"></a></td>
                        <td>{{ member.name }}</td>
                        <td><a href="{{ member.home_page }}" target="_blank">Website</a></td>
                        <td><a href="{{ member.lattes }}" target="_blank">Lattes</a></td>
                        <td>{{ member.desde }}</td>
                        <td>{{ member.saiu }}</td>
                        <td><a href="{{ member.github }}" target="_blank">Github</a></td>
                        <td><a href="{{ member.linkedin }}" target="_blank">LinkedIn</a></td>
                        <td><a href="{{ member.instagram }}" target="_blank">Instagram</a></td>
                        <td><a href="{{ member.twitter }}" target="_blank">Twitter</a></td>
                        <td>{{ member.category }}</td>
                        <td>{{ member.funcao }}</td>
                    </tr>
                {% endfor %}
                 {% assign filtered_equipe = site.equipe_old | where: "ex-projeto", project_name | sort: "name" | sort: 'importance'  %}
                {% for member in filtered_equipe %}
                    <tr>
                        <td>❌</td>
                        <td><a href="{{ member.img }}" target="_blank"><img src="{{ member.img }}" alt="{{ member.name }}" style="width:40px;height:40px;"></a></td>
                        <td>{{ member.name }}</td>
                        <td><a href="{{ member.home_page }}" target="_blank">Website</a></td>
                        <td><a href="{{ member.lattes }}" target="_blank">Lattes</a></td>
                        <td>{{ member.desde }}</td>
                        <td>{{ member.saiu }}</td>
                        <td><a href="{{ member.github }}" target="_blank">Github</a></td>
                        <td><a href="{{ member.linkedin }}" target="_blank">LinkedIn</a></td>
                        <td><a href="{{ member.instagram }}" target="_blank">Instagram</a></td>
                        <td><a href="{{ member.twitter }}" target="_blank">Twitter</a></td>
                        <td>{{ member.category }}</td>
                        <td>{{ member.funcao }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% endfor %}
    <!-- Seção de ex-integrantes por projeto -->
{%- assign ex_alunos = site.equipe_old | where: "ex-projeto", page.projeto | sort: "name" | sort: "importance" -%}

{% if ex_alunos.size > 0 %}
  <h2 class="category">Ex-integrantes</h2>
  <div class="grid">
    {% for member in ex_alunos %}
      {% include equipe.html %}
    {% endfor %}
  </div>
{% endif %}
</div>
