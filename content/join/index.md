---
title: Join
date: 2026-07-23
type: landing

sections:
  # =====================================================
  # HERO
  # =====================================================
  - block: markdown
    content:
      title: ""
      text: |
        <div class="join-hero">
          <div class="join-hero-image">
            <picture>
              <source srcset="/media/join-layers.webp" type="image/webp">
              <img src="/media/join-layers.jpg" alt="HCMI Lab research environment">
            </picture>
          </div>
          <div class="join-hero-overlay"></div>
          <div class="join-hero-content">
            <div class="join-eyebrow">JOIN US</div>
            <h1>Join the HCMI Lab</h1>
            <p>
              The lab supervises PhD, MASc, MEng and undergraduate students,
              and hosts visiting researchers and postdoctoral fellows.
              Positions depend on funding and supervisory capacity.
            </p>
            <div class="join-hero-cta">
              <a href="#positions" class="join-btn join-btn-primary">
                View Open Positions →
              </a>
              <a href="#apply" class="join-btn join-btn-outline">
                How to Apply
              </a>
            </div>
          </div>
        </div>
    design:
      columns: '1'
      css_class: join-hero-section
  # =====================================================
  # QUICK NAVIGATION
  # =====================================================
  - block: markdown
    content:
      title: ""
      text: |
        <div class="join-container join-quicknav">
          <div class="join-section-label">
            <span>QUICK NAVIGATION</span>
          </div>
          <div class="join-quicknav-grid">
            <a href="#positions" class="join-nav-card">
              <span class="join-nav-icon">
                <i class="fas fa-users"></i>
              </span>
              <span>Open Positions</span>
              <small>→</small>
            </a>
            <a href="#apply" class="join-nav-card">
              <span class="join-nav-icon">
                <i class="far fa-file-alt"></i>
              </span>
              <span>How to Apply</span>
              <small>→</small>
            </a>
            <a href="#funding" class="join-nav-card">
              <span class="join-nav-icon">
                <i class="fas fa-graduation-cap"></i>
              </span>
              <span>Funding</span>
              <small>→</small>
            </a>
            <a href="#resources" class="join-nav-card">
              <span class="join-nav-icon">
                <i class="far fa-book-open"></i>
              </span>
              <span>Resources</span>
              <small>→</small>
            </a>
            <a href="#faq" class="join-nav-card">
              <span class="join-nav-icon">
                <i class="far fa-question-circle"></i>
              </span>
              <span>FAQs</span>
              <small>→</small>
            </a>
            <a href="#contact" class="join-nav-card">
              <span class="join-nav-icon">
                <i class="far fa-envelope"></i>
              </span>
              <span>Contact</span>
              <small>→</small>
            </a>
          </div>
        </div>
    design:
      columns: '1'
      css_class: join-section join-section-nav
  # =====================================================
  # ABOUT + RESEARCH AREAS
  # =====================================================
  - block: markdown
    content:
      title: ""
      text: |
        <div class="join-container">
          <div class="join-about-grid">
            <div class="join-about-text">
              <div class="join-section-label">
                <span>ABOUT</span>
              </div>
              <h2 class="join-h2">About the Lab</h2>
              <p>
                The HCMI Lab at Toronto Metropolitan University studies
                generative search and LLM-based retrieval, fairness and
                adversarial robustness in ranking, and governance on online
                and decentralized platforms.
              </p>
              <p>
                See <a href="/publication/">Publications</a> for current work.
              </p>
            </div>
            <div class="join-about-areas">
              <div class="join-section-label">
                <span>RESEARCH AREAS</span>
              </div>
              <div class="join-pills">
                <span class="join-pill">Generative Search</span>
                <span class="join-pill">LLM-Based Retrieval</span>
                <span class="join-pill">LLM-as-a-Judge</span>
                <span class="join-pill">Fair Ranking</span>
                <span class="join-pill">Adversarial IR</span>
                <span class="join-pill">Query Performance Prediction</span>
                <span class="join-pill">Platform Governance</span>
                <span class="join-pill">Decentralized Systems (DAOs)</span>
              </div>
            </div>
          </div>
        </div>
    design:
      columns: '1'
      css_class: join-section
  # =====================================================
  # OPEN POSITIONS
  # =====================================================
  - block: markdown
    content:
      title: ""
      text: |
        <div class="join-container" id="positions">
          <div class="join-section-label">
            <span>OPEN POSITIONS</span>
          </div>
          <h2 class="join-h2">Open Positions</h2>
          <!-- PHD / MASC -->
          <div id="phd" class="join-position-card">
            <div class="join-position-top">
              <div>
                <h3>PhD &amp; MASc Students</h3>
                <p>
                  Thesis-based graduate students in information retrieval,
                  machine learning or related areas.
                </p>
              </div>
            </div>
            <div class="join-position-grid">
              <div>
                <h4>AREAS</h4>
                <ul>
                  <li>Generative search and LLM-based retrieval</li>
                  <li>LLM-as-a-judge and retrieval evaluation</li>
                  <li>Fair ranking and adversarial robustness</li>
                  <li>Platform governance and DAOs</li>
                </ul>
              </div>
              <div>
                <h4>REQUIREMENTS</h4>
                <ul>
                  <li>Degree in CS, ECE, statistics or a related field (a master's for PhD applicants)</li>
                  <li>Prior research: a thesis, publication or substantial project</li>
                  <li>Proficiency in Python and a deep learning framework</li>
                  <li>Meets TMU graduate English language requirements</li>
                </ul>
              </div>
            </div>
          </div>
          <!-- MENG -->
          <div id="meng" class="join-position-card">
            <div class="join-position-top">
              <div>
                <h3>MEng Students</h3>
                <p>
                  Course-based master's students completing a project
                  with the lab.
                </p>
              </div>
            </div>
            <div class="join-position-grid">
              <div>
                <h4>AREAS</h4>
                <ul>
                  <li>LLM-based retrieval and RAG systems</li>
                  <li>Evaluation pipelines for search and LLMs</li>
                </ul>
              </div>
              <div>
                <h4>REQUIREMENTS</h4>
                <ul>
                  <li>Enrolled in a TMU MEng program</li>
                  <li>Proficiency in Python</li>
                  <li>Coursework in machine learning</li>
                </ul>
              </div>
            </div>
          </div>
          <!-- UNDERGRAD -->
          <div id="undergrad" class="join-position-card">
            <div class="join-position-top">
              <div>
                <h3>Undergraduate Students</h3>
                <p>
                  Research assistant, internship and directed-study positions.
                </p>
              </div>
            </div>
            <div class="join-position-grid">
              <div>
                <h4>REQUIREMENTS</h4>
                <ul>
                  <li>Completed coursework in programming and statistics</li>
                  <li>Proficiency in Python</li>
                </ul>
              </div>
              <div>
                <h4>INCLUDE IN YOUR EMAIL</h4>
                <ul>
                  <li>Transcript</li>
                  <li>Available hours per week</li>
                </ul>
              </div>
            </div>
          </div>
          <!-- VISITING -->
          <div id="visiting" class="join-position-card">
            <div class="join-position-top">
              <div>
                <h3>Visiting Students &amp; Visiting Scholars</h3>
                <p>
                  Researchers from other institutions working on a defined
                  joint project.
                </p>
              </div>
            </div>
            <div class="join-position-grid">
              <div>
                <h4>POSSIBLE ARRANGEMENTS</h4>
                <ul>
                  <li>Research visit (1–6 months)</li>
                  <li>Short-term exchanges</li>
                  <li>Collaborative projects</li>
                </ul>
              </div>
              <div>
                <h4>REQUIREMENTS</h4>
                <ul>
                  <li>A proposed project aligned with the lab's work</li>
                  <li>Funding from the home institution or an external source</li>
                </ul>
              </div>
            </div>
          </div>
          <!-- POSTDOC -->
          <div id="postdoc" class="join-position-card">
            <div class="join-position-top">
              <div>
                <h3>Postdoctoral Fellows</h3>
                <p>
                  PhD holders in information retrieval, machine learning
                  or a related field.
                </p>
              </div>
            </div>
            <div class="join-position-grid">
              <div>
                <h4>REQUIREMENTS</h4>
                <ul>
                  <li>First-author publications at relevant venues (e.g. SIGIR, CIKM, ECIR, ICWSM)</li>
                  <li>A research statement</li>
                </ul>
              </div>
              <div>
                <h4>AREAS</h4>
                <ul>
                  <li>Generative search and LLM evaluation</li>
                  <li>Fair and robust neural ranking</li>
                  <li>Platform governance and decentralized systems</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
    design:
      columns: '1'
      css_class: join-section join-section-alt
  # =====================================================
  # HOW TO APPLY
  # =====================================================
  - block: markdown
    content:
      title: ""
      text: |
        <div class="join-container" id="apply">
          <div class="join-section-label">
            <span>HOW TO APPLY</span>
          </div>
          <h2 class="join-h2">How to Apply</h2>
          <div class="join-steps">
            <div class="join-step">
              <span class="join-step-num">1</span>
              <div class="join-step-content">
                <span class="join-step-index">01</span>
                <h3>Prepare Your Documents</h3>
                <p>
                  A CV and a short statement of research interest.
                </p>
              </div>
            </div>
            <div class="join-step">
              <span class="join-step-num">2</span>
              <div class="join-step-content">
                <span class="join-step-index">02</span>
                <h3>Read Recent Publications</h3>
                <p>
                  Your email should refer to specific work from the lab.
                </p>
              </div>
            </div>
            <div class="join-step">
              <span class="join-step-num">3</span>
              <div class="join-step-content">
                <span class="join-step-index">03</span>
                <h3>Use This Email Subject</h3>
                <div class="join-code">
                  Prospective (PhD/MASc) Student | Your Name | Research Interest
                </div>
                <p class="join-example">
                  Example:
                  Prospective PhD Student | Jane Smith |
                  Fairness in Large Language Models
                </p>
              </div>
            </div>
            <div class="join-step">
              <span class="join-step-num">4</span>
              <div class="join-step-content">
                <span class="join-step-index">04</span>
                <h3>Email Contents</h3>
                <div class="join-apply-columns">
                  <ul>
                    <li>Degree program and intended start term</li>
                    <li>Research interests, with reference to lab publications</li>
                    <li>Prior research: thesis, papers or code</li>
                    <li>CV attached</li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="join-step">
              <span class="join-step-num">5</span>
              <div class="join-step-content">
                <span class="join-step-index">05</span>
                <h3>Selection &amp; Interview</h3>
                <p>
                  Shortlisted candidates are contacted for an interview,
                  online or in person.
                </p>
              </div>
            </div>
            <div class="join-step">
              <span class="join-step-num">6</span>
              <div class="join-step-content">
                <span class="join-step-index">06</span>
                <h3>Submit Your Formal Application</h3>
                <p>
                  If invited, apply through TMU Graduate Admissions.
                </p>
              </div>
            </div>
          </div>
          <div class="join-lookfor">
            <div class="join-lookfor-icon">
              <i class="far fa-lightbulb"></i>
            </div>
            <div>
              <h3>What I Look For</h3>
              <p>
                Evidence of independent technical work: a thesis, paper
                or substantial code repository.
              </p>
            </div>
          </div>
        </div>
    design:
      columns: '1'
      css_class: join-section
  # =====================================================
  # FUNDING
  # =====================================================
  - block: markdown
    content:
      title: ""
      text: |
        <div class="join-container" id="funding">
          <div class="join-section-label">
            <span>FUNDING OPPORTUNITIES</span>
          </div>
          <h2 class="join-h2">Funding Opportunities</h2>
          <div class="join-funding-grid">
            <div class="join-funding-card">
              <h3>CANADIAN STUDENTS</h3>
              <ul>
                <li>NSERC Graduate Scholarships</li>
                <li>TMU Graduate Awards</li>
                <li>Ontario Graduate Scholarship (OGS)</li>
              </ul>
            </div>
            <div class="join-funding-card">
              <h3>INTERNATIONAL STUDENTS</h3>
              <ul>
                <li>Vanier Canada Graduate Scholarship</li>
                <li>TMU International Entrance Scholarship</li>
                <li>Mitacs Globalink</li>
                <li>Other external funding opportunities</li>
              </ul>
            </div>
          </div>
        </div>
    design:
      columns: '1'
      css_class: join-section join-section-alt
  # =====================================================
  # RESOURCES
  # =====================================================
  - block: markdown
    content:
      title: ""
      text: |
        <div class="join-container" id="resources">
          <div class="join-section-label">
            <span>USEFUL RESOURCES</span>
          </div>
          <div class="join-resource-links">
            <a href="https://www.torontomu.ca/graduate/">Graduate Studies →</a>
            <a href="/publication/">Publications →</a>
            <a href="https://www.torontomu.ca/graduate/">
              Funding Guide →
            </a>
            <a href="#apply">
              Application Tips →
            </a>
            <a href="#faq">
              FAQ →
            </a>
            <a href="#contact">
              Contact →
            </a>
          </div>
          <div id="faq" class="join-faq">
            <h3>Frequently Asked Questions</h3>
            <details>
              <summary>Do I need previous research experience?</summary>
              <p>
                Required for PhD and postdoctoral applicants. Not required
                for undergraduate positions.
              </p>
            </details>
            <details>
              <summary>Should I contact the lab before applying?</summary>
              <p>
                Yes. Graduate applicants should contact the lab before
                submitting a formal application.
              </p>
            </details>
          </div>
        </div>
    design:
      columns: '1'
      css_class: join-section
  # =====================================================
  # FINAL CTA
  # =====================================================
  - block: markdown
    content:
      title: ""
      text: |
        <div class="join-cta-section" id="contact">
          <div class="join-cta">
            <h2>Read Before You Reach Out</h2>
            <p>
              Emails that do not follow the subject format above may not
              receive a reply.
            </p>
            <div class="join-hero-cta">
              <a
                href="#positions"
                class="join-btn join-btn-primary">
                View Open Positions →
              </a>
              <a
                href="mailto:mzihayat@torontomu.ca?subject=Prospective%20Student%20%7C%20Your%20Name%20%7C%20Research%20Interest"
                class="join-btn join-btn-outline">
                Contact Me →
              </a>
            </div>
          </div>
        </div>
    design:
      columns: '1'
      css_class: join-section

---