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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: The FGL Holdings API provides access to platform services and data for enterprise integration and automation.
  name: FGL Holdings API
  slug: fgl-holdings-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fgl-holdings-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fglife.com
created: '2026-04-19'
description: FGL Holdings is a major US corporation and Fortune 1000 company. The FGL Holdings API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Fgl Holdings Finops
  service_category: Insurance / Annuities
  slug: fgl-holdings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fgl-holdings.png
layout: provider
modified: '2026-04-19'
name: FGL Holdings
nav: Providers
network: true
overview: FGL Holdings publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Annuities, and Financial Services.
plans:
- name: Fgl Holdings Plans Pricing
  plan_count: 1
  slug: fgl-holdings-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 1
  name: Fgl Holdings Rate Limits
  slug: fgl-holdings-rate-limits
score:
  band: emerging
  composite: 16.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.0
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fgl-holdings/refs/heads/main/screenshots/fgl-holdings-2026-06-20T181145.png
security:
- kind: domain-security
  name: Fgl Holdings Domain Security
  slug: fgl-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fgl-holdings
tags:
- Insurance
- Annuities
- Financial Services
website: https://www.fglife.com
---
