---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: United Auto Credit Corporation dealer financing integration providing non-prime auto lending origination, 24/7 application access, instant credit decisions, and contract printing for dealership partne
  name: UACC Dealer Financing Portal
  slug: uacc-dealer-portal
- description: AI-powered automotive retail analytics platform providing vehicle appraisal intelligence, market promotion data, and profit optimization tools for dealerships, leveraging machine learning across 7 mil
  name: CarStory Automotive Analytics Platform
  slug: carstory-analytics
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vroom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vroom.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.vroom.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.unitedautocredit.net/dealers/faq
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/vroom-project
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vroom
- group: company
  title: ''
  type: Blog
  url: https://ir.vroom.com/news-events/press-releases/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unitedautocredit.net/dealerpartners.aspx
- group: operate
  title: ''
  type: StatusPage
  url: https://ir.vroom.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/vroomcars
- group: commercial
  title: ''
  type: Plans
  url: plans/vroom-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vroom-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vroom-finops.yml
created: '2026-06-13'
description: Vroom, Inc. is a Houston-based automotive technology company that operated as an online used vehicle retailer offering no-haggle pricing, nationwide home delivery, and digital financing. In January 2024 Vroom ceased direct-to-consumer e-commerce vehicle sales and pivoted to focus on its two B2B subsidiaries — United Auto Credit Corporation (UACC), a non-prime automotive finance lender serving 7,300+ dealerships, and CarStory, an AI-powered analytics and digital retail services platform processing over 7 million vehicle listings per day. The company exited Chapter 11 bankruptcy protection in January 2025. Current API-adjacent services include the UACC dealer portal for financing origination and the CarStory analytics platform for inventory appraisal, promotion, and profit tracking — both available to dealer partners under negotiated B2B agreements.
finops:
- name: Vroom Finops
  service_category: ''
  slug: vroom-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vroom.png
jsonld:
- class_count: 0
  name: Vroom Context
  property_count: 6
  slug: vroom-context
layout: provider
modified: '2026-06-13'
name: Vroom
nav: Providers
network: true
overview: 'Vroom publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Used Vehicles, Vehicle Financing, Auto Finance, and Dealer Analytics.


  The Vroom catalog on APIs.io includes 1 JSON-LD context.


  Vroom''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Vroom Plans Pricing
  plan_count: 2
  slug: vroom-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 3
  name: Vroom Rate Limits
  slug: vroom-rate-limits
score:
  band: emerging
  composite: 25.8
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 28.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vroom/refs/heads/main/screenshots/vroom-2026-06-20T201143.png
security:
- kind: domain-security
  name: Vroom Domain Security
  slug: vroom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vroom
tags:
- Automotive
- Used Vehicles
- Vehicle Financing
- Auto Finance
- Dealer Analytics
- AI Analytics
- Non-Prime Lending
- Vehicle Inventory
website: https://www.vroom.com
---
