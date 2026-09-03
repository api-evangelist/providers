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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Access-controlled trading API for the Figure Markets exchange (EP3 matching engine on Provenance Blockchain) covering markets, trading, and account operations. Requires authentication; no public OpenA
  name: Figure Markets Exchange API
  slug: figure-markets-exchange-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.figuremarkets.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.figuremarkets.com/c/signup/personal
- group: start
  title: ''
  type: Login
  url: https://www.figuremarkets.com/c/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.figuremarkets.com/exchange/fees/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.figuremarkets.com/disclosures/
- group: company
  title: ''
  type: Blog
  url: https://www.figure.com/blog/tag/crypto/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/figuremarkets
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/figure-markets-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/figure-markets-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/figure-markets-conformance.yml
created: '2026-07-17'
description: Figure Markets is a blockchain-native digital-asset marketplace built on the Provenance Blockchain that lets individuals and institutions trade, borrow against, and earn yield on crypto and real-world assets from a single account. Its exchange runs on Connamara's EP3 matching engine with FIX and REST APIs, offering a central limit order book for crypto (BTC, ETH, and more), equities, bonds, alternative assets, and YLDS, the first SEC-registered yielding stablecoin. Products include Figure Exchange (pro trading), crypto-backed loans, Democratized Prime (HELOC-backed yield), and self-custodied wallets, bridging traditional order-book finance with on-chain clearing and settlement. The company is backed by DCM Ventures. The trading API is served from api.figuremarkets.com and is access-controlled; no public OpenAPI is currently published.
image: https://www.datocms-assets.com/33246/1775661796-markets-logo-512.png
layout: provider
modified: '2026-07-19'
name: Figure Markets
nav: Providers
network: true
overview: 'Figure Markets publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Cryptocurrency, Digital Assets, and Exchange.


  Figure Markets'' developer surface includes signup flow, pricing, engineering blog, and 7 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 16.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/figure-markets/refs/heads/main/screenshots/figure-markets-2026-07-25T214442.png
security:
- kind: domain-security
  name: Figure Markets Domain Security
  slug: figure-markets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: figure-markets
tags:
- Company
- Fintech
- Cryptocurrency
- Digital Assets
- Exchange
- Trading
- Blockchain
- Lending
- Stablecoins
- Provenance Blockchain
website: https://www.figuremarkets.com/
---
