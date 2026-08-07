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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Omise Agentic Access
  operation_count: 52
  slug: omise-agentic-access
  summary_line: 52 operations · 25 acting
api_count: 13
apis:
- description: Account profile and balance.
  name: Omise Account API
  slug: omise-account-api
- description: Cards saved against a customer.
  name: Omise Cards API
  slug: omise-cards-api
- description: Core payment object - authorize, capture, reverse, expire.
  name: Omise Charges API
  slug: omise-charges-api
- description: Saved customers and their reusable cards.
  name: Omise Customers API
  slug: omise-customers-api
- description: Cardholder chargebacks and evidence.
  name: Omise Disputes API
  slug: omise-disputes-api
- description: Account events backing webhooks.
  name: Omise Events API
  slug: omise-events-api
- description: Shareable payment links.
  name: Omise Links API
  slug: omise-links-api
- description: Bank-account recipients that transfers pay out to.
  name: Omise Recipients API
  slug: omise-recipients-api
- description: Full or partial refunds against a charge.
  name: Omise Refunds API
  slug: omise-refunds-api
- description: Recurring charges and transfers.
  name: Omise Schedules API
  slug: omise-schedules-api
- description: Non-card / local payment method sources.
  name: Omise Sources API
  slug: omise-sources-api
- description: Single-use card tokenization on the vault host.
  name: Omise Tokens API
  slug: omise-tokens-api
- description: Payouts from your balance to a recipient bank account.
  name: Omise Transfers API
  slug: omise-transfers-api
artifact_total: 20
collections:
- collection_type: open
  name: Omise (Opn Payments) API
  slug: open-omise
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/omise-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omise-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/omise-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/omise
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opn-payments
- group: company
  title: ''
  type: Website
  url: https://www.omise.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.omise.co
- group: commercial
  title: ''
  type: Plans
  url: plans/omise-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/omise-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/omise-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.omise.co/blog
created: '2026-07-12'
description: Omise (now Opn Payments, part of Opn) is a Southeast Asian online payment gateway serving Thailand, Japan, and Singapore. Its REST API lets developers accept card payments and local methods - PromptPay, TrueMoney, internet and mobile banking, installments, and QR wallets - through Charges, Tokens, Sources, and Customers, plus Refunds, Disputes, Transfers, Recipients, Schedules, Links, and Events/webhooks. Card data is tokenized on a separate PCI-scoped vault host. The company rebranded from Omise to Opn in 2022; the API keeps the api.omise.co and vault.omise.co hosts.
finops:
- name: Omise Finops
  service_category: Payments and Financial Services
  slug: omise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/omise.png
layout: provider
modified: '2026-07-12'
name: Omise
nav: Providers
network: true
overview: 'Omise publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account API, Cards API, Charges API, and 10 more. Tagged areas include Payments, Payment Gateway, Thailand, Southeast Asia, and Charges.


  Omise''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Omise Plans Pricing
  plan_count: 3
  slug: omise-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 2
  name: Omise Rate Limits
  slug: omise-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Omise Authentication
  slug: omise-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Omise Domain Security
  slug: omise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: omise
tags:
- Payments
- Payment Gateway
- Thailand
- Southeast Asia
- Charges
- Tokens
- Sources
- PromptPay
- Cards
- Fintech
website: https://www.omise.co
---
