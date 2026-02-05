---
# Leave the homepage title empty to use the site title
title:
date: 2025-09-03
type: landing


sections:

  # - block: markdown
  #   content:
  #     text: ""
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['10px', '0', '20px', '0']
  #     css_class: fullscreen

  # - block: markdown
  #   content:
  #     title: Human-Centered Machine Intelligence Lab
  #   design:
  #     columns: '1'
  #     spacing:
  #       padding: ['60px', '0', '20px', '0']
  #     css_class: text-center

  # Section 1: Identity and Mission
  - block: markdown
    content:
      title: ""
      text: |
        <div class="home-identity-container">
          <div class="home-identity-text">
            <h1>HCMI<br>Lab</h1>
            <p>The Human-Centered Machine Intelligence Lab is a research lab focused on advancing AI and machine learning systems that are fair, transparent, and aligned with human values.</p>
          </div>
          <div class="home-identity-image">
            <img src="media/hero-image.jpg" alt="HCMI Lab" class="hero-image">
          </div>
        </div>
    design:
      columns: '1'
      background:
        color: '#FFFFFF'
      spacing:
        padding: ['100px', '0', '100px', '0']
      css_class: home-section-identity

  # Section 2: Latest News
  - block: markdown
    content:
      title: "Latest News"
      text: |
        <div class="news-puzzle-container">
          <div class="news-card news-card-small">
            <h3>Accepted in WSDM 2026</h3>
            <p>Our paper on "Self-Paced Fair Ranking with Loss as a Proxy for Bias" by Hai Son Le, Shirin Seyedsalehi, Morteza Zihayat, and Ebrahim Bagheri has been accepted at WSDM 2026.</p>
            <div class="read-more-sec">
              <a href="/publication/self-paced-fair-ranking-loss-proxy-bias/" class="arrow">Read More</a>
            </div>
          </div>
          <div class="news-card news-card-large">
            <h3>Accepted in ECIR 2026</h3>
            <p>Our paper on "Refairmulate: A Benchmark Dataset for Gender-Fair Query Reformulations" by Hai Son Le, Shirin Seyedsalehi, Morteza Zihayat, and Ebrahim Bagheri has been accepted at ECIR 2026 (Top-tier conference in Information Retrieval).</p>
            <div class="read-more-sec">
              <a href="/publication/refairmulate-benchmark-dataset-gender-fair-query-reformulations/" class="arrow">Read More</a>
            </div>
          </div>
          <div class="news-card news-card-small">
            <h3>Accepted in ECIR 2026</h3>
            <p>Our paper on "When Attention Becomes Exposure in Generative Search" by Shayan Alipour, Mehdi Kargar, and Morteza Zihayat has been accepted at ECIR 2026 (Top-tier conference in Information Retrieval).</p>
            <div class="read-more-sec">
              <a href="/publication/when-attention-becomes-exposure-generative-search/" class="arrow">Read More</a>
            </div>
          </div>
          <div class="news-card news-card-small">
            <h3>Accepted in WWW 2026</h3>
            <p>Our paper on "Decentralized in Name Only: The Centralization of DAO Labor" by Lingling Zhang, Morteza Zihayat, and Ebrahim Bagheri has been accepted at WWW 2026.</p>
            <div class="read-more-sec">
              <a href="/publication/decentralized-in-name-only-centralization-dao-labor/" class="arrow">Read More</a>
            </div>
          </div>
          <div class="news-card news-card-large">
            <h3>Accepted in WWW 2026</h3>
            <p>Our paper on "Graph Poisoning for Node Rank Manipulation" by Seyed Mohammad Hosseini, Radin Hamidi Rad, Morteza Zihayat, and Ebrahim Bagheri has been accepted at WWW 2026, investigating graph poisoning attacks designed to manipulate node rankings.</p>
            <div class="read-more-sec">
              <a href="/publication/graph-poisoning-node-rank-manipulation/" class="arrow">Read More</a>
            </div>
          </div>
          <div class="news-card news-card-small">
            <h3>Accepted in CIKM 2025</h3>
            <p>Our paper on "LLM-as-a-Judge in Entity Retrieval: Assessing Explicit and Implicit Relevance" by Mohammad Hossein Saliminabi, Negar Arabzadeh, Seyed Mohammad Hosseini, Dimitrios Androutsos, Morteza Zihayat, and Ebrahim Bagheri has been accepted at CIKM 2025.</p>
            <div class="read-more-sec">
              <a href="/publication/llm-as-a-judge-entity-retrieval/" class="arrow">Read More</a>
            </div>
          </div>
          <div class="news-card news-card-small">
            <h3>Accepted in CIKM 2025</h3>
            <p>Our paper on "Datasets for Supervised Adversarial Attacks on Neural Rankers" by Amir Khosrojerdi, Amin Bigdeli, Radin Hamidi Rad, Morteza Zihayat, Charles LA Clarke, and Ebrahim Bagheri has been accepted at CIKM 2025.</p>
            <div class="read-more-sec">
              <a href="/publication/datasets-supervised-adversarial-attacks-neural-rankers/" class="arrow">Read More</a>
            </div>
          </div>
          <div class="news-card news-card-small">
            <h3>New Paper: The Gray Area</h3>
            <p>Our recent paper on "The Gray Area: Characterizing Moderator Disagreement on Reddit" by Shayan Alipour, Shruti Phadke, Seyed Shahabeddin Mousavi, Amirhossein Afsharrad, Morteza Zihayat, and Mattia Samory has been published on arXiv.</p>
            <div class="read-more-sec">
              <a href="/publication/gray-area-characterizing-moderator-disagreement-reddit/" class="arrow">Read More</a>
            </div>
          </div>
        </div>
    design:
      columns: '1'
      background:
        color: '#FFFFFF'
      spacing:
        padding: ['100px', '0', '100px', '0']
      css_class: home-section-news

  # Section 3: Research Collaborators
  - block: markdown
    content:
      title: "Our past and current Research Collaborators"
      subtitle: "Our past and current collaborators"
      text: |
        <div class="row">
          <div class="col-6 col-lg-3 text-center mb-4">
            <img src="media/ibm-logo.jpg" alt="IBM" class="img-fluid" style="max-height: 80px;">
          </div>
          <div class="col-6 col-lg-3 text-center mb-4">
            <img src="media/nserc-logo.jpg" alt="NSERC" class="img-fluid" style="max-height: 80px;">
          </div>
          <div class="col-6 col-lg-3 text-center mb-4">
            <img src="media/mitacs-logo.jpg" alt="MITACS" class="img-fluid" style="max-height: 80px;">
          </div>
          <div class="col-6 col-lg-3 text-center mb-4">
            <img src="media/att.jpg" alt="AT&T" class="img-fluid" style="max-height: 80px;">
          </div>
          <div class="col-6 col-lg-3 text-center mb-4">
            <img src="media/university-waterloo-logo.jpg" alt="University of Waterloo" class="img-fluid" style="max-height: 80px;">
          </div>
          <div class="col-6 col-lg-3 text-center mb-4">
            <img src="media/university-toronto-logo.jpg" alt="University of Toronto" class="img-fluid" style="max-height: 80px;">
          </div>
          <div class="col-6 col-lg-3 text-center mb-4">
            <img src="/media/globe-mail-logo.jpg" alt="Globe and Mail" class="img-fluid" style="max-height: 80px;">
          </div>
        </div>
    design:
      columns: '1'
      background:
        color: '#FFFFFF'
      spacing:
        padding: ['80px', '0', '80px', '0']
      css_class: home-section-collaborators

  - block: markdown
    content:
      text: ""
    design:
      columns: '1'
---