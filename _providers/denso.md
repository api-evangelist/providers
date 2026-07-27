---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/denso-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/denso
- group: company
  title: ''
  type: Website
  url: https://www.denso.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/denso-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/denso-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/denso-finops.yml
created: '2026-05-06'
description: Denso Corporation is a Japanese global Tier 1 automotive components manufacturer headquartered in Kariya, Aichi. Denso designs and supplies thermal, powertrain, mobility electronics, and electrification systems to global automakers.
finops:
- name: Denso Finops
  service_category: Industrial / Automotive
  slug: denso-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/denso.png
layout: provider
modified: '2026-05-06'
name: Denso
nav: Providers
network: true
overview: Denso is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Tier 1 Supplier, Components, Thermal Management, and Electrification.
plans:
- name: Denso Plans Pricing
  plan_count: 1
  slug: denso-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 1
  name: Denso Rate Limits
  slug: denso-rate-limits
score:
  band: emerging
  composite: 15.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/denso/refs/heads/main/screenshots/denso-2026-06-20T175916.png
security:
- kind: domain-security
  name: Denso Domain Security
  slug: denso-domain-security
  summary_line: TLSv1.3 · DMARC
slug: denso
tags:
- Automotive
- Tier 1 Supplier
- Components
- Thermal Management
- Electrification
website: https://www.denso.com/
---
