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
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-09-25'
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
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/authentication/pave-bank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pave-bank-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/conventions/pave-bank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pave-bank-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/conventions/pave-bank-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/pave-bank-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/errors/pave-bank-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/pave-bank-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/asyncapi/pave-bank-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pave-bank-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/packages/pave-bank-packages.yml
  title: ''
  type: Packages
  url: packages/pave-bank-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/packages/pave-bank-packages.yml
  title: ''
  type: SDKs
  url: packages/pave-bank-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/conformance/pave-bank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pave-bank-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/conformance/pave-bank-conformance.yml
  title: ''
  type: Compliance
  url: conformance/pave-bank-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/sandbox/pave-bank-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pave-bank-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/lifecycle/pave-bank-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pave-bank-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/llms/pave-bank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pave-bank-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pave-bank/refs/heads/main/security/pave-bank-domain-security.yml
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
random_paper: 5
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 64.3
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 39.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 20.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
