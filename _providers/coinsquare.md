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
api_count: 1
apis:
- description: Coinsquare provides cryptocurrency trading services. Documentation is limited and no machine-readable contract was found.
  name: Coinsquare API
  slug: coinsquare-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinsquare/refs/heads/main/well-known/coinsquare-coinsquare-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coinsquare-coinsquare-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinsquare/refs/heads/main/well-known/coinsquare-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coinsquare-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coinsquare/refs/heads/main/well-known/coinsquare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinsquare-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinsquare/refs/heads/main/hosts/coinsquare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinsquare-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinsquare/refs/heads/main/vendors/coinsquare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinsquare-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.coinsquare.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://coinsquare.statuspage.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coinsquare.com/en-ca/learn/privacy-coins-how-privacy-coins-could-take-over-the-digital-currency-world
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coinsquare.com/en-ca/learn/prices-fluctuate-as-waltonchain-deletes-tweet-announcing-alibaba-partnership
- group: start
  title: ''
  type: Login
  url: https://app-new.coinsquare.com/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://www.coinsquare.com/fr-ca/blog/guides
- group: company
  title: ''
  type: Blog
  url: https://www.coinsquare.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.coinsquare.com/fr-ca/legal/onboarding-promotion-terms-and-conditions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coinsquare
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinsquare/refs/heads/main/security/coinsquare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinsquare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coinsquare.com/en-ca
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://app-new.coinsquare.com/mcp
  - status: 403
    url: https://status.coinsquare.com/mcp
  - status: 200
    url: https://www.coinsquare.com/en-ca
  - status: 403
    url: https://forgeglobal.com/coinsquare_stock/
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Coinsquare provides a platform for Canadians to buy, sell, and trade Bitcoin, Ethereum, and over 60 other cryptocurrencies. It operates as a CIRO‑registered investment dealer and marketplace member, offering more than 3,000 trading pairs and custodial services with external licensed custodians. The service includes identity verification to meet AML/KYC regulations and offers in‑app support for users.
layout: provider
modified: '2026-10-09'
name: Coinsquare
nav: Providers
network: true
overview: 'Coinsquare is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency Exchange, Trading Platform, Canadian Market, Asset Custody, and Identity Verification.


  Coinsquare''s developer surface includes support, pricing, documentation, engineering blog, getting-started guide, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 9.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coinsquare Domain Security
  slug: coinsquare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coinsquare
tags:
- Cryptocurrency Exchange
- Trading Platform
- Canadian Market
- Asset Custody
- Identity Verification
website: https://www.coinsquare.com/en-ca
---
