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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hutchinson-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hutchinson
- group: company
  title: ''
  type: Website
  url: https://www.hutchinson.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/hutchinson-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hutchinson-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hutchinson-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hutchinson.com/en/news
created: '2026-05-06'
description: Hutchinson SA is a French global Tier 1 automotive supplier headquartered in Paris, a subsidiary of TotalEnergies. Hutchinson designs and manufactures anti-vibration systems, sealing systems, fluid transfer, precision rubber components, and aerospace systems for the automotive, aerospace, defense, and industrial sectors.
finops:
- name: Hutchinson Finops
  service_category: Industrial / Automotive
  slug: hutchinson-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hutchinson.png
layout: provider
modified: '2026-05-06'
name: Hutchinson
nav: Providers
network: true
overview: 'Hutchinson is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Tier 1 Supplier, Anti-Vibration, Sealing, and Fluid Transfer.


  Hutchinson''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Hutchinson Plans Pricing
  plan_count: 1
  slug: hutchinson-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Hutchinson Rate Limits
  slug: hutchinson-rate-limits
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 14.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hutchinson/refs/heads/main/screenshots/hutchinson-2026-06-20T182959.png
security:
- kind: domain-security
  name: Hutchinson Domain Security
  slug: hutchinson-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hutchinson
tags:
- Automotive
- Tier 1 Supplier
- Anti-Vibration
- Sealing
- Fluid Transfer
- Aerospace
website: https://www.hutchinson.com/
---
