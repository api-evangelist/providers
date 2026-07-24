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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: REST API for submitting order and purchase data to Northbeam for attribution processing. Accepts batches of up to 1,000 orders per request via POST with JSON payload.
  name: Northbeam Orders API
  slug: orders-api
- description: REST API for uploading hourly spend records from non-integrated ad platforms so Northbeam can attribute revenue to channel-level spend accurately.
  name: Northbeam Spend API
  slug: spend-api
- description: REST API for exporting attribution performance metrics including revenue, transactions, CAC, AOV, and creative analytics across multiple attribution windows and models.
  name: Northbeam Data Export API
  slug: data-export-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/northbeam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.northbeam.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.northbeam.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/north-beam
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/northbeam
- group: company
  title: ''
  type: Blog
  url: https://www.northbeam.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.northbeam.io/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/northbeam
- group: commercial
  title: ''
  type: Plans
  url: plans/northbeam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/northbeam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/northbeam-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/northbeam-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/northbeam-context.jsonld
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-13'
description: Multi-touch marketing attribution platform for e-commerce with a REST API for accessing channel-level ROAS, media mix modeling data, and creative performance metrics.
finops:
- name: Northbeam Finops
  service_category: ''
  slug: northbeam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/northbeam.png
jsonld:
- class_count: 11
  name: Northbeam Context
  property_count: 38
  slug: northbeam-context
layout: provider
modified: '2026-06-13'
name: Northbeam
nav: Providers
network: true
overview: 'Northbeam publishes 1 API on the [APIs.io](https://apis.io/) network: Orders API. Tagged areas include Marketing Attribution, Multi-Touch Attribution, E-Commerce, ROAS, and Media Mix Modeling.


  The Northbeam catalog on APIs.io includes 1 JSON-LD context.


  Northbeam''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Northbeam Plans Pricing
  plan_count: 3
  slug: northbeam-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 7
  name: Northbeam Rate Limits
  slug: northbeam-rate-limits
score:
  band: thin
  composite: 41.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.5
    developer_ergonomics: 10.9
    discoverability: 87.5
    governance: 13.2
    operational_transparency: 36.8
  previous_composite: 41.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/northbeam/refs/heads/main/screenshots/northbeam-2026-06-20T190413.png
security:
- kind: domain-security
  name: Northbeam Domain Security
  slug: northbeam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: northbeam
tags:
- Marketing Attribution
- Multi-Touch Attribution
- E-Commerce
- ROAS
- Media Mix Modeling
- Creative Analytics
- Performance Marketing
website: https://www.northbeam.io
---
