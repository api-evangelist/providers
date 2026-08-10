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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Shippit Agentic Access
  operation_count: 10
  slug: shippit-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 6
apis:
- description: Initiate carrier bookings for orders.
  name: Shippit Book API
  slug: shippit-book-api
- description: Retrieve shipping labels and documents for an order.
  name: Shippit Label API
  slug: shippit-label-api
- description: Merchant account settings, operating hours, and webhooks.
  name: Shippit Merchant API
  slug: shippit-merchant-api
- description: Create, retrieve, update, and cancel shipping orders.
  name: Shippit Orders API
  slug: shippit-orders-api
- description: Live multi-carrier shipping quotes.
  name: Shippit Quote API
  slug: shippit-quote-api
- description: Pull-based order tracking.
  name: Shippit Tracking API
  slug: shippit-tracking-api
artifact_total: 13
collections:
- collection_type: open
  name: Shippit API
  slug: open-shippit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shippit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shippit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shippit-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shippit
- group: company
  title: ''
  type: Website
  url: https://www.shippit.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shippit.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/shippit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shippit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shippit-finops.yml
created: '2026-07-12'
description: Shippit is an Australian multi-carrier shipping and fulfillment platform for retailers and e-commerce merchants across Australia, New Zealand, and Southeast Asia. Its REST API (v3) lets merchants request live carrier quotes, create and cancel orders, book consignments with carriers, retrieve A6 shipping labels and pick slips, and track parcels via pull requests or push webhooks. Authentication is a per-merchant API key passed as an HTTP Bearer token, with a staging sandbox and a production environment.
finops:
- name: Shippit Finops
  service_category: Shipping and Logistics
  slug: shippit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shippit.png
layout: provider
modified: '2026-07-12'
name: Shippit
nav: Providers
network: true
overview: 'Shippit publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Book API, Label API, Merchant API, and 3 more. Tagged areas include Shipping, Logistics, Fulfillment, Australia, and APAC.


  Shippit''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Shippit Plans Pricing
  plan_count: 3
  slug: shippit-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 1
  name: Shippit Rate Limits
  slug: shippit-rate-limits
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Shippit Authentication
  slug: shippit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shippit Domain Security
  slug: shippit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shippit
tags:
- Shipping
- Logistics
- Fulfillment
- Australia
- APAC
- Multi-Carrier
- Labels
- Tracking
- Parcels
- E-commerce Logistics
- SaaS
website: https://www.shippit.com
---
