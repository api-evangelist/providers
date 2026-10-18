---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Office of Fossil Energy and Carbon Management (FECM) conducts research, development, demonstration, and deployment to minimize the environmental and climate impacts of fossil energy production and
  name: Office of Fossil Energy and Carbon Management
  slug: office-of-fossil-energy-and-carbon-management
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/office-of-fossil-energy-and-carbon-management/refs/heads/main/plans/office-of-fossil-energy-and-carbon-management-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/office-of-fossil-energy-and-carbon-management-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/office-of-fossil-energy-and-carbon-management/refs/heads/main/rate-limits/office-of-fossil-energy-and-carbon-management-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/office-of-fossil-energy-and-carbon-management-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/office-of-fossil-energy-and-carbon-management/refs/heads/main/finops/office-of-fossil-energy-and-carbon-management-finops.yml
  title: ''
  type: FinOps
  url: finops/office-of-fossil-energy-and-carbon-management-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.energy.gov/newsroom
- group: company
  title: ''
  type: BlogRSS
  url: https://www.energy.gov/rss/energygov/2193718
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/office-of-fossil-energy-and-carbon-management/refs/heads/main/security/office-of-fossil-energy-and-carbon-management-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/office-of-fossil-energy-and-carbon-management-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/fecmgov
created: '2024-12-03'
description: The Office of Fossil Energy and Carbon Management is a division of the U.S. Department of Energy that is focused on addressing the challenges of reducing greenhouse gas emissions and advancing clean energy technologies. The office works to develop and deploy technologies that can capture, store, and utilize carbon dioxide emissions from fossil fuel sources, such as coal and natural gas.
finops:
- has_sources: false
  method: generated
  name: Office Of Fossil Energy And Carbon Management Finops
  primary_unit: ''
  service_category: API
  slug: office-of-fossil-energy-and-carbon-management-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/office-of-fossil-energy-and-carbon-management.png
layout: provider
modified: '2026-10-06'
name: Office of Fossil Energy and Carbon Management
nav: Providers
network: true
overview: 'Office of Fossil Energy and Carbon Management is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government.


  Office of Fossil Energy and Carbon Management''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Office Of Fossil Energy And Carbon Management Plans Pricing
  plan_count: 3
  slug: office-of-fossil-energy-and-carbon-management-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Office Of Fossil Energy And Carbon Management Rate Limits
  slug: office-of-fossil-energy-and-carbon-management-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/office-of-fossil-energy-and-carbon-management/refs/heads/main/screenshots/office-of-fossil-energy-and-carbon-management-2026-06-20T190634.png
security:
- kind: domain-security
  name: Office Of Fossil Energy And Carbon Management Domain Security
  slug: office-of-fossil-energy-and-carbon-management-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: office-of-fossil-energy-and-carbon-management
tags:
- Federal Government
---
