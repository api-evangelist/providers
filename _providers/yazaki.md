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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yazaki-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yazaki-corporation
- group: company
  title: ''
  type: Website
  url: https://www.yazaki-group.com/global/
- group: commercial
  title: ''
  type: Plans
  url: plans/yazaki-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yazaki-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yazaki-finops.yml
created: '2026-05-06'
description: Yazaki Corporation is a Japanese global Tier 1 automotive supplier headquartered in Tokyo. Yazaki is a leading manufacturer of automotive wiring harnesses, connectors, instrumentation, and electrical distribution systems for global automakers.
finops:
- name: Yazaki Finops
  service_category: Industrial / Automotive
  slug: yazaki-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yazaki.png
layout: provider
modified: '2026-05-06'
name: Yazaki
nav: Providers
network: true
overview: Yazaki is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Tier 1 Supplier, Wiring Harnesses, Connectors, and Instrumentation.
plans:
- name: Yazaki Plans Pricing
  plan_count: 1
  slug: yazaki-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 1
  name: Yazaki Rate Limits
  slug: yazaki-rate-limits
score:
  band: emerging
  composite: 13.5
  delta: -1.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yazaki/refs/heads/main/screenshots/yazaki-2026-06-20T201737.png
security:
- kind: domain-security
  name: Yazaki Domain Security
  slug: yazaki-domain-security
  summary_line: TLSv1.3
slug: yazaki
tags:
- Automotive
- Tier 1 Supplier
- Wiring Harnesses
- Connectors
- Instrumentation
website: https://www.yazaki-group.com/global/
---
