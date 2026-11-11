---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
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
      text: |-
        Aolong Xu studies how the brain constructs and adapts the space around the body. His research follows two lines of inquiry.

        **1. Flexibility and plasticity of peripersonal space (PPS)**  
        This line examines how PPS adapts to different contexts and tasks. A central theme is the comparison between hand-centered and foot-centered PPS. The aim is to identify functional and neural differences between body parts in multisensory integration and action planning.

        **2. Similarities and differences between spatial representations**  
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
