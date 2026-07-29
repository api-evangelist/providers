---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Dlocal Agentic Access
  operation_count: 34
  slug: dlocal-agentic-access
  summary_line: 34 operations · 18 acting
api_count: 17
apis:
- description: Distribute funds globally with multi-currency support and local compliance across 60+ emerging market countries. Includes payout submission and retrieval, balance checking, quote generation for curren
  name: dLocal Payouts API
  slug: dlocal-payouts-api
- description: Complete solution for marketplaces and platforms with automated account onboarding, KYC information handling, bank account management, transfer operations, and account status and balance queries.
  name: dLocal Platforms API
  slug: dlocal-platforms-api
- description: Identity verification and document management API supporting verification creation and retrieval, document management, and status updates for compliance workflows across emerging markets.
  name: dLocal Verification API
  slug: dlocal-verification-api
- description: Platform sub-account management
  name: dLocal Accounts API
  slug: dlocal-accounts-api
- description: Query account balances
  name: dLocal Balance API
  slug: dlocal-balance-api
- description: Bank account registration and management
  name: dLocal Bank Accounts API
  slug: dlocal-bank-accounts-api
- description: Manage chargeback disputes
  name: dLocal Chargebacks API
  slug: dlocal-chargebacks-api
- description: Foreign exchange rate queries
  name: dLocal Currency API
  slug: dlocal-currency-api
- description: Document upload and management
  name: dLocal Documents API
  slug: dlocal-documents-api
- description: Know Your Customer verification
  name: dLocal KYC API
  slug: dlocal-kyc-api
- description: Query available local payment methods
  name: dLocal Payment Methods API
  slug: dlocal-payment-methods-api
- description: Create and manage payment transactions
  name: dLocal Payments API
  slug: dlocal-payments-api
- description: Submit and manage disbursements
  name: dLocal Payouts API
  slug: dlocal-payouts-api
- description: Reverse payment transactions
  name: dLocal Refunds API
  slug: dlocal-refunds-api
- description: Card tokenization operations
  name: dLocal Tokens API
  slug: dlocal-tokens-api
- description: Fund transfers between accounts
  name: dLocal Transfers API
  slug: dlocal-transfers-api
- description: Identity verification requests
  name: dLocal Verifications API
  slug: dlocal-verifications-api
artifact_total: 29
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dlocal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dlocal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dlocal-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.dlocal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dlocal.com/docs/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.dlocal.com/reference/payins-security
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/dlocal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dlocal
- group: company
  title: ''
  type: Blog
  url: https://www.dlocal.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dlocal.com/faqs/faqs-solutions/
- group: operate
  title: ''
  type: StatusPage
  url: https://dlocal.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/dLocalPayments
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/dlocal-dev
- group: commercial
  title: ''
  type: Plans
  url: plans/dlocal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dlocal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dlocal-finops.yml
created: 2026-06-13
description: dLocal is an emerging markets payment platform that enables global merchants to accept and disburse local payment methods and currencies through a single REST API. The platform covers 60+ countries across Africa, Asia, and Latin America, providing payins, payouts, and platform-as-a-service capabilities with 1,000+ local payment methods including cards, cash, bank transfers, mobile money, and eWallets.
examples:
- key_count: 4
  name: Create Payment
  slug: create-payment
- key_count: 4
  name: Create Payout
  slug: create-payout
finops:
- name: Dlocal Finops
  service_category: ''
  slug: dlocal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dlocal.png
json_schemas:
- name: dLocal Payment
  property_count: 16
  slug: payment
- name: dLocal Payout
  property_count: 13
  slug: payout
jsonld:
- class_count: 2
  name: Dlocal Context
  property_count: 56
  slug: dlocal-context
layout: provider
modified: 2026-06-13
name: dLocal
nav: Providers
network: true
overview: 'dLocal publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Payouts API, Accounts API, Balance API, and 12 more. Tagged areas include Payments, Emerging Markets, Payins, Payouts, and Fintech.


  The dLocal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  dLocal''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Dlocal Plans Pricing
  plan_count: 1
  slug: dlocal-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 0
  name: Dlocal Rate Limits
  slug: dlocal-rate-limits
rules:
- name: dLocal API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: dlocal-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.3
  delta: -5.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.8
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/dlocal/refs/heads/main/screenshots/dlocal-2026-06-20T180058.png
security:
- kind: authentication
  name: Dlocal Authentication
  slug: dlocal-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dlocal Domain Security
  slug: dlocal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dlocal
tags:
- Payments
- Emerging Markets
- Payins
- Payouts
- Fintech
- Latin America
- Africa
- Asia
- Local Payment Methods
- Payment Processing
website: https://www.dlocal.com/
---
