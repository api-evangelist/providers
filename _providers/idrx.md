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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Idrx Agentic Access
  operation_count: 13
  slug: idrx-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 2
apis:
- description: Onboard users and manage their bank accounts.
  name: IDRX Onboarding API
  slug: idrx-onboarding-api
- description: Mint, redeem, and bridge IDRX, and query rates/fees/history.
  name: IDRX Transaction API
  slug: idrx-transaction-api
artifact_total: 7
asyncapis:
- description: ''
  name: Idrx Callback Webhooks
  slug: idrx-callback-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.idrx.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.idrx.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.idrx.co/api/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.idrx.co/api/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://app.idrx.co
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.idrx.co/services/fees
- group: operate
  title: ''
  type: Support
  url: mailto:support@idrx.co
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/idrx-co
- group: other
  title: ''
  type: Whitepaper
  url: https://docs.idrx.co/introduction/idrx-whitepaper
- group: auth
  title: ''
  type: Authentication
  url: authentication/idrx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/idrx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/idrx-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/idrx-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/idrx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/idrx-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/idrx-callback-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/idrx-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/idrx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/idrx-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/idrx-llms.txt
created: '2026-07-17'
description: IDRX is a stablecoin pegged 1:1 to the Indonesian Rupiah (IDR), issued by a regulated Indonesian entity and available across multiple EVM chains and Solana. Its REST API lets business (organization) accounts onboard KYC-verified users, register bank accounts, and process mint (fiat IDR -> IDRX / USDT on-chain), redeem (IDRX -> fiat IDR to a bank account), and bridge (cross-chain) transactions, plus query swap rates, fees, supported bank methods, and transaction history. Requests are authenticated with an API key and an HMAC-SHA256 request signature, and settlement is confirmed via single-delivery webhooks or transaction-history polling. IDRX is a portfolio company of a16z (crypto).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/idrx.png
layout: provider
mcp_servers:
- description: ''
  name: idrx-mcp.yml
  slug: idrx-mcpyml
modified: '2026-07-19'
name: IDRX
nav: Providers
network: true
overview: 'IDRX publishes 2 APIs on the [APIs.io](https://apis.io/) network: Onboarding API and Transaction API. Tagged areas include Stablecoin, Cryptocurrency, Payments, Blockchain, and Fintech.


  The IDRX catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  IDRX''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, authentication, and 14 more developer resources.'
random_paper: 31
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 72.6
    developer_ergonomics: 65.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 45.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/idrx/refs/heads/main/screenshots/idrx-2026-07-25T222044.png
security:
- kind: authentication
  name: Idrx Authentication
  slug: idrx-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Idrx Domain Security
  slug: idrx-domain-security
  summary_line: TLSv1.3
slug: idrx
tags:
- Stablecoin
- Cryptocurrency
- Payments
- Blockchain
- Fintech
- Indonesia
- Rupiah
- Web3
- On-Ramp
- Digital Currency
website: https://docs.idrx.co
---
