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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: true
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Pintu Pro's institutional/partner trading API. A unified message format is used over both an HTTP endpoint and a WebSocket transport, authenticated with an HMAC-SHA256 signature computed from an API k
  name: Pintu Pro Partner API
  slug: pintu-pro-partner-api
artifact_total: 6
asyncapis:
- description: ''
  name: Pintu Partner Asyncapi
  slug: pintu-partner-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pintu.pro/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pintu.pro/
- group: company
  title: ''
  type: Website
  url: https://pintu.co.id
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pintu-crypto
- group: company
  title: ''
  type: Blog
  url: https://pintu.co.id/en/news
- group: operate
  title: ''
  type: Support
  url: https://pintu.co.id/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pintu.co.id/en/pages/pintu-pro-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pintu.co.id/en/pages/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/pintu-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pintu-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pintu-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/pintu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pintu-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pintu-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pintu-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pintu-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pintu-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pintu-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pintu-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://pintu.co.id/security/bug-bounty
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pintu-partner-asyncapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pintu-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/pintu-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pintu-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://pintu.co.id/en/faq/safe-to-use-pintu
created: '2026-07-17'
description: Pintu (PT Pintu Kemana Saja) is an Indonesian cryptocurrency exchange and investment app founded in April 2020 and headquartered in Jakarta. Licensed as a Physical Crypto Asset Trader (PFAK) under Bappebti and now supervised by the OJK, Pintu serves more than four million retail users with spot trading, crypto futures, staking/Earn, and a self-custody Web3 wallet connecting to DeFi and NFT dApps. Beyond the consumer app, Pintu operates Pintu Pro, an institutional and partner trading platform whose HMAC-signed WebSocket + HTTP API (docs.pintu.pro) lets market makers and partners place and cancel orders and stream execution reports and trades against production and sandbox environments. Pintu has raised over 150M USD across a Lightspeed-led 35M Series A+ (2021) and a 113M Series B (2022) with Intudo, Pantera Capital, and Northstar.
image: https://assets.pintu.co.id/frontend/strapi-prod/pintu_thumbnail_card_6a039be9aa.png
layout: provider
modified: '2026-07-20'
name: Pintu
nav: Providers
network: true
overview: 'Pintu publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Crypto Exchange, Trading, and Fintech.


  The Pintu catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pintu''s developer surface includes documentation, engineering blog, support, authentication, sandbox, and 20 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 22.6
    developer_ergonomics: 41.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 40.3
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Pintu Authentication
  slug: pintu-authentication
  summary_line: apiKey/hmac · 1 scheme
- kind: domain-security
  name: Pintu Domain Security
  slug: pintu-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pintu Vulnerability Disclosure
  slug: pintu-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Pintu Trust Center
  slug: pintu-trust-center
  summary_line: ISO/IEC 27001:2022
slug: pintu
tags:
- Company
- Cryptocurrency
- Crypto Exchange
- Trading
- Fintech
- Digital Assets
- Web3
- Indonesia
- WebSocket
- Institutional Trading
website: https://pintu.co.id
---
