---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: Request-for-Quote swap API for the Clipper DEX. Aggregators retrieve pool state (price feeds, k factor), request firm quotes, and sign quotes to obtain the EIP-2098 signature/calldata needed to execut
  name: Clipper RFQ API
  slug: clipper-rfq-api
- description: GraphQL API endpoints hosted on The Graph that index Clipper's smart contracts across Ethereum, Optimism, Polygon, and Arbitrum — pools, swaps, deposits, withdrawals, volume, and fee data for analytic
  name: Clipper Subgraph (GraphQL)
  slug: clipper-subgraph
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipyard-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shipyardsoftware.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clipper.exchange
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clipper.exchange/disclaimers-and-technical/integrating-with-clipper-rfq/api-reference/api-v2/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clipper.exchange/disclaimers-and-technical/integrating-with-clipper-rfq/guides/how-to-use-clipper-rfq-api
- group: company
  title: ''
  type: Blog
  url: https://www.shipyardsoftware.org/journal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shipyard-software
- group: operate
  title: ''
  type: Support
  url: http://discord.clipper.exchange
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.clipper.exchange/disclaimers-and-technical/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.clipper.exchange/disclaimers-and-technical/privacy-policy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/shipyardsw
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shipyard-software-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shipyard-software-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shipyard-software-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shipyard-software-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shipyard-software-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shipyard-software-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shipyard-software-data-model.yml
created: '2026-07-17'
description: Shipyard Software is the DeFi technology company behind Clipper, a decentralized exchange (DEX) designed for retail traders that offers blue-chip token swaps with no impermanent loss for liquidity providers. Founded in 2021 by Mark Lurie and backed by Polychain and others, Shipyard built market-making technology across eight blockchains before being acquired by Sushi Labs in January 2025. Clipper, now governed by AdmiralDAO, exposes a Request-for-Quote (RFQ) swap API for DEX aggregators and a Graph-hosted GraphQL subgraph for querying on-chain pool data.
image: https://cdn.prod.website-files.com/60df16dcc790bfc63d95ec12/61d7236cbf760c5b4af9369f_shipyard-illustrations-social.png
layout: provider
modified: '2026-07-21'
name: Shipyard Software
nav: Providers
network: true
overview: 'Shipyard Software publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defi, DEX, Decentralized Exchange, and Cryptocurrency.


  Shipyard Software''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 108
score:
  band: thin
  composite: 34.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 43.2
    developer_ergonomics: 43.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 34.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Shipyard Software Authentication
  slug: shipyard-software-authentication
  summary_line: apiKey/http-basic · 2 schemes
- kind: domain-security
  name: Shipyard Software Domain Security
  slug: shipyard-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shipyard-software
tags:
- Company
- Defi
- DEX
- Decentralized Exchange
- Cryptocurrency
- Trading
- Blockchain
- Web3
- Liquidity
- RFQ
website: https://www.shipyardsoftware.org
---
