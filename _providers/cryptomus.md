---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Cryptomus Agentic Access
  operation_count: 24
  slug: cryptomus-agentic-access
  summary_line: 24 operations · 22 acting
api_count: 1
apis:
- description: REST API for creating cryptocurrency payouts, processing mass withdrawals, and transferring funds between personal and business wallets with support for auto-conversion.
  name: Cryptomus Payout API
  slug: cryptomus-payout-api
- baseURL: https://api.cryptomus.com/v1
  baseurl_source: declared
  description: REST API for creating and managing recurring cryptocurrency payment subscriptions with configurable billing periods (weekly, monthly, quarterly) and discount periods.
  name: Cryptomus Recurring Payments API
  slug: cryptomus-recurring-payments-api
- description: REST and WebSocket API for accessing real-time cryptocurrency exchange rates, order books, tickers, trade history, market cap data, and executing spot exchange orders with conversion calculations.
  name: Cryptomus Exchange and Market Data API
  slug: cryptomus-exchange-and-market-data-api
- baseURL: https://api.cryptomus.com/v1
  baseurl_source: declared
  description: Access exchange rates, trading pairs, and market data
  name: Cryptomus Exchange API
  slug: cryptomus-exchange-api
- baseURL: https://api.cryptomus.com/v1
  baseurl_source: declared
  description: Create and manage payment invoices for merchant integrations
  name: Cryptomus Payments API
  slug: cryptomus-payments-api
- baseURL: https://api.cryptomus.com/v1
  baseurl_source: declared
  description: Create and manage cryptocurrency payouts
  name: Cryptomus Payouts API
  slug: cryptomus-payouts-api
- baseURL: https://api.cryptomus.com/v1
  baseurl_source: declared
  description: Create and manage recurring payment subscriptions
  name: Cryptomus Recurring Payments API
  slug: cryptomus-recurring-payments-api
- baseURL: https://api.cryptomus.com/v1
  baseurl_source: declared
  description: Create and manage static cryptocurrency wallets
  name: Cryptomus Wallets API
  slug: cryptomus-wallets-api
- baseURL: https://api.cryptomus.com/v1
  baseurl_source: declared
  description: Test and manage webhook notifications
  name: Cryptomus Webhooks API
  slug: cryptomus-webhooks-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cryptomus Exchange API
  slug: open-cryptomus-exchange-api
- collection_type: open
  name: Cryptomus Exchange Payments API
  slug: open-cryptomus-payments-api
- collection_type: open
  name: Cryptomus Exchange Payouts API
  slug: open-cryptomus-payouts-api
- collection_type: open
  name: Cryptomus Exchange Recurring Payments API
  slug: open-cryptomus-recurring-payments-api
- collection_type: open
  name: Cryptomus Exchange Wallets API
  slug: open-cryptomus-wallets-api
- collection_type: open
  name: Cryptomus Exchange Webhooks API
  slug: open-cryptomus-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cryptomus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cryptomus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cryptomus-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://doc.cryptomus.com/merchant-api/getting-api-keys
- group: other
  title: ''
  type: Request Format
  url: https://doc.cryptomus.com/merchant-api/request-format
- group: design
  title: ''
  type: Webhooks
  url: https://doc.cryptomus.com/merchant-api/payments/webhook
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/cryptomus/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/cryptomus/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/cryptomus/refs/heads/main/finops/finops.yml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/cryptomus/refs/heads/main/json-ld/cryptomus.jsonld
- group: company
  title: ''
  type: Website
  url: https://cryptomus.com/
- group: other
  title: ''
  type: Fees
  url: https://cryptomus.com/fees/payment
- group: build
  title: ''
  type: SDKs
  url: https://doc.cryptomus.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cryptomus.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cryptomus.com/terms
created: '2026-06-13'
description: Cryptomus is a cryptocurrency payment gateway providing REST APIs for accepting crypto payments, creating invoices, processing payouts, managing recurring billing, and accessing real-time exchange rate and market data across 100+ cryptocurrencies.
examples:
- key_count: 4
  name: Create Invoice
  slug: create-invoice
- key_count: 4
  name: Create Payout
  slug: create-payout
- key_count: 4
  name: Create Recurring
  slug: create-recurring
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cryptomus.png
json_schemas:
- name: Cryptomus Payment Object
  property_count: 21
  slug: payment
- name: Cryptomus Payout Object
  property_count: 13
  slug: payout
- name: Cryptomus Recurring Payment Object
  property_count: 16
  slug: recurring
jsonld:
- class_count: 0
  name: Cryptomus Context
  property_count: 0
  slug: cryptomus
layout: provider
modified: '2026-06-13'
name: Cryptomus
nav: Providers
network: true
overview: 'Cryptomus publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Recurring Payments API, Exchange API, Payments API, and 4 more. Tagged areas include Cryptocurrency, Payments, Invoices, Payouts, and Exchange Rates.


  The Cryptomus catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cryptomus'' developer surface includes authentication and 14 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 6
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cryptomus API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cryptomus-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 66.2
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cryptomus/refs/heads/main/screenshots/cryptomus-2026-06-20T175312.png
security:
- kind: authentication
  name: Cryptomus Authentication
  slug: cryptomus-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cryptomus Domain Security
  slug: cryptomus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cryptomus
tags:
- Cryptocurrency
- Payments
- Invoices
- Payouts
- Exchange Rates
- Crypto Gateway
website: https://cryptomus.com/
---
