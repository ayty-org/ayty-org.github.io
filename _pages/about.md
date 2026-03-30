---
layout: about
title: Home
permalink: /
subtitle: Laboratório de Engenharia de Software Aplicada

editais: true  # includes a list of news items
latest_posts: true  # includes a list of the newest posts
social: true  # includes social icons at the bottom of the page
---

O AYTY é um laboratório vinculado ao Departamento de Ciências Exatas do Campus IV da Universidade Federal da Paraíba (UFPB), situado em Rio Tinto-PB. Fundado em 2011, atuamos na integração entre universidade e setor produtivo por meio de projetos de cooperação, pesquisa aplicada e extensão. [Conheça nossa equipe](/equipe) e os [projetos que desenvolvemos](/projetos/).

<!-- Métricas -->
<div class="row ayty-stats">
  <div class="col-6 col-md-3"><div class="ayty-stat-box">
    <div class="ayty-stat-number">300+</div>
    <div class="ayty-stat-label">alunos formados</div>
  </div></div>
  <div class="col-6 col-md-3"><div class="ayty-stat-box">
    <div class="ayty-stat-number">20+</div>
    <div class="ayty-stat-label">projetos executados</div>
  </div></div>
  <div class="col-6 col-md-3"><div class="ayty-stat-box">
    <div class="ayty-stat-number">8</div>
    <div class="ayty-stat-label">projetos em andamento</div>
  </div></div>
  <div class="col-6 col-md-3"><div class="ayty-stat-box">
    <div class="ayty-stat-number">1</div>
    <div class="ayty-stat-label">startup spinoff criada</div>
  </div></div>
</div>

**Nossa missão** é desenvolver soluções por meio de pesquisa aplicada alinhada à realidade das empresas e capacitar pessoas a partir da vivência em projetos reais.

**Nossos valores:**
<div class="ayty-valores">
  <span class="ayty-valor"><i class="fas fa-users"></i> Colaboração</span>
  <span class="ayty-valor"><i class="fas fa-heart"></i> Humildade</span>
  <span class="ayty-valor"><i class="fas fa-comments"></i> Comunicação clara</span>
  <span class="ayty-valor"><i class="fas fa-bullseye"></i> Comprometimento</span>
  <span class="ayty-valor"><i class="fas fa-lightbulb"></i> Proatividade</span>
  <span class="ayty-valor"><i class="fas fa-shield-alt"></i> Responsabilidade</span>
</div>

<div class="ayty-filosofia">
  Nosso interesse são projetos de longo prazo. Relacionamento de longo prazo só se constrói com confiança, diálogo e geração de valor mútuo — e interesse genuíno em fazer dar certo. Essa é a nossa filosofia.
</div>

<div class="ayty-cta">
  <a href="/portfolio" class="ayty-btn-cta">
    <i class="fas fa-briefcase"></i> Veja nosso portfolio
  </a>
</div>

<!-- Notícias -->

<h3>Últimas notícias:</h3>
<div class="noticias-grid" id="noticias-ghost"></div>

<script>
  function formatarData(pubDate) {
    const data = new Date(pubDate);
    return data.toLocaleDateString('pt-BR', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
    });
  }

  fetch("https://api.rss2json.com/v1/api.json?rss_url=https://news.ayty.org/rss/")
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById("noticias-ghost");
      container.innerHTML = "";

      data.items.slice(0, 4).forEach(post => {
        const card = document.createElement("div");
        card.className = "noticia-card";

        const dataFormatada = formatarData(post.pubDate);
        const thumb = post.thumbnail || (post.enclosure && post.enclosure.link) || '';

        card.innerHTML = (thumb ? `<img src="${thumb}" alt="" class="noticia-thumb">` : '')
          + `<div class="noticia-card-body">
               <small>${dataFormatada}</small>
               <a href="${post.link}" target="_blank" rel="noopener">${post.title}</a>
             </div>`;

        container.appendChild(card);
      });
    })
    .catch(error => {
      console.error("Erro ao carregar o feed:", error);
    });
</script>
<i>(<a href="https://news.ayty.org" target="new">Leia mais em https://news.ayty.org ...</a>)</i>
<br/>
