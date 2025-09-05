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

  - block: markdown
    content:
      title: "Human Centered Machine Intelligence Lab"
      subtitle: ''
      text: |
        The Human Centered Machine Intelligence Lab is dedicated to shaping AI systems that are ethical,
        fair, and accountable. Our vision is to advance research in fairness aware information retrieval,
        human compatible AI, and trustworthy infrastructures that align intelligent technologies with
        human values and the public good.
    design:
      columns: '1'
      background:
        video:
          filename: video.mp4
          filters:
            brightness: 0.7
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['80px', '0', '120px', '0']
      css_class: fullscreen hero-large-title

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
        color: '#adb5bd'
      spacing:
        padding: ['40px', '0', '40px', '0']

  # - block: collection
  #   content:
  #     title: Latest News
  #     count: 5
  #     filters:
  #       page_type: post
  #     order: desc
  #   design:
  #     view: card
  #     columns: '1'

  
  - block: collection
    content:
      title: Latest Publications
      count: 8
      filters:
        folders:
          - publication
      order: desc
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      text: ""
    design:
      columns: '1'
---