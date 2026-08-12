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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Skydropx Agentic Access
  operation_count: 32
  slug: skydropx-agentic-access
  summary_line: 32 operations · 14 acting
api_count: 9
apis:
- description: Reusable saved addresses and carrier validation.
  name: Skydropx Address Templates API
  slug: skydropx-address-templates-api
- description: OAuth2 client-credentials token issuance.
  name: Skydropx Authentication API
  slug: skydropx-authentication-api
- description: Carrier services, packagings, and consignment-note codes.
  name: Skydropx Catalog API
  slug: skydropx-catalog-api
- description: Prepaid credit balance and extra charges.
  name: Skydropx Finance API
  slug: skydropx-finance-api
- description: Orders and their generated shipping label URLs.
  name: Skydropx Orders and Labels API
  slug: skydropx-orders-and-labels-api
- description: Schedule and manage carrier pickups (recolecciones).
  name: Skydropx Pickups API
  slug: skydropx-pickups-api
- description: Multi-carrier rate quotations for a parcel.
  name: Skydropx Quotations API
  slug: skydropx-quotations-api
- description: Create, list, retrieve, cancel, and protect shipments.
  name: Skydropx Shipments API
  slug: skydropx-shipments-api
- description: Track shipments and report tracking events.
  name: Skydropx Tracking API
  slug: skydropx-tracking-api
artifact_total: 16
collections:
- collection_type: open
  name: Skydropx Pro API
  slug: open-skydropx
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/skydropx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skydropx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skydropx-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skydropx
- group: company
  title: ''
  type: Website
  url: https://www.skydropx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skydropx.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/skydropx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skydropx-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/skydropx-finops.yml
created: '2026-07-12'
description: Skydropx is a Mexican multi-carrier shipping and logistics platform that lets e-commerce sellers and businesses compare rates, generate labels, schedule pickups, and track parcels across national and international carriers from a single API. Its modern Skydropx Pro API (base https://pro.skydropx.com/api/v1) is a REST interface secured with OAuth2 client-credentials Bearer tokens and covers quotations, shipments, labels/orders, pickups, address templates, tracking, and account credit balances. A separate classic Skydropx API (https://api.skydropx.com/v1, authenticated with an API key Token header) and a Radar tracking API also exist. Billing is prepaid - the platform is free to use and you pay per label from a wallet balance.
finops:
- name: Skydropx Finops
  service_category: Shipping and Logistics
  slug: skydropx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skydropx.png
layout: provider
modified: '2026-07-12'
name: Skydropx
nav: Providers
network: true
overview: 'Skydropx publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Address Templates API, Authentication API, Catalog API, and 6 more. Tagged areas include Shipping, Logistics, Multi-Carrier, Mexico, and Latin America.


  Skydropx''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Skydropx Plans Pricing
  plan_count: 2
  slug: skydropx-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 3
  name: Skydropx Rate Limits
  slug: skydropx-rate-limits
score:
  band: thin
  composite: 32.9
  delta: -3.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.3
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
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Skydropx Authentication
  slug: skydropx-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Skydropx Domain Security
  slug: skydropx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: skydropx
tags:
- Shipping
- Logistics
- Multi-Carrier
- Mexico
- Latin America
- Labels
- Rates
- Parcels
- Tracking
- Fulfillment
- SaaS
website: https://www.skydropx.com/
---
