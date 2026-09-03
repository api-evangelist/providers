---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: ERC-4337 bundler JSON-RPC endpoint. Accepts User Operations into the mempool, estimates UserOp gas, returns a UserOp and its receipt by hash, and lists supported EntryPoint addresses. One endpoint per
  name: Cometh Connect Bundler API
  slug: cometh-connect-bundler-api
- description: ERC-4337 paymaster JSON-RPC endpoint for transaction sponsorship (pm_sponsorUserOperation, pm_supportedEntryPoints) plus REST routes to read and register the sponsored contract addresses and sponsored
  name: Cometh Connect Paymaster API
  slug: cometh-connect-paymaster-api
- description: Connect backend API used by the Connect 4337 SDK for wallet lifecycle and recovery — wallet init and import, WebAuthn signer creation and address prediction, project parameters, relayed transaction st
  name: Cometh Connect API
  slug: cometh-connect-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cometh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cometh.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cometh.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.cometh.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cometh.io/bundler/bundler-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cometh.io/quick-start/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://app.cometh.io/register?product=connect
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cometh-hq
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cometh.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.cometh.io/
- group: auth
  title: ''
  type: Compliance
  url: https://security.cometh.io/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Cometh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/comethstudio
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@comethio
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cometh-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/cometh-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cometh-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cometh-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cometh-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cometh-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cometh-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cometh-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cometh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cometh-rate-limits.yml
created: '2026-08-17'
description: Cometh is a French DeFi infrastructure provider building regulated, API-first crypto financial services for European fintechs, asset managers and corporates — custody, staking and yield, digital-asset trading, and payment settlement — on a composable ERC-4337 / Safe smart-account stack inside a MiCA-aligned regulatory perimeter (registered DASP; CASP licence AMF No. A2025-008; ISO 27001:2022). The publicly documented and callable surface today is Cometh Connect, a white-label ERC-4337 smart-wallet SDK with passkey (WebAuthn) signers, ERC-7579 session keys, social recovery and gasless transactions, served by an ERC-4337 Bundler JSON-RPC, a Paymaster JSON-RPC with sponsorship REST routes, and the Connect backend API. Every endpoint is gated at a Kong gateway by a project apikey (query string, front end) or apisecret (header, back end) issued from the app.cometh.io dashboard. The broader "DeFi-as-a-Service" API layer is sales-gated and its documentation is marked coming soon. Cometh
  was acquired by crypto market-data provider Kaiko, announced December 2025.
image: https://framerusercontent.com/images/Q1Csh4cl9JXyPBmGbxE2xtSPpFE.png
layout: provider
modified: '2026-08-17'
name: Cometh
nav: Providers
network: true
overview: 'Cometh publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Account Abstraction, ERC-4337, and Smart Wallet.


  Cometh''s developer surface includes documentation, API reference, getting-started guide, signup flow, YouTube channel, authentication, sandbox, and 17 more developer resources.'
plans:
- name: Cometh Plans Pricing
  plan_count: 0
  slug: cometh-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Cometh Rate Limits
  slug: cometh-rate-limits
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 29.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cometh/refs/heads/main/screenshots/cometh-2026-09-02T145130.png
security:
- kind: authentication
  name: Cometh Authentication
  slug: cometh-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cometh Domain Security
  slug: cometh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Cometh Trust Center
  slug: cometh-trust-center
  summary_line: ISO/IEC 27001:2022, MiCA / CASP licence, AMF No. A2025-008 (granted December 2025), Registered DASP (Digital Asset Service Provider)
slug: cometh
tags:
- Company
- Blockchain
- Account Abstraction
- ERC-4337
- Smart Wallet
- Paymaster
- Bundler
- Passkeys
- WebAuthn
- Gasless Transactions
- DeFi
- Custody
- Staking
- Payments
- JSON-RPC
- MiCA
- SAFe
- Web3
website: https://www.cometh.io/
---
