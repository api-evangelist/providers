---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: ShipHero's primary public API built on GraphQL, providing programmatic access to warehouse management data and operations including inventory, orders, shipments, purchase orders, returns, wholesale or
  name: ShipHero GraphQL API
  slug: graphql-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/shiphero-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shiphero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shiphero.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shiphero.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.shiphero.com/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Shiphero
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shiphero
- group: company
  title: ''
  type: Blog
  url: https://shiphero.com/blog
- group: other
  title: ''
  type: X
  url: https://x.com/weareshiphero
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shiphero.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/shiphero-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shiphero-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shiphero-finops.yml
created: '2026-06-12'
description: ShipHero is a warehouse management system (WMS) and fulfillment platform designed for brands and third-party logistics (3PL) providers operating eCommerce direct-to-consumer fulfillment. The platform exposes a GraphQL public API with 69 queries, 120 mutations, and 599 types covering inventory, orders, shipments, purchase orders, returns, and warehouse operations. Authentication uses JWT bearer tokens obtained via username and password credentials, with access tokens valid for 28 days and refresh-token-based renewal. ShipHero enforces a credit-based rate limit system and supports 18 webhook event types for real-time integration with fulfillment workflows.
finops:
- name: Shiphero Finops
  service_category: ''
  slug: shiphero-finops
graphqls:
- description: 'ShipHero exposes a single GraphQL endpoint that provides programmatic access to warehouse management and fulfillment operations. The API covers inventory, orders, shipments, purchase orders, returns, '
  name: ShipHero GraphQL API
  slug: shiphero-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shiphero.png
jsonld:
- class_count: 46
  name: Shiphero Context
  property_count: 37
  slug: shiphero-context
layout: provider
modified: '2026-06-12'
name: ShipHero
nav: Providers
network: true
overview: 'ShipHero publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Warehouse Management, Fulfillment, E-Commerce, GraphQL, and Inventory.


  The ShipHero catalog on APIs.io includes 1 JSON-LD context.


  ShipHero''s developer surface includes documentation, getting-started guide, engineering blog, and 10 more developer resources.'
plans:
- name: Shiphero Plans Pricing
  plan_count: 3
  slug: shiphero-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 6
  name: Shiphero Rate Limits
  slug: shiphero-rate-limits
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 47.9
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 40.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shiphero/refs/heads/main/screenshots/shiphero-2026-06-20T193816.png
security:
- kind: domain-security
  name: Shiphero Domain Security
  slug: shiphero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Shiphero Trust Center
  slug: shiphero-trust-center
  summary_line: SOC 2, GDPR
slug: shiphero
tags:
- Warehouse Management
- Fulfillment
- E-Commerce
- GraphQL
- Inventory
- Order
- Shipments
- 3PL
- Logistics
website: https://shiphero.com/
---
