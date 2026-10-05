---
# Leave the homepage title empty to use the site title
title:
date: 2025-09-03
type: landing

sections:

  - block: markdown
    content:
      title: ""
      text: |
        <div class="home-hero-inner">
          <div class="home-hero-copy">
            <p class="home-kicker">HCMI Lab <span>/</span> Toronto Metropolitan University</p>
            <h1>Human-Centered<br>Machine Intelligence</h1>
            <p class="home-hero-lead">The HCMI Lab at Toronto Metropolitan University studies generative search, the evaluation and robustness of neural ranking and LLM-based retrieval, and governance on online and decentralized platforms.</p>
            <div class="home-hero-actions">
              <a class="home-btn home-btn-primary" href="/publication/">Our Research</a>
              <a class="home-btn home-btn-ghost" href="/join/">Join Us</a>
            </div>
          </div>
          <div class="home-hero-visual">
            <img src="/media/hero-image.png" alt="A hand touching a glowing node in a human-centered network">
            <span class="home-hero-watermark">
                <span>SCROLL</span>
               <span class="scroll-line"></span>
            </span>
          </div>
        </div>
    design:
      columns: '1'
      background:
        color: '#FFFFFF'
      spacing:
        padding: ['0', '0', '0', '0']
      css_class: home-hero

  - block: home-news
    content:
      title: ""
    design:
      columns: '1'
      background:
        color: '#FFFFFF'
      spacing:
        padding: ['0', '0', '0', '0']
      css_class: home-news

  - block: markdown
    content:
      title: ""
      text: |
        <div class="home-focus-inner" id="home-focus">
          <div class="home-focus-copy">
            <p class="home-eyebrow">Research</p>
            <h2>Focus areas</h2>
            <p>Generative search and LLM-based retrieval; LLM-as-a-judge evaluation; fair and bias-aware ranking; adversarial robustness of neural rankers; query performance prediction; platform governance and decentralized autonomous organizations.</p>
            <a class="home-btn home-btn-ghost home-btn-dark" href="/publication/">Learn more <span aria-hidden="true">→</span></a>
          </div>
          <div class="home-focus-board" aria-hidden="true">
            <svg class="home-focus-lines" viewBox="0 0 560 420" preserveAspectRatio="none">
              <line x1="300" y1="110" x2="170" y2="250"></line>
              <line x1="330" y1="120" x2="430" y2="270"></line>
            </svg>
            <div class="home-note home-note-values">
              <h3>Generative<br>Search</h3>
              <p>retrieval<br>generation<br>exposure</p>
            </div>
            <div class="home-note home-note-impact">
              <h3>Online<br>Platforms</h3>
              <p>moderation<br>governance<br>DAOs</p>
            </div>
            <div class="home-note home-note-intel">
              <h3>Trustworthy<br>Ranking</h3>
              <p>fairness<br>robustness<br>evaluation</p>
            </div>
          </div>
        </div>
    design:
      columns: '1'
      background:
        color: '#F7F8FA'
      spacing:
        padding: ['0', '0', '0', '0']
      css_class: home-focus

  - block: home-linkedin
    content:
      title: ""
    design:
      columns: '1'
      background:
        color: '#FFFFFF'
      spacing:
        padding: ['0', '0', '0', '0']
      css_class: home-posts

  - block: markdown
    content:
      title: ""
      text: |
        <div class="home-wrap" id="home-collaborators">
          <h2>Collaborators</h2>
          <p class="home-collaborators-sub">Industry, academic, and funding partners, past and present.</p>
          <div class="home-logo-row">
            <img src="media/ibm-logo.jpg" alt="IBM">
            <img src="media/nserc-logo.jpg" alt="NSERC">
            <img src="media/mitacs-logo.jpg" alt="Mitacs">
            <img src="media/att.jpg" alt="AT&amp;T">
            <img src="media/university-waterloo-logo.jpg" alt="University of Waterloo">
            <img src="media/university-toronto-logo.jpg" alt="University of Toronto">
            <img src="/media/globe-mail-logo.jpg" alt="The Globe and Mail">
          </div>
        </div>
    design:
      columns: '1'
      background:
        color: '#FFFFFF'
      spacing:
        padding: ['0', '0', '0', '0']
      css_class: home-collaborators
---
