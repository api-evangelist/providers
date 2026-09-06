---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dstzc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dstcar.com
created: '2026-07-17'
description: dstzc (地上铁, DiShangTie Green Technology, Shenzhen) is a leading Chinese provider of digitalized operations-management solutions for new-energy (electric) logistics vehicles. It operates a full-lifecycle fleet platform covering vehicle sales and leasing, digital fleet management, safety and risk management, maintenance, charging and battery-swap services, and residual-value management, reporting 224,000+ operational vehicles across 3,246 service locations spanning all 333 prefecture-level regions of mainland China. It is a portfolio company of Qiming Venture Partners. The company has no public API or developer surface; this profile is maintained as a company lead in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dstzc.png
layout: provider
modified: '2026-07-18'
name: dstzc
nav: Providers
network: true
overview: dstzc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Electric Vehicles, Fleet Management, and New Energy.
random_paper: 6
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dstzc/refs/heads/main/screenshots/dstzc-2026-07-25T212437.png
security:
- kind: domain-security
  name: Dstzc Domain Security
  slug: dstzc-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: dstzc
tags:
- Company
- Logistics
- Electric Vehicles
- Fleet Management
- New Energy
- Transportation
- Mobility
- China
website: https://www.dstcar.com
---
