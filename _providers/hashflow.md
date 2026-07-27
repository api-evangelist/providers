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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 33.7
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: 'REST API for takers/aggregators: discover market makers, query indicative price levels, request signed executable RFQ quotes, and check trader rate-limit restrictions. Quotes settle on-chain via Hashf'
  name: Hashflow Taker API v3
  slug: hashflow-taker-api-v3
- description: 'REST API for market makers: publish price levels, receive RFQs, sign quotes, and manage restrictions on the Hashflow exchange.'
  name: Hashflow Market Maker API v3
  slug: hashflow-market-maker-api-v3
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.hashflow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hashflow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hashflow.com/hashflow
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hashflow.com/hashflow/taker/getting-started-api-v3
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hashflow.com/hashflow/taker/getting-started-api-v3
- group: company
  title: ''
  type: Blog
  url: https://blog.hashflow.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashflownetwork
- group: start
  title: ''
  type: SignUp
  url: https://app.hashflow.com/
- group: operate
  title: ''
  type: Support
  url: https://hashflow.com/discord
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.hashflow.com/hashflow/hashflow/protocol-fees-and-revenue-share
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hashflow-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/hashflow-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hashflow-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hashflow-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hashflow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hashflow-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hashflow-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hashflow-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hashflow-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hashflow-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hashflow-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hashflow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://immunefi.com/bounty/hashflow/
created: '2026-07-17'
description: Hashflow is a decentralized exchange (DEX) and the leading request-for-quote (RFQ) trading platform in crypto. Instead of an automated market maker (AMM) pricing curve, Hashflow brokers signed, off-chain-priced quotes from a network of professional market makers, giving traders zero-slippage, MEV-protected swaps across EVM chains and Solana, including cross-chain trades. Market makers publish price levels and respond to RFQs with EIP-712 signed quotes that settle on-chain via the HashflowRouter contract. Developers integrate through the Taker API v3 (market-makers, price-levels, rfq, and restrictions endpoints) and market-maker tooling, with first-party JavaScript and Python SDKs.
image: https://www.hashflow.com/logo.png
layout: provider
mcp_servers:
- description: ''
  name: hashflow-mcp.yml
  slug: hashflow-mcpyml
modified: '2026-07-19'
name: Hashflow
nav: Providers
network: true
overview: 'Hashflow publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defi, DEX, RFQ, and Trading.


  Hashflow''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, pricing, and 17 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 33.7
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 33.7
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hashflow/refs/heads/main/screenshots/hashflow-2026-07-25T220747.png
security:
- kind: authentication
  name: Hashflow Authentication
  slug: hashflow-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hashflow Domain Security
  slug: hashflow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hashflow Vulnerability Disclosure
  slug: hashflow-vulnerability-disclosure
  summary_line: disclosure policy published
slug: hashflow
tags:
- Company
- Defi
- DEX
- RFQ
- Trading
- Crypto
- Market Making
- Cross-Chain
- Blockchain
- Web3
website: https://www.hashflow.com/
---
