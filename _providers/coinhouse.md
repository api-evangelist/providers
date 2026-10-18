---
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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinhouse/refs/heads/main/hosts/coinhouse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinhouse-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinhouse/refs/heads/main/vendors/coinhouse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinhouse-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.coinhouse.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coinhouse.com/price-solana
- group: company
  title: ''
  type: Newsroom
  url: https://www.coinhouse.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.coinhouse.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinhouse/refs/heads/main/security/coinhouse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinhouse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coinhouse.com/
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found on any discovered host.
  evidence:
  - status: 403
    url: https://api.coinhouse.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Coinhouse is a French cryptocurrency brokerage and investment platform offering buying, selling, and staking of major digital assets such as Bitcoin, Ethereum, and Solana. Founded in 2014, it provides services for private individuals, corporate clients, and wealth advisors, featuring automated recurring purchases (DCA), crypto staking rewards, and a dedicated app. The company emphasizes security, regulatory compliance, and educational resources through its Academy and blog, positioning itself as a trusted gateway to the crypto market for European customers.
layout: provider
modified: '2026-10-09'
name: Coinhouse
nav: Providers
network: true
overview: 'Coinhouse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Brokerage, Finance, Europe, and Investment.


  Coinhouse''s developer surface includes support, pricing, engineering blog, and 5 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coinhouse Domain Security
  slug: coinhouse-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: coinhouse
tags:
- Cryptocurrency
- Brokerage
- Finance
- Europe
- Investment
website: https://www.coinhouse.com/
---
