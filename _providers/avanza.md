---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/avanza/well-known/avanza-avanza-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avanza-avanza-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.avanza.se/sakerhet-villkor/sakerhet.html
- group: auth
  href: https://artifacts.apis.io/avanza/well-known/avanza-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avanza-security.txt
- group: agent
  href: https://artifacts.apis.io/avanza/well-known/avanza-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avanza-well-known.yml
- group: other
  href: https://artifacts.apis.io/avanza/hosts/avanza-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avanza-hosts.yml
- group: auth
  href: https://artifacts.apis.io/avanza/security/avanza-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avanza-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/avanza/security/avanza-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avanza-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avanza.se/
coverage:
  checked: '2026-10-15'
  detail: Avanza provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://avanza.se/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Avanza is a Swedish online stock broker and financial services platform offering trading, savings, and investment products to private investors. The company provides a modern web and mobile experience, extensive market data, and a range of APIs for account information, trading, and portfolio management. Avanza aims to democratize investing with low fees and user-friendly tools, serving millions of customers across Sweden.
image: https://cdn.avanza.se/frontend/resources/images/open-graph-default-logo.png
layout: provider
modified: '2026-10-14'
name: Avanza
nav: Providers
network: true
overview: Avanza is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Brokerage, Investment, and Sweden.
random_paper: 17
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 3.9
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 11.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/avanza/avanza-2026-11-03T121420.png
security:
- kind: domain-security
  name: Avanza Domain Security
  slug: avanza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avanza Vulnerability Disclosure
  slug: avanza-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: avanza
tags:
- Finance
- Brokerage
- Investment
- Sweden
website: https://avanza.se/
---
