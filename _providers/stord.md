---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - security
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for managing orders, inventory, shipments, and returns within the Stord commerce fulfillment platform. Built with an API-first design using JSON:API specification and OpenAPI annotations. Sup
  name: Stord API
  slug: stord-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/stord/security/stord-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/stord-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/stord/security/stord-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stord-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stord.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.stord.com/integrations
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/stordco
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stord
- group: company
  title: ''
  type: Blog
  url: https://www.stord.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stord.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stord.com/
- group: other
  title: ''
  type: X
  url: https://x.com/getstord
- group: commercial
  href: https://artifacts.apis.io/stord/plans/stord-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stord-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/stord/rate-limits/stord-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stord-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/stord/finops/stord-finops.yml
  title: ''
  type: FinOps
  url: finops/stord-finops.yml
created: '2026-06-13'
description: Stord is a commerce fulfillment platform that combines physical warehouse infrastructure with integrated software to manage omnichannel logistics for DTC and B2B brands. The platform provides REST APIs for managing orders, inventory, shipments, and returns across a network of 20+ fulfillment nodes, with pre-built integrations for Shopify, BigCommerce, Magento, WooCommerce, Amazon, and ERP systems such as Oracle NetSuite. Stord One Commerce (OMS) and Stord One Warehouse (WMS) deliver real-time supply chain visibility and AI-powered parcel optimization, powering over $10 billion in annual commerce for brands including AG1, Native, and Legion Athletics.
finops:
- has_sources: false
  method: generated
  name: Stord Finops
  primary_unit: ''
  service_category: ''
  slug: stord-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stord.png
layout: provider
modified: '2026-06-13'
name: Stord
nav: Providers
network: true
overview: 'Stord is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Commerce Fulfillment, Order Management, Inventory, Shipment Tracking, and Returns Management.


  Stord''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Stord Plans Pricing
  plan_count: 0
  slug: stord-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Stord Rate Limits
  slug: stord-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 19.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stord/stord-2026-06-20T194604.png
security:
- kind: domain-security
  name: Stord Domain Security
  slug: stord-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stord Trust Center
  slug: stord-trust-center
  summary_line: SOC 2, GDPR
slug: stord
tags:
- Commerce Fulfillment
- Order Management
- Inventory
- Shipment Tracking
- Returns Management
- Warehouse Management
- Logistics
- Supply Chain
- Shopify Integration
- BigCommerce Integration
- ERP Integration
- EDI
website: https://www.stord.com/
---
