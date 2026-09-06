---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.3
  scored_at: '2026-09-05'
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
overview: 'Shipyard Software publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeFi, DEX, Decentralized Exchange, and Cryptocurrency.


  Shipyard Software''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 33.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shipyard-software/refs/heads/main/screenshots/shipyard-software-2026-09-02T155237.png
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
- DeFi
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
