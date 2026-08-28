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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Tap Payments Agentic Access
  operation_count: 29
  slug: tap-payments-agentic-access
  summary_line: 29 operations · 13 acting
api_count: 10
apis:
- description: Server-to-server HTTP POST callbacks (Instant Payment Notification) that Tap sends to your configured endpoint when a charge, authorize, invoice, or recurring payment changes state. Payloads are signe
  name: Tap Payments Webhooks
  slug: tap-payments-webhooks
- description: Authorize (hold) funds for later capture.
  name: Tap Payments Authorize API
  slug: tap-payments-authorize-api
- description: Business, merchant, and destination onboarding.
  name: Tap Payments Business API
  slug: tap-payments-business-api
- description: Saved cards (card-on-file) attached to a customer.
  name: Tap Payments Cards API
  slug: tap-payments-cards-api
- description: Charge a card or other payment source.
  name: Tap Payments Charges API
  slug: tap-payments-charges-api
- description: Customer records for vaulting and recurring payments.
  name: Tap Payments Customers API
  slug: tap-payments-customers-api
- description: Hosted, payable invoices.
  name: Tap Payments Invoices API
  slug: tap-payments-invoices-api
- description: Settlements paid out to the merchant.
  name: Tap Payments Payouts API
  slug: tap-payments-payouts-api
- description: Refund a captured charge.
  name: Tap Payments Refunds API
  slug: tap-payments-refunds-api
- description: Single-use tokenization of cards and wallets.
  name: Tap Payments Tokens API
  slug: tap-payments-tokens-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tap Payments Authorize API
  slug: open-tap-payments-authorize-api
- collection_type: open
  name: Tap Payments Authorize Business API
  slug: open-tap-payments-business-api
- collection_type: open
  name: Tap Payments Authorize Cards API
  slug: open-tap-payments-cards-api
- collection_type: open
  name: Tap Payments Authorize Charges API
  slug: open-tap-payments-charges-api
- collection_type: open
  name: Tap Payments Authorize Customers API
  slug: open-tap-payments-customers-api
- collection_type: open
  name: Tap Payments Authorize Invoices API
  slug: open-tap-payments-invoices-api
- collection_type: open
  name: Tap Payments Authorize Payouts API
  slug: open-tap-payments-payouts-api
- collection_type: open
  name: Tap Payments Authorize Refunds API
  slug: open-tap-payments-refunds-api
- collection_type: open
  name: Tap Payments Authorize Tokens API
  slug: open-tap-payments-tokens-api
- collection_type: open
  name: Tap Payments API
  slug: open-tap-payments
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tap-payments-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tap-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tap-payments-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tap-Payments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tap-payments
- group: company
  title: ''
  type: Website
  url: https://www.tap.company
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tap.company/docs/get-started
- group: commercial
  title: ''
  type: Plans
  url: plans/tap-payments-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tap-payments-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tap-payments-finops.yml
created: '2026-07-12'
description: Tap Payments is a payment gateway and financial infrastructure provider for the Middle East and North Africa (MENA). Its REST API lets merchants accept online payments across the GCC and Egypt - cards (Visa, Mastercard, Amex), local schemes (mada in Saudi Arabia, KNET in Kuwait, Benefit in Bahrain), and wallets (Apple Pay, Google Pay) - through Charges and Authorize/Capture flows, with Tokens for saved cards, Customers, Refunds, Invoices, Payouts, and merchant onboarding via the Business API. Authentication is a secret API key passed as a Bearer token, with separate test and live keys issued from the Tap dashboard.
finops:
- name: Tap Payments Finops
  service_category: Payments and Financial Services
  slug: tap-payments-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tap-payments.png
layout: provider
modified: '2026-07-12'
name: Tap Payments
nav: Providers
network: true
overview: 'Tap Payments publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authorize API, Business API, Cards API, and 6 more. Tagged areas include Payments, Fintech, Payment Gateway, MENA, and Middle East.


  Tap Payments'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Tap Payments Plans Pricing
  plan_count: 3
  slug: tap-payments-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Tap Payments Rate Limits
  slug: tap-payments-rate-limits
score:
  band: thin
  composite: 35.5
  delta: 1.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.7
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Tap Payments Authentication
  slug: tap-payments-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tap Payments Domain Security
  slug: tap-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tap-payments
tags:
- Payments
- Fintech
- Payment Gateway
- MENA
- Middle East
- Online Payments
- Charges
- Cards
- KNET
- mada
- Financial Infrastructure
website: https://www.tap.company
---
