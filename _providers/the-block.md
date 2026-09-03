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
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: 'Request-only REST API for searching and retrieving current and historical crypto news coverage from The Block, returned as JSON filtered by keyword, topic, article length, and publication date (up to '
  name: The Block News API
  slug: the-block-news-api
- description: Access to The Block's web3 fundraising and deals database - company and investor profiles and deal-level funding data. Licensed to Block Pro subscribers; no public OpenAPI is published.
  name: The Block Deals / Funding API
  slug: the-block-deals-api
- description: Programmatic access to The Block's library of proprietary blockchain and ecosystem datasets and charts. Licensed to Block Pro subscribers; no public OpenAPI is published.
  name: The Block Ecosystems / Data API
  slug: the-block-ecosystems-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.theblock.co
- group: start
  title: ''
  type: Portal
  url: https://www.theblock.pro/
- group: company
  title: ''
  type: Blog
  url: https://www.theblock.co/latest
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheBlockCrypto
- group: start
  title: ''
  type: SignUp
  url: https://go.theblock.co/pro-demo-request
- group: start
  title: ''
  type: Login
  url: https://www.theblock.pro/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.theblock.co/terms-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.theblock.co/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-block-domain-security.yml
created: '2026-07-17'
description: The Block is a New York-based digital-assets research, analysis, and news brand founded in 2018, covering cryptocurrency, blockchain, and Web3 markets. Its subscription platform, The Block Pro, packages breaking news, in-depth research, proprietary datasets, and venture-funding intelligence for professional investors, funds, and enterprises. The Block Pro also exposes a set of license-gated APIs - a real-time News API (REST, request-only, JSON), a Deals/Funding API, an Ecosystems/Data API, and a WebSocket news stream - available only to organizations holding a Block Pro subscription. The APIs have no public developer portal or OpenAPI definition; access and technical documentation are arranged through The Block's client-services team.
image: https://avatars.githubusercontent.com/u/44381976?v=4
layout: provider
modified: '2026-07-25'
name: The Block
nav: Providers
network: true
overview: 'The Block publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Digital Assets, News, and Market Data.


  The Block''s developer surface includes developer portal, engineering blog, signup flow, and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-block/refs/heads/main/screenshots/the-block-2026-09-02T163324.png
security:
- kind: domain-security
  name: The Block Domain Security
  slug: the-block-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: the-block
tags:
- Company
- Cryptocurrency
- Digital Assets
- News
- Market Data
- Research
- Web3
- Blockchain
- Financial Data
- Media
website: https://www.theblock.co
---
