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
- acting_count: 3
  human_in_the_loop: 0
  name: Cerebrium Agentic Access
  operation_count: 3
  slug: cerebrium-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 3
apis:
- description: Surfaces app logs, metrics, and platform status through the CLI (cerebrium logs, cerebrium status), the app dashboard, and the public status page.
  name: Cerebrium Logs / Status API
  slug: cerebrium-logs-status-api
- description: The Inference API from Cerebrium — 1 operation(s) for inference.
  name: Cerebrium Inference API
  slug: cerebrium-inference-api
- description: The OpenAI Compatible API from Cerebrium — 2 operation(s) for openai compatible.
  name: Cerebrium OpenAI Compatible API
  slug: cerebrium-openai-compatible-api
artifact_total: 10
collections:
- collection_type: open
  name: Cerebrium Cortex Inference API
  slug: open-cerebrium
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cerebrium-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerebrium-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cerebrium-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CerebriumAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cerebrium
- group: company
  title: ''
  type: Website
  url: https://www.cerebrium.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.cerebrium.ai/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/cerebrium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cerebrium-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cerebrium-finops.yml
created: '2026-06-20'
description: Cerebrium is a serverless GPU infrastructure platform for real-time AI and ML workloads. Developers package code with the Cortex framework and Cerebrium CLI, then deploy each function as an authenticated REST endpoint on autoscaling GPU/CPU compute billed per second, with streaming, WebSocket, async, and OpenAI-compatible invocation patterns.
finops:
- name: Cerebrium Finops
  service_category: AI and Machine Learning
  slug: cerebrium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cerebrium.png
layout: provider
modified: '2026-06-20'
name: Cerebrium
nav: Providers
network: true
overview: 'Cerebrium publishes 2 APIs on the [APIs.io](https://apis.io/) network: Inference API and OpenAI Compatible API. Tagged areas include AI, GPU, Serverless, Inference, and ML Infrastructure.


  Cerebrium''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Cerebrium Plans Pricing
  plan_count: 4
  slug: cerebrium-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 4
  name: Cerebrium Rate Limits
  slug: cerebrium-rate-limits
score:
  band: thin
  composite: 39.1
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Cerebrium Authentication
  slug: cerebrium-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cerebrium Domain Security
  slug: cerebrium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cerebrium
tags:
- AI
- GPU
- Serverless
- Inference
- ML Infrastructure
website: https://www.cerebrium.ai
---
