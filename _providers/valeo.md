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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valeo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/valeoai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/valeo
- group: company
  title: ''
  type: Website
  url: https://www.valeo.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/valeo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/valeo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/valeo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.valeo.com/en/press-releases/
created: '2026-05-06'
description: Valeo is a French global Tier 1 automotive supplier headquartered in Paris. Valeo designs and manufactures comfort and driving assistance, powertrain, thermal, and visibility systems for the automotive industry, with a strong focus on electrification and ADAS.
finops:
- name: Valeo Finops
  service_category: Industrial / Automotive
  slug: valeo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/valeo.png
layout: provider
modified: '2026-05-06'
name: Valeo
nav: Providers
network: true
overview: 'Valeo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Tier 1 Supplier, ADAS, Powertrain, and Thermal.


  Valeo''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Valeo Plans Pricing
  plan_count: 1
  slug: valeo-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Valeo Rate Limits
  slug: valeo-rate-limits
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 14.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valeo/refs/heads/main/screenshots/valeo-2026-06-20T200750.png
security:
- kind: domain-security
  name: Valeo Domain Security
  slug: valeo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: valeo
tags:
- Automotive
- Tier 1 Supplier
- ADAS
- Powertrain
- Thermal
- Visibility
website: https://www.valeo.com/
---
