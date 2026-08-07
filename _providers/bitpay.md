---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Bitpay Agentic Access
  operation_count: 24
  slug: bitpay-agentic-access
  summary_line: 24 operations · 8 acting
api_count: 13
apis:
- description: Manage payment requests sent to specific buyers with fixed-price line items typically denominated in fiat currency. Supports email billing and recurring payment scheduling via subscriptions.
  name: BitPay Bills API
  slug: bitpay-bills-api
- description: Submit cryptocurrency withdrawal payments to active BitPay recipients for customer payouts, marketplace disbursements, affiliate networks, and payroll processing.
  name: BitPay Payouts API
  slug: bitpay-payouts-api
- description: Process full or partial refunds associated with invoices. Supports automatic handling of underpaid and overpaid amounts with cryptocurrency refund workflows.
  name: BitPay Refunds API
  slug: bitpay-refunds-api
- description: Access transfer reports documenting payment profits settled from BitPay to merchant bank accounts and cryptocurrency wallets. Supports USD, EUR, GBP, CAD, AUD, NZD, MXN, and major cryptocurrencies.
  name: BitPay Settlements API
  slug: bitpay-settlements-api
- description: Retrieve exchange rate data representing fiat currency equivalents per cryptocurrency unit. Supports BTC, ETH, BCH, XRP, DOGE, and stablecoins against major fiat currencies.
  name: BitPay Rates API
  slug: bitpay-rates-api
- description: Access account balance records by currency and track individual ledger entries. Provides accounting data for merchant financial reconciliation.
  name: BitPay Ledgers API
  slug: bitpay-ledgers-api
- description: Manage payment requests sent to specific buyers with fixed-price line items.
  name: BitPay Bills API
  slug: bitpay-bills-api
- description: Create and manage time-sensitive payment requests with fixed prices in fiat or cryptocurrency.
  name: BitPay Invoices API
  slug: bitpay-invoices-api
- description: Access account balance records by currency and track individual ledger entries.
  name: BitPay Ledgers API
  slug: bitpay-ledgers-api
- description: Submit cryptocurrency withdrawal payments to active BitPay recipients.
  name: BitPay Payouts API
  slug: bitpay-payouts-api
- description: Retrieve exchange rate data representing fiat currency equivalents per cryptocurrency unit.
  name: BitPay Rates API
  slug: bitpay-rates-api
- description: Process full or partial refunds associated with invoices.
  name: BitPay Refunds API
  slug: bitpay-refunds-api
- description: Access transfer reports documenting payment profits settled from BitPay.
  name: BitPay Settlements API
  slug: bitpay-settlements-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitpay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitpay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: https://developer.bitpay.com/docs/api-integrations-additional-information
- group: build
  title: ''
  type: SDKs
  url: https://developer.bitpay.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bitpay.com/docs
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/bitpay/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/bitpay/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/bitpay/refs/heads/main/finops/finops.yml
- group: operate
  title: ''
  type: Status
  url: https://status.bitpay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitpay.com/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.bitpay.com/hc/en-us
- group: design
  title: ''
  type: Webhooks
  url: https://developer.bitpay.com/docs/api-integrations-additional-information
- group: build
  title: ''
  type: GitHub
  url: https://github.com/bitpay
- group: start
  title: ''
  type: Signup
  url: https://bitpay.com/dashboard/signup
- group: company
  title: ''
  type: Blog
  url: https://bitpay.com/blog
description: BitPay is a cryptocurrency payment processing platform offering REST APIs for accepting Bitcoin and altcoin payments, creating invoices, managing refunds, processing payouts, and accessing settlement and ledger data. BitPay handles cryptocurrency conversion and fiat settlement to bank accounts and crypto wallets.
examples:
- key_count: 4
  name: Create Invoice
  slug: create-invoice
- key_count: 4
  name: Create Payout
  slug: create-payout
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitpay.png
json_schemas:
- name: BitPay Invoice
  property_count: 20
  slug: invoice
- name: BitPay Payout
  property_count: 15
  slug: payout
jsonld:
- class_count: 24
  name: Bitpay Context
  property_count: 0
  slug: bitpay
layout: provider
modified: '2026-06-13'
name: BitPay
nav: Providers
network: true
overview: 'BitPay publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Bills API, Payouts API, Refunds API, and 10 more. Tagged areas include Cryptocurrency, Payments, Bitcoin, Blockchain, and Invoices.


  The BitPay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BitPay''s developer surface includes authentication, documentation, status page, support, GitHub presence, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 84
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: BitPay API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bitpay-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.0
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitpay/refs/heads/main/screenshots/bitpay-2026-06-20T173317.png
security:
- kind: domain-security
  name: Bitpay Domain Security
  slug: bitpay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitpay
tags:
- Cryptocurrency
- Payments
- Bitcoin
- Blockchain
- Invoices
- Payouts
- Settlement
---
