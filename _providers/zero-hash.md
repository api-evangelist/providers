---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-08-11'
api_count: 31
apis:
- description: Authenticated WebSocket feed delivering a full account-balance snapshot on subscribe followed by incremental balance-updated events, plus RFQ liquidity bid/ask price levels per subscribed symbol. Ever
  name: zerohash Private WebSocket API
  slug: zerohash-private-websocket-api
- description: Create and Manage Accounts
  name: Zero Hash Accounts API
  slug: zero-hash-accounts-api
- description: View available assets
  name: Zero Hash Assets API
  slug: zero-hash-assets-api
- description: Awards Distribution Service
  name: Zero Hash Awards API
  slug: zero-hash-awards-api
- description: Central Limit Order Book
  name: Zero Hash CLOB API
  slug: zero-hash-clob-api
- description: Convert and Withdraw Services
  name: Zero Hash Convert and Withdraw API
  slug: zero-hash-convert-and-withdraw-api
- description: Create and Manage Customer Accounts (MTA)
  name: Zero Hash Customer Accounts (MTA) API
  slug: zero-hash-customer-accounts-mta-api
- description: Create deposit addressed and monitor deposits to accounts
  name: Zero Hash Deposits API
  slug: zero-hash-deposits-api
- description: Create and Manage Entity Participants
  name: Zero Hash Entity Participants API
  slug: zero-hash-entity-participants-api
- description: Fund Services
  name: Zero Hash Fund API
  slug: zero-hash-fund-api
- description: Obtain the index price on an instrument
  name: Zero Hash Index API
  slug: zero-hash-index-api
- description: Create and Manage Individual Participants
  name: Zero Hash Individual Participants API
  slug: zero-hash-individual-participants-api
- description: Request For Quote and Execution Services
  name: Zero Hash Liquidity API
  slug: zero-hash-liquidity-api
- description: Market Data Services
  name: Zero Hash Market Data API
  slug: zero-hash-market-data-api
- description: The Movements API from Zero Hash — 1 operation(s) for movements.
  name: Zero Hash Movements API
  slug: zero-hash-movements-api
- description: The Organization Token API from Zero Hash — 1 operation(s) for organization token.
  name: Zero Hash Organization Token API
  slug: zero-hash-organization-token-api
- description: Participant jurisdiction endpoints
  name: Zero Hash Participant Jurisdictions API
  slug: zero-hash-participant-jurisdictions-api
- description: Power your checkout with crypto and stablecoins
  name: Zero Hash Payins API
  slug: zero-hash-payins-api
- description: Payment Services
  name: Zero Hash Payments API
  slug: zero-hash-payments-api
- description: Crypto payouts
  name: Zero Hash Payouts API
  slug: zero-hash-payouts-api
- description: Positions and Balances monitoring
  name: Zero Hash Positions API
  slug: zero-hash-positions-api
- description: Basic API Endpoints
  name: Zero Hash Public API
  slug: zero-hash-public-api
- description: Generic Participant management endpoints
  name: Zero Hash Query Participants API
  slug: zero-hash-query-participants-api
- description: Rewards Distribution Service
  name: Zero Hash Rewards API
  slug: zero-hash-rewards-api
- description: SDK Authorization Services
  name: Zero Hash SDK Authorization API
  slug: zero-hash-sdk-authorization-api
- description: Staking, Unstaking and associated Rewards Services
  name: Zero Hash Staking API
  slug: zero-hash-staking-api
- description: The Trade Strategy API from Zero Hash — 13 operation(s) for trade strategy.
  name: Zero Hash Trade Strategy API
  slug: zero-hash-trade-strategy-api
- description: Trade Settlement Services
  name: Zero Hash Trades API
  slug: zero-hash-trades-api
- description: Initiate and monitor transfers between accounts
  name: Zero Hash Transfers API
  slug: zero-hash-transfers-api
- description: The User Token API from Zero Hash — 1 operation(s) for user token.
  name: Zero Hash User Token API
  slug: zero-hash-user-token-api
- description: Initiate and monitor withdrawals from accounts
  name: Zero Hash Withdrawals API
  slug: zero-hash-withdrawals-api
artifact_total: 38
asyncapis:
- description: ''
  name: Zero Hash Webhooks
  slug: zero-hash-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zero-hash-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zero-hash-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zero-hash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zerohash.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zerohash.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zerohash.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zerohash.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zerohash.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://zerohash.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://zerohash.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seedcx
- group: commercial
  title: ''
  type: Pricing
  url: https://zerohash.com/disclosures/pricing-and-fees
- group: start
  title: ''
  type: SignUp
  url: https://zerohash.com/contact
- group: start
  title: ''
  type: Login
  url: https://portal.zerohash.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.zerohash.com/page/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.zerohash.com/page/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zerohash.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zero-hash-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.zerohash.com/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://zerohash.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/zero-hash-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/zero-hash-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zero-hash-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/zero-hash-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zero-hash-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zero-hash-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/zero-hash-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zero-hash-packages.yml
- group: design
  title: ''
  type: Components
  url: components/zero-hash-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zero-hash-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zero-hash-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zero-hash-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zero-hash-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zero-hash-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zero-hash-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zero-hash-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zero-hash-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zero-hash-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zero-hash-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: Zero Hash is a regulated digital-asset infrastructure provider that lets banks, brokerages, fintechs, payroll platforms and payment service providers embed crypto, stablecoin and tokenized-asset capability without holding licenses or running blockchain infrastructure themselves. The platform covers trading (RFQ liquidity and a central limit order book reachable over REST and FIX 5.0), qualified custody, staking, rewards and portfolio strategies, plus a Transact side that handles on/off ramps, account funding, payins, payouts, remittances and settlement across 100+ assets and 40+ chains. Participant onboarding, KYC, sanctions screening, jurisdiction evaluation and travel-rule handling are exposed as first-class API resources, and a Tokenize product line covers a tokenization engine and tokenization payment rails. Integration surfaces include a 167-operation REST API secured with HMAC-SHA256 request signing, a private WebSocket feed for balances and RFQ prices, a FIX gateway for
  CLOB order entry and market data, an outbound webhook catalog, and a large family of embeddable JavaScript/React SDK modules for buy, sell, onboarding, funding, withdrawals and account linking.
image: https://cdn.prod.website-files.com/68c59605946d2fed8ac8bcbd/6a0c76136695e559d8cffe0f_zerohash%20-%20512.png
layout: provider
mcp_servers:
- description: ''
  name: zero-hash-mcp.yml
  slug: zero-hash-mcpyml
modified: '2026-08-05'
name: Zero Hash
nav: Providers
network: true
overview: 'Zero Hash publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Assets API, Awards API, and 27 more. Tagged areas include Company, crypto-infrastructure, digital-assets, stablecoins, and payments.


  The Zero Hash catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zero Hash''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
random_paper: 101
scopes:
- name: Zero Hash Scopes
  scope_count: 4
  slug: zero-hash-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 61.4
  delta: 1.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.4
    developer_ergonomics: 69.0
    discoverability: 68.5
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 60.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Zero Hash Authentication
  slug: zero-hash-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Zero Hash Domain Security
  slug: zero-hash-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zero Hash Vulnerability Disclosure
  slug: zero-hash-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Zero Hash Trust Center
  slug: zero-hash-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 1, SOC 2 Type 2, ISO/IEC 27001:2022, Regulation SCI, DORA, GDPR, CCPA, 23 NYCRR 500
slug: zero-hash
tags:
- Company
- crypto-infrastructure
- digital-assets
- stablecoins
- payments
- payouts
- tokenization
- custody
- staking
- settlement
- embedded-finance
- on-off-ramp
- liquidity
- fix-protocol
- webhooks
- websockets
- kyc
- compliance
- remittances
- agentic-finance
website: https://zerohash.com/
---
