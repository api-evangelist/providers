---
aid: ai-habitat
url: https://raw.githubusercontent.com/api-evangelist/ai-habitat/refs/heads/main/apis.yml
apis:
  - aid: ai-habitat:ai-habitat
    name: AI Habitat
    tags:
      - Embodied AI
      - Simulation
      - Robotics
      - Python
      - Computer Vision
      - Reinforcement Learning
    humanURL: https://aihabitat.org/
    properties:
      - url: https://aihabitat.org/
        type: Documentation
      - url: https://aihabitat.org/docs/
        type: Documentation
        title: API Documentation
      - url: https://github.com/facebookresearch/habitat-sim
        type: GitHubRepository
        title: Habitat-Sim GitHub
      - url: https://github.com/facebookresearch/habitat-lab
        type: GitHubRepository
        title: Habitat-Lab GitHub
      - url: https://pypi.org/project/habitat-sim/
        type: SDK
        title: Habitat-Sim Python Package
      - url: https://pypi.org/project/habitat-lab/
        type: SDK
        title: Habitat-Lab Python Package
    description: AI Habitat simulation framework for embodied AI research, including Habitat-Sim (high-performance 3D simulator) and Habitat-Lab (modular training library). Supports navigation, manipulation, and human-robot collaboration tasks across photorealistic 3D indoor environments.
name: AI Habitat
tags:
  - Artificial Intelligence
  - Simulation
  - Embodied AI
  - Robotics
  - Computer Vision
  - Reinforcement Learning
  - Machine Learning
  - Open Source
  - Research
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-17'
modified: '2026-04-19'
position: Consuming
description: AI Habitat is an open-source simulation platform from Meta AI Research for embodied AI research. It provides high-performance 3D simulated environments for training and evaluating AI agents on navigation, manipulation, and human-robot collaboration tasks. Habitat-Sim delivers 10,000+ FPS simulation and Habitat-Lab provides a modular library for defining tasks, training agents, and running benchmarks.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: AI Habitat GitHub Organization
    url: https://github.com/facebookresearch
    type: GitHubOrganization
    description: Meta AI Research GitHub organization hosting Habitat repositories.
  - name: Habitat-Sim Repository
    url: https://github.com/facebookresearch/habitat-sim
    type: GitHubRepository
    description: High-performance 3D simulator for embodied AI research (C++/Python).
  - name: Habitat-Lab Repository
    url: https://github.com/facebookresearch/habitat-lab
    type: GitHubRepository
    description: Modular library for embodied AI task definition, training, and benchmarking.
  - name: Habitat Documentation
    url: https://aihabitat.org/docs/
    type: Documentation
    description: Official documentation for AI Habitat platform.
  - name: Habitat Challenge
    url: https://aihabitat.org/challenge/
    type: Portal
    description: Annual Habitat Challenge competition on EvalAI for embodied AI navigation.
  - name: Habitat Discussions
    url: https://github.com/facebookresearch/habitat-lab/discussions
    type: Forum
    description: Community forum for Habitat questions and support.
  - name: Habitat HuggingFace
    url: https://huggingface.co/ai-habitat
    type: Portal
    description: AI Habitat datasets and models on HuggingFace.
  - name: Habitat-Sim PyPI
    url: https://pypi.org/project/habitat-sim/
    type: SDK
    title: Python Package (habitat-sim)
    description: Install Habitat-Sim via pip or conda.
  - name: Habitat-Lab PyPI
    url: https://pypi.org/project/habitat-lab/
    type: SDK
    title: Python Package (habitat-lab)
    description: Install Habitat-Lab via pip.
  - name: PARTNR Planner
    url: https://github.com/facebookresearch/partnr-planner
    type: Tools
    description: PARTNR benchmark for human-robot collaboration using Large Planning Models with Habitat.
  - type: Features
    data:
      - name: High-Performance Simulation
        description: Habitat-Sim achieves 10,000+ FPS on a single GPU and 8,000+ steps/second for robot simulation, enabling fast RL training.
      - name: Photorealistic 3D Environments
        description: Supports HM3D, MatterPort3D, Gibson, Replica, and HSSD datasets with high visual fidelity.
      - name: Physics-Enabled Simulation
        description: Bullet physics engine integration for realistic object interactions and manipulation tasks.
      - name: Robot Support via URDF
        description: Configurable robot models including Fetch mobile manipulator, Franka arm, and AlienGo quadruped.
      - name: Configurable Sensors
        description: RGB, depth, semantic, and egomotion sensors for varied agent perception configurations.
      - name: Modular Task Framework
        description: Habitat-Lab provides modular task definition, agent configuration, and benchmarking tools.
      - name: Imitation and Reinforcement Learning
        description: Built-in support for IL and RL training pipelines for embodied AI agents.
      - name: Human-Robot Collaboration
        description: Habitat 3.0 co-habitat supports humans, avatars, and robots sharing simulated environments.
      - name: Parallelizable Across Clusters
        description: Designed for large-scale distributed training across GPU clusters.
      - name: Annual Benchmark Challenge
        description: Habitat Challenge on EvalAI provides standardized evaluation of navigation and manipulation agents.
  - type: UseCases
    data:
      - name: Embodied Navigation Research
        description: Train and evaluate AI agents on point-goal, object-goal, and image-goal navigation tasks in 3D environments.
      - name: Robot Manipulation Research
        description: Develop manipulation skills for pick-and-place, rearrangement, and tool use with simulated robot arms.
      - name: Human-Robot Collaboration
        description: Research human-robot teaming for household tasks using the PARTNR benchmark and Habitat 3.0.
      - name: Reinforcement Learning Training
        description: Fast simulation enables RL agents to explore millions of environment steps for policy learning.
      - name: Dataset Creation and Annotation
        description: Generate synthetic data, annotations, and demonstrations for embodied AI training datasets.
  - type: Integrations
    data:
      - name: PyTorch
        description: Deep learning framework integration for neural network training and inference.
      - name: HuggingFace
        description: Datasets and models available on HuggingFace Hub at ai-habitat organization.
      - name: EvalAI
        description: Habitat Challenge evaluation hosted on EvalAI platform for standardized benchmarking.
      - name: Conda / conda-forge
        description: Conda package distribution via conda-forge and aihabitat channels.
      - name: Bullet Physics
        description: Bullet physics engine for realistic rigid-body simulation and manipulation.
      - name: ROS
        description: Robot Operating System integration for sim-to-real transfer research.
---
