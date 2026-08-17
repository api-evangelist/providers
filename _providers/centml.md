---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Centml Agentic Access
  operation_count: 14
  slug: centml-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 5
apis:
- description: The Chat API from CentML — 1 operation(s) for chat.
  name: CentML Chat API
  slug: centml-chat-api
- description: The Clusters API from CentML — 2 operation(s) for clusters.
  name: CentML Clusters API
  slug: centml-clusters-api
- description: The Completions API from CentML — 1 operation(s) for completions.
  name: CentML Completions API
  slug: centml-completions-api
- description: The Deployments API from CentML — 6 operation(s) for deployments.
  name: CentML Deployments API
  slug: centml-deployments-api
- description: The Models API from CentML — 2 operation(s) for models.
  name: CentML Models API
  slug: centml-models-api
artifact_total: 20
asyncapis:
- description: AsyncAPI 2.6 description of CentML's **chat completion streaming** surface. CentML does not publish a WebSocket API. The only asynchronous / event-style transport documented at https://docs.centml.ai/
  name: CentML Chat Completions Streaming (HTTP + SSE)
  slug: centml-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CentML Chat API
  slug: open-centml-chat-api
- collection_type: open
  name: CentML Chat Clusters API
  slug: open-centml-clusters-api
- collection_type: open
  name: CentML Chat Completions API
  slug: open-centml-completions-api
- collection_type: open
  name: CentML Chat Deployments API
  slug: open-centml-deployments-api
- collection_type: open
  name: CentML Chat Models API
  slug: open-centml-models-api
- collection_type: open
  name: CentML API
  slug: open-centml
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/centml-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centml-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/centml-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CentML
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/centml
- group: company
  title: ''
  type: Website
  url: https://centml.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.centml.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/centml-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/centml-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/centml-finops.yml
created: '2026-06-21'
description: CentML is an AI inference optimization platform that serves popular open models through OpenAI-compatible serverless endpoints and lets teams stand up dedicated, autoscaling model-serving deployments and compute clusters. The serverless inference API runs at https://api.centml.com/openai/v1 with Bearer API keys, while a separate platform (control-plane) API manages deployments and clusters.
finops:
- name: Centml Finops
  service_category: AI and Machine Learning
  slug: centml-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/centml.png
layout: provider
modified: '2026-06-21'
name: CentML
nav: Providers
network: true
overview: 'CentML publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Clusters API, Completions API, and 2 more. Tagged areas include AI, LLM, Inference, Serverless, and GPU.


  The CentML catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  CentML''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Centml Plans Pricing
  plan_count: 3
  slug: centml-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 4
  name: Centml Rate Limits
  slug: centml-rate-limits
rules:
- name: CentML API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: centml-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.3
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/centml/refs/heads/main/screenshots/centml-2026-07-25T204927.png
security:
- kind: authentication
  name: Centml Authentication
  slug: centml-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Centml Domain Security
  slug: centml-domain-security
  summary_line: TLSv1.3 · DMARC
slug: centml
tags:
- AI
- LLM
- Inference
- Serverless
- GPU
website: https://centml.ai/
---
