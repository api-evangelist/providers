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
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.7
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: The core zerohash REST API — 167 operations across participants, accounts, assets, trades, liquidity (RFQ), the central limit order book, deposits, withdrawals, transfers, positions, market data, paym
  name: zerohash API
  slug: zerohash-api
- description: Session and access-token API behind the zerohash Auth product for onchain account linking across custodial and non-custodial wallets. Two operations — OAuth 2.0 client-credentials token issuance and s
  name: zerohash Auth (Connect) API
  slug: zerohash-auth-connect-api
- description: Authenticated WebSocket feed delivering a full account-balance snapshot on subscribe followed by incremental balance-updated events, plus RFQ liquidity bid/ask price levels per subscribed symbol. Ever
  name: zerohash Private WebSocket API
  slug: zerohash-private-websocket-api
artifact_total: 9
asyncapis:
- description: ''
  name: Zero Hash Webhooks
  slug: zero-hash-webhooks
common:
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
modified: '2026-08-05'
name: Zero Hash
nav: Providers
network: true
overview: 'Zero Hash publishes 2 APIs on the [APIs.io](https://apis.io/) network: zerohash API and zerohash Auth (Connect) API. Tagged areas include Company, crypto-infrastructure, digital-assets, stablecoins, and payments.


  The Zero Hash catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zero Hash''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
random_paper: 9
scopes:
- name: Zero Hash Scopes
  scope_count: 4
  slug: zero-hash-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 63.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 70.6
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 55.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
