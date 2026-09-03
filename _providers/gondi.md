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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'The off-chain Gondi GraphQL API (api.gondi.xyz/graphql) is the order/offer book and indexing layer behind the Gondi NFT lending protocol. It exposes 76 queries and 48 mutations across 325 types: Sign-'
  name: Gondi GraphQL API
  slug: gondi-graphql
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.gondi.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gondi.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://gondixyz.github.io/gondi-js/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gondi.xyz/learn/how-to-make-a-loan-offer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gondixyz
- group: company
  title: ''
  type: Blog
  url: https://www.gondi.xyz/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/gondi
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.gondi.xyz/gondi-v3/protocol-fees
- group: start
  title: ''
  type: SignUp
  url: https://www.gondi.xyz/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gondi.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gondi.xyz/privacy
- group: docs
  title: ''
  type: GraphQL
  url: graphql/gondi-graphql.md
- group: build
  title: ''
  type: Packages
  url: packages/gondi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gondi-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gondi-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gondi-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gondi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gondi-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gondi-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gondi-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gondi-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gondi-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gondi-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gondi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.gondi.xyz/vulnerability-disclosure
created: '2026-07-17'
description: 'Gondi is a decentralized, non-custodial, peer-to-peer protocol for trading and financing NFTs, deployed on Ethereum mainnet and HypeEVM. NFT owners borrow WETH, HYPE, or USDC against ERC-721 / ERC-1155 collateral with pro-rata interest, no oracles, and no forced liquidations, while lenders compete to refinance loans to better terms (full, tranche, and trim-the-top refinancing). Beyond the on-chain smart contracts, Gondi operates an off-chain GraphQL API at api.gondi.xyz that powers the dApp and the official gondi-js (TypeScript) and Python SDKs: it is the order/offer book and indexer for generating, signing, saving, listing, hiding, and renegotiating loan offers, browsing collections, NFTs, listings, orders, and loans, and managing users, linked wallets, notifications, and API keys. Authentication is Sign-In With Ethereum (EIP-4361) plus programmatic API keys. Gondi is backed by Pantera Capital.'
graphqls:
- description: Gondi is a decentralized, non-custodial, peer-to-peer protocol for trading and financing NFTs,
  name: Gondi GraphQL API
  slug: gondi-graphql
image: https://cdn.gondi.xyz/site/og/og-image-gondi-v4.png
layout: provider
mcp_servers:
- description: ''
  name: Gondi MCP Server
  slug: gondi-mcp-server
modified: '2026-07-19'
name: Gondi
nav: Providers
network: true
overview: 'Gondi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, NFT, DeFi, and Lending.


  Gondi''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 19 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 37.2
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 35.4
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gondi/refs/heads/main/screenshots/gondi-2026-07-25T220037.png
security:
- kind: authentication
  name: Gondi Authentication
  slug: gondi-authentication
  summary_line: siwe/apiKey · 2 schemes
- kind: domain-security
  name: Gondi Domain Security
  slug: gondi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gondi Vulnerability Disclosure
  slug: gondi-vulnerability-disclosure
  summary_line: disclosure policy published
slug: gondi
tags:
- Company
- Crypto
- NFT
- DeFi
- Lending
- NFT Finance
- GraphQL
- Web3
website: https://www.gondi.xyz/
---
