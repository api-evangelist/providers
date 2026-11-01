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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/iexexchange-io/hosts/iexexchange-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iexexchange-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/iexexchange-io/vendors/iexexchange-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iexexchange-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iex.io/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://notifications.iex.io/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iex.io/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iex.io/documents/pricing-tier-aceess-fee-reform
- group: company
  title: ''
  type: Newsroom
  url: https://www.iex.io/news
- group: auth
  href: https://artifacts.apis.io/iexexchange-io/security/iexexchange-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iexexchange-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iexexchange.io
created: '2026-10-22'
description: IEX Group, Inc. operates the IEX Exchange, a U.S. equities market focused on providing fair and transparent trading. The company offers market data, trading venues, and technology solutions for investors and institutions. IEX emphasizes speed bumps to reduce predatory high‑frequency trading, and provides APIs for market data, order routing, and analytics. It is publicly known for its mission to level the playing field for all market participants.
image: https://cdn.prod.website-files.com/63bc910a330e72662c5681bc/640645b90ac2aca1a1409fa6_IEX_Open-Graph.jpg
layout: provider
modified: '2026-10-22'
name: IEX
nav: Providers
network: true
overview: 'IEX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Stock Market, Trading, Market Data, and Technology.


  IEX''s developer surface includes pricing and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Iexexchange Io Domain Security
  slug: iexexchange-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iexexchange-io
tags:
- Finance
- Stock Market
- Trading
- Market Data
- Technology
website: https://www.iexexchange.io
---
