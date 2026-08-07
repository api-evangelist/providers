---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: 'The Pathmind web application''s public REST API. Two operations: list the authenticated user''s projects, and upload an AnyLogic simulation model (optionally into an existing project) to create a Pathmi'
  name: Pathmind API
  slug: pathmind-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://pathmind.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PathmindAI
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/PathmindAI/pathmind-webapp
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/PathmindAI/pathmind-api/blob/main/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/PathmindAI/pathmind-webapp/blob/dev/pathmind-api/src/main/resources/openapi.yaml
- group: build
  title: ''
  type: Packages
  url: packages/skymind-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/skymind-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/skymind-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skymind-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/skymind-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skymind-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/skymind-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skymind-domain-security.yml
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/skymind_stock/
created: '2026-08-05'
description: 'Pathmind (formerly Skymind, the company behind the Deeplearning4j open-source deep learning library) was a San Francisco reinforcement-learning company that let simulation engineers train RL policies against AnyLogic and Python simulations without writing machine-learning code. The product had three parts: the Pathmind Helper, an AnyLogic palette item that exposed a simulation''s observations, actions and reward function to Pathmind; a cloud training service where uploaded models became experiments; and Pathmind Serving, a FastAPI/Ray policy server that turned a trained policy into a REST prediction endpoint. A small first-party REST API (project listing and AnyLogic model upload, authenticated with an X-PM-API-TOKEN header) and a first-party Python simulation API on PyPI were published. Pathmind ceased operating in November 2021 — its own final release, pathmind-webapp v1.8.6, is titled "Final release - disabling sign-ups and upgrades" — and the app, API and marketing hosts
  no longer serve. The artifacts in this repository are the surviving public first-party surface, harvested from the company''s own GitHub organization and PyPI.'
image: https://raw.githubusercontent.com/PathmindAI/pathmind-webapp/dev/pathmind-webapp/src/main/resources/static/frontend/images/pathmind-logo-100x100.png
layout: provider
modified: '2026-08-05'
name: Pathmind
nav: Providers
network: true
overview: 'Pathmind publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, Reinforcement Learning, and Simulation.


  Pathmind''s developer surface includes documentation, API reference, changelog, and 11 more developer resources.'
random_paper: 89
score:
  band: thin
  composite: 31.5
  delta: -0.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 57.4
    developer_ergonomics: 21.7
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 31.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Skymind Authentication
  slug: skymind-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Skymind Domain Security
  slug: skymind-domain-security
  summary_line: TLSv1.3
slug: skymind
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Reinforcement Learning
- Simulation
- Optimization
- Supply Chain
- Manufacturing
- Defunct
website: https://pathmind.com/
---
