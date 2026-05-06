---
aid: newton
name: Newton
description: Newton is a Linux Foundation open source physics engine, contributed by Disney Research, NVIDIA, and Google DeepMind. Built on NVIDIA Warp and integrating MuJoCo Warp as a backend, Newton targets roboticists and simulation researchers, providing GPU-accelerated, differentiable, OpenUSD-compatible physics simulation for AI training, robotics, gaming, and scientific research.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Linux Foundation
  - Physics
  - Simulation
  - Robotics
  - GPU
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/newton/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: newton:newton
    name: Newton Physics Engine
    description: Newton is a Python library and physics simulation engine. It is consumed programmatically via Python (not as an HTTP API), targeting robotics simulation, reinforcement learning, and physics-based AI training workloads on GPU.
    humanURL: https://newton-physics.github.io/newton/
    tags:
      - AI
      - Physics
      - Simulation
      - Robotics
      - GPU
    properties:
      - type: Documentation
        url: https://newton-physics.github.io/newton/
      - type: SourceCode
        url: https://github.com/newton-physics/newton
      - type: GitHubOrg
        url: https://github.com/newton-physics
common:
  - type: Documentation
    name: Newton Documentation
    description: Official documentation for the Newton physics engine.
    url: https://newton-physics.github.io/newton/
  - type: SourceCode
    name: Newton Source Code
    description: Source code repository for Newton.
    url: https://github.com/newton-physics/newton
  - type: GitHubOrg
    name: Newton GitHub Organization
    description: GitHub organization hosting Newton and related projects.
    url: https://github.com/newton-physics
  - type: LinuxFoundation
    name: Linux Foundation
    description: Newton is a Linux Foundation hosted project.
    url: https://www.linuxfoundation.org/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
