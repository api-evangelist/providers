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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Increase Com Agentic Access
  operation_count: 84
  slug: increase-com-agentic-access
  summary_line: 84 operations · 38 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: Routing and account number pairs that can receive funds.
  name: Increase Account Numbers API
  slug: increase-com-account-numbers-api
- description: Deposit accounts held at Increase partner banks.
  name: Increase Accounts API
  slug: increase-com-accounts-api
- description: FedACH credit and debit transfers, inbound and outbound.
  name: Increase ACH Transfers API
  slug: increase-com-ach-transfers-api
- description: Double-entry sub-ledger built on Increase money movement.
  name: Increase Bookkeeping API
  slug: increase-com-bookkeeping-api
- description: Card authorization and settlement lifecycle.
  name: Increase Card Payments API
  slug: increase-com-card-payments-api
- description: Digital and physical card profiles and wallet tokens.
  name: Increase Card Profiles API
  slug: increase-com-card-profiles-api
- description: Virtual and physical commercial cards.
  name: Increase Cards API
  slug: increase-com-cards-api
- description: Printed and mailed checks and check deposits.
  name: Increase Check Transfers API
  slug: increase-com-check-transfers-api
- description: KYC/KYB entities that own accounts.
  name: Increase Entities API
  slug: increase-com-entities-api
- description: Events and webhook Event Subscriptions.
  name: Increase Events API
  slug: increase-com-events-api
- description: Counterparty bank accounts you send to or debit.
  name: Increase External Accounts API
  slug: increase-com-external-accounts-api
- description: Physical lockbox addresses and inbound mail.
  name: Increase Lockboxes API
  slug: increase-com-lockboxes-api
- description: Instant RTP transfers, inbound and outbound.
  name: Increase Real-Time Payments API
  slug: increase-com-real-time-payments-api
- description: Sandbox-only endpoints for deterministic testing.
  name: Increase Simulations API
  slug: increase-com-simulations-api
- description: Settled, pending, and declined ledger transactions.
  name: Increase Transactions API
  slug: increase-com-transactions-api
- description: Fedwire transfers and drawdown requests.
  name: Increase Wire Transfers API
  slug: increase-com-wire-transfers-api
artifact_total: 24
collections:
- collection_type: open
  name: Increase API
  slug: open-increase-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/increase-com-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/increase-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/increase-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/increase-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Increase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/increase
- group: company
  title: ''
  type: Website
  url: https://increase.com
- group: docs
  title: ''
  type: Documentation
  url: https://increase.com/documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/increase-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/increase-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/increase-com-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://increase.com/updates.xml
created: '2026-07-02'
description: Increase is a bank-grade payments and financial infrastructure platform that exposes a single REST API for moving and holding money in the United States - ACH transfers, real-time payments (RTP and FedNow), domestic and international wires, physical and mailed checks, deposit accounts and account numbers, card issuing and card acquiring, ledgering and bookkeeping, KYC/KYB entities, and lockboxes. Increase connects directly to the Federal Reserve and card networks through partner banks, and every state change is delivered as an Event over HTTP webhooks. The API is documented with a public OpenAPI 3.1 spec (https://api.increase.com/openapi.json) and Stainless-generated SDKs for Python, TypeScript, Java, Kotlin, Go, Ruby, PHP, and C#. Base URL https://api.increase.com with a sandbox at https://sandbox.increase.com.
finops:
- name: Increase Com Finops
  service_category: Financial Infrastructure and Payments
  slug: increase-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/increase-com.png
layout: provider
modified: '2026-07-02'
name: Increase
nav: Providers
network: true
overview: 'Increase publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Account Numbers API, Accounts API, ACH Transfers API, and 13 more. Tagged areas include Payments, Banking, Financial Infrastructure, ACH, and Wire Transfers.


  Increase''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Increase Com Plans Pricing
  plan_count: 2
  slug: increase-com-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: Increase Com Rate Limits
  slug: increase-com-rate-limits
score:
  band: thin
  composite: 35.9
  delta: 0.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.8
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.4
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Increase Com Authentication
  slug: increase-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Increase Com Domain Security
  slug: increase-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Increase Com Vulnerability Disclosure
  slug: increase-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: increase-com
tags:
- Payments
- Banking
- Financial Infrastructure
- ACH
- Wire Transfers
- Real-Time Payments
- Cards
- Fintech
website: https://increase.com
---
