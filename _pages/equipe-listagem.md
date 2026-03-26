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
            {%- assign all_equipe = site.equipe | sort: "name" | sort: "importance" -%}
            {%- for member in all_equipe -%}
              {%- for p in member.projetos -%}
                {%- if p.nome == project_name and p.ativo -%}
                <tr>
                    <td>✅</td>
                    <td><a href="{{ member.img }}" target="_blank"><img src="{{ member.img }}" alt="{{ member.name }}" style="width:40px;height:40px;"></a></td>
                    <td>{{ member.name }}</td>
                    <td><a href="{{ member.home_page }}" target="_blank">Website</a></td>
                    <td><a href="{{ member.lattes }}" target="_blank">Lattes</a></td>
                    <td>{{ p.desde }}</td>
                    <td>{{ p.saiu }}</td>
                    <td><a href="{{ member.github }}" target="_blank">Github</a></td>
                    <td><a href="{{ member.linkedin }}" target="_blank">LinkedIn</a></td>
                    <td><a href="{{ member.instagram }}" target="_blank">Instagram</a></td>
                    <td><a href="{{ member.twitter }}" target="_blank">Twitter</a></td>
                    <td>{{ member.category }}</td>
                    <td>{{ p.funcao }}</td>
                </tr>
                {%- endif -%}
              {%- endfor -%}
            {%- endfor -%}
            {%- for member in all_equipe -%}
              {%- for p in member.projetos -%}
                {%- if p.nome == project_name and p.ativo == false -%}
                <tr>
                    <td>❌</td>
                    <td><a href="{{ member.img }}" target="_blank"><img src="{{ member.img }}" alt="{{ member.name }}" style="width:40px;height:40px;"></a></td>
                    <td>{{ member.name }}</td>
                    <td><a href="{{ member.home_page }}" target="_blank">Website</a></td>
                    <td><a href="{{ member.lattes }}" target="_blank">Lattes</a></td>
                    <td>{{ p.desde }}</td>
                    <td>{{ p.saiu }}</td>
                    <td><a href="{{ member.github }}" target="_blank">Github</a></td>
                    <td><a href="{{ member.linkedin }}" target="_blank">LinkedIn</a></td>
                    <td><a href="{{ member.instagram }}" target="_blank">Instagram</a></td>
                    <td><a href="{{ member.twitter }}" target="_blank">Twitter</a></td>
                    <td>{{ member.category }}</td>
                    <td>{{ p.funcao }}</td>
                </tr>
                {%- endif -%}
              {%- endfor -%}
            {%- endfor -%}
        </tbody>
    </table>
    {% endfor %}
</div>
