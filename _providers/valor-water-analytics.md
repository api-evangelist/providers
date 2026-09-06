---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://valorwater.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.xylem.com:443/en-us/brand/xylem-vue/ — a different registrable domain (valorwater.com -> xylem.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/valor-water-analytics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valor-water-analytics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://valorwater.com
created: '2026-07-17'
description: Valor Water Analytics was a San Francisco-based water analytics company that built financial data and dashboard tools for water utilities, including leak and revenue-loss detection. A Y Combinator, Imagine H2O, and 500 Global portfolio company, it was acquired by Xylem Inc. (completed February 2, 2018) and folded into Xylem's digital portfolio, now represented by the Xylem Vue platform. valorwater.com redirects to Xylem Vue, and no independent API surface remains published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/valor-water-analytics.png
layout: provider
modified: '2026-07-21'
name: Valor Water Analytics
nav: Providers
network: true
overview: Valor Water Analytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Water, Analytics, Utilities, and Data.
random_paper: 11
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 4
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 4.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valor-water-analytics/refs/heads/main/screenshots/valor-water-analytics-2026-09-02T165332.png
security:
- kind: domain-security
  name: Valor Water Analytics Domain Security
  slug: valor-water-analytics-domain-security
  summary_line: TLSv1.2 · DMARC
slug: valor-water-analytics
tags:
- Company
- Water
- Analytics
- Utilities
- Data
- Acquired
website: https://valorwater.com
---
