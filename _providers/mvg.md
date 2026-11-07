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
api_count: 1
apis:
- description: Public transit information API for Munich (MVG).
  name: MVG API
  slug: mvg-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/mvg/security/mvg-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mvg-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mvg/well-known/mvg-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mvg-security.txt
- group: auth
  href: https://artifacts.apis.io/mvg/well-known/mvg-mvg-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mvg-mvg-security.txt
- group: agent
  href: https://artifacts.apis.io/mvg/well-known/mvg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mvg-well-known.yml
- group: other
  href: https://artifacts.apis.io/mvg/hosts/mvg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mvg-hosts.yml
- group: build
  href: https://artifacts.apis.io/mvg/packages/mvg-packages.yml
  title: ''
  type: SDKs
  url: packages/mvg-packages.yml
- group: build
  href: https://artifacts.apis.io/mvg/packages/mvg-packages.yml
  title: ''
  type: Packages
  url: packages/mvg-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.mvg.de/news/gopc.html
- group: auth
  href: https://artifacts.apis.io/mvg/security/mvg-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mvg-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mvg/security/mvg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mvg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mvg.de/
created: '2026-10-28'
description: MVG (Münchner Verkehrsgesellschaft) operates public transportation in Munich, Germany, providing U‑Bahn, bus, and tram services. It offers ticketing options such as MVV tickets, subscriptions, and the Deutschlandticket, along with real‑time news and the MVGO app for journey planning and mobility solutions across the city.
image: https://www.mvg.de/.imaging/wig/wastl/ogImage/dam/mvg/start/startseite/herobilder/u-bahn-innsbruckerring-neu0.jpg0/jcr:content/Weichenerneuerung-Herobild.webp
layout: provider
modified: '2026-10-28'
name: MVG (Munich transit)
nav: Providers
network: true
overview: MVG (Munich transit) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transportation, Public Transit, Munich, and Germany.
random_paper: 18
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 8.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mvg/mvg-2026-11-03T135926.png
security:
- kind: domain-security
  name: Mvg Domain Security
  slug: mvg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mvg Vulnerability Disclosure
  slug: mvg-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mvg
tags:
- Company
- Transportation
- Public Transit
- Munich
- Germany
website: https://mvg.de/
---
