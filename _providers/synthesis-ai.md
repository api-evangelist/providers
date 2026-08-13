---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.6
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: http://synthesis.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Synthesis-AI-Dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synthesis-ai
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/synthesis-ai_stock/
- group: build
  title: ''
  type: Packages
  url: packages/synthesis-ai-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/synthesis-ai-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synthesis-ai-domain-security.yml
- group: build
  title: ''
  type: Examples
  url: examples/synthesis-ai-human-api-job-complex-example.json
coverage:
  checked: '2026-08-05'
  detail: Synthesis AI was dissolved during 2024-2025 — synthesis.ai now answers only over HTTP with a Gandi "parked by the owner" page (the identical 2332-byte body is returned for every path, including a control path, so every 200 is a soft-404), and the FaceAPI/HumanAPI documentation host docs.synthesis.ai has been removed from DNS entirely.
  evidence:
  - status: 200
    url: http://synthesis.ai/
  - status: 200
    url: http://synthesis.ai/openapi.json
  - status: 200
    url: http://synthesis.ai/this-path-does-not-exist-ae-control-12345
  - status: 0
    url: https://docs.synthesis.ai/
  reason: defunct
  state: none
created: '2026-08-05'
description: 'Synthesis AI was a San Francisco synthetic-data company, founded in 2019 by Yashar Behzadi, that generated photorealistic, pixel-perfectly labeled images of humans for training computer-vision models. It sold that capability as an API: FaceAPI for labeled facial imagery and, from November 2021, HumanAPI for whole-body 3D digital humans, plus an Identities API for selecting subjects. Jobs were described as JSON documents (identities, expressions, gaze, head turn, hair, accessories, bodies and clothing, gesture animations, camera and light rigs, HDRI environments) and submitted through a command-line client or web console, with rendered output downloaded by job ID. The company raised a $17M Series A in 2022 on more than $24M total funding and was dissolved during 2024-2025. Its API is gone: synthesis.ai is a parked Gandi holding page reachable only over HTTP, and docs.synthesis.ai and api.synthesis.ai no longer resolve. What survives publicly is the Synthesis-AI-Dev GitHub organization
  (17 public repositories, including the Human API input-JSON appendix and the client tooling) and the official synthesisai package on PyPI.'
examples:
- key_count: 2
  name: Synthesis Ai Human Api Job Complex Example
  slug: synthesis-ai-human-api-job-complex-example
image: https://avatars.githubusercontent.com/u/55990723?v=4
layout: provider
modified: '2026-08-05'
name: Synthesis AI
nav: Providers
network: true
overview: 'Synthesis AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Synthetic Data, Computer Vision, Machine Learning, and Artificial Intelligence.


  Synthesis AI''s developer surface includes code examples and 7 more developer resources.'
random_paper: 49
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Synthesis Ai Domain Security
  slug: synthesis-ai-domain-security
  summary_line: no transport/DNS hardening detected
slug: synthesis-ai
tags:
- Company
- Synthetic Data
- Computer Vision
- Machine Learning
- Artificial Intelligence
- Digital Humans
- Training Data
- 3D
website: http://synthesis.ai/
---
