---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
lastmod: 2026-11-11
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: tenerife.jpg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false
  - block: markdown
    id: research
    content:
      title: Research
      subtitle: ''
      intro: How sensory information shapes perception and the space around the body.
      themes:
        - title: Multisensory integration
          description: How does the brain combine information from different senses to shape perception and action? Aolong studies multisensory integration in peripersonal space, comparing hand- and foot-centered representations using immersive VR, behavioral experiments, and EEG.
        - title: Spatial representations
          description: How do peripersonal space, reaching space, and interpersonal space overlap and differ? His work examines the cognitive and neural mechanisms behind these spatial representations.
      text: |-
        Aolong Xu studies how the brain constructs and adapts the space around the body. His research follows two lines of inquiry.

        ### Multisensory integration

        This line examines how the brain combines information from different senses to shape perception and action. A focus is the flexibility and plasticity of peripersonal space (PPS) across different contexts and tasks, comparing hand-centered and foot-centered representations.

        ### Spatial representations

        This line examines how the brain represents peripersonal space, reaching space, and interpersonal space. It tests how these spaces differ in their cognitive and neural mechanisms. The results inform theories of social behavior, motor control, and sensory processing.

        Methods include immersive VR, behavioral experiments, and EEG.
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Publications
      text: ""
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      view: citation
  - block: markdown
    id: profiles
    content:
      title: Find me online
      subtitle: ''
      text: |-
        Based in Ghent, Belgium.

        **Email**  
        [aolong.xu@ugent.be](mailto:aolong.xu@ugent.be)

        **[Google Scholar](https://scholar.google.com/citations?user=DIYaStkAAAAJ&hl=en)**  
        Browse my publications and citations.

        **[LinkedIn](https://www.linkedin.com/in/aolong-xu-646024356/)**  
        View my professional profile and connect with me.

        **[Xiaohongshu](https://xhslink.cn/o/i7PD1T4HcW)**  
        Explore my posts on Xiaohongshu (RedNote).
    design:
      columns: '1'
---
