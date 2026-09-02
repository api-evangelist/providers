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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Omise Agentic Access
  operation_count: 52
  slug: omise-agentic-access
  summary_line: 52 operations · 25 acting
api_count: 1
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
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Omise (Opn Payments) Account API
  slug: open-omise-account-api
- collection_type: open
  name: Omise (Opn Payments) Account Cards API
  slug: open-omise-cards-api
- collection_type: open
  name: Omise (Opn Payments) Account Charges API
  slug: open-omise-charges-api
- collection_type: open
  name: Omise (Opn Payments) Account Customers API
  slug: open-omise-customers-api
- collection_type: open
  name: Omise (Opn Payments) Account Disputes API
  slug: open-omise-disputes-api
- collection_type: open
  name: Omise (Opn Payments) Account Events API
  slug: open-omise-events-api
- collection_type: open
  name: Omise (Opn Payments) Account Links API
  slug: open-omise-links-api
- collection_type: open
  name: Omise (Opn Payments) Account Recipients API
  slug: open-omise-recipients-api
- collection_type: open
  name: Omise (Opn Payments) Account Refunds API
  slug: open-omise-refunds-api
- collection_type: open
  name: Omise (Opn Payments) Account Schedules API
  slug: open-omise-schedules-api
- collection_type: open
  name: Omise (Opn Payments) Account Sources API
  slug: open-omise-sources-api
- collection_type: open
  name: Omise (Opn Payments) Account Tokens API
  slug: open-omise-tokens-api
- collection_type: open
  name: Omise (Opn Payments) Account Transfers API
  slug: open-omise-transfers-api
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
random_paper: 16
rate_limits:
- limit_count: 2
  name: Omise Rate Limits
  slug: omise-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.7
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 36.8
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omise/refs/heads/main/screenshots/omise-2026-08-07T190141.png
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
