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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Programmatic access to LF Energy project resources, grid data APIs, and energy sector tools.
  name: LF Energy API
  slug: lf-energy-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lf-energy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lf-energy-foundation
- group: docs
  title: ''
  type: Documentation
  url: https://lfenergy.org/projects/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/lf-energy
- group: other
  title: ''
  type: Projects
  url: https://lfenergy.org/projects/
- group: other
  title: ''
  type: Landscape
  url: https://landscape.lfenergy.org/
- group: company
  title: ''
  type: Blog
  url: https://lfenergy.org/feed/
created: '2026-03-16'
description: LF Energy is a Linux Foundation project building open source technology solutions for the power grid and energy sector. Launched in 2018, it accelerates the energy transition through open source collaboration and hosts projects for grid modernization, flexibility, and decarbonization.
finops:
- name: Lf Energy Finops
  service_category: API
  slug: lf-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lf-energy.png
layout: provider
modified: '2026-04-28'
name: LF Energy
nav: Providers
network: true
overview: 'LF Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Linux Foundation, Power Grid, and Sustainability.


  LF Energy''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Lf Energy Plans Pricing
  plan_count: 3
  slug: lf-energy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Lf Energy Rate Limits
  slug: lf-energy-rate-limits
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lf-energy/refs/heads/main/screenshots/lf-energy-2026-06-20T184453.png
security:
- kind: domain-security
  name: Lf Energy Domain Security
  slug: lf-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lf-energy
tags:
- Energy
- Linux Foundation
- Power Grid
- Sustainability
---
