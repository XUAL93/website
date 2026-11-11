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
    content:
      title: '📚 Research'
      subtitle: ''
      text: |-
        Aolong Xu studies how the brain constructs and adapts the space around the body. His research follows two lines of inquiry.

        **1. Plasticity of peripersonal space (PPS)**  
        This line examines how PPS adapts to different contexts, tasks, and sensory feedback. A central theme is the comparison between hand-centered and foot-centered PPS. The aim is to identify functional and neural differences between body parts in multisensory integration and action preparation.

        **2. Neural and cognitive architecture of spatial representations**  
        This line examines how the brain represents peripersonal space, reaching space, and interpersonal space. It tests how these spaces differ in their cognitive and neural mechanisms. The results inform theories of social behavior, motor control, and sensory processing.

        Methods include immersive VR, behavioral experiments, and EEG.  
        Collaboration enquiries are welcome.
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
---
