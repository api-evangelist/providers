---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: 'Core REST API for generating price quotes for truckload shipments, tendering loads to Uber Freight''s carrier network, and cancelling tenders. Returns guaranteed spot rates with expiration timestamps. '
  name: Uber Freight Loads API
  slug: uber-freight-loads-api
- description: Scheduling API implementing the Scheduling Standards Consortium (SSC) Technical Standard for automated dock appointment booking across Uber Freight's TMS network of 1,500+ facilities. Enables carriers
  name: Uber Freight Scheduling API
  slug: uber-freight-scheduling-api
- description: Provides real-time shipment visibility from pickup through delivery across Uber Freight's carrier network. Used by TMS integrations with Oracle Transportation Management, SAP, Blue Yonder, and BluJay.
  name: Uber Freight Real-Time Tracking API
  slug: uber-freight-real-time-tracking-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uber-freight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uberfreight.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uberfreight.com/get-started
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/uber
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uber-freight/
- group: company
  title: ''
  type: Blog
  url: https://www.uberfreight.com/en-US/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uberfreight.com/en-US/partners/integrations
- group: operate
  title: ''
  type: StatusPage
  url: https://uber.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/UberFreight
- group: commercial
  title: ''
  type: Plans
  url: plans/uber-freight-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uber-freight-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uber-freight-finops.yml
created: '2026-06-13'
description: Uber Freight is a digital freight brokerage platform providing 24/7 access to truckload freight with instant quoting and booking, real-time shipment visibility, lane management, and carrier network pricing. Its REST APIs enable shippers and TMS platforms to generate price quotes, tender loads, cancel tenders, and automate facility scheduling — all backed by a network of 50,000+ carriers across the U.S. and Europe. API access uses OAuth 2.0 client credentials and requires approval of the freight.loads scope through the Uber developer portal.
finops:
- name: Uber Freight Finops
  service_category: ''
  slug: uber-freight-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uber-freight.png
layout: provider
modified: '2026-06-13'
name: Uber Freight
nav: Providers
network: true
overview: 'Uber Freight publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Freight, Logistics, Trucking, Shipping, and Transportation.


  Uber Freight''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Uber Freight Plans Pricing
  plan_count: 2
  slug: uber-freight-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 4
  name: Uber Freight Rate Limits
  slug: uber-freight-rate-limits
score:
  band: emerging
  composite: 21.3
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 21.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uber-freight/refs/heads/main/screenshots/uber-freight-2026-06-20T195933.png
security:
- kind: domain-security
  name: Uber Freight Domain Security
  slug: uber-freight-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: uber-freight
tags:
- Freight
- Logistics
- Trucking
- Shipping
- Transportation
- Supply Chain
- Truckload
- Carrier Network
- TMS
- Digital Freight Broker
website: https://www.uberfreight.com/
---
