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
api_count: 1
apis:
- description: REST API for String's fiat-for-Web3-gaming platform — quotes and transactions (fiat on/off ramp, NFT purchase, cross-chain), plus management of API keys, contracts, platforms (games), members, organiz
  name: String API
  slug: string-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://string.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.string.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.string.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.string.xyz/reference/get_apikeys
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.string.xyz/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/String-xyz
- group: start
  title: ''
  type: SignUp
  url: https://sandbox.string.xyz/login
- group: start
  title: ''
  type: Sandbox
  url: sandbox/string-technology-inc-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/string-technology-inc-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/string-technology-inc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/string-technology-inc-packages.yml
- group: design
  title: ''
  type: Components
  url: components/string-technology-inc-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/string-technology-inc-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/string-technology-inc-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/string-technology-inc-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/string-technology-inc-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/string-technology-inc-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/string-technology-inc-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/string-technology-inc-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/string-technology-inc-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: String (string.xyz) is a fiat interoperability platform for Web3 gaming, operated by String Technology Inc and backed by 500 Global. String lets game developers accept credit-card and bank payments natively inside their games, acting as the merchant of record and counterparty for fiat on/off ramps, NFT purchases, and cross-chain payments. A player pays fiat on traditional rails and String delivers the digital asset on-chain — either by interacting with the game's smart contract to mint/send an NFT or by sending a token from its treasury to the player's wallet. String ships three integration surfaces — String Checkout (drop-in payment app), a Unity SDK, and String Direct (custom web SDK) — all wrapping a REST API at string-api.xyz that covers API keys, contracts, platforms (games), members, organizations, users (players), saved cards, wallet-signature login, quotes, and transactions.
image: https://avatars.githubusercontent.com/u/104804397?v=4
layout: provider
mcp_servers:
- description: ''
  name: string-technology-inc-mcp.yml
  slug: string-technology-inc-mcpyml
modified: '2026-07-21'
name: String Technology Inc
nav: Providers
network: true
overview: 'String Technology Inc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Web3, Gaming, and Fiat On-Ramp.


  String Technology Inc''s developer surface includes documentation, API reference, getting-started guide, signup flow, sandbox, authentication, and 15 more developer resources.'
random_paper: 43
score:
  band: emerging
  composite: 28.8
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.8
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: String Technology Inc Authentication
  slug: string-technology-inc-authentication
  summary_line: apiKey/walletSignature/session · 4 schemes
- kind: domain-security
  name: String Technology Inc Domain Security
  slug: string-technology-inc-domain-security
  summary_line: TLSv1.3 · HSTS
slug: string-technology-inc
tags:
- Company
- Payments
- Web3
- Gaming
- Fiat On-Ramp
- Cryptocurrency
- NFT
- Merchant of Record
- Developer Tools
website: https://string.xyz
---
