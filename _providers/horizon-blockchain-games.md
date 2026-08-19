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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 302
  human_in_the_loop: 1
  name: Horizon Blockchain Games Agentic Access
  operation_count: 302
  slug: horizon-blockchain-games-agentic-access
  summary_line: 302 operations · 302 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: The Analytics API from Horizon Blockchain Games — 177 operation(s) for analytics.
  name: Horizon Blockchain Games Analytics API
  slug: horizon-blockchain-games-analytics-api
- description: The Marketplace API from Horizon Blockchain Games — 34 operation(s) for marketplace.
  name: Horizon Blockchain Games Marketplace API
  slug: horizon-blockchain-games-marketplace-api
- description: Endpoints accessible by passing your project-access-key in the header. This is injected whenever you login automatically.
  name: Horizon Blockchain Games public API
  slug: horizon-blockchain-games-public-api
- description: The Rpc API from Horizon Blockchain Games — 32 operation(s) for rpc.
  name: Horizon Blockchain Games Rpc API
  slug: horizon-blockchain-games-rpc-api
- description: Endpoints that require a Sequence service token intended to be secret. You can manually generate one on Sequence Builder and pass it as a Bearer Token.
  name: Horizon Blockchain Games secret API
  slug: horizon-blockchain-games-secret-api
artifact_total: 16
asyncapis:
- description: ''
  name: Horizon Blockchain Games Webhooks
  slug: horizon-blockchain-games-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Api Analytics API
  slug: open-horizon-blockchain-games-analytics-api
- collection_type: open
  name: Api Analytics Marketplace API
  slug: open-horizon-blockchain-games-marketplace-api
- collection_type: open
  name: Api Analytics public API
  slug: open-horizon-blockchain-games-public-api
- collection_type: open
  name: Api Analytics Rpc API
  slug: open-horizon-blockchain-games-rpc-api
- collection_type: open
  name: Api Analytics secret API
  slug: open-horizon-blockchain-games-secret-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/horizon-blockchain-games-analytics-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://horizongames.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sequence.build
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sequence.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sequence.xyz/api-references/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sequence.xyz/solutions/builder/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.sequence.xyz/en/
- group: company
  title: ''
  type: Blog
  url: https://sequence.xyz/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0xsequence
- group: commercial
  title: ''
  type: Pricing
  url: https://sequence.xyz/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sequence.build
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sequence.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sequence.xyz/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sequence.info
- group: auth
  title: ''
  type: Authentication
  url: authentication/horizon-blockchain-games-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/horizon-blockchain-games-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/horizon-blockchain-games-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/horizon-blockchain-games-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/horizon-blockchain-games-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/horizon-blockchain-games-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/horizon-blockchain-games-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/horizon-blockchain-games-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/horizon-blockchain-games-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/horizon-blockchain-games-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/horizon-blockchain-games-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/horizon-blockchain-games-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/horizon-blockchain-games-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/horizon-blockchain-games-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/horizon-blockchain-games-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/horizon-blockchain-games-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/horizon-blockchain-games-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Horizon Blockchain Games is the web3 gaming studio and infrastructure company behind Skyweaver and the Sequence platform (sequence.xyz / 0xsequence) — a modular, open-source web3 development stack for onchain apps, DeFi, stablecoins, and games. Sequence unifies smart-contract wallets, embedded Wallet-as-a-Service, 1-click cross-chain payments, an NFT marketplace, a multi-chain indexer, token metadata, a transaction relayer with gas sponsorship, a node gateway, analytics, and SDKs for Web, Unity, Unreal, React Native, and Go. Its APIs are webrpc JSON-RPC-over-HTTP services spanning 40+ EVM chains, authenticated with project access keys. Sequence was acquired by Polygon Labs. This profile was enriched by the API Evangelist pipeline from Sequence's public developer surface.
image: https://sequence.xyz/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: horizon-blockchain-games-mcp.yml
  slug: horizon-blockchain-games-mcpyml
modified: '2026-07-19'
name: Horizon Blockchain Games
nav: Providers
network: true
overview: 'Horizon Blockchain Games publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Marketplace API, public API, and 2 more. Tagged areas include Company, Consumer, Blockchain, Web3, and Gaming.


  The Horizon Blockchain Games catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Horizon Blockchain Games'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 46
score:
  band: developing
  composite: 48.4
  delta: -2.7
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 16.7
    contract_quality: 55.1
    developer_ergonomics: 63.7
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 34.2
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/horizon-blockchain-games/refs/heads/main/screenshots/horizon-blockchain-games-2026-07-25T221424.png
security:
- kind: authentication
  name: Horizon Blockchain Games Authentication
  slug: horizon-blockchain-games-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Horizon Blockchain Games Domain Security
  slug: horizon-blockchain-games-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: horizon-blockchain-games
tags:
- Company
- Consumer
- Blockchain
- Web3
- Gaming
- NFT
- Wallet
- Cryptocurrency
- Smart Contracts
- Marketplace
- Developer Tools
- Ethereum
website: https://horizongames.net/
---
