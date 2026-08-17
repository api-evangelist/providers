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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Brl Agentic Access
  operation_count: 65
  slug: brl-agentic-access
  summary_line: 65 operations · 27 acting
api_count: 10
apis:
- description: The Accounts API from BRL — 27 operation(s) for accounts.
  name: BRL Accounts API
  slug: brl-accounts-api
- description: The Assets API from BRL — 4 operation(s) for assets.
  name: BRL Assets API
  slug: brl-assets-api
- description: The Claims API from BRL — 2 operation(s) for claims.
  name: BRL Claims API
  slug: brl-claims-api
- description: The Nft Transfers API from BRL — 1 operation(s) for nft transfers.
  name: BRL Nft Transfers API
  slug: brl-nft-transfers-api
- description: The Orders API from BRL — 2 operation(s) for orders.
  name: BRL Orders API
  slug: brl-orders-api
- description: The Quotes API from BRL — 1 operation(s) for quotes.
  name: BRL Quotes API
  slug: brl-quotes-api
- description: The Tax Exemption API from BRL — 1 operation(s) for tax exemption.
  name: BRL Tax Exemption API
  slug: brl-tax-exemption-api
- description: The Transfers API from BRL — 1 operation(s) for transfers.
  name: BRL Transfers API
  slug: brl-transfers-api
- description: The Wallets API from BRL — 4 operation(s) for wallets.
  name: BRL Wallets API
  slug: brl-wallets-api
- description: The Withdrawals API from BRL — 2 operation(s) for withdrawals.
  name: BRL Withdrawals API
  slug: brl-withdrawals-api
artifact_total: 26
asyncapis:
- description: ''
  name: Brl Webhooks
  slug: brl-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crown API & Webhooks Accounts API
  slug: open-brl-accounts-api
- collection_type: open
  name: Crown API & Webhooks Accounts Assets API
  slug: open-brl-assets-api
- collection_type: open
  name: Crown API & Webhooks Accounts Claims API
  slug: open-brl-claims-api
- collection_type: open
  name: Crown API & Webhooks Accounts Nft Transfers API
  slug: open-brl-nft-transfers-api
- collection_type: open
  name: Crown API & Webhooks Accounts Orders API
  slug: open-brl-orders-api
- collection_type: open
  name: Crown API & Webhooks Accounts Quotes API
  slug: open-brl-quotes-api
- collection_type: open
  name: Crown API & Webhooks Accounts Tax Exemption API
  slug: open-brl-tax-exemption-api
- collection_type: open
  name: Crown API & Webhooks Accounts Transfers API
  slug: open-brl-transfers-api
- collection_type: open
  name: Crown API & Webhooks Accounts Wallets API
  slug: open-brl-wallets-api
- collection_type: open
  name: Crown API & Webhooks Accounts Withdrawals API
  slug: open-brl-withdrawals-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brl-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://brl.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.crown-brlv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crown-brlv.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.crown-brlv.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.crown-brlv.com/guides/api-keys-setup
- group: start
  title: ''
  type: SignUp
  url: https://onboarding.crown-brlv.com/start
- group: start
  title: ''
  type: Login
  url: https://app.crown-brlv.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://d2bv8dtly8iz1m.cloudfront.net/crown/Crown_PT_Termo_de_Privacidade_27a36188f2.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crown-brl/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/brl-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brl-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/brl-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brl-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brl-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brl-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brl-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brl-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brl-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/brl-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brl-agentic-access.yml
created: '2026-07-17'
description: Crown (brl.xyz) is a Brazilian fintech, backed by Paradigm, Coinbase Ventures and Paxos, that issues BRLV — a stablecoin pegged 1:1 to the Brazilian Real and backed by Brazilian federal government bonds held in a bankruptcy-remote structure under temporary authorization from the Banco Central do Brasil. The Crown API lets partners create known-taxpayer accounts and sub-accounts, provision wallets, fund balances via PIX and TED, request quotes and place conversion orders across fiat (BRL/USD) and tokens (BRLV, wBRLY, USDC, USDT on Base and Ethereum mainnet), move tokens on-chain, claim accumulated yield from reward certificates (including recurring auto-claims and NFT reward-certificate transfers), withdraw via PIX/TED or token, track Brazilian monthly tax-exemption progress, and subscribe to webhooks for deposit, order, transfer, withdrawal, claim and sub-account approval events. Authentication pairs an X-API-Key identifier with a short-lived (<50s) self-signed RS256 JWT that
  binds each request's URI, nonce and SHA-256 body hash.
image: https://raw.githubusercontent.com/api-evangelist/brl/refs/heads/main/apis.yml
layout: provider
mcp_servers:
- description: ''
  name: brl-mcp.yml
  slug: brl-mcpyml
modified: '2026-07-18'
name: BRL
nav: Providers
network: true
overview: 'BRL publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Assets API, Claims API, and 7 more. Tagged areas include Company, Crypto, Stablecoin, Payments, and Brazil.


  The BRL catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  BRL''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, and 17 more developer resources.'
random_paper: 22
score:
  band: thin
  composite: 40.1
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 66.1
    developer_ergonomics: 47.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brl/refs/heads/main/screenshots/brl-2026-07-25T203938.png
security:
- kind: authentication
  name: Brl Authentication
  slug: brl-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Brl Domain Security
  slug: brl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brl
tags:
- Company
- Crypto
- Stablecoin
- Payments
- Brazil
- PIX
- Fintech
- Blockchain
- Digital Assets
- Wallets
- Yield
website: https://brl.xyz
---
