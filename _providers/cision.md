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
api_count: 3
apis:
- description: REST API for CisionOne that allows connection of media monitoring data with internal tools and BI platforms. Provides access to mention streams, aggregated analytics, and media coverage data. Response
  name: CisionOne API
  slug: cisionone-api
- description: API providing access to Cision's media contacts database with over 1.4 million journalist, blogger, and influencer contacts for targeted PR outreach and media list management.
  name: Cision Media Database API
  slug: media-database-api
- description: 'API for distributing press releases through PR Newswire''s wire service, enabling programmatic submission, distribution management, and delivery confirmation for press releases across local, national, '
  name: PR Newswire Distribution API
  slug: pr-distribution-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cision.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cision.atlassian.net/wiki/spaces/CSM/pages/26385776684/CisionOne+-+API
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cision
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cision
- group: company
  title: ''
  type: Blog
  url: https://www.cision.com/us/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cision.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://oneuptime.cision.com/
- group: other
  title: ''
  type: X
  url: https://x.com/cision
- group: commercial
  title: ''
  type: Plans
  url: plans/cision-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cision-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cision-finops.yml
created: '2026-06-13'
description: Cision is an AI-powered PR and earned media software platform offering REST APIs for media database access, press release distribution, media monitoring, analytics, and influencer identification. CisionOne provides a REST API that connects media monitoring data with internal tools, BI platforms, and reporting systems.
finops:
- name: Cision Finops
  service_category: ''
  slug: cision-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cision.png
jsonld:
- class_count: 0
  name: Cision Context
  property_count: 5
  slug: cision-context
layout: provider
modified: '2026-06-13'
name: Cision
nav: Providers
network: true
overview: 'Cision publishes 1 API on the [APIs.io](https://apis.io/) network: CisionOne API. Tagged areas include PR Software, Public Relations, Earned Media, Media Monitoring, and Press Release Distribution.


  The Cision catalog on APIs.io includes 1 JSON-LD context.


  Cision''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Cision Plans Pricing
  plan_count: 5
  slug: cision-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 2
  name: Cision Rate Limits
  slug: cision-rate-limits
score:
  band: thin
  composite: 39.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 47.2
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 39.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cision/refs/heads/main/screenshots/cision-2026-06-20T174406.png
security:
- kind: domain-security
  name: Cision Domain Security
  slug: cision-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cision
tags:
- PR Software
- Public Relations
- Earned Media
- Media Monitoring
- Press Release Distribution
- Media Database
- Influencer Identification
- Analytics
website: https://www.cision.com/
---
