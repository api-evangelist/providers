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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gestamp-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gestamp
- group: company
  title: ''
  type: Website
  url: https://www.gestamp.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/gestamp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gestamp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gestamp-finops.yml
created: '2026-05-06'
description: Gestamp Automocion is a Spanish global Tier 1 automotive supplier headquartered in Madrid. Gestamp designs and manufactures metal components for vehicle bodies, chassis, and mechanisms, with focus on lightweighting and structural safety for global automakers.
finops:
- name: Gestamp Finops
  service_category: Industrial / Automotive
  slug: gestamp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gestamp.png
layout: provider
modified: '2026-05-06'
name: Gestamp
nav: Providers
network: true
overview: Gestamp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Tier 1 Supplier, Metal Stamping, Body, and Chassis.
plans:
- name: Gestamp Plans Pricing
  plan_count: 1
  slug: gestamp-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Gestamp Rate Limits
  slug: gestamp-rate-limits
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 13.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gestamp/refs/heads/main/screenshots/gestamp-2026-06-20T181808.png
security:
- kind: domain-security
  name: Gestamp Domain Security
  slug: gestamp-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: gestamp
tags:
- Automotive
- Tier 1 Supplier
- Metal Stamping
- Body
- Chassis
website: https://www.gestamp.com/
---
