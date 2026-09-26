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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/koinex/refs/heads/main/security/koinex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/koinex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://koinex.in/
created: '2026-07-17'
description: 'Koinex was an Indian digital-asset exchange launched in 2017, describing itself as India''s first and largest cryptocurrency exchange with more than one million users. It offered spot trading across multiple crypto assets with INR pairs before regulatory uncertainty around Indian banking access forced it to shut down all services in June 2019, asking users to withdraw their holdings by July 15, 2019. The company is DEFUNCT: koinex.in now serves only a single static wind-down notice directing former users to claim any crypto assets left on the platform through CoinDCX, with which Koinex partnered for the transition. There is no live product, developer portal, documentation, or API surface; the domain''s TLS certificate expired in March 2025 and every path other than the notice returns 403. Retained in the API Evangelist network as a historical record of a shut-down crypto exchange and as a Pantera Capital portfolio lead.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/koinex.png
layout: provider
modified: '2026-07-19'
name: Koinex
nav: Providers
network: true
overview: Koinex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Cryptocurrency Exchange, Digital Assets, and Trading.
random_paper: 16
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  lifecycle: defunct
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/koinex/refs/heads/main/screenshots/koinex-2026-07-25T224111.png
security:
- kind: domain-security
  name: Koinex Domain Security
  slug: koinex-domain-security
  summary_line: no transport/DNS hardening detected
slug: koinex
tags:
- Company
- Crypto
- Cryptocurrency Exchange
- Digital Assets
- Trading
- India
- Fintech
- Defunct
website: https://koinex.in/
---
