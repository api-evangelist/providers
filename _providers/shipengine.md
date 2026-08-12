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
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipengine-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ShipEngine
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shipengine
- group: company
  title: ''
  type: Website
  url: https://www.shipengine.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/shipengine-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shipengine-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shipengine-finops.yml
created: '2026-05-08'
description: ShipEngine (an Auctane / ShipStation company) is a shipping API for rate shopping, label generation, tracking, and address validation across major carriers.
finops:
- name: Shipengine Finops
  service_category: Shipping
  slug: shipengine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shipengine.png
layout: provider
modified: '2026-05-08'
name: ShipEngine
nav: Providers
network: true
overview: ShipEngine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Logistics, Multi-Carrier, Labels, and ShipStation.
plans:
- name: Shipengine Plans Pricing
  plan_count: 1
  slug: shipengine-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Shipengine Rate Limits
  slug: shipengine-rate-limits
score:
  band: minimal
  composite: 8.1
  delta: -5.2
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/shipengine/refs/heads/main/screenshots/shipengine-2026-06-20T193812.png
security:
- kind: domain-security
  name: Shipengine Domain Security
  slug: shipengine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shipengine
tags:
- Shipping
- Logistics
- Multi-Carrier
- Labels
- ShipStation
website: https://www.shipengine.com/
---
