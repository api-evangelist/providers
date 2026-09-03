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
  scored_at: '2026-09-02'
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
random_paper: 16
rate_limits:
- limit_count: 1
  name: Shipengine Rate Limits
  slug: shipengine-rate-limits
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 86.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 4.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
