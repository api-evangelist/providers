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
  url: security/mahle-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mahle
- group: company
  title: ''
  type: Website
  url: https://www.mahle.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/mahle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mahle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mahle-finops.yml
created: '2026-05-06'
description: MAHLE is a German global Tier 1 automotive supplier headquartered in Stuttgart. MAHLE designs and manufactures thermal management, electrification, engine systems and components, filtration, and mechatronics for passenger cars, commercial vehicles, and off-highway equipment.
finops:
- name: Mahle Finops
  service_category: Industrial / Automotive
  slug: mahle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mahle.png
layout: provider
modified: '2026-05-06'
name: MAHLE
nav: Providers
network: true
overview: MAHLE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Tier 1 Supplier, Thermal Management, Engine Components, and Filtration.
plans:
- name: Mahle Plans Pricing
  plan_count: 1
  slug: mahle-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 1
  name: Mahle Rate Limits
  slug: mahle-rate-limits
score:
  band: emerging
  composite: 13.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 13.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mahle/refs/heads/main/screenshots/mahle-2026-06-20T184848.png
security:
- kind: domain-security
  name: Mahle Domain Security
  slug: mahle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mahle
tags:
- Automotive
- Tier 1 Supplier
- Thermal Management
- Engine Components
- Filtration
website: https://www.mahle.com/
---
