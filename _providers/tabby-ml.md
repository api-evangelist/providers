---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Tabby Ml Agentic Access
  operation_count: 8
  slug: tabby-ml-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 6
apis:
- description: OpenAI-compatible chat completions and inline chat / Answer Engine.
  name: Tabby Chat API
  slug: tabby-ml-chat-api
- description: Code completion endpoint powering Tabby's IDE plugins.
  name: Tabby Completions API
  slug: tabby-ml-completions-api
- description: Client telemetry event logging.
  name: Tabby Events API
  slug: tabby-ml-events-api
- description: Server health and settings.
  name: Tabby Health API
  slug: tabby-ml-health-api
- description: Doc ingestion into the Answer Engine knowledge base.
  name: Tabby Ingestion API
  slug: tabby-ml-ingestion-api
- description: Model registry configured on the server.
  name: Tabby Models API
  slug: tabby-ml-models-api
artifact_total: 13
collections:
- collection_type: open
  name: Tabby Server API
  slug: open-tabby-ml
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tabby-ml-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tabby-ml-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tabby-ml-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TabbyML
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tabbyml
- group: company
  title: ''
  type: Website
  url: https://www.tabbyml.com
- group: docs
  title: ''
  type: Documentation
  url: https://tabby.tabbyml.com/docs/welcome/
- group: commercial
  title: ''
  type: Plans
  url: plans/tabby-ml-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tabby-ml-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tabby-ml-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tabbyml.com/blog
created: '2026-07-11'
description: Tabby is an open-source, self-hosted AI coding assistant - a privacy-first alternative to GitHub Copilot from TabbyML (Apache-2.0). You run the Tabby server yourself (Docker, a consumer-grade GPU, or your own cloud); there is no shared multi-tenant API and no external calls to third parties. The server exposes an OpenAPI-documented REST surface (Swagger UI at /swagger-ui, spec at /api-docs/openapi.json) for code completion, OpenAI-compatible chat completions, an Answer Engine backed by a doc-ingestion knowledge base, health, model registry, and telemetry events. Because it is self-hosted, the base URL is your own instance (default http://localhost:8080). TabbyML also offers hosted Team and Enterprise plans.
finops:
- name: Tabby Ml Finops
  service_category: AI and Machine Learning
  slug: tabby-ml-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tabby-ml.png
layout: provider
modified: '2026-07-11'
name: Tabby
nav: Providers
network: true
overview: 'Tabby publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Events API, and 3 more. Tagged areas include AI Coding Assistant, Code Completion, Open Source, Developer Tools, and LLM.


  Tabby''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Tabby Ml Plans Pricing
  plan_count: 4
  slug: tabby-ml-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 4
  name: Tabby Ml Rate Limits
  slug: tabby-ml-rate-limits
score:
  band: thin
  composite: 36.7
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.8
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tabby Ml Authentication
  slug: tabby-ml-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tabby Ml Domain Security
  slug: tabby-ml-domain-security
  summary_line: HSTS
slug: tabby-ml
tags:
- AI Coding Assistant
- Code Completion
- Open Source
- Developer Tools
- LLM
- AI
- Self-Hosted
- Code Generation
- Copilot Alternative
website: https://www.tabbyml.com
---
