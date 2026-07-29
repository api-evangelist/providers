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
- acting_count: 17
  human_in_the_loop: 1
  name: Polar Sh Agentic Access
  operation_count: 39
  slug: polar-sh-agentic-access
  summary_line: 39 operations · 17 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: Benefits (entitlements) attached to products.
  name: Polar benefits API
  slug: polar-sh-benefits-api
- description: Hosted checkout sessions and reusable checkout links.
  name: Polar checkouts API
  slug: polar-sh-checkouts-api
- description: Customer-facing portal endpoints (Customer Session token).
  name: Polar customer_portal API
  slug: polar-sh-customer-portal-api
- description: Customers, external IDs, and aggregated customer state.
  name: Polar customers API
  slug: polar-sh-customers-api
- description: Usage event ingestion for metered billing.
  name: Polar events API
  slug: polar-sh-events-api
- description: License key issuance, validation, and activation.
  name: Polar license_keys API
  slug: polar-sh-license-keys-api
- description: Usage meters aggregating ingested events.
  name: Polar meters API
  slug: polar-sh-meters-api
- description: Orders, invoices, and receipts.
  name: Polar orders API
  slug: polar-sh-orders-api
- description: Product catalog and embedded pricing.
  name: Polar products API
  slug: polar-sh-products-api
- description: Recurring subscriptions.
  name: Polar subscriptions API
  slug: polar-sh-subscriptions-api
- description: Webhook endpoint management and deliveries.
  name: Polar webhooks API
  slug: polar-sh-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: Polar API
  slug: open-polar-sh
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/polar-sh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polar-sh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polar-sh-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/polarsource
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/polar-software
- group: company
  title: ''
  type: Website
  url: https://polar.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://polar.sh/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/polar-sh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/polar-sh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/polar-sh-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://polar.sh/blog
created: '2026-06-21'
description: Polar is an open-source, developer-first monetization platform that acts as a Merchant of Record (MoR), handling billing, payments, and global sales tax so software teams can sell digital products, subscriptions, usage-based billing, and license keys. The Polar API (https://api.polar.sh/v1) exposes products, prices, checkouts, customers, subscriptions, orders, benefits, license keys, a customer portal, usage meters/events, and webhooks behind Bearer organization access tokens. Not affiliated with Polar Electro (fitness wearables) or the Polaris design system.
finops:
- name: Polar Sh Finops
  service_category: Billing and Payments
  slug: polar-sh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/polar-sh.png
layout: provider
modified: '2026-06-21'
name: Polar
nav: Providers
network: true
overview: 'Polar publishes 11 APIs on the [APIs.io](https://apis.io/) network, including benefits API, checkouts API, customer_portal API, and 8 more. Tagged areas include Billing, Payments, Merchant of Record, Monetization, and Subscriptions.


  Polar''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Polar Sh Plans Pricing
  plan_count: 6
  slug: polar-sh-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Polar Sh Rate Limits
  slug: polar-sh-rate-limits
score:
  band: thin
  composite: 34.7
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
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
  name: Polar Sh Authentication
  slug: polar-sh-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Polar Sh Domain Security
  slug: polar-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: polar-sh
tags:
- Billing
- Payments
- Merchant of Record
- Monetization
- Subscriptions
- Usage Based Billing
website: https://polar.sh/
---
