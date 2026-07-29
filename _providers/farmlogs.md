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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Field boundary mapping and per-field record-keeping, the original core of FarmLogs. This capability now lives inside Bushel Farm (formerly Bushel Farm/FarmLogs); no self-serve public REST reference, b
  name: FarmLogs Fields
  slug: fields
- description: In-season multispectral satellite imagery used to spot yield threats, stress, and management issues field-by-field. A marquee FarmLogs feature historically; no openly documented public imagery API end
  name: FarmLogs Satellite Imagery / NDVI
  slug: satellite-imagery
- description: 'Field-level rainfall and weather tracking with season-over-season comparisons. Bushel Farm continues to market a "Stop Checking Your Rain Gauges" rainfall feature descended from FarmLogs, but exposes '
  name: FarmLogs Weather & Rainfall
  slug: weather
- description: 'Yield tracking, cost-of-production, and field/crop/farm-level profit-and-loss calculations. Bushel Farm''s marketing page notes production records can be shared "into your ERP or database using an API '
  name: FarmLogs Yield & Profitability
  slug: yield-and-profitability
- description: Field activity logging and in-field scouting notes, plus machine/equipment activity ingested from John Deere Operations Center and Climate FieldView integrations. These are inbound partner integration
  name: FarmLogs Activities & Scouting
  slug: activities-and-scouting
artifact_total: 10
collections:
- collection_type: open
  name: FarmLogs API
  slug: open-farmlogs
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/farmlogs-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/farmlogs
- group: company
  title: ''
  type: Website
  url: https://www.farmlogs.com
- group: docs
  title: ''
  type: Documentation
  url: https://bushelpowered.com/solutions/farm-management/
- group: commercial
  title: ''
  type: Plans
  url: plans/farmlogs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/farmlogs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/farmlogs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://bushelpowered.com/blog
created: '2026-07-03'
description: FarmLogs was a farm management platform founded in 2011 (by Jesse Vollmar and Brad Koch, operating as AgriSight Inc.) offering field mapping, in-season satellite imagery, weather/rainfall tracking, yield estimation, and profitability tools for row-crop farmers. FarmLogs was acquired by Bushel in June 2021, and in March 2023 Bushel retired the FarmLogs brand in favor of "Bushel Farm," the next generation of its farm management software. As of this review, farmlogs.com 301-redirects to bushelfarm.com, which itself redirects to bushelpowered.com - the standalone FarmLogs product and website no longer exist. Bushel does publish a public API, but it is for a separate product line (Bushel Fulfillment and Bushel Production, covering grain contracts and scale-ticket data for grain merchandising) rather than for the FarmLogs-lineage farm-management capabilities (fields, imagery, weather, yield). No self-serve, openly documented public API exists for the farm-management product as of
  the review date.
finops:
- name: Farmlogs Finops
  service_category: Software as a Service
  slug: farmlogs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/farmlogs.png
layout: provider
modified: '2026-07-03'
name: FarmLogs
nav: Providers
network: true
overview: 'FarmLogs publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Fields, Satellite Imagery / NDVI, Weather & Rainfall, and 2 more. Tagged areas include Agriculture, Farm Management, Precision Agriculture, Satellite Imagery, and Acquired.


  FarmLogs'' developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Farmlogs Plans Pricing
  plan_count: 1
  slug: farmlogs-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 1
  name: Farmlogs Rate Limits
  slug: farmlogs-rate-limits
score:
  band: emerging
  composite: 25.3
  delta: -3.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/farmlogs/refs/heads/main/screenshots/farmlogs-2026-07-25T214231.png
security:
- kind: domain-security
  name: Farmlogs Domain Security
  slug: farmlogs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: farmlogs
tags:
- Agriculture
- Farm Management
- Precision Agriculture
- Satellite Imagery
- Acquired
- Discontinued Brand
website: https://www.farmlogs.com
---
