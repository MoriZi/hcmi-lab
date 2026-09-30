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
            <p class="home-hero-lead">The HCMI Lab at Toronto Metropolitan University explores how to build intelligent systems that work for people.</p>
            <div class="home-hero-actions">
              <a class="home-btn home-btn-primary" href="/publication/">Our Research</a>
              <a class="home-btn home-btn-ghost" href="#home-focus">Learn More</a>
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
            <p class="home-eyebrow">Our Focus</p>
            <h2>Building AI that understands and supports human life.</h2>
            <p>We bring together computer science, psychology, design, and the humanities to create intelligent systems that are fair, transparent, and aligned with human values.</p>
            <a class="home-btn home-btn-ghost home-btn-dark" href="/publication/">Learn more <span aria-hidden="true">→</span></a>
          </div>
          <div class="home-focus-board" aria-hidden="true">
            <svg class="home-focus-lines" viewBox="0 0 560 420" preserveAspectRatio="none">
              <line x1="300" y1="110" x2="170" y2="250"></line>
              <line x1="330" y1="120" x2="430" y2="270"></line>
            </svg>
            <div class="home-note home-note-values">
              <h3>Human Values</h3>
              <p>fairness<br>transparency<br>trust</p>
            </div>
            <div class="home-note home-note-impact">
              <h3>Real-World Impact</h3>
              <p>well-being<br>opportunity</p>
            </div>
            <div class="home-note home-note-intel">
              <h3>Machine<br>Intelligence</h3>
              <p>learning<br>reasoning<br>adaptation</p>
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
          <h2>Our past and current Research Collaborators</h2>
          <p class="home-collaborators-sub">Our past and current collaborators</p>
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
