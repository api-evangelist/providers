---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://highjump.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.infios.com/en — a different registrable domain (highjump.com -> infios.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: company
  title: ''
  type: Website
  url: https://highjump.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/high-jump-software-domain-security.yml
created: '2026-07-17'
description: 'HighJump Software was a Minneapolis-based provider of supply chain execution software, best known for its warehouse management system (WMS) and its extensible, configurable architecture for distribution, direct-store-delivery, and manufacturing operations. The company was acquired by Battery Ventures in 2014, expanded through acquisitions (Accellos, Nexus, TrueCommerce lines), then acquired by Körber in 2017 and folded into Körber Supply Chain Software. As of 2024 the portfolio was rebranded Infios. The standalone HighJump brand is retired: highjump.com now 301-redirects to infios.com, and the company publishes no public developer portal, API documentation, or machine-readable API specification. This profile is retained as a historical / acquired-company record in the API Evangelist network.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/high-jump-software.png
layout: provider
modified: '2026-07-19'
name: High Jump Software
nav: Providers
network: true
overview: High Jump Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Warehouse Management, Logistics, and Transportation Management.
random_paper: 19
score:
  band: minimal
  composite: 5.0
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
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/high-jump-software/refs/heads/main/screenshots/high-jump-software-2026-07-25T221204.png
security:
- kind: domain-security
  name: High Jump Software Domain Security
  slug: high-jump-software-domain-security
  summary_line: TLSv1.3 · DMARC
slug: high-jump-software
tags:
- Company
- Supply Chain
- Warehouse Management
- Logistics
- Transportation Management
- Distribution
- Supply Chain Execution
- Acquired
website: https://highjump.com
---
