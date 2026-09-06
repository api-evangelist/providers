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
  url: security/trinkerr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.trinkerr.com
- group: build
  title: ''
  type: Packages
  url: packages/trinkerr-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trinkerr-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trinkerr-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/trinkerr
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@trinkerr
- group: other
  title: ''
  type: MobileApp
  url: https://play.google.com/store/apps/details?id=com.trinkerr.app
created: '2026-07-17'
description: Trinkerr is a Bengaluru, India algorithmic and social trading platform founded in 2021 by Manvendra Singh and Gaurav Agarwal, backed by Accel and India Quotient. Its mobile app (com.trinkerr.app) automates trades with ready-made algos crafted by industry experts for stock market enthusiasts. As of 2026-07-21 the company website trinkerr.com resolves to a GoDaddy parked page, no api/docs/developer subdomains resolve, and no developer portal, API documentation, or public API surface could be found, though the Google Play listing, LinkedIn, and YouTube channel remain live. Trinkerr does not currently publish a public API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trinkerr.png
layout: provider
modified: '2026-07-21'
name: Trinkerr
nav: Providers
network: true
overview: 'Trinkerr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Saas, Trading, Algorithmic Trading, and Fintech.


  Trinkerr''s developer surface includes YouTube channel and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 2.3
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
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 2.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trinkerr/refs/heads/main/screenshots/trinkerr-2026-09-02T164237.png
security:
- kind: domain-security
  name: Trinkerr Domain Security
  slug: trinkerr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trinkerr
tags:
- Company
- Cloud Saas
- Trading
- Algorithmic Trading
- Fintech
- India
- Stock Market
website: https://www.trinkerr.com
---
