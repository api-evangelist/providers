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
- description: Public API not publicly documented; no machine‑readable contract discovered.
  name: Bourse Direct API
  slug: bourse-direct-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/boursedirect/hosts/boursedirect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boursedirect-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.boursedirect.fr/fr/support
- group: start
  title: ''
  type: Login
  url: https://www.boursedirect.fr/fr/login
- group: auth
  href: https://artifacts.apis.io/boursedirect/security/boursedirect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boursedirect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boursedirect.fr
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found after probing known hosts and documentation pages.
  evidence:
  - status: 404
    url: https://api.boursedirect.fr/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bourse Direct is a French online brokerage offering trading services for stocks, ETFs, options, futures, and cryptocurrencies. It provides a web platform for investors to manage accounts, access real‑time market data, view research, and execute trades across multiple markets including Euronext Paris, NYSE, and Nasdaq. The site includes pricing information, support resources, and regulatory disclosures, reflecting its role as a retail investment service in France.
image: https://www.boursedirect.fr/media/cms/corporate/images/logo-bourse-direct.jpeg
layout: provider
modified: '2026-11-02'
name: Bourse Direct
nav: Providers
network: true
overview: 'Bourse Direct is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Brokerage, Trading, and France.


  Bourse Direct''s developer surface includes support and 4 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boursedirect Domain Security
  slug: boursedirect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boursedirect
tags:
- Company
- Finance
- Brokerage
- Trading
- France
website: https://www.boursedirect.fr
---
