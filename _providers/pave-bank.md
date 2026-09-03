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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'Partner API for programmable multi-asset banking: Accounts, Address, Balance, Crypto, Documents, FX, Return, RFI, Sandbox, Statement, Transactions, and Transfer resources, plus real-time signed webhoo'
  name: Pave Bank Partner API
  slug: pave-bank-partner-api
artifact_total: 4
asyncapis:
- description: ''
  name: Pave Bank Webhooks
  slug: pave-bank-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://pavebank.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pavebank.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pavebank.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pavebank.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pavebank.com/docs
- group: auth
  title: ''
  type: Authentication
  url: authentication/pave-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pave-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/pave-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pave-bank-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pave-bank-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/pave-bank-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pave-bank-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pave-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/pave-bank-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pave-bank-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pave-bank-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pave-bank-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pave-bank-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pavebank
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pavebank.com/en/legal?tab=privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.pavebank.com
created: '2026-07-17'
description: Pave Bank is a licensed, regulated digital bank (National Bank of Georgia, License 305) delivering multi-asset, programmable banking. Its Partner API lets developers open and manage accounts, initiate domestic and cross-border transfers, execute FX, hold and move 29 fiat currencies plus digital assets (USDT, USDC, BTC, ETH), read real-time balances and transaction history, generate bank statements, and receive signed real-time webhooks. Pave positions itself as an "operating system for money" with an app-and-API programmability model built on a first-party Go Application Development Kit (PDK). Authentication is OAuth 2.0 client credentials with role-based access; requests support idempotency keys and optional JWT payload signing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pave-bank.png
layout: provider
modified: '2026-07-20'
name: Pave Bank
nav: Providers
network: true
overview: 'Pave Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, Payments, and Digital Assets.


  The Pave Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pave Bank''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 16 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 39.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 32.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/screenshots/pave-bank-2026-08-07T191602.png
security:
- kind: authentication
  name: Pave Bank Authentication
  slug: pave-bank-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Pave Bank Domain Security
  slug: pave-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pave-bank
tags:
- Company
- Fintech
- Banking
- Payments
- Digital Assets
- Stablecoins
- Cross-Border Payments
- Programmable Money
website: https://pavebank.com/en
---
