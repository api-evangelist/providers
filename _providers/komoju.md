---
access_model:
  confidence: high
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Komoju Agentic Access
  operation_count: 28
  slug: komoju-agentic-access
  summary_line: 28 operations · 16 acting
api_count: 1
apis:
- baseURL: https://komoju.com/api/v1
  baseurl_source: declared
  description: Konbini payment barcodes for compatible convenience-store payments.
  name: KOMOJU Barcodes API
  slug: komoju-barcodes-api
- baseURL: https://komoju.com/api/v1
  baseurl_source: declared
  description: Store and manage customers with saved payment details for reuse.
  name: KOMOJU Customers API
  slug: komoju-customers-api
- baseURL: https://komoju.com/api/v1
  baseurl_source: declared
  description: Webhook events emitted by KOMOJU, queryable after the fact.
  name: KOMOJU Events API
  slug: komoju-events-api
- baseURL: https://komoju.com/api/v1
  baseurl_source: declared
  description: List the payment methods available to the authenticated merchant.
  name: KOMOJU Payment Methods API
  slug: komoju-payment-methods-api
- baseURL: https://komoju.com/api/v1
  baseurl_source: declared
  description: Create, capture, refund, cancel, and query payments across all payment methods.
  name: KOMOJU Payments API
  slug: komoju-payments-api
- baseURL: https://komoju.com/api/v1
  baseurl_source: declared
  description: Hosted checkout sessions that collect payment or customer details.
  name: KOMOJU Sessions API
  slug: komoju-sessions-api
- baseURL: https://komoju.com/api/v1
  baseurl_source: declared
  description: Recurring payments charged against a saved customer.
  name: KOMOJU Subscriptions API
  slug: komoju-subscriptions-api
- baseURL: https://komoju.com/api/v1
  baseurl_source: declared
  description: Tokenize payment details (short-term tokens and 3DS secure tokens).
  name: KOMOJU Tokens API
  slug: komoju-tokens-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KOMOJU Barcodes API
  slug: open-komoju-barcodes-api
- collection_type: open
  name: KOMOJU Barcodes Customers API
  slug: open-komoju-customers-api
- collection_type: open
  name: KOMOJU Barcodes Events API
  slug: open-komoju-events-api
- collection_type: open
  name: KOMOJU Barcodes Payment Methods API
  slug: open-komoju-payment-methods-api
- collection_type: open
  name: KOMOJU Barcodes Payments API
  slug: open-komoju-payments-api
- collection_type: open
  name: KOMOJU Barcodes Sessions API
  slug: open-komoju-sessions-api
- collection_type: open
  name: KOMOJU Barcodes Subscriptions API
  slug: open-komoju-subscriptions-api
- collection_type: open
  name: KOMOJU Barcodes Tokens API
  slug: open-komoju-tokens-api
- collection_type: open
  name: KOMOJU API
  slug: open-komoju
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/komoju-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/komoju-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/komoju-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/komoju
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/komoju
- group: company
  title: ''
  type: Website
  url: https://en.komoju.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.komoju.com
- group: commercial
  title: ''
  type: Plans
  url: plans/komoju-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/komoju-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/komoju-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://en.komoju.com/blog/
created: '2026-07-12'
description: KOMOJU is a Japan-focused global payment gateway operated by Degica. Its REST API lets web and e-commerce merchants accept a wide range of local and international payment methods through one interface - credit cards, convenience store (konbini) cash payments, bank transfer, Pay-easy (ATM), and e-money / mobile wallets such as PayPay, Merpay, au PAY, Rakuten Pay, LINE Pay, Alipay, and WeChat Pay - plus a hosted checkout (Sessions), tokenization, saved customers, subscriptions, and webhook events. Base URL is https://komoju.com/api/v1 with HTTP Basic authentication using a secret or publishable API key.
finops:
- name: Komoju Finops
  service_category: Payments and Financial Services
  slug: komoju-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/komoju.png
layout: provider
modified: '2026-07-12'
name: KOMOJU
nav: Providers
network: true
overview: 'KOMOJU publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Barcodes API, Customers API, Events API, and 5 more. Tagged areas include Payments, Payment Gateway, Japan, Konbini, and Cards.


  KOMOJU''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Komoju Plans Pricing
  plan_count: 3
  slug: komoju-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Komoju Rate Limits
  slug: komoju-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 27.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/komoju/refs/heads/main/screenshots/komoju-2026-07-25T224141.png
security:
- kind: authentication
  name: Komoju Authentication
  slug: komoju-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Komoju Domain Security
  slug: komoju-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: komoju
tags:
- Payments
- Payment Gateway
- Japan
- Konbini
- Cards
- PayPay
- Bank Transfer
- E-Money
- Checkout
- Fintech
website: https://en.komoju.com
---
