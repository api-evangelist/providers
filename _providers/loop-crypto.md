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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for accepting crypto and stablecoin payments — customers, entities, merchants, tokens, payments, payouts, and webhooks. Authenticated with api-key and entity-id headers; URI-path versioned (v
  name: Loop Crypto API
  slug: loop-crypto-api
artifact_total: 4
asyncapis:
- description: ''
  name: Loop Crypto Webhooks
  slug: loop-crypto-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.loopcrypto.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.loopcrypto.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://www.loopcrypto.xyz/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.loopcrypto.xyz/docs/get-set-up
- group: start
  title: ''
  type: SignUp
  url: https://www.loopcrypto.xyz/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.loopcrypto.xyz/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LoopCrypto
- group: auth
  title: ''
  type: Authentication
  url: authentication/loop-crypto-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loop-crypto-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/loop-crypto-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loop-crypto-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/loop-crypto-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/loop-crypto-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/loop-crypto-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/loop-crypto-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/loop-crypto-cli.yml
- group: design
  title: ''
  type: Components
  url: components/loop-crypto-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loop-crypto-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loop-crypto-llms.txt
created: '2026-07-17'
description: 'Loop Crypto is a crypto and stablecoin payment processor that lets merchants, billing software, and e-commerce platforms accept crypto and stablecoin payments end to end: charging a wallet, storing payment methods, accepting stablecoins, ERC-20 tokens, and Solana SPL tokens, and settling to merchants in either fiat or crypto. Loop offers payment links, an embeddable Pay/PayIn checkout component, a white-labelable Connect widget, and a REST API (v1/v2, api-key + entity-id header auth) covering customers, entities, merchants, tokens, payments, payouts, and webhooks, plus out-of-the-box integrations with Stripe, Chargebee, and OpenPay. Backed by a16z. NOTE: Loop is winding down and folding into Lead; the service was sunset on 2026-02-13 and is not recommended for new integrations.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loop-crypto.png
layout: provider
modified: '2026-07-20'
name: Loop Crypto
nav: Providers
network: true
overview: 'Loop Crypto publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cryptocurrency, Stablecoins, and Web3.


  The Loop Crypto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Loop Crypto''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, authentication, sandbox, and 12 more developer resources.'
random_paper: 40
score:
  band: thin
  composite: 36.3
  delta: 3.7
  facets:
    commercial_clarity: 13.2
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Loop Crypto Authentication
  slug: loop-crypto-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Loop Crypto Domain Security
  slug: loop-crypto-domain-security
  summary_line: DNSSEC · DMARC
slug: loop-crypto
tags:
- Company
- Payments
- Cryptocurrency
- Stablecoins
- Web3
- Payment Processing
- Billing
- Solana
- Ethereum
website: https://docs.loopcrypto.xyz
---
