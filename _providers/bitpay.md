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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Bitpay Agentic Access
  operation_count: 24
  slug: bitpay-agentic-access
  summary_line: 24 operations · 8 acting
api_count: 1
apis:
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Manage payment requests sent to specific buyers with fixed-price line items typically denominated in fiat currency. Supports email billing and recurring payment scheduling via subscriptions.
  name: BitPay Bills API
  slug: bitpay-bills-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Submit cryptocurrency withdrawal payments to active BitPay recipients for customer payouts, marketplace disbursements, affiliate networks, and payroll processing.
  name: BitPay Payouts API
  slug: bitpay-payouts-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Process full or partial refunds associated with invoices. Supports automatic handling of underpaid and overpaid amounts with cryptocurrency refund workflows.
  name: BitPay Refunds API
  slug: bitpay-refunds-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Access transfer reports documenting payment profits settled from BitPay to merchant bank accounts and cryptocurrency wallets. Supports USD, EUR, GBP, CAD, AUD, NZD, MXN, and major cryptocurrencies.
  name: BitPay Settlements API
  slug: bitpay-settlements-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Retrieve exchange rate data representing fiat currency equivalents per cryptocurrency unit. Supports BTC, ETH, BCH, XRP, DOGE, and stablecoins against major fiat currencies.
  name: BitPay Rates API
  slug: bitpay-rates-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Access account balance records by currency and track individual ledger entries. Provides accounting data for merchant financial reconciliation.
  name: BitPay Ledgers API
  slug: bitpay-ledgers-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Manage payment requests sent to specific buyers with fixed-price line items.
  name: BitPay Bills API
  slug: bitpay-bills-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Create and manage time-sensitive payment requests with fixed prices in fiat or cryptocurrency.
  name: BitPay Invoices API
  slug: bitpay-invoices-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Access account balance records by currency and track individual ledger entries.
  name: BitPay Ledgers API
  slug: bitpay-ledgers-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Submit cryptocurrency withdrawal payments to active BitPay recipients.
  name: BitPay Payouts API
  slug: bitpay-payouts-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Retrieve exchange rate data representing fiat currency equivalents per cryptocurrency unit.
  name: BitPay Rates API
  slug: bitpay-rates-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Process full or partial refunds associated with invoices.
  name: BitPay Refunds API
  slug: bitpay-refunds-api
- baseURL: https://bitpay.com
  baseurl_source: declared
  description: Access transfer reports documenting payment profits settled from BitPay.
  name: BitPay Settlements API
  slug: bitpay-settlements-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BitPay Bills API
  slug: open-bitpay-bills-api
- collection_type: open
  name: BitPay Bills Invoices API
  slug: open-bitpay-invoices-api
- collection_type: open
  name: BitPay Bills Ledgers API
  slug: open-bitpay-ledgers-api
- collection_type: open
  name: BitPay Bills Payouts API
  slug: open-bitpay-payouts-api
- collection_type: open
  name: BitPay Bills Rates API
  slug: open-bitpay-rates-api
- collection_type: open
  name: BitPay Bills Refunds API
  slug: open-bitpay-refunds-api
- collection_type: open
  name: BitPay Bills Settlements API
  slug: open-bitpay-settlements-api
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
random_paper: 19
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: BitPay API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bitpay-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 63.3
    catalog_earned_first_party: 0.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 9.8
    contract_quality: 56.0
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 9.2
  previous_composite: 40.9
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
