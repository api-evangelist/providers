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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.1
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'OpenAPI-compatible REST API for scoring, calibrating, and optimizing LLM outputs against rubrics of natural-language questions. Authenticated with an API key (WITHPI_API_KEY) sent as an Authorization '
  name: Pi Scoring API
  slug: pi-scoring-api
artifact_total: 2
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://withpi.ai
- group: docs
  title: ''
  type: Documentation
  url: https://code.withpi.ai
- group: docs
  title: ''
  type: APIReference
  url: https://code.withpi.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://code.withpi.ai/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withpi
- group: operate
  title: ''
  type: ChangeLog
  url: https://withpi.ai/release-notes
- group: build
  title: ''
  type: Packages
  url: packages/pi-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pi-labs-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pi-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pi-labs-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pi-labs-llms.txt
created: '2026-07-17'
description: Pi Labs (withpi.ai) is an applied-AI company, backed by Accel and later acquired by Microsoft, that builds tooling to evaluate and enhance AI applications. Its core product, Pi Scorer, is a deterministic, roughly 200ms foundation model that scores any text against a rubric of natural-language questions — reported to be about 500x more efficient than using an LLM as a judge. Teams use it to calibrate rubrics, gate and rank LLM outputs, and close the loop across training, inference, and feedback. The scoring engine is exposed as an OpenAPI-compatible REST API at api.withpi.ai with official Python and TypeScript SDKs (both published as "withpi"), a copilot for building scoring specs, and a Promptfoo integration (Pi Scorer).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pi-labs.png
layout: provider
modified: '2026-07-20'
name: Pi Labs
nav: Providers
network: true
overview: 'Pi Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Evaluation, LLM, and Scoring.


  Pi Labs'' developer surface includes documentation, API reference, getting-started guide, changelog, authentication, and 7 more developer resources.'
random_paper: 24
score:
  band: emerging
  composite: 21.1
  delta: -2.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 53.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.7
  provenance:
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Pi Labs Authentication
  slug: pi-labs-authentication
  summary_line: apiKey · 1 scheme
slug: pi-labs
tags:
- Company
- AI
- Evaluation
- LLM
- Scoring
- Machine Learning
- Developer Tools
website: https://withpi.ai
---
