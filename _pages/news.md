---
layout: page
title: Notícias
permalink: /news/
description: 
nav: false
nav_order: 2
---

<h2>Últimas notícias:</h2>
<ul id="noticias-ghost"></ul>

<script>
  fetch("https://api.rss2json.com/v1/api.json?rss_url=https://news.ayty.org/rss/")
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById("noticias-ghost");
      data.items.slice(0, 5).forEach(post => {
        const li = document.createElement("li");
        li.innerHTML = `<a href="${post.link}" target="_blank">${post.title}</a>`;
        container.appendChild(li);
      });
    })
    .catch(error => {
      console.error("Erro ao carregar o feed:", error);
    });
</script>