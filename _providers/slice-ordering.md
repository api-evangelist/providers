---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: Logical, modeled grouping for the pizzeria (shop) records that anchor the Slice platform - profile, address, hours, service areas, and pickup/delivery availability. Reflected in the Owner's Portal sho
  name: Slice Shops API (Modeled)
  slug: slice-shops-api
- description: Logical, modeled grouping for a shop's menu - categories, items, sizes, toppings, and pricing (the Owner's Portal exposes shop menu items at owners.slicelife.com/shops/{id}/menu/items). No public endp
  name: Slice Menu API (Modeled)
  slug: slice-menu-api
- description: Logical, modeled grouping for online orders placed for pickup or delivery - cart, checkout, order status, and fulfillment. Central to Slice's per-order commercial model (a flat per-order fee to the sh
  name: Slice Orders API (Modeled)
  slug: slice-orders-api
- description: 'Logical, modeled grouping for the diner accounts, order history, and marketing/loyalty relationships that Slice manages on behalf of shops (consumer identity is handled via Auth0). No public endpoint '
  name: Slice Customers API (Modeled)
  slug: slice-customers-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slice-ordering-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/slicelife
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/slice
- group: company
  title: ''
  type: Website
  url: https://slicelife.com
- group: company
  title: ''
  type: Website
  url: https://slice.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.slicelife.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.slicebank.com/
- group: start
  title: ''
  type: SignUp
  url: https://slice.com/get-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://slice.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.slicelife.com/
created: '2026-07-04'
description: Slice is a done-for-you online ordering, marketing, payments, and point-of-sale platform for independent pizzerias, serving more than 19,000 shops across all 50 states and 3,000+ cities. Consumers order through slicelife.com and the Slice apps; shop owners run their business through slice.com, the Owner's Portal (owners.slicelife.com), and the Slice Register POS. Slice does publish a developer portal titled "Slice Public API" at developer.slicelife.com (built on Stoplight) and a separate merchant/banking API portal at developer.slicebank.com, but neither is an open, self-serve API - there is no public API-key signup and the endpoint reference is not openly rendered or documented for third parties. API access is partner-gated and arranged through Slice's partnerships team (partner@slicelife.com). The APIs listed below are logical groupings modeled from the platform's known merchant surfaces (shops, menus, orders, customers); no public OpenAPI definition is available, so no specification
  is included.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/slice-ordering.png
layout: provider
modified: '2026-07-04'
name: Slice
nav: Providers
network: true
overview: 'Slice publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Online Ordering, Food Delivery, Pizzerias, Restaurants, and Point of Sale.


  Slice''s developer surface includes documentation, signup flow, pricing, engineering blog, and 6 more developer resources.'
random_paper: 90
score:
  band: minimal
  composite: 10.5
  delta: -2.9
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Slice Ordering Domain Security
  slug: slice-ordering-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: slice-ordering
tags:
- Online Ordering
- Food Delivery
- Pizzerias
- Restaurants
- Point of Sale
- Payments
- SMB
- Partner API
website: https://slicelife.com
---
