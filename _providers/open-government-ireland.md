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
api_count: 1
apis:
- description: Ireland Government Open Data
  name: Open Government, Ireland
  slug: open-government-ireland
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-government-ireland-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.gov.ie/pages/developers
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://data.gov.ie/blog
created: '2026-05-28'
description: Ireland Government Open Data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-government-ireland.png
layout: provider
modified: '2026-05-28'
name: Open Government, Ireland
nav: Providers
network: true
overview: 'Open Government, Ireland publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.


  Open Government, Ireland''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 5.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-government-ireland/refs/heads/main/screenshots/open-government-ireland-2026-06-20T190801.png
security:
- kind: domain-security
  name: Open Government Ireland Domain Security
  slug: open-government-ireland-domain-security
  summary_line: TLSv1.3 · HSTS
slug: open-government-ireland
tags:
- Government
- Public APIs
website: https://data.gov.ie/pages/developers
---
