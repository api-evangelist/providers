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
- acting_count: 8
  human_in_the_loop: 0
  name: Geidea Agentic Access
  operation_count: 10
  slug: geidea-agentic-access
  summary_line: 10 operations · 8 acting
api_count: 1
apis:
- description: Programmatically create, update, fetch, delete, and send (by email or SMS) shareable payment links so customers can pay without a full storefront integration. Available for Egypt and the UAE. Exact re
  name: Geidea Pay by Link API
  slug: geidea-pay-by-link-api
- description: Create, update, fetch, delete, and send payment invoices (KSA) that customers settle through a Geidea-hosted payment page. Exact request paths are documented in the Geidea API reference; endpoint sche
  name: Geidea Pay by Invoice API
  slug: geidea-pay-by-invoice-api
- description: Create a payment session for the hosted Geidea Checkout page.
  name: Geidea Checkout API
  slug: geidea-checkout-api
- description: Server-to-server 3-D Secure authentication and card payment.
  name: Geidea Direct API API
  slug: geidea-direct-api-api
- description: Retrieve stored instrument tokens for cards on file.
  name: Geidea Tokenization API
  slug: geidea-tokenization-api
- description: Capture, void, refund, cancel, and fetch transactions and orders.
  name: Geidea Transaction Management API
  slug: geidea-transaction-management-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Geidea Payment Gateway Checkout API
  slug: open-geidea-checkout-api
- collection_type: open
  name: Geidea Payment Gateway Checkout Direct API API
  slug: open-geidea-direct-api-api
- collection_type: open
  name: Geidea Payment Gateway Checkout Tokenization API
  slug: open-geidea-tokenization-api
- collection_type: open
  name: Geidea Payment Gateway Checkout Transaction Management API
  slug: open-geidea-transaction-management-api
- collection_type: open
  name: Geidea Payment Gateway API
  slug: open-geidea
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/geidea-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geidea-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/geidea-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GeideaSolutions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geidea
- group: company
  title: ''
  type: Website
  url: https://www.geidea.net
- group: docs
  title: ''
  type: Documentation
  url: https://docs.geidea.net
- group: commercial
  title: ''
  type: Plans
  url: plans/geidea-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/geidea-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/geidea-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://geidea.net/merchants/en/about-us/news-room.html
created: '2026-07-12'
description: Geidea is a Saudi-headquartered fintech and payments platform serving merchants across the MENA region (Saudi Arabia, Egypt, and the UAE). Its Payment Gateway lets merchants accept card and wallet payments through a hosted Geidea Checkout (HPP) page or a server-to-server Direct API for PCI-DSS-compliant merchants, covering the full transaction lifecycle - create session, 3-D Secure authentication, pay, capture, void, refund, cancel, tokenization, Pay by Link, and Pay by Invoice - with support for mada, Visa, Mastercard, Apple Pay, Google Pay, Meeza QR, and BNPL. Payments are authenticated with a merchant public key and API password over HTTP Basic auth plus an HMAC request signature, and results are delivered back to merchants via webhook (callback) notifications.
finops:
- name: Geidea Finops
  service_category: Payments and Financial Services
  slug: geidea-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geidea.png
layout: provider
modified: '2026-07-12'
name: Geidea
nav: Providers
network: true
overview: 'Geidea publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Checkout API, Direct API API, Tokenization API, and 1 more. Tagged areas include Payments, Payment Gateway, Saudi Arabia, Egypt, and MENA.


  Geidea''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Geidea Plans Pricing
  plan_count: 2
  slug: geidea-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Geidea Rate Limits
  slug: geidea-rate-limits
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 56.3
    developer_ergonomics: 27.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 33.2
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
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geidea/refs/heads/main/screenshots/geidea-2026-07-25T215522.png
security:
- kind: authentication
  name: Geidea Authentication
  slug: geidea-authentication
  summary_line: http/signature · 2 schemes
- kind: domain-security
  name: Geidea Domain Security
  slug: geidea-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: geidea
tags:
- Payments
- Payment Gateway
- Saudi Arabia
- Egypt
- MENA
- mada
- Cards
- Point-of-Sale
- Checkout
- Fintech
website: https://www.geidea.net
---
