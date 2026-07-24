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
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The Amedisys API provides access to platform services and data for enterprise integration and automation.
  name: Amedisys API
  slug: amedisys-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amedisys-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amedisys
- group: company
  title: ''
  type: Website
  url: https://www.amedisys.com
created: '2026-04-19'
description: Amedisys is a major US corporation and Fortune 1000 company. The Amedisys API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Amedisys Finops
  service_category: Healthcare
  slug: amedisys-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amedisys.png
layout: provider
modified: '2026-04-19'
name: Amedisys
nav: Providers
network: true
overview: Amedisys publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Home Health, Hospice, and Healthcare.
plans:
- name: Amedisys Plans Pricing
  plan_count: 1
  slug: amedisys-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 1
  name: Amedisys Rate Limits
  slug: amedisys-rate-limits
score:
  band: minimal
  composite: 14.9
  delta: -0.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.3
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amedisys/refs/heads/main/screenshots/amedisys-2026-06-20T171900.png
security:
- kind: domain-security
  name: Amedisys Domain Security
  slug: amedisys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amedisys
tags:
- Home Health
- Hospice
- Healthcare
website: https://www.amedisys.com
---
