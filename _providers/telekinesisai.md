---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telekinesisai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://telekinesis.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.telekinesis.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.telekinesis.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.telekinesis.ai/skills/overview.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.telekinesis.ai/getting-started/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://platform.telekinesis.ai/api-keys
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/telekinesis-ai
- group: operate
  title: ''
  type: Support
  url: https://telekinesis.ai/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.telekinesis.ai/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.telekinesis.ai/legal/privacy.html
- group: build
  title: ''
  type: Packages
  url: packages/telekinesisai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/telekinesisai-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telekinesisai-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telekinesisai-llms.txt
created: '2026-07-17'
description: Telekinesis is a Physical AI company building a unified Python SDK and large-scale "skill library" for industrial robotics and computer vision. Its composable skills span perception (2D/3D detection, segmentation, 6D pose estimation, point clouds), planning, control, reinforcement learning, and Vision-Language-Model agents that orchestrate complete robotics systems. Developers install the official telekinesis-ai SDK from PyPI, authenticate with an API key from platform.telekinesis.ai, and run skills either cloud-hosted or on-premise. The stack includes BabyROS (a lightweight ROS-style pub/sub middleware on Zenoh), a Data Engine for synthetic dataset generation, and NVIDIA Isaac Sim integration for simulation-to-real transfer. Telekinesis targets high-mix manufacturing use cases such as assembly, machine tending, bin picking, CNC loading, and inspection, and is a Techstars portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telekinesisai.png
layout: provider
modified: '2026-07-21'
name: Telekinesis.ai
nav: Providers
network: true
overview: 'Telekinesis.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Computer Vision, Physical AI, and Industrial Automation.


  Telekinesis.ai''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 9 more developer resources.'
random_paper: 45
score:
  band: emerging
  composite: 22.7
  delta: -1.9
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 24.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Telekinesisai Authentication
  slug: telekinesisai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Telekinesisai Domain Security
  slug: telekinesisai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: telekinesisai
tags:
- Company
- Robotics
- Computer Vision
- Physical AI
- Industrial Automation
- Manufacturing Automation
- 6D Pose Estimation
- Motion Planning
- Reinforcement Learning
- Python SDK
- Embodied Intelligence
- Agents
website: https://telekinesis.ai/
---
