---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'Open-source Python library for evaluating and tracking LLM applications. Provides feedback functions (groundedness, relevance, etc.), tracing, and a local dashboard. Distributed via PyPI under Apache '
  name: TruLens (Open Source)
  slug: trulens
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truera-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truera
- group: company
  title: ''
  type: Website
  url: https://truera.com/
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/truera/trulens
- group: commercial
  title: ''
  type: Plans
  url: plans/truera-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truera-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/truera-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://truera.com/feed/
created: '2026-05-08'
description: TruEra was an AI quality, observability, and governance platform that was acquired by Snowflake in May 2024. The standalone TruEra product is being absorbed into Snowflake's Cortex/AI platform. The open-source TruLens evaluation library (originally from TruEra) remains active as a standalone Python project for LLM and RAG evaluation.
finops:
- name: Truera Finops
  service_category: AI Observability
  slug: truera-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truera.png
layout: provider
modified: '2026-07-25'
name: TruEra (Snowflake)
nav: Providers
network: true
overview: 'TruEra (Snowflake) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Evaluation, Observability, AI Governance, LLM, and RAG.


  TruEra (Snowflake)''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Truera Plans Pricing
  plan_count: 2
  slug: truera-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Truera Rate Limits
  slug: truera-rate-limits
score:
  band: emerging
  composite: 12.3
  delta: 2.6
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 9.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truera/refs/heads/main/screenshots/truera-2026-06-20T195755.png
security:
- kind: domain-security
  name: Truera Domain Security
  slug: truera-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: truera
tags:
- AI Evaluation
- Observability
- AI Governance
- LLM
- RAG
- Snowflake
website: https://truera.com/
---
