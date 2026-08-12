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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: REST API v4 for managing business locations, syndicating listings to 80+ directories, aggregating and responding to reviews, tracking local search rankings with heatmaps, and retrieving unified analyt
  name: Synup API
  slug: synup-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.synup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.synup.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/synup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synup
- group: company
  title: ''
  type: Blog
  url: https://www.synup.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.synup.com/en/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.synup.com/
- group: other
  title: ''
  type: X
  url: https://x.com/synupinc
- group: commercial
  title: ''
  type: Plans
  url: plans/synup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/synup-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/synup-finops.yml
created: '2026-06-13'
description: Synup is a local marketing platform providing a REST API for managing business listings, syndicating location data to 80+ directories, tracking and responding to reviews, and monitoring local search performance. The platform serves marketing agencies with white-label tools covering listings sync, reputation management, social media, SEO, and analytics.
finops:
- name: Synup Finops
  service_category: ''
  slug: synup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synup.png
jsonld:
- class_count: 33
  name: Synup Context
  property_count: 2
  slug: synup-context
layout: provider
modified: '2026-06-13'
name: Synup
nav: Providers
network: true
overview: 'Synup publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Local Marketing, Listings Management, Reputation Management, Local SEO, and Reviews.


  The Synup catalog on APIs.io includes 1 JSON-LD context.


  Synup''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Synup Plans Pricing
  plan_count: 3
  slug: synup-plans-pricing
random_paper: 111
rate_limits:
- limit_count: 0
  name: Synup Rate Limits
  slug: synup-rate-limits
score:
  band: thin
  composite: 33.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synup/refs/heads/main/screenshots/synup-2026-06-20T194835.png
security:
- kind: domain-security
  name: Synup Domain Security
  slug: synup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: synup
tags:
- Local Marketing
- Listings Management
- Reputation Management
- Local SEO
- Reviews
- Social Media
- Analytics
website: https://www.synup.com/
---
