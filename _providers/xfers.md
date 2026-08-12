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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: verified
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-08-11'
api_count: 20
apis:
- description: API to manage Bank Account
  name: Xfers Bank Account API
  slug: xfers-bank-account-api
- description: API for Charges
  name: Xfers Charge API
  slug: xfers-charge-api
- description: The Convenience Store Transfers API from Xfers — 1 operation(s) for convenience store transfers.
  name: Xfers Convenience Store Transfers API
  slug: xfers-convenience-store-transfers-api
- description: The cutting_edge API from Xfers — 2 operation(s) for cutting_edge.
  name: Xfers cutting_edge API
  slug: xfers-cutting-edge-api
- description: The Direct Bank Transfer Payments API from Xfers — 1 operation(s) for direct bank transfer payments.
  name: Xfers Direct Bank Transfer Payments API
  slug: xfers-direct-bank-transfer-payments-api
- description: API for Disbursement
  name: Xfers Disbursements API
  slug: xfers-disbursements-api
- description: API for e-signature
  name: Xfers E-signature API
  slug: xfers-e-signature-api
- description: The Fixed Virtual Account Bank Transfers API from Xfers — 2 operation(s) for fixed virtual account bank transfers.
  name: Xfers Fixed Virtual Account Bank Transfers API
  slug: xfers-fixed-virtual-account-bank-transfers-api
- description: '**For user case 1:** When a user is performing a top-up via [GET /transfer_info](http://docs.xfers.io/#get-transfer-info), they might forget to enter their contact number which is needed for our syste'
  name: Xfers Intents API
  slug: xfers-intents-api
- description: Loans Management
  name: Xfers Loans API
  slug: xfers-loans-api
- description: The Modify Payments API from Xfers — 1 operation(s) for modify payments.
  name: Xfers Modify Payments API
  slug: xfers-modify-payments-api
- description: The Payment Queries API from Xfers — 1 operation(s) for payment queries.
  name: Xfers Payment Queries API
  slug: xfers-payment-queries-api
- description: The Payment Queries (Hide first) API from Xfers — 1 operation(s) for payment queries (hide first).
  name: Xfers Payment Queries (Hide first) API
  slug: xfers-payment-queries-hide-first-api
- description: API for Payout
  name: Xfers Payout API
  slug: xfers-payout-api
- description: Register and verify new users.
  name: Xfers Registration API
  slug: xfers-registration-api
- description: API for Repayment
  name: Xfers Repayments API
  slug: xfers-repayments-api
- description: API for testing purposes
  name: Xfers Testing API
  slug: xfers-testing-api
- description: The Unique Amount Bank Transfers API from Xfers — 1 operation(s) for unique amount bank transfers.
  name: Xfers Unique Amount Bank Transfers API
  slug: xfers-unique-amount-bank-transfers-api
- description: Manage User and Accounts
  name: Xfers User Account API
  slug: xfers-user-account-api
- description: API for Withdrawal
  name: Xfers Withdraw API
  slug: xfers-withdraw-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xfers-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xfers-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xfers-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://xfers.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.xfers.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.xfers.io/Singapore
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Xfers
- group: operate
  title: ''
  type: StatusPage
  url: https://xfers.statuspage.io
- group: operate
  title: ''
  type: Support
  url: https://support.straitsx.com/hc/en-us/requests/new
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/1eebf10c08b8f90bdded
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/453dd7b670533289a719
created: '2026-07-17'
description: Xfers is a Southeast Asian payments infrastructure company founded in Singapore in 2015 and backed by 500 Global, providing bank-transfer collection, payouts, escrow-style wallets, and lending disbursement APIs across Singapore and Indonesia. Xfers merged with Payfazz in 2022 to form the Fazz Financial Group, with its regulated Singapore dollar stablecoin and payments business continuing as StraitsX; the Xfers v3 API documentation for Singapore and Indonesia remains published at docs.xfers.io.
image: https://docs.xfers.io/Xfers_X_Blue_Small.png
layout: provider
mcp_servers:
- description: ''
  name: xfers-mcp.yml
  slug: xfers-mcpyml
modified: '2026-07-21'
name: Xfers
nav: Providers
network: true
overview: 'Xfers publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Bank Account API, Charge API, Convenience Store Transfers API, and 17 more. Tagged areas include Payments, Fintech, Bank Transfers, Digital Wallets, and Lending.


  Xfers'' developer surface includes authentication, documentation, API reference, support, and 7 more developer resources.'
random_paper: 88
score:
  band: thin
  composite: 31.9
  delta: -1.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 62.1
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Xfers Authentication
  slug: xfers-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Xfers Domain Security
  slug: xfers-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: xfers
tags:
- Payments
- Fintech
- Bank Transfers
- Digital Wallets
- Lending
- Singapore
- Indonesia
- Southeast Asia
website: https://xfers.com
---
