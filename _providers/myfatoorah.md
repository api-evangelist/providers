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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Myfatoorah Agentic Access
  operation_count: 14
  slug: myfatoorah-agentic-access
  summary_line: 14 operations · 14 acting
api_count: 9
apis:
- description: Create invoices and payment links.
  name: MyFatoorah Invoicing API
  slug: myfatoorah-invoicing-api
- description: Inquire on invoice and transaction status.
  name: MyFatoorah Payment Status API
  slug: myfatoorah-payment-status-api
- description: Discover payment methods and execute payments against a gateway.
  name: MyFatoorah Payments API
  slug: myfatoorah-payments-api
- description: Recurring card payment management.
  name: MyFatoorah Recurring API
  slug: myfatoorah-recurring-api
- description: Full and partial refunds.
  name: MyFatoorah Refunds API
  slug: myfatoorah-refunds-api
- description: Embedded card-entry sessions and saved-card tokens.
  name: MyFatoorah Sessions API
  slug: myfatoorah-sessions-api
- description: Shipping lookups, charges, and pickups.
  name: MyFatoorah Shipping API
  slug: myfatoorah-shipping-api
- description: Marketplace supplier onboarding and split settlement.
  name: MyFatoorah Suppliers API
  slug: myfatoorah-suppliers-api
- description: Retrieve webhook events triggered by MyFatoorah.
  name: MyFatoorah Webhooks API
  slug: myfatoorah-webhooks-api
artifact_total: 16
collections:
- collection_type: open
  name: MyFatoorah API
  slug: open-myfatoorah
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/myfatoorah-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/myfatoorah-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/myfatoorah-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MyFatoorahHub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/myfatoorah
- group: company
  title: ''
  type: Website
  url: https://myfatoorah.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.myfatoorah.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/myfatoorah-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/myfatoorah-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/myfatoorah-finops.yml
created: '2026-07-12'
description: MyFatoorah is a Kuwait-based online payment gateway and invoicing platform serving merchants across the GCC and wider MENA region (Kuwait, Saudi Arabia, UAE, Qatar, Egypt, Bahrain, Oman, and Jordan). Its REST API lets businesses create invoices and payment links, execute and direct-charge card payments, run embedded checkout sessions, issue refunds, manage recurring payments, onboard marketplace suppliers, calculate shipping, and receive webhook notifications. MyFatoorah aggregates regional and international payment methods including KNET, mada, Benefit, Meeza, OmanNet, Visa, Mastercard, American Express, Apple Pay, Google Pay, and STC Pay. The API is region-scoped - a shared test host plus per-country live hosts - and authenticated with a Bearer API token.
finops:
- name: Myfatoorah Finops
  service_category: Payments and Financial Services
  slug: myfatoorah-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/myfatoorah.png
layout: provider
modified: '2026-07-12'
name: MyFatoorah
nav: Providers
network: true
overview: 'MyFatoorah publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Invoicing API, Payment Status API, Payments API, and 6 more. Tagged areas include Payments, Payment Gateway, Kuwait, GCC, and MENA.


  MyFatoorah''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Myfatoorah Plans Pricing
  plan_count: 3
  slug: myfatoorah-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 2
  name: Myfatoorah Rate Limits
  slug: myfatoorah-rate-limits
score:
  band: thin
  composite: 34.9
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.9
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Myfatoorah Authentication
  slug: myfatoorah-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Myfatoorah Domain Security
  slug: myfatoorah-domain-security
  summary_line: HSTS · DMARC
slug: myfatoorah
tags:
- Payments
- Payment Gateway
- Kuwait
- GCC
- MENA
- KNET
- mada
- Benefit
- Invoices
- Cards
- Fintech
website: https://myfatoorah.com/
---
