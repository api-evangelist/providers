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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Freeplay Agentic Access
  operation_count: 29
  slug: freeplay-agentic-access
  summary_line: 29 operations · 18 acting
api_count: 10
apis:
- description: List agents within a project.
  name: Freeplay Agents API
  slug: freeplay-agents-api
- description: Record completions and aggregate completion statistics.
  name: Freeplay Completions API
  slug: freeplay-completions-api
- description: Curate datasets and their test cases.
  name: Freeplay Datasets API
  slug: freeplay-datasets-api
- description: Record completion-level and trace-level feedback.
  name: Freeplay Feedback API
  slug: freeplay-feedback-api
- description: List workspace projects.
  name: Freeplay Projects API
  slug: freeplay-projects-api
- description: Create, version, retrieve, and deploy prompt templates.
  name: Freeplay Prompt Templates API
  slug: freeplay-prompt-templates-api
- description: API-only search over sessions, traces, and completions.
  name: Freeplay Search API
  slug: freeplay-search-api
- description: List, search, and delete sessions.
  name: Freeplay Sessions API
  slug: freeplay-sessions-api
- description: Create, list, and retrieve batch test runs.
  name: Freeplay Test Runs API
  slug: freeplay-test-runs-api
- description: Record traces that group related completions.
  name: Freeplay Traces API
  slug: freeplay-traces-api
artifact_total: 18
collections:
- collection_type: open
  name: Freeplay HTTP API
  slug: open-freeplay
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freeplay-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/freeplay-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freeplay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freeplay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freeplayai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freeplay-ai
- group: company
  title: ''
  type: Website
  url: https://freeplay.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freeplay.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/freeplay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/freeplay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/freeplay-finops.yml
created: '2026-06-20'
description: Freeplay is an LLM product experimentation, evaluation, and observability platform for cross-functional teams. Its HTTP API and SDKs make Freeplay the source of truth for prompt templates, record completions and sessions/traces from production, curate test datasets, run batch test runs and LLM-judge evaluations, and capture human and customer feedback.
finops:
- name: Freeplay Finops
  service_category: AI and Machine Learning
  slug: freeplay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freeplay.png
layout: provider
modified: '2026-06-20'
name: Freeplay
nav: Providers
network: true
overview: 'Freeplay publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Completions API, Datasets API, and 7 more. Tagged areas include AI, LLM, Evaluation, Observability, and Prompt Management.


  Freeplay''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Freeplay Plans Pricing
  plan_count: 3
  slug: freeplay-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 3
  name: Freeplay Rate Limits
  slug: freeplay-rate-limits
score:
  band: thin
  composite: 39.5
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 55.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freeplay/refs/heads/main/screenshots/freeplay-2026-06-20T181534.png
security:
- kind: authentication
  name: Freeplay Authentication
  slug: freeplay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Freeplay Domain Security
  slug: freeplay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Freeplay Trust Center
  slug: freeplay-trust-center
  summary_line: SOC 2, ISO 27001
slug: freeplay
tags:
- AI
- LLM
- Evaluation
- Observability
- Prompt Management
- Experimentation
website: https://freeplay.ai/
---
