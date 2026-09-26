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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/robinhood/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/quantopian/refs/heads/main/packages/quantopian-packages.yml
  title: ''
  type: Packages
  url: packages/quantopian-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quantopian
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quantopian/refs/heads/main/security/quantopian-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quantopian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quantopian.com/
created: '2026-07-17'
description: Quantopian was a Boston-based crowd-sourced quantitative investment firm and algorithmic-trading platform (backed by a16z and Bessemer Venture Partners) where members wrote, backtested, and shared Python trading algorithms against historical market data. The company ceased operations in November 2020 and its intellectual property was acquired by Robinhood; its public developer platform and hosted API are retired. Its widely-used open-source Python libraries - Zipline (backtesting), Pyfolio, Alphalens, Empyrical, and trading-calendars - remain published on PyPI and its GitHub organization stays live.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quantopian.png
layout: provider
modified: '2026-09-16'
name: Quantopian
nav: Providers
network: true
overview: Quantopian is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Algorithmic Trading, Quantitative Finance, Fintech, and Backtesting.
random_paper: 10
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
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
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
security:
- kind: domain-security
  name: Quantopian Domain Security
  slug: quantopian-domain-security
  summary_line: DNSSEC · DMARC
slug: quantopian
tags:
- Company
- Algorithmic Trading
- Quantitative Finance
- Fintech
- Backtesting
- Open Source
- Python
- Investing
- Defunct
website: https://www.quantopian.com/
---
