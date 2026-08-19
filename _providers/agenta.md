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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Agenta Agentic Access
  operation_count: 25
  slug: agenta-agentic-access
  summary_line: 25 operations · 19 acting
api_count: 7
apis:
- description: Create and manage LLM applications and their variants.
  name: Agenta Applications API
  slug: agenta-applications-api
- description: Fetch and deploy versioned prompt configurations.
  name: Agenta Configs API
  slug: agenta-configs-api
- description: Run evaluations of variants against testsets.
  name: Agenta Evaluations API
  slug: agenta-evaluations-api
- description: Configure evaluators used to score variants.
  name: Agenta Evaluators API
  slug: agenta-evaluators-api
- description: Ingest LLM telemetry over OTLP/HTTP.
  name: Agenta OpenTelemetry API
  slug: agenta-opentelemetry-api
- description: Manage evaluation datasets (testsets).
  name: Agenta Testsets API
  slug: agenta-testsets-api
- description: Query observability traces and spans.
  name: Agenta Traces API
  slug: agenta-traces-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agenta Applications API
  slug: open-agenta-applications-api
- collection_type: open
  name: Agenta Applications Configs API
  slug: open-agenta-configs-api
- collection_type: open
  name: Agenta Applications Evaluations API
  slug: open-agenta-evaluations-api
- collection_type: open
  name: Agenta Applications Evaluators API
  slug: open-agenta-evaluators-api
- collection_type: open
  name: Agenta Applications OpenTelemetry API
  slug: open-agenta-opentelemetry-api
- collection_type: open
  name: Agenta Applications Testsets API
  slug: open-agenta-testsets-api
- collection_type: open
  name: Agenta Applications Traces API
  slug: open-agenta-traces-api
- collection_type: open
  name: Agenta API
  slug: open-agenta
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agenta-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agenta-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agenta-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Agenta-AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agenta-ai
- group: company
  title: ''
  type: Website
  url: https://agenta.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agenta.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/agenta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agenta-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/agenta-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://agenta.ai/blog
created: '2026-06-20'
description: Agenta is an open-source LLMOps platform that brings prompt management, LLM evaluation, and LLM observability together in one place. Its cloud REST API at https://cloud.agenta.ai/api exposes apps and variants, versioned prompt configurations, evaluations and evaluators, testsets, and OpenTelemetry-based tracing, all authenticated with a Bearer API key. The platform is MIT licensed and can be self-hosted or used via Agenta Cloud.
finops:
- name: Agenta Finops
  service_category: AI and Machine Learning
  slug: agenta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agenta.png
layout: provider
modified: '2026-06-20'
name: Agenta
nav: Providers
network: true
overview: 'Agenta publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Configs API, Evaluations API, and 4 more. Tagged areas include AI, LLMOps, Prompt Management, LLM Evaluation, and Observability.


  Agenta''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Agenta Plans Pricing
  plan_count: 5
  slug: agenta-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: Agenta Rate Limits
  slug: agenta-rate-limits
score:
  band: thin
  composite: 38.4
  delta: -0.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agenta/refs/heads/main/screenshots/agenta-2026-06-20T170004.png
security:
- kind: authentication
  name: Agenta Authentication
  slug: agenta-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agenta Domain Security
  slug: agenta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agenta
tags:
- AI
- LLMOps
- Prompt Management
- LLM Evaluation
- Observability
website: https://agenta.ai/
---
