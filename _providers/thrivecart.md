---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: REST API for a ThriveCart account. Reads products, bump offers, upsells, downsells and their pricing options; searches transactions and affiliates; reads customer records; refunds transactions; cancel
  name: ThriveCart API
  slug: thrivecart-api
artifact_total: 12
asyncapis:
- description: ThriveCart delivers account events to subscriber endpoints over HTTP POST. Two surfaces exist and they do not share event names. **Event Subscription API (this document).** Created programmatically wi
  name: ThriveCart Event Subscriptions
  slug: thrivecart-events-asyncapi
collections:
- collection_type: postman
  name: ThriveCart API
  slug: postman-thrivecart-api
- collection_type: open
  name: ThriveCart API
  slug: open-thrivecart-api
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thrivecart-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://thrivecart.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.thrivecart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.thrivecart.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.thrivecart.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.thrivecart.com/documentation/
- group: build
  title: ''
  type: Postman
  url: https://apidocs.thrivecart.com/
- group: operate
  title: ''
  type: Support
  url: https://support.thrivecart.com/
- group: company
  title: ''
  type: Blog
  url: https://thrivecart.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://thrivecart.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thrivecart
- group: operate
  title: ''
  type: Roadmap
  url: https://thrivecart.com/resources/roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://thrivecart.com/products/proplus/
- group: start
  title: ''
  type: SignUp
  url: https://checkout.thrivecart.com/thrivecart-standard-monthly-plan/
- group: start
  title: ''
  type: Login
  url: https://thrivecart.com/signin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thrivecart.com/legal/thrivecart/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thrivecart.com/legal/thrivecart/?tab=privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://thrivecart.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://thrivecart.com/blog/category/product-updates/
- group: build
  title: ''
  type: Packages
  url: packages/thrivecart-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/thrivecart-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thrivecart-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/thrivecart-security.txt
- group: auth
  title: ''
  type: Security
  url: security/thrivecart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/thrivecart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thrivecart-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thrivecart-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thrivecart-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/thrivecart-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/thrivecart-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/thrivecart-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/thrivecart-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/thrivecart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thrivecart-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thrivecart-llms.txt
created: '2026-08-12'
description: ThriveCart is a hosted shopping cart, checkout and course platform for creators, coaches and digital-product sellers, operated by ThriveCart LLC. It sells one-time and recurring digital and physical products through customisable checkout pages with order bumps, one-click upsells and downsells, A/B testing, abandoned-cart recovery, sales-tax automation and a built-in affiliate centre, and bundles a learning-management product (ThriveCart Learn / ThriveCart Academy). Payments are processed through Stripe, PayPal, Authorize.net and ThrivePay Installments rather than by ThriveCart itself. The public ThriveCart API is a bearer-token REST surface at https://thrivecart.com/api/external covering products, bump offers, upsells, downsells, pricing options, transactions, customers, subscriptions, affiliates, Learn students and event subscriptions, with an account-wide webhook surface and a targeted Event Subscription API alongside it.
image: https://thrivecart.com/wp-content/uploads/2025/07/TC-logo-on-White.png
layout: provider
mcp_servers:
- description: ''
  name: thrivecart-mcp.yml
  slug: thrivecart-mcpyml
modified: '2026-08-12'
name: ThriveCart
nav: Providers
network: true
overview: 'ThriveCart publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Checkout, Shopping Cart, Payments, and eCommerce.


  The ThriveCart catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ThriveCart''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Thrivecart Plans Pricing
  plan_count: 3
  slug: thrivecart-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 1
  name: Thrivecart Rate Limits
  slug: thrivecart-rate-limits
scopes:
- name: Thrivecart Scopes
  scope_count: 0
  slug: thrivecart-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.1
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 59.7
    developer_ergonomics: 58.7
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 73.7
  previous_composite: 63.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Thrivecart Authentication
  slug: thrivecart-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Thrivecart Domain Security
  slug: thrivecart-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Thrivecart Vulnerability Disclosure
  slug: thrivecart-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Thrivecart Trust Center
  slug: thrivecart-trust-center
  summary_line: PCI DSS, GDPR, CCPA
slug: thrivecart
tags:
- Company
- Checkout
- Shopping Cart
- Payments
- eCommerce
- Subscriptions
- Affiliate Marketing
- Learning Management
- Creator Economy
- Webhooks
website: https://thrivecart.com/
---
