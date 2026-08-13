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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Pin Payments Agentic Access
  operation_count: 24
  slug: pin-payments-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 4
apis:
- description: Tokenize and retrieve stored card details.
  name: Pin Payments Cards API
  slug: pin-payments-cards-api
- description: Create and manage charges against cards or customers.
  name: Pin Payments Charges API
  slug: pin-payments-charges-api
- description: Store customer profiles with payment sources for repeat billing.
  name: Pin Payments Customers API
  slug: pin-payments-customers-api
- description: Issue and inspect refunds against charges.
  name: Pin Payments Refunds API
  slug: pin-payments-refunds-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pin-payments-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pin-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pin-payments-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pinpayments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pin-payments
- group: company
  title: ''
  type: Website
  url: https://pinpayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pinpayments.com/developers/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://pinpayments.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://dashboard.pinpayments.com/sign_up
- group: start
  title: ''
  type: Login
  url: https://dashboard.pinpayments.com/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pinpayments.com/legals/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pinpayments.com/legals/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://pinpayments.com/blog
created: '2025-02-17'
description: A complete payments solution, built for speed and simplicity around your unique business needs. The Pin Payments API enables developers to charge cards, manage customers, store payment sources, issue refunds, and run subscriptions through a RESTful JSON interface secured with HTTP Basic authentication.
finops:
- name: Pin Payments Finops
  service_category: API
  slug: pin-payments-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pin-payments.png
layout: provider
modified: '2026-05-19'
name: Pin Payments
nav: Providers
network: true
overview: 'Pin Payments publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cards API, Charges API, Customers API, and 1 more. Tagged areas include Payments, Cards, Subscriptions, and Refunds.


  Pin Payments'' developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Pin Payments Plans Pricing
  plan_count: 3
  slug: pin-payments-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Pin Payments Rate Limits
  slug: pin-payments-rate-limits
score:
  band: thin
  composite: 36.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.7
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pin-payments/refs/heads/main/screenshots/pin-payments-2026-06-20T191711.png
security:
- kind: authentication
  name: Pin Payments Authentication
  slug: pin-payments-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pin Payments Domain Security
  slug: pin-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pin-payments
tags:
- Payments
- Cards
- Subscriptions
- Refunds
website: https://pinpayments.com/
---
