---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://geo.api.gouv.fr/adresse'', ''status'': 301, ''note'': ''declared website redirects to https://adresse.data.gouv.fr/outils/api-doc/adresse — a different registrable domain (api.gouv.fr -> data.gouv.fr), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- description: Address search via the French Government
  name: French Address Search
  slug: french-address-search
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/french-address-search-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geo.api.gouv.fr/adresse
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://ghost.adresse.data.gouv.fr/rss/
created: '2026-05-28'
description: Address search via the French Government
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/french-address-search.png
layout: provider
modified: '2026-05-28'
name: French Address Search
nav: Providers
network: true
overview: 'French Address Search publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.


  French Address Search''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 6.5
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
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/french-address-search/refs/heads/main/screenshots/french-address-search-2026-06-20T181536.png
security:
- kind: domain-security
  name: French Address Search Domain Security
  slug: french-address-search-domain-security
  summary_line: TLSv1.3 · DMARC
slug: french-address-search
tags:
- Open Data
- Public APIs
website: https://geo.api.gouv.fr/adresse
---
