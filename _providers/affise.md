---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: REST API for the Affise Performance platform enabling admins and affiliates to manage offers, track conversions, retrieve statistics, handle publisher payouts, and automate billing operations programm
  name: Affise Performance API
  slug: affise-performance-api
- description: Mobile Measurement Partner API enabling mobile app attribution tracking, install measurement, event tracking, and audience analytics for iOS, Android, and cross-platform mobile applications.
  name: Affise MMP API
  slug: affise-mmp-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/affise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://affise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help-center.affise.com/en/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/affise
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/affise-com/
- group: company
  title: ''
  type: Blog
  url: https://affise.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://affise.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.affise.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/GetAffise
- group: commercial
  title: ''
  type: Plans
  url: plans/affise-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/affise-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/affise-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://affise.com/blog/feed/
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/affise-context.jsonld
created: '2026-06-13'
description: Affise is a performance marketing platform with a REST API for managing affiliate offers, publishers, conversions, payouts, and accessing detailed campaign analytics. The API supports both admin and affiliate panel operations using API key authentication with GET and POST methods across statistics, conversions, offers, partners, and billing endpoints.
finops:
- name: Affise Finops
  service_category: ''
  slug: affise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/affise.png
jsonld:
- class_count: 37
  name: Affise Context
  property_count: 4
  slug: affise-context
layout: provider
modified: '2026-06-13'
name: Affise
nav: Providers
network: true
overview: 'Affise publishes 1 API on the [APIs.io](https://apis.io/) network: Performance API. Tagged areas include Affiliate Marketing, Performance Marketing, Conversions, Publishers, and Analytics.


  The Affise catalog on APIs.io includes 1 JSON-LD context.


  Affise''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Affise Plans Pricing
  plan_count: 7
  slug: affise-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 0
  name: Affise Rate Limits
  slug: affise-rate-limits
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/affise/refs/heads/main/screenshots/affise-2026-06-20T165649.png
security:
- kind: domain-security
  name: Affise Domain Security
  slug: affise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: affise
tags:
- Affiliate Marketing
- Performance Marketing
- Conversions
- Publishers
- Analytics
- Attribution
website: https://affise.com/
---
