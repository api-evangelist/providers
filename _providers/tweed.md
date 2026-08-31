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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Legacy marketplace/collections API — obtain a JWT with your API key and secret, then manage NFT collections and in-platform tokens for token checkout.
  name: Tweed API (V1)
  slug: tweed-api-v1
- description: The assets API from Tweed — 5 operation(s) for assets.
  name: Tweed assets API
  slug: tweed-assets-api
- description: The audit-event-mappings API from Tweed — 1 operation(s) for audit-event-mappings.
  name: Tweed audit-event-mappings API
  slug: tweed-audit-event-mappings-api
- description: The auth API from Tweed — 3 operation(s) for auth.
  name: Tweed auth API
  slug: tweed-auth-api
- description: The blockchains API from Tweed — 4 operation(s) for blockchains.
  name: Tweed blockchains API
  slug: tweed-blockchains-api
- description: The checkout API from Tweed — 4 operation(s) for checkout.
  name: Tweed checkout API
  slug: tweed-checkout-api
- description: The contracts API from Tweed — 5 operation(s) for contracts.
  name: Tweed contracts API
  slug: tweed-contracts-api
- description: The items API from Tweed — 5 operation(s) for items.
  name: Tweed items API
  slug: tweed-items-api
- description: The payouts API from Tweed — 4 operation(s) for payouts.
  name: Tweed payouts API
  slug: tweed-payouts-api
- description: The platform-webhooks API from Tweed — 3 operation(s) for platform-webhooks.
  name: Tweed platform-webhooks API
  slug: tweed-platform-webhooks-api
- description: The Rate API from Tweed — 1 operation(s) for rate.
  name: Tweed Rate API
  slug: tweed-rate-api
- description: The tickets API from Tweed — 1 operation(s) for tickets.
  name: Tweed tickets API
  slug: tweed-tickets-api
artifact_total: 28
asyncapis:
- description: ''
  name: Tweed Webhooks
  slug: tweed-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tweed assets API
  slug: open-tweed-assets-api
- collection_type: open
  name: Tweed assets audit-event-mappings API
  slug: open-tweed-audit-event-mappings-api
- collection_type: open
  name: Tweed assets auth API
  slug: open-tweed-auth-api
- collection_type: open
  name: Tweed assets blockchains API
  slug: open-tweed-blockchains-api
- collection_type: open
  name: Tweed assets checkout API
  slug: open-tweed-checkout-api
- collection_type: open
  name: Tweed assets contracts API
  slug: open-tweed-contracts-api
- collection_type: open
  name: Tweed assets items API
  slug: open-tweed-items-api
- collection_type: open
  name: Tweed assets payouts API
  slug: open-tweed-payouts-api
- collection_type: open
  name: Tweed assets platform-webhooks API
  slug: open-tweed-platform-webhooks-api
- collection_type: open
  name: Tweed assets Rate API
  slug: open-tweed-rate-api
- collection_type: open
  name: Tweed assets tickets API
  slug: open-tweed-tickets-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/tweed-api-v2-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.paytweed.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.paytweed.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paytweed.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paytweed.com/developer-tools/api/api-v2/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paytweed.com/getting-started/embedded-wallets-or-waas
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.paytweed.com/developer-tools/pricing
- group: auth
  title: ''
  type: Authentication
  url: authentication/tweed-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tweed-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/tweed-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tweed-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tweed-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tweed-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tweed-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.paytweed.com/getting-started/token-checkout-or-payments/legacy-token-checkout/features/aml-and-kyc-policy-overview
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tweed-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tweed-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tweed-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tweed-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/tweed-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tweed-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tweed is an Accel-backed embedded-crypto platform offering Wallet-as-a-Service and NFT/token checkout APIs. Platforms embed self-custodial wallets (social login recovery, EIP-1193 EVM provider) and sell fungible and non-fungible tokens to buyers paying by card, Apple Pay, or Google Pay, with fiat, native, or stablecoin settlement across 12+ chains including Ethereum, Polygon, Base, Solana, and Tezos. A REST API (V2) manages contracts, items, payouts, checkouts, and HMAC-signed webhooks; note the marketing site and dashboard host were unreachable as of July 2026 while the docs, API, and npm SDKs remain live.
image: https://2034179314-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgQyCg5IN7Cv6AnUUpGl2%2Ficon%2F7r4C3KWx4NfmxABWz0oa%2FIcon-Square_Black-4x.jpeg?alt=media&token=55a8df5f-9429-454e-b864-52cb0bea5e25
layout: provider
mcp_servers:
- description: ''
  name: Tweed MCP Server
  slug: tweed-mcp-server
modified: '2026-07-21'
name: Tweed
nav: Providers
network: true
overview: 'Tweed publishes 11 APIs on the [APIs.io](https://apis.io/) network, including assets API, audit-event-mappings API, auth API, and 8 more. Tagged areas include Company, Payments, Crypto, Wallets, and NFT.


  The Tweed catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tweed''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, sandbox, and 16 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 4.5
    contract_quality: 48.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 39.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Tweed Authentication
  slug: tweed-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Tweed Domain Security
  slug: tweed-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tweed
tags:
- Company
- Payments
- Crypto
- Wallets
- NFT
- Blockchain
- Web3
- Checkout
website: https://www.paytweed.com/
---
