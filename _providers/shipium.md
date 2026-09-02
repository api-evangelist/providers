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
  scored_at: '2026-09-01'
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
random_paper: 11
rate_limits:
- limit_count: 1
  name: Shipium Rate Limits
  slug: shipium-rate-limits
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 86.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
