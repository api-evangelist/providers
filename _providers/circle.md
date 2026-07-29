---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 3
  name: Circle Agentic Access
  operation_count: 30
  slug: circle-agentic-access
  summary_line: 30 operations · 18 acting · 3 human-in-the-loop
api_count: 7
apis:
- description: Sponsor gas fees on behalf of users or let users pay gas in USDC via Circle Paymaster, removing native-token friction from onboarding.
  name: Gas Station and Paymaster
  slug: gas-station
- description: The NFTs API from Circle — 1 operation(s) for nfts.
  name: Circle NFTs API
  slug: circle-nfts-api
- description: The Signing API from Circle — 4 operation(s) for signing.
  name: Circle Signing API
  slug: circle-signing-api
- description: The Tokens API from Circle — 1 operation(s) for tokens.
  name: Circle Tokens API
  slug: circle-tokens-api
- description: The Transactions API from Circle — 12 operation(s) for transactions.
  name: Circle Transactions API
  slug: circle-transactions-api
- description: The Wallet Sets API from Circle — 4 operation(s) for wallet sets.
  name: Circle Wallet Sets API
  slug: circle-wallet-sets-api
- description: The Wallets API from Circle — 7 operation(s) for wallets.
  name: Circle Wallets API
  slug: circle-wallets-api
artifact_total: 21
asyncapis:
- description: AsyncAPI description of Circle's outbound webhook (notification) surfaces. Circle delivers event notifications by POSTing a JSON body to a subscriber endpoint that is registered via product-specific n
  name: Circle Webhook Notifications
  slug: circle-webhooks-asyncapi
collections:
- collection_type: open
  name: Circle Web3 Services (W3S) — Developer-Controlled Wallets API
  slug: open-circle
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/circle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/circle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/circle-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/circleco
- group: company
  title: ''
  type: Website
  url: https://www.circle.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.circle.com/
- group: start
  title: ''
  type: Console
  url: https://console.circle.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.circle.com/w3s/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.circle.com/w3s/getting-started
- group: operate
  title: ''
  type: StatusPage
  url: https://status.circle.com/
- group: operate
  title: ''
  type: Support
  url: https://support.usdc.circle.com/
- group: company
  title: ''
  type: Blog
  url: https://www.circle.com/blog
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/buildoncircle
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/circlefin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.circle.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.circle.com/legal/terms-of-service
- group: design
  title: ''
  type: JSONLD
  url: json-ld/circle-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/circle-wallet-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/circle-transaction-schema.json
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/circle-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Spectral
  url: rules/circle-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.circle.com/llms.txt
created: '2024-11-07'
description: Circle Internet Financial is the issuer of USDC and EURC and operates a developer platform for moving regulated stablecoin money across the internet. Their APIs cover programmable wallets (developer- and user-controlled), gas sponsorship, the Cross-Chain Transfer Protocol (CCTP), Gateway unified balances, the Smart Contract Platform, the Circle Payments Network (CPN) for cross-border payments, compliance, StableFX trading on Arc, and xReserve for issuing USDC-backed stablecoins.
finops:
- name: Circle Finops
  service_category: API
  slug: circle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/circle.png
json_schemas:
- name: Circle Transaction
  property_count: 17
  slug: circle-transaction
- name: Circle Wallet
  property_count: 11
  slug: circle-wallet
jsonld:
- class_count: 0
  name: Circle Context
  property_count: 6
  slug: circle-context
layout: provider
modified: '2026-05-30'
name: Circle
nav: Providers
network: true
overview: 'Circle publishes 6 APIs on the [APIs.io](https://apis.io/) network, including NFTs API, Signing API, Tokens API, and 3 more. Tagged areas include Blockchain, Compliance, Cross-Chain, Currency, and Money.


  The Circle catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Circle''s developer surface includes authentication, developer portal, developer console, getting-started guide, support, engineering blog, and 16 more developer resources.'
plans:
- name: Circle Plans Pricing
  plan_count: 3
  slug: circle-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 5
  name: Circle Rate Limits
  slug: circle-rate-limits
rules:
- name: Circle API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: circle-asyncapi-spectral-rules
- name: Circle API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: circle-jsonschema-spectral-rules
- name: Circle API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: circle-rules
score:
  band: developing
  composite: 54.3
  delta: -5.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 67.8
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 52.6
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/circle/refs/heads/main/screenshots/circle-2026-06-20T174349.png
security:
- kind: authentication
  name: Circle Authentication
  slug: circle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Circle Domain Security
  slug: circle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: circle
tags:
- Blockchain
- Compliance
- Cross-Chain
- Currency
- Money
- Payments
- Stablecoin
- Transfers
- USDC
- Wallets
website: https://www.circle.com/
---
