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
- group: company
  title: ''
  type: Website
  url: https://tradevela.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tradevela
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vela-fka-sr-labs/refs/heads/main/packages/vela-fka-sr-labs-packages.yml
  title: ''
  type: Packages
  url: packages/vela-fka-sr-labs-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vela-fka-sr-labs/refs/heads/main/llms/vela-fka-sr-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vela-fka-sr-labs-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vela-fka-sr-labs/refs/heads/main/security/vela-fka-sr-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vela-fka-sr-labs-domain-security.yml
created: '2026-07-17'
description: Vela Trading Technologies (formerly SR Labs) was a New York-based provider of low-latency market data feed handlers, execution gateways, and multi-asset trading platforms (SuperFeed, Metro, DMA Platform) for capital markets, surfaced here as an Insight Partners portfolio company. Vela merged into Exegy in May 2021 and no longer operates independently - tradevela.com is offline (HTTPS refused at probe time) while its DNS now points at Exegy mail infrastructure. Vela published no self-serve public HTTP API; SuperFeed was delivered via the open-source OpenMAMA API (C++/C#/Java) with an OpenMAMA Developer Program, and its 2017 OptionsCity acquisition exposed the now-decommissioned City Trader REST API, for which a first-party Python client survives on the legacy GitHub org. See the exegy profile for the successor company's current surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vela-fka-sr-labs.png
layout: provider
modified: '2026-07-21'
name: Vela (FKA SR Labs)
nav: Providers
network: true
overview: Vela (FKA SR Labs) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Market Data, Trading, and Low Latency.
random_paper: 16
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 4
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
  name: Vela Fka Sr Labs Domain Security
  slug: vela-fka-sr-labs-domain-security
  summary_line: DMARC
slug: vela-fka-sr-labs
tags:
- Company
- Finance
- Market Data
- Trading
- Low Latency
- Options
- OpenMAMA
- Defunct
website: https://tradevela.com/
---
