---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
api_count: 1
apis:
- description: REST API for querying multi-touch attribution data, channel performance metrics, customer journeys, and media spend effectiveness across all integrated marketing channels.
  name: Rockerbox API
  slug: rockerbox-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rockerbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rockerbox.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.rockerbox.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/rockerbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rockerbox
- group: company
  title: ''
  type: Blog
  url: https://www.rockerbox.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rockerbox.com/plans
- group: other
  title: ''
  type: X
  url: https://x.com/rockerbox
- group: commercial
  title: ''
  type: Plans
  url: plans/rockerbox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rockerbox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rockerbox-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.rockerbox.com/blog/rss.xml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/rockerbox-context.jsonld
created: 2026-06-13
description: Rockerbox is a unified marketing measurement platform with a REST API for querying multi-touch attribution data, channel performance, customer journeys, and media spend effectiveness across 100+ integrations, combining MTA, Marketing Mix Modeling, and incrementality testing on a SOC2-certified data foundation.
finops:
- name: Rockerbox Finops
  service_category: ''
  slug: rockerbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rockerbox.png
jsonld:
- class_count: 7
  name: Rockerbox Context
  property_count: 6
  slug: rockerbox-context
layout: provider
modified: 2026-06-13
name: Rockerbox
nav: Providers
network: true
overview: 'Rockerbox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing Attribution, Multi-Touch Attribution, Marketing Mix Modeling, Incrementality Testing, and Media Spend.


  The Rockerbox catalog on APIs.io includes 1 JSON-LD context.


  Rockerbox''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Rockerbox Plans Pricing
  plan_count: 1
  slug: rockerbox-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Rockerbox Rate Limits
  slug: rockerbox-rate-limits
score:
  band: thin
  composite: 33.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.8
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 33.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rockerbox/refs/heads/main/screenshots/rockerbox-2026-06-20T193150.png
security:
- kind: domain-security
  name: Rockerbox Domain Security
  slug: rockerbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rockerbox
tags:
- Marketing Attribution
- Multi-Touch Attribution
- Marketing Mix Modeling
- Incrementality Testing
- Media Spend
- Customer Journeys
- Marketing Analytics
website: https://www.rockerbox.com/
---
