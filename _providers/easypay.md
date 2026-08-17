---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: REST API for the EasyPay/Fawaterak payment gateway. Authenticated with a vendor Bearer token, it lists available payment methods, creates invoice and payment links, initiates payment on an invoice, an
  name: Fawaterak API v2
  slug: fawaterak-api-v2
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://fawaterk.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.fawaterk.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://app.fawaterk.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://app.fawaterk.com/documentation
- group: start
  title: ''
  type: SignUp
  url: https://fawaterk.com/join-us/
- group: start
  title: ''
  type: Login
  url: https://app.fawaterk.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://fawaterk.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fawaterk.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fawaterk.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://fawaterk.com/blogs/
- group: operate
  title: ''
  type: Support
  url: https://fawaterk.com/contact-us/
- group: auth
  title: ''
  type: Authentication
  url: authentication/easypay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/easypay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/easypay-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/easypay-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/easypay-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/easypay-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/easypay-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/easypay-mcp.yml
created: '2026-07-17'
description: EasyPay (Fawaterak) is an Egyptian digital payment gateway that lets businesses accept online payments and send invoices and payment links over WhatsApp or SMS without needing a website. It supports Visa, MasterCard, Meeza, Fawry, mobile wallets, and cash collection, and serves more than 20,000 businesses across retail and e-commerce, healthcare, education, real estate, logistics, and hospitality. The Fawaterak REST API (base https://app.fawaterk.com/api/v2/) is authenticated with a vendor Bearer token and exposes operations to list payment methods, create invoice/payment links, initiate payment on an invoice, and retrieve invoice data, with rate limiting signalled via X-RateLimit-* response headers.
image: https://fawaterk.com/wp-content/uploads/2023/01/fawaterak-logo.png
layout: provider
mcp_servers:
- description: ''
  name: easypay-mcp.yml
  slug: easypay-mcpyml
modified: '2026-07-18'
name: EasyPay
nav: Providers
network: true
overview: 'EasyPay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Payment Gateway, Invoicing, and Fintech.


  EasyPay''s developer surface includes documentation, API reference, signup flow, pricing, engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 1
  name: Easypay Rate Limits
  slug: easypay-rate-limits
score:
  band: emerging
  composite: 27.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 27.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/easypay/refs/heads/main/screenshots/easypay-2026-07-25T212717.png
security:
- kind: authentication
  name: Easypay Authentication
  slug: easypay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Easypay Domain Security
  slug: easypay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: easypay
tags:
- Company
- Payments
- Payment Gateway
- Invoicing
- Fintech
- E-commerce
- Egypt
- Online Payments
website: https://fawaterk.com
---
