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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipium-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shipium
- group: company
  title: ''
  type: Website
  url: https://www.shipium.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/shipium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shipium-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shipium-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://www.shipium.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.shipium.com/blog
created: '2026-05-08'
description: Shipium is a shipping platform for high-volume e-commerce, optimizing carrier selection, multi-warehouse delivery promises, and parcel routing.
finops:
- name: Shipium Finops
  service_category: Shipping
  slug: shipium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shipium.png
layout: provider
modified: '2026-05-08'
name: Shipium
nav: Providers
network: true
overview: 'Shipium is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Logistics, E-Commerce, Carrier Selection, and Optimization.


  Shipium''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Shipium Plans Pricing
  plan_count: 1
  slug: shipium-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Shipium Rate Limits
  slug: shipium-rate-limits
score:
  band: minimal
  composite: 8.5
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 8.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Shipium Domain Security
  slug: shipium-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shipium
tags:
- Shipping
- Logistics
- E-Commerce
- Carrier Selection
- Optimization
website: https://www.shipium.com/
---
