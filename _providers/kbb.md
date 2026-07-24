---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: RESTful API providing access to Kelley Blue Book vehicle data, values, and content. Endpoints cover vehicle information, new and used pricing, expert and consumer ratings and reviews, cost-of-ownershi
  name: InfoDriver Web Service (IDWS) 4.0
  slug: idws
- description: High-volume vehicle identification number processing service for enriching large vehicle inventories with KBB data and valuations. Suited for lenders, fleet operators, and auction platforms.
  name: Batch VIN Service
  slug: batch-vin
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kbb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kbb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kbb.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/enovaauto/kbb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kelley-blue-book
- group: company
  title: ''
  type: Blog
  url: https://b2b.kbb.com/resources/
- group: commercial
  title: ''
  type: Pricing
  url: https://b2b.kbb.com/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.isitdownrightnow.com/kbb.com.html
- group: other
  title: ''
  type: X
  url: https://x.com/KelleyBlueBook
- group: commercial
  title: ''
  type: Plans
  url: plans/kbb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kbb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kbb-finops.yml
created: 2026-06-13
description: Kelley Blue Book (KBB) is the vehicle valuation and automotive information platform trusted by consumers, dealers, lenders, and OEMs since 1926. KBB provides REST APIs for new and used car values, pricing data, vehicle specifications, expert and consumer ratings, cost-of-ownership projections, fuel cost calculations, and dealer trade-in tools. The InfoDriver Web Service (IDWS) 4.0 delivers JSON over HTTPS authenticated via API key, and is licensed to B2B partners including automotive dealers, lenders, fleet operators, and industry data consumers. Values are updated twice monthly to reflect current market conditions.
finops:
- name: Kbb Finops
  service_category: ''
  slug: kbb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kbb.png
layout: provider
modified: 2026-06-13
name: Kelley Blue Book
nav: Providers
network: true
overview: 'Kelley Blue Book publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Vehicle Valuation, Car Pricing, Trade-In, and Vehicle Data.


  Kelley Blue Book''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Kbb Plans Pricing
  plan_count: 3
  slug: kbb-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 5
  name: Kbb Rate Limits
  slug: kbb-rate-limits
score:
  band: emerging
  composite: 28.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 28.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kbb/refs/heads/main/screenshots/kbb-2026-06-20T183932.png
security:
- kind: domain-security
  name: Kbb Domain Security
  slug: kbb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kbb
tags:
- Automotive
- Vehicle Valuation
- Car Pricing
- Trade-In
- Vehicle Data
- Dealer Tools
website: https://www.kbb.com/
---
