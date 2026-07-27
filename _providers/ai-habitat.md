---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: AI Habitat simulation framework for embodied AI research, including Habitat-Sim (high-performance 3D simulator) and Habitat-Lab (modular training library). Supports navigation, manipulation, and human
  name: AI Habitat
  slug: ai-habitat
artifact_total: 52
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ai-habitat-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/facebookresearch
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/facebookresearch/habitat-sim
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/facebookresearch/habitat-lab
- group: docs
  title: ''
  type: Documentation
  url: https://aihabitat.org/docs/
- group: start
  title: ''
  type: Portal
  url: https://aihabitat.org/challenge/
- group: operate
  title: ''
  type: Forums
  url: https://github.com/facebookresearch/habitat-lab/discussions
- group: start
  title: ''
  type: Portal
  url: https://huggingface.co/ai-habitat
- group: build
  title: Python Package (habitat-sim)
  type: SDKs
  url: https://pypi.org/project/habitat-sim/
- group: build
  title: Python Package (habitat-lab)
  type: SDKs
  url: https://pypi.org/project/habitat-lab/
- group: build
  title: ''
  type: Tools
  url: https://github.com/facebookresearch/partnr-planner
created: '2025-02-17'
description: AI Habitat is an open-source simulation platform from Meta AI Research for embodied AI research. It provides high-performance 3D simulated environments for training and evaluating AI agents on navigation, manipulation, and human-robot collaboration tasks. Habitat-Sim delivers 10,000+ FPS simulation and Habitat-Lab provides a modular library for defining tasks, training agents, and running benchmarks.
examples:
- key_count: 5
  name: Ai Habitat Agent Config Example
  slug: ai-habitat-agent-config-example
- key_count: 4
  name: Ai Habitat Agent Observation Example
  slug: ai-habitat-agent-observation-example
- key_count: 6
  name: Ai Habitat Episode Example
  slug: ai-habitat-episode-example
- key_count: 2
  name: Ai Habitat Navigation Goal Example
  slug: ai-habitat-navigation-goal-example
- key_count: 5
  name: Ai Habitat Observation Example
  slug: ai-habitat-observation-example
- key_count: 6
  name: Ai Habitat Sensor Spec Example
  slug: ai-habitat-sensor-spec-example
- key_count: 7
  name: Ai Habitat Simulator Config Example
  slug: ai-habitat-simulator-config-example
- key_count: 5
  name: Ai Habitat Task Config Example
  slug: ai-habitat-task-config-example
features:
- description: Habitat-Sim achieves 10,000+ FPS on a single GPU and 8,000+ steps/second for robot simulation, enabling fast RL training.
  name: High-Performance Simulation
- description: Supports HM3D, MatterPort3D, Gibson, Replica, and HSSD datasets with high visual fidelity.
  name: Photorealistic 3D Environments
- description: Bullet physics engine integration for realistic object interactions and manipulation tasks.
  name: Physics-Enabled Simulation
- description: Configurable robot models including Fetch mobile manipulator, Franka arm, and AlienGo quadruped.
  name: Robot Support via URDF
- description: RGB, depth, semantic, and egomotion sensors for varied agent perception configurations.
  name: Configurable Sensors
- description: Habitat-Lab provides modular task definition, agent configuration, and benchmarking tools.
  name: Modular Task Framework
- description: Built-in support for IL and RL training pipelines for embodied AI agents.
  name: Imitation and Reinforcement Learning
- description: Habitat 3.0 co-habitat supports humans, avatars, and robots sharing simulated environments.
  name: Human-Robot Collaboration
- description: Designed for large-scale distributed training across GPU clusters.
  name: Parallelizable Across Clusters
- description: Habitat Challenge on EvalAI provides standardized evaluation of navigation and manipulation agents.
  name: Annual Benchmark Challenge
finops:
- name: Ai Habitat Finops
  service_category: API
  slug: ai-habitat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ai-habitat.png
integrations:
- description: Deep learning framework integration for neural network training and inference.
  name: PyTorch
- description: Datasets and models available on HuggingFace Hub at ai-habitat organization.
  name: HuggingFace
- description: Habitat Challenge evaluation hosted on EvalAI platform for standardized benchmarking.
  name: EvalAI
- description: Conda package distribution via conda-forge and aihabitat channels.
  name: Conda / conda-forge
- description: Bullet physics engine for realistic rigid-body simulation and manipulation.
  name: Bullet Physics
- description: Robot Operating System integration for sim-to-real transfer research.
  name: ROS
json_schemas:
- name: AgentConfig
  property_count: 5
  slug: ai-habitat-agent-config
- name: AgentObservation
  property_count: 4
  slug: ai-habitat-agent-observation
- name: Episode
  property_count: 6
  slug: ai-habitat-episode
- name: NavigationGoal
  property_count: 2
  slug: ai-habitat-navigation-goal
- name: Observation
  property_count: 5
  slug: ai-habitat-observation
- name: SensorSpec
  property_count: 6
  slug: ai-habitat-sensor-spec
- name: SimulatorConfig
  property_count: 7
  slug: ai-habitat-simulator-config
- name: TaskConfig
  property_count: 5
  slug: ai-habitat-task-config
json_structures:
- name: Ai Habitat Agent Config Structure
  property_count: 5
  slug: ai-habitat-agent-config-structure
- name: Ai Habitat Agent Observation Structure
  property_count: 4
  slug: ai-habitat-agent-observation-structure
- name: Ai Habitat Episode Structure
  property_count: 6
  slug: ai-habitat-episode-structure
- name: Ai Habitat Navigation Goal Structure
  property_count: 2
  slug: ai-habitat-navigation-goal-structure
- name: Ai Habitat Observation Structure
  property_count: 5
  slug: ai-habitat-observation-structure
- name: Ai Habitat Sensor Spec Structure
  property_count: 6
  slug: ai-habitat-sensor-spec-structure
- name: Ai Habitat Simulator Config Structure
  property_count: 7
  slug: ai-habitat-simulator-config-structure
- name: Ai Habitat Task Config Structure
  property_count: 5
  slug: ai-habitat-task-config-structure
jsonld:
- class_count: 7
  name: Ai Habitat Context
  property_count: 13
  slug: ai-habitat-context
layout: provider
modified: '2026-04-19'
name: AI Habitat
nav: Providers
network: true
overview: 'AI Habitat publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Simulation, Embodied AI, Robotics, and Computer Vision.


  The AI Habitat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Habitat''s developer surface includes documentation, developer portal, tooling, and 8 more developer resources.'
plans:
- name: Ai Habitat Plans Pricing
  plan_count: 3
  slug: ai-habitat-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: Ai Habitat Rate Limits
  slug: ai-habitat-rate-limits
rules:
- name: AI Habitat API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ai-habitat-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 20.8
    developer_ergonomics: 23.9
    discoverability: 80.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 39.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ai-habitat/refs/heads/main/screenshots/ai-habitat-2026-06-20T170703.png
security:
- kind: domain-security
  name: Ai Habitat Domain Security
  slug: ai-habitat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ai-habitat
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
use_cases:
- description: Train and evaluate AI agents on point-goal, object-goal, and image-goal navigation tasks in 3D environments.
  name: Embodied Navigation Research
- description: Develop manipulation skills for pick-and-place, rearrangement, and tool use with simulated robot arms.
  name: Robot Manipulation Research
- description: Research human-robot teaming for household tasks using the PARTNR benchmark and Habitat 3.0.
  name: Human-Robot Collaboration
- description: Fast simulation enables RL agents to explore millions of environment steps for policy learning.
  name: Reinforcement Learning Training
- description: Generate synthetic data, annotations, and demonstrations for embodied AI training datasets.
  name: Dataset Creation and Annotation
website: https://aihabitat.org/challenge/
---
