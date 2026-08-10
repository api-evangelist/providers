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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Bridge Agentic Access
  operation_count: 128
  slug: bridge-agentic-access
  summary_line: 128 operations · 57 acting
api_count: 24
apis:
- description: The API Keys API from Bridge — 2 operation(s) for api keys.
  name: Bridge API Keys API
  slug: bridge-api-keys-api
- description: The Associated Persons API from Bridge — 1 operation(s) for associated persons.
  name: Bridge Associated Persons API
  slug: bridge-associated-persons-api
- description: The Batch Settlements API from Bridge — 1 operation(s) for batch settlements.
  name: Bridge Batch Settlements API
  slug: bridge-batch-settlements-api
- description: The Bridge Wallets API from Bridge — 6 operation(s) for bridge wallets.
  name: Bridge Bridge Wallets API
  slug: bridge-bridge-wallets-api
- description: The Cards API from Bridge — 18 operation(s) for cards.
  name: Bridge Cards API
  slug: bridge-cards-api
- description: The Crypto Return Policies API from Bridge — 2 operation(s) for crypto return policies.
  name: Bridge Crypto Return Policies API
  slug: bridge-crypto-return-policies-api
- description: The Customers API from Bridge — 9 operation(s) for customers.
  name: Bridge Customers API
  slug: bridge-customers-api
- description: The Developers API from Bridge — 2 operation(s) for developers.
  name: Bridge Developers API
  slug: bridge-developers-api
- description: The Exchange Rates API from Bridge — 1 operation(s) for exchange rates.
  name: Bridge Exchange Rates API
  slug: bridge-exchange-rates-api
- description: The External Accounts API from Bridge — 6 operation(s) for external accounts.
  name: Bridge External Accounts API
  slug: bridge-external-accounts-api
- description: The Fiat Payout Configuration API from Bridge — 1 operation(s) for fiat payout configuration.
  name: Bridge Fiat Payout Configuration API
  slug: bridge-fiat-payout-configuration-api
- description: The Funds Requests API from Bridge — 1 operation(s) for funds requests.
  name: Bridge Funds Requests API
  slug: bridge-funds-requests-api
- description: The KYC Links API from Bridge — 2 operation(s) for kyc links.
  name: Bridge KYC Links API
  slug: bridge-kyc-links-api
- description: The Liquidation Addresses API from Bridge — 8 operation(s) for liquidation addresses.
  name: Bridge Liquidation Addresses API
  slug: bridge-liquidation-addresses-api
- description: The Lists API from Bridge — 2 operation(s) for lists.
  name: Bridge Lists API
  slug: bridge-lists-api
- description: The Plaid API from Bridge — 2 operation(s) for plaid.
  name: Bridge Plaid API
  slug: bridge-plaid-api
- description: The Prefunded Accounts API from Bridge — 3 operation(s) for prefunded accounts.
  name: Bridge Prefunded Accounts API
  slug: bridge-prefunded-accounts-api
- description: The Rewards API from Bridge — 4 operation(s) for rewards.
  name: Bridge Rewards API
  slug: bridge-rewards-api
- description: The Sandbox API from Bridge — 1 operation(s) for sandbox.
  name: Bridge Sandbox API
  slug: bridge-sandbox-api
- description: The Static Memos API from Bridge — 5 operation(s) for static memos.
  name: Bridge Static Memos API
  slug: bridge-static-memos-api
- description: The Transfers API from Bridge — 5 operation(s) for transfers.
  name: Bridge Transfers API
  slug: bridge-transfers-api
- description: The Travel Rule API from Bridge — 1 operation(s) for travel rule.
  name: Bridge Travel Rule API
  slug: bridge-travel-rule-api
- description: The Virtual Accounts API from Bridge — 7 operation(s) for virtual accounts.
  name: Bridge Virtual Accounts API
  slug: bridge-virtual-accounts-api
- description: The Webhooks API from Bridge — 6 operation(s) for webhooks.
  name: Bridge Webhooks API
  slug: bridge-webhooks-api
artifact_total: 30
asyncapis:
- description: ''
  name: Bridge Webhooks
  slug: bridge-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.bridge.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.bridge.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.bridge.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.bridge.xyz/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.bridge.xyz/get-started/introduction/quick-start/get-set-up-with-bridge
- group: company
  title: ''
  type: Blog
  url: https://www.bridge.xyz/blog
- group: operate
  title: ''
  type: Support
  url: https://apidocs.bridge.xyz/
- group: start
  title: ''
  type: Login
  url: https://dashboard.bridge.xyz/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bridge.xyz/legal/overview
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bridge.xyz/legal/eea-privacy-policy/this-document
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.bridge.xyz/changelog
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/bridge-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/bridge-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bridge-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bridge-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bridge-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bridge-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bridge-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bridge-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bridge-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bridge-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bridge-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bridge-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bridge-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bridge-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bridge-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bridge-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bridge-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bridge-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bridge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bridge-domain-security.yml
created: '2026-07-17'
description: 'Bridge is stablecoin payment and money-movement infrastructure for developers. Its composable REST APIs let businesses accept, hold, convert, and pay out stablecoins and fiat through a single integration: onboard customers with KYC/KYB, issue USD/EUR/MXN virtual accounts, orchestrate cross-chain and cross-border transfers, custody balances in Bridge Wallets, convert between stablecoins, issue stablecoin-backed cards (via Stripe Issuing), and issue your own stablecoin. The Bridge API is versioned at /v0, authenticated with a scoped Api-Key header, and supports idempotent writes plus a webhook event surface. Bridge was acquired by Stripe. Backed by Ribbit Capital.'
image: https://www.bridge.xyz/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: bridge-mcp.yml
  slug: bridge-mcpyml
modified: '2026-07-18'
name: Bridge
nav: Providers
network: true
overview: 'Bridge publishes 24 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Associated Persons API, Batch Settlements API, and 21 more. Tagged areas include Company, Crypto, Stablecoins, Payments, and Money Movement.


  The Bridge catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bridge''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 25 more developer resources.'
random_paper: 41
scopes:
- name: Bridge Scopes
  scope_count: 0
  slug: bridge-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 67.4
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bridge/refs/heads/main/screenshots/bridge-2026-07-25T203806.png
security:
- kind: authentication
  name: Bridge Authentication
  slug: bridge-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bridge Domain Security
  slug: bridge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bridge
tags:
- Company
- Crypto
- Stablecoins
- Payments
- Money Movement
- Cross-Border Payments
- Virtual Accounts
- Wallets
- Cards
- Fintech
website: https://www.bridge.xyz
---
