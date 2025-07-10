---
layout: about
title: Home
permalink: /
subtitle: Laboratório de Engenharia de Software Aplicada

editais: true  # includes a list of news items
latest_posts: true  # includes a list of the newest posts
social: true  # includes social icons at the bottom of the page
---

O AYTY é um laboratório vinculado ao Departamento de Ciências Exatas do Campus IV da Universidade Federal da Paraíba (UFPB), situado em Rio Tinto-PB. Fundado em 2011, o AYTY tem como missão fortalecer a integração entre a universidade e o setor produtivo por meio de projetos de cooperação, pesquisa aplicada e atividades de extensão. O laboratório conta com a participação de professores pesquisadores da UFPB e de outras instituições, atuando de forma colaborativa em iniciativas que geram impacto acadêmico, tecnológico e social. [Conheça nossa equipe](/equipe) e os [projetos que desenvolvemos](/projetos/).

**Nossa missão** é desenvolver soluções por meio de pesquisa aplicada alinhada à realidade das empresas e capacitar pessoas a partir da vivência em projetos reais.

**Nossos valores:** No AYTY, acreditamos que o crescimento profissional acontece em equipe, com respeito, humildade e colaboração. Valorizamos relações humanas saudáveis, comunicação clara e apoio mútuo, cultivando responsabilidade, comprometimento, pensamento de dono e atitude proativa. Com profissionalismo, resiliência e dedicação, formamos pessoas que se importam com seu próprio desenvolvimento e com o dos outros.

[Sobre nossa caneca.](/caneca)


<b>Acesse nosso [portfolio](/portfolio) para saber como nós podemos ajudar a sua empresa ou organização.</b>


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

  function gerarResumo(htmlContent) {
    const div = document.createElement("div");
    div.innerHTML = htmlContent;
    const texto = div.innerText.trim();
    return texto.length > 140 ? texto.substring(0, 140).trim() + "…" : texto;
  }

  fetch("https://api.rss2json.com/v1/api.json?rss_url=https://news.ayty.org/rss/")
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById("noticias-ghost");
      container.innerHTML = "";

      data.items.slice(0, 5).forEach(post => {
        const card = document.createElement("div");
        card.className = "noticia-card";

        const dataFormatada = formatarData(post.pubDate);
        const resumo = gerarResumo(post.content);

        card.innerHTML = `
          <small>${dataFormatada}</small>
          <a href="${post.link}" target="_blank" rel="noopener">${post.title}</a>
        `;

        container.appendChild(card);
      });
    })
    .catch(error => {
      console.error("Erro ao carregar o feed:", error);
    });
</script>
<br/>