---
title: People
date: 2022-10-24

type: landing

sections:
  - block: markdown
    content:
      text: |
        <span class="people-kicker">HCMI Lab</span>
        <h1>People</h1>
        <p>Faculty, researchers, students and alumni.</p>
    design:
      css_class: "people-hero"

  - block: markdown
    content:
      text: |
        <div class="people-section-header">
          <div class="people-section-label-group">
            <span class="people-section-label">01 Faculties</span>
          </div>
        </div>
    design:
      css_class: "people-section-pi-header"

  - block: people
    id: principal-investigator
    content:
      user_groups:
          - Principal Investigator
      sort_by: Params.weight
      sort_ascending: true
    design:
      show_interests: true
      show_role: true
      show_social: true
      css_class: "people-section-pi"

  - block: people
    id: faculty
    content:
      user_groups:
          - Faculty
      sort_by: Params.weight
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true
      css_class: "people-section-faculty"

  - block: markdown
    content:
      text: |
        <div class="people-section-header">
          <div class="people-section-label-group">
            <span class="people-section-label">02 Researchers</span>
          </div>
        </div>
    design:
      css_class: "people-section-researchers-header"

  - block: people
    id: researchers
    content:
      user_groups:
          - Researchers
      sort_by: Params.weight
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true
      css_class: "people-section-researchers"

  - block: markdown
    content:
      text: |
        <div class="people-section-header people-alumni-header">
          <div class="people-section-label-group">
            <span class="people-section-label">03 Alumni</span>
          </div>
        </div>
        <div class="people-alumni-grid">
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/r-etamadi.jpg" data-profile-src="/images/alumni/r-etamadi.jpg" alt=""><div><h3>R. Etemadi</h3><p class="people-alumni-degree">Postdoc</p><p>Team Formation in Community Question Answering</p><span>2018 – 2022</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/p-pouladzadeh.png" data-profile-src="/images/alumni/p-pouladzadeh.jpg" alt=""><div><h3>P. Pouladzadeh</h3><p class="people-alumni-degree">Postdoc</p><p>A Sequential Model to Predict Frequency Variations over a Clock Network</p><span>2018 – 2019</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/s-seyedsalehi.jpg" data-profile-src="/images/alumni/s-seyedsalehi.jpg" alt=""><div><h3>S. Seyedsalehi</h3><p class="people-alumni-degree">PhD</p><p>Bias in Neural Embedding Techniques</p><span>2020 – 2025</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/y-li.jpg" data-profile-src="/images/alumni/y-li.jpg" alt=""><div><h3>Y. Li</h3><p class="people-alumni-degree">PhD</p><p>Explaining Homophily in Conspiracy Theories</p><span>2021 – 2025</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/h-s-le.jpg" data-profile-src="/images/alumni/h-s-le.jpg" alt=""><div><h3>H. S. Le</h3><p class="people-alumni-degree">MSc</p><p>Machine Learning and Data Science</p><span>– 2026</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/s-salamati.jpg" data-profile-src="/images/alumni/s-salamati.jpg" alt=""><div><h3>S. Salamat</h3><p class="people-alumni-degree">MSc</p><p>Convincingness in Information Retrieval</p><span>2022 – 2024</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/a-jowhar.jpg" data-profile-src="/images/alumni/a-jowhar.jpg" alt=""><div><h3>A. Jowhar</h3><p class="people-alumni-degree">MSc</p><p>Can it screen? Exploring the usability of data driven lean canvas framework for startup selection in accelerators</p><span>2020 – 2022</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/m-i-zadehnoori.jpg" data-profile-src="/images/alumni/m-i-zadehnoori.jpg" alt=""><div><h3>M. I. Zadehnouri</h3><p class="people-alumni-degree">MSc</p><p>Lucrative Startups Screening for Seed Accelerators: A Data-Driven Selection Criteria Pipeline</p><span>2019 – 2021</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/s-sorkhani.jpg" data-profile-src="/images/alumni/s-sorkhani.jpg" alt=""><div><h3>S. Sorkhani</h3><p class="people-alumni-degree">MSc</p><p>Learning to Rank for Question Routing in Community Question Answering Platforms</p><span>2019 – 2021</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/a-joukova.jpg" data-profile-src="/images/alumni/a-joukova.jpg" alt=""><div><h3>A. Joukova</h3><p class="people-alumni-degree">MSc</p><p>Identifying discriminative attributes for differentiation between depressed and non-depressed social media users</p><span>2020 – 2021</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/a-mok.jpg" data-profile-src="/images/alumni/a-mok.jpg" alt=""><div><h3>A. Mok</h3><p class="people-alumni-degree">MSc</p><p>A Triple Bottom Line Analysis of Sustainability Trends in the Luxury Fashion Industry: A Topic Modeling Approach</p><span>2019 – 2021</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/s-kavaratzis.jpg" data-profile-src="/images/alumni/s-kavaratzis.jpg" alt=""><div><h3>S. Kavaratzis</h3><p class="people-alumni-degree">MSc</p><p>How Well We Know Wellness: Closing The Gap On Wellness Program Research In The Workplace Through Mixed-Methods Topic Modeling</p><span>2020 – 2021</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/a-bigdeli.jpg" data-profile-src="/images/alumni/a-bigdeli.jpg" alt=""><div><h3>A. Bigdeli</h3><p class="people-alumni-degree">MSc</p><p>Gender Bias in Information Retrieval Systems</p><span>2020 – 2021</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/r-etwaroo.jpg" data-profile-src="/images/alumni/r-etwaroo.jpg" alt=""><div><h3>R. Etwaroo</h3><p class="people-alumni-degree">MSc</p><p>A Non-Factoid Question Answering System for Prior Art Search</p><span>2019 – 2020</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/media/profile-placeholder.svg" data-profile-src="/images/alumni/h-walia.jpg" alt=""><div><h3>H. Walia</h3><p class="people-alumni-degree">MSc</p><p>Customer Acquisition Through Direct Marketing Campaign Analysis</p><span>2018 – 2019</span></div></article>
          <article class="people-alumni-card"><img class="people-alumni-avatar" src="/images/alumni/l-r-ong.png" data-profile-src="/images/alumni/l-r-ong.jpg" alt=""><div><h3>L. R. Ong</h3><p class="people-alumni-degree">MSc</p><p>Predicting Depression using Personality and Social Network Data</p><span>2018 – 2019</span></div></article>
        </div>
    design:
      css_class: "people-alumni"
      columns: '1'

---
