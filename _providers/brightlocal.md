---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
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
api_count: 1
apis:
- description: RESTful API providing programmatic access to BrightLocal local SEO tools including local rank tracking, listings management, citation building, reputation management, and AI-powered insights. Uses API
  name: BrightLocal API
  slug: brightlocal-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightlocal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightlocal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.brightlocal.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/BrightLocal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bright-local-seo/
- group: company
  title: ''
  type: Blog
  url: https://www.brightlocal.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brightlocal.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brightlocal.com/
- group: other
  title: ''
  type: X
  url: https://x.com/brightlocal
- group: commercial
  title: ''
  type: Plans
  url: plans/brightlocal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brightlocal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brightlocal-finops.yml
created: '2026-06-13'
description: BrightLocal is a local SEO platform offering a REST API for managing local business listings, tracking Google rankings, monitoring reviews, auditing citations, and generating local search reports. Used by 15,000+ agencies and businesses to rank higher in local search.
finops:
- name: Brightlocal Finops
  service_category: ''
  slug: brightlocal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brightlocal.png
jsonld:
- class_count: 21
  name: Brightlocal Context
  property_count: 24
  slug: brightlocal-context
layout: provider
modified: '2026-06-13'
name: BrightLocal
nav: Providers
network: true
overview: 'BrightLocal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Local SEO, Business Listings, Rank Tracking, Reviews, and Citations.


  The BrightLocal catalog on APIs.io includes 1 JSON-LD context.


  BrightLocal''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Brightlocal Plans Pricing
  plan_count: 6
  slug: brightlocal-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 0
  name: Brightlocal Rate Limits
  slug: brightlocal-rate-limits
score:
  band: emerging
  composite: 26.2
  delta: -3.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 17.7
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brightlocal/refs/heads/main/screenshots/brightlocal-2026-06-20T173703.png
security:
- kind: domain-security
  name: Brightlocal Domain Security
  slug: brightlocal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brightlocal
tags:
- Local SEO
- Business Listings
- Rank Tracking
- Reviews
- Citations
website: https://www.brightlocal.com/
---
