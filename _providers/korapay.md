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
- acting_count: 15
  human_in_the_loop: 0
  name: Korapay Agentic Access
  operation_count: 30
  slug: korapay-agentic-access
  summary_line: 30 operations · 15 acting
api_count: 7
apis:
- description: Real-time available and pending balances per currency.
  name: Kora Balances API
  slug: korapay-balances-api
- description: Pay-ins - card, bank transfer, mobile money, and pay-with-bank.
  name: Kora Charges API
  slug: korapay-charges-api
- description: Exchange rates and multi-currency conversions.
  name: Kora Currency Conversion API
  slug: korapay-currency-conversion-api
- description: Bank / mobile-money lookups, account resolution, and payout utilities.
  name: Kora Misc API
  slug: korapay-misc-api
- description: Disbursements to bank accounts and mobile money wallets.
  name: Kora Payouts API
  slug: korapay-payouts-api
- description: Refunds for completed pay-in transactions.
  name: Kora Refunds API
  slug: korapay-refunds-api
- description: Dedicated NGN and USD virtual bank accounts.
  name: Kora Virtual Bank Accounts API
  slug: korapay-virtual-bank-accounts-api
artifact_total: 14
collections:
- collection_type: open
  name: Kora (Korapay) Merchant API
  slug: open-korapay
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/korapay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/korapay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/korapay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/korapay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/korapay
- group: company
  title: ''
  type: Website
  url: https://www.korahq.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.korapay.com/docs/getting-started
- group: commercial
  title: ''
  type: Plans
  url: plans/korapay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/korapay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/korapay-finops.yml
created: '2026-07-12'
description: Kora (formerly Korapay) is a pan-African payments infrastructure company that lets businesses collect payments, disburse payouts, run settlements, issue cards, verify identities, and check balances across African markets. The Kora merchant REST API (base https://api.korapay.com/merchant/api/v1) supports pay-ins via card, bank transfer, mobile money, and pay-with-bank; single, bulk, and remittance payouts; NGN and USD virtual bank accounts; balances; refunds; and multi-currency conversion, with test and live modes authenticated by public and secret API keys and webhook events verified with an HMAC SHA-256 signature.
finops:
- name: Korapay Finops
  service_category: Payments and Financial Services
  slug: korapay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/korapay.png
layout: provider
modified: '2026-07-12'
name: Kora
nav: Providers
network: true
overview: 'Kora publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Balances API, Charges API, Currency Conversion API, and 4 more. Tagged areas include Payments, Payment Gateway, Africa, Nigeria, and Collections.


  Kora''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Korapay Plans Pricing
  plan_count: 3
  slug: korapay-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 4
  name: Korapay Rate Limits
  slug: korapay-rate-limits
score:
  band: thin
  composite: 36.4
  delta: -1.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.4
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.2
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Korapay Authentication
  slug: korapay-authentication
  summary_line: http/hmac/encryption · 4 schemes
- kind: domain-security
  name: Korapay Domain Security
  slug: korapay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: korapay
tags:
- Payments
- Payment Gateway
- Africa
- Nigeria
- Collections
- Payouts
- Disbursements
- Virtual Bank Account
- Cards
- Fintech
website: https://www.korahq.com
---
