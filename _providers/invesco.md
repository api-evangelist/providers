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
  url: security/invesco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.invesco.com/
- group: company
  title: ''
  type: Website
  url: https://www.invesco.com/corporate/en/home.html
- group: company
  title: ''
  type: Website
  url: https://www.invesco.com/qqq-etf/en/home.html
- group: company
  title: ''
  type: AboutUs
  url: https://www.invesco.com/us/en/about-us.html
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.invesco.com/corporate/en/investor-relations.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Invesco
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/invesco/
created: '2026-05-23'
description: 'Invesco Ltd. (NYSE: IVZ) is a global independent investment management firm headquartered in Atlanta, Georgia, with approximately $1.95 trillion in assets under management. The firm operates a broad set of ETF, mutual fund, and institutional strategies, anchored by the Invesco QQQ Trust (QQQ) tracking the Nasdaq-100, the Invesco Solar ETF (TAN), and the Invesco BulletShares defined-maturity bond ETF suite. Invesco has recently extended its thematic ETF lineup into AI infrastructure and divested its remaining MassMutual stake. No public developer APIs are documented at this time; fund, ETF, and performance data are distributed through institutional market-data channels (Bloomberg, Refinitiv, NYSE) rather than a developer portal.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/invesco.png
layout: provider
modified: '2026-05-23'
name: Invesco
nav: Providers
network: true
overview: 'Invesco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Investment Management, Asset Management, ETFs, QQQ, and Mutual Funds.


  Invesco''s developer surface includes GitHub presence and 7 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 1.9
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
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 1.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/invesco/refs/heads/main/screenshots/invesco-2026-06-20T183518.png
security:
- kind: domain-security
  name: Invesco Domain Security
  slug: invesco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: invesco
tags:
- Investment Management
- Asset Management
- ETFs
- QQQ
- Mutual Funds
- Financial-Services
- Public Company
website: https://www.invesco.com/
---
