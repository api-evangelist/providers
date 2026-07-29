---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://senderwallet.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.senderwallet.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.senderwallet.io/api-reference/near
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.senderwallet.io/guide/getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:support@sender.org
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@senderlabs
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sender-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/sender-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sender-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sender-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sender-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sender-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sender-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sender-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sender-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://senderwallet.io/securityreport
created: '2026-07-17'
description: 'Sender (Sender Wallet, by Sender Labs / SENDER TECH LIMITED) is a self-custody multi-chain Web3 wallet for NEAR, Ethereum and all EVM-compatible chains (Polygon, BNB Chain, Arbitrum, Optimism, Avalanche, Scroll, zkSync Era, TON and 20+ networks), shipping as a Chrome/Brave/Edge browser extension and iOS and Android apps. For developers, Sender exposes an injected browser-provider API: dApps detect the wallet on window.sender.near / window.sender.ethereum (with legacy window.near support), request sign-in / account access, and sign and broadcast transactions. The Ethereum provider follows EIP-1193 and EIP-1102; NEAR exposes requestSignIn, signAndSendTransaction and request. The wallet is audited by SlowMist and runs a bug bounty. Surfaced as a portfolio company of Pantera Capital.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sender.png
layout: provider
modified: '2026-07-21'
name: Sender
nav: Providers
network: true
overview: 'Sender is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Wallet, Web3, and Blockchain.


  Sender''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 10 more developer resources.'
random_paper: 74
score:
  band: emerging
  composite: 21.0
  delta: -1.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 18.4
  previous_composite: 22.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sender Authentication
  slug: sender-authentication
  summary_line: wallet-connect · 2 schemes
- kind: domain-security
  name: Sender Domain Security
  slug: sender-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Sender Vulnerability Disclosure
  slug: sender-vulnerability-disclosure
  summary_line: contact published
slug: sender
tags:
- Company
- Crypto
- Wallet
- Web3
- Blockchain
- Ethereum
- NEAR
- DeFi
- Self-Custody
website: https://senderwallet.io/
---
