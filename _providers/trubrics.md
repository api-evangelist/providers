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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Trubrics Agentic Access
  operation_count: 2
  slug: trubrics-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 2
apis:
- description: The Events API from Trubrics — 1 operation(s) for events.
  name: Trubrics Events API
  slug: trubrics-events-api
- description: The LLM Events API from Trubrics — 1 operation(s) for llm events.
  name: Trubrics LLM Events API
  slug: trubrics-llm-events-api
artifact_total: 9
collections:
- collection_type: open
  name: Trubrics Ingestion API
  slug: open-trubrics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trubrics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trubrics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trubrics-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trubrics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trubrics
- group: company
  title: ''
  type: Website
  url: https://www.trubrics.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trubrics.com
- group: commercial
  title: ''
  type: Plans
  url: plans/trubrics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trubrics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trubrics-finops.yml
created: '2026-06-20'
description: Trubrics is a product analytics platform for AI and LLM applications. It captures user and AI events together - prompts, generations, feedback, sign ups and conversions - through JavaScript and Python SDKs and a public HTTP ingestion API, then surfaces them as product analytics for understanding adoption, quality, and cost of AI features.
finops:
- name: Trubrics Finops
  service_category: Analytics
  slug: trubrics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trubrics.png
layout: provider
modified: '2026-06-20'
name: Trubrics
nav: Providers
network: true
overview: 'Trubrics publishes 2 APIs on the [APIs.io](https://apis.io/) network: Events API and LLM Events API. Tagged areas include AI, LLM, Product Analytics, Event Tracking, and Feedback.


  Trubrics'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Trubrics Plans Pricing
  plan_count: 3
  slug: trubrics-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 4
  name: Trubrics Rate Limits
  slug: trubrics-rate-limits
score:
  band: thin
  composite: 39.4
  delta: -1.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.3
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
screenshot: https://raw.githubusercontent.com/api-evangelist/trubrics/refs/heads/main/screenshots/trubrics-2026-06-20T195747.png
security:
- kind: authentication
  name: Trubrics Authentication
  slug: trubrics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trubrics Domain Security
  slug: trubrics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trubrics
tags:
- AI
- LLM
- Product Analytics
- Event Tracking
- Feedback
website: https://www.trubrics.com
---
