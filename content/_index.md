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

  - block: markdown
    content:
      title: ""
      text: |
        <div class="home-wrap" id="home-news">
          <div class="home-section-head">
            <div>
              <p class="home-eyebrow">Latest News</p>
              <h2>News &amp; Updates</h2>
            </div>
            <a class="home-text-link" href="/post/">View all news <span aria-hidden="true">→</span></a>
          </div>

          <a class="home-news-featured" href="/join/">
            <img class="home-news-featured-bg" src="/media/we-are-hiring.png" alt="">
            <div class="home-news-featured-copy">
              <span class="home-pill">We're hiring</span>
              <h3>Join the HCMI Lab</h3>
              <p>We are actively recruiting motivated PhD, MASc, MEng, undergraduate, visiting, and postdoctoral researchers passionate about trustworthy, responsible, and human-centered AI. Explore openings, research areas, and how to apply.</p>
              <span class="home-text-link">See Openings &amp; How to Apply</span>
            </div>
          </a>

          <div class="home-news-grid">
            <article class="home-news-card">
              <div class="home-news-meta"><span>Publication</span><time>Sep 12, 2025</time></div>
              <h3><a href="/publication/failing-forward-query-failure-retrieval-judgment-generation/">LLM-Based Query Expansion for Fair Information Retrieval</a></h3>
              <p>Our paper on the effectiveness of LLM-based query expansion for fair and inclusive information retrieval has been accepted at SIGIR 2026.</p>
              <a class="home-card-arrow" href="/publication/failing-forward-query-failure-retrieval-judgment-generation/" aria-label="Read more">→</a>
            </article>
            <article class="home-news-card">
              <div class="home-news-meta"><span>Event</span><time>Sep 05, 2025</time></div>
              <h3><a href="/event/">HCMI at NeurIPS 2025</a></h3>
              <p>We will present our latest work on human-centered evaluation of generative systems at NeurIPS 2025 in San Diego.</p>
              <a class="home-card-arrow" href="/event/" aria-label="Read more">→</a>
            </article>
            <article class="home-news-card">
              <div class="home-news-meta"><span>Publication</span><time>Aug 21, 2025</time></div>
              <h3><a href="/publication/regularization-framework-gender-bias-mitigation-dense-neural-rankers/">Towards Trustworthy AI in Real-World Applications</a></h3>
              <p>A new study on mitigating bias in systems of collaboration has been accepted at CIKM 2025.</p>
              <a class="home-card-arrow" href="/publication/regularization-framework-gender-bias-mitigation-dense-neural-rankers/" aria-label="Read more">→</a>
            </article>
            <article class="home-news-card">
              <div class="home-news-meta"><span>Research</span><time>Aug 12, 2025</time></div>
              <h3><a href="/publication/">New Project: Human-AI Collaboration in Decision Making</a></h3>
              <p>We are launching a new research project exploring how humans and AI can better collaborate in high-stakes decision making.</p>
              <a class="home-card-arrow" href="/publication/" aria-label="Read more">→</a>
            </article>
            <article class="home-news-card">
              <div class="home-news-meta"><span>Event</span><time>Jul 30, 2025</time></div>
              <h3><a href="/event/">Workshop on Human-Centered ML at TMU</a></h3>
              <p>We hosted a workshop on human-centered machine learning with researchers from across Canada.</p>
              <a class="home-card-arrow" href="/event/" aria-label="Read more">→</a>
            </article>
            <article class="home-news-card">
              <div class="home-news-meta"><span>News</span><time>Jul 15, 2025</time></div>
              <h3><a href="/people/">HCMI Lab Welcomes New Graduate Students</a></h3>
              <p>We are excited to welcome new MSc and PhD students to the lab for the 2025–2026 academic year.</p>
              <a class="home-card-arrow" href="/people/" aria-label="Read more">→</a>
            </article>
          </div>

          <div class="home-center">
            <a class="home-btn home-btn-outline" href="/post/">Show more</a>
          </div>
        </div>
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
              <h3>Machine Intelligence</h3>
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

  - block: markdown
    content:
      title: ""
      text: |
        <div class="home-wrap" id="home-posts">
          <div class="home-section-head">
            <h2>Latest Posts</h2>
            <a class="home-text-link" href="https://ca.linkedin.com/in/morteza-zihayat" target="_blank" rel="noopener">View on LinkedIn <span aria-hidden="true">→</span></a>
          </div>
          <div class="home-posts-grid">
            <article class="home-post-card">
              <div class="home-post-media home-post-media-a"></div>
              <div class="home-post-body">
                <p class="home-post-brand">in HCMI Lab</p>
                <h3>We're hiring! Join the HCMI Lab</h3>
                <p>We are looking for motivated PhD, MASc, MEng and postdoctoral researchers to join our team. If you're passionate about...</p>
              </div>
            </article>
            <article class="home-post-card">
              <div class="home-post-media home-post-media-b"></div>
              <div class="home-post-body">
                <p class="home-post-brand">in HCMI Lab</p>
                <h3>Our paper on LLM-based Query Expansion for Fair Information Retrieval...</h3>
                <p>Excited to share that our paper has been accepted at SIGIR 2026. This work explores how LLMs can support fairer...</p>
              </div>
            </article>
            <article class="home-post-card">
              <div class="home-post-media home-post-media-c"></div>
              <div class="home-post-body">
                <p class="home-post-brand">in HCMI Lab</p>
                <h3>Reflections from CHI 2026</h3>
                <p>Our team had a great experience at CHI 2026 in Yokohama. It was inspiring to see so much progress in human-centered AI research.</p>
              </div>
            </article>
            <article class="home-post-card">
              <div class="home-post-media home-post-media-d"></div>
              <div class="home-post-body">
                <p class="home-post-brand">in HCMI Lab</p>
                <h3>Welcome to our new graduate students!</h3>
                <p>We're excited to welcome our new MSc and PhD students to the lab. Looking forward to an amazing year ahead.</p>
              </div>
            </article>
          </div>
        </div>
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
