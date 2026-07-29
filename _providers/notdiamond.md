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
  name: Notdiamond Agentic Access
  operation_count: 6
  slug: notdiamond-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 4
apis:
- description: The Custom Routers API from Not Diamond — 2 operation(s) for custom routers.
  name: Not Diamond Custom Routers API
  slug: notdiamond-custom-routers-api
- description: The Feedback API from Not Diamond — 2 operation(s) for feedback.
  name: Not Diamond Feedback API
  slug: notdiamond-feedback-api
- description: The Model Routing API from Not Diamond — 1 operation(s) for model routing.
  name: Not Diamond Model Routing API
  slug: notdiamond-model-routing-api
- description: The Models API from Not Diamond — 1 operation(s) for models.
  name: Not Diamond Models API
  slug: notdiamond-models-api
artifact_total: 11
collections:
- collection_type: open
  name: Not Diamond API
  slug: open-notdiamond
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/notdiamond-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notdiamond-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/notdiamond-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.notdiamond.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Not-Diamond
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/not-diamond
- group: company
  title: ''
  type: Website
  url: https://www.notdiamond.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.notdiamond.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/notdiamond-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/notdiamond-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/notdiamond-finops.yml
created: '2026-06-20'
description: Not Diamond is an AI model router that determines the best LLM to call for any given prompt. Its REST API routes each request to the optimal model across providers based on quality, cost, and latency tradeoffs, accepts real-time feedback to personalize routing, and can train custom routers from evaluation datasets.
finops:
- name: Notdiamond Finops
  service_category: AI and Machine Learning
  slug: notdiamond-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/notdiamond.png
layout: provider
modified: '2026-06-20'
name: Not Diamond
nav: Providers
network: true
overview: 'Not Diamond publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Custom Routers API, Feedback API, Model Routing API, and 1 more. Tagged areas include AI, LLM, Model Routing, Router, and Orchestration.


  Not Diamond''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Notdiamond Plans Pricing
  plan_count: 2
  slug: notdiamond-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 3
  name: Notdiamond Rate Limits
  slug: notdiamond-rate-limits
score:
  band: thin
  composite: 37.1
  delta: -2.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/notdiamond/refs/heads/main/screenshots/notdiamond-2026-06-20T190525.png
security:
- kind: authentication
  name: Notdiamond Authentication
  slug: notdiamond-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Notdiamond Domain Security
  slug: notdiamond-domain-security
  summary_line: TLSv1.3 · HSTS
slug: notdiamond
tags:
- AI
- LLM
- Model Routing
- Router
- Orchestration
website: https://www.notdiamond.ai
---
