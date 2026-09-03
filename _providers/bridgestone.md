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
  url: security/bridgestone-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bridgestone
- group: company
  title: ''
  type: Website
  url: https://www.bridgestone.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/bridgestone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bridgestone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bridgestone-finops.yml
created: '2026-05-06'
description: Bridgestone Corporation is a Japanese global tire and rubber manufacturer headquartered in Tokyo. Bridgestone produces tires for passenger, commercial, off-road, and aircraft applications, plus diversified rubber and chemical products, and is one of the largest tire makers in the world.
finops:
- name: Bridgestone Finops
  service_category: Industrial / Tires
  slug: bridgestone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bridgestone.png
layout: provider
modified: '2026-05-06'
name: Bridgestone
nav: Providers
network: true
overview: Bridgestone is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Tires, Rubber, Automotive, and OEM Supplier.
plans:
- name: Bridgestone Plans Pricing
  plan_count: 1
  slug: bridgestone-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Bridgestone Rate Limits
  slug: bridgestone-rate-limits
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 12.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bridgestone/refs/heads/main/screenshots/bridgestone-2026-06-20T173655.png
security:
- kind: domain-security
  name: Bridgestone Domain Security
  slug: bridgestone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bridgestone
tags:
- Tires
- Rubber
- Automotive
- OEM Supplier
website: https://www.bridgestone.com/
---
