---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Imgix Agentic Access
  operation_count: 6
  slug: imgix-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 2
apis:
- description: The imgix Rendering API can optimize your images, improve your page speed, and make it easy to create responsive designs. Images are processed and delivered in real-time via URL parameters.
  name: Imgix Rendering API
  slug: imgix-rendering-api
- description: The Sources API from Imgix — 4 operation(s) for sources.
  name: Imgix Sources API
  slug: imgix-sources-api
artifact_total: 26
collections:
- collection_type: open
  name: imgix Management API
  slug: open-imgix
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/imgix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imgix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/imgix-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/imgix
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/imgix
- group: company
  title: ''
  type: Website
  url: https://imgix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.imgix.com/
- group: operate
  title: ''
  type: Support
  url: https://support.imgix.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.imgix.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://imgix.com/blog
created: '2024-11-13'
description: imgix is a real-time image processing and CDN service that helps developers optimize images, improve page speed, and build responsive designs. The imgix Rendering API provides powerful image transformation and optimization capabilities directly through URL parameters.
features:
- 'Starter $25/mo: 100 credits, 50 GB storage, 100 GB bandwidth'
- 'Basic $75/mo: 375 credits, 187.5 GB storage, 375 GB bandwidth'
- 'Midrange $150/mo: 830 credits'
- 'Growth $300/mo: 1,875 credits'
- 'Growth Plus $500/mo: 3,570 credits'
- 'Enterprise: custom credits and workflows'
- Per-extra-credit declines from $0.25 (Starter) to $0.12 (Growth Plus)
- On-the-fly URL-based image transformations
- 100+ transformation parameters
- 'Render API: unmetered requests (counted in credits)'
- 'Management API: 100 req/sec/source'
- Master image counts toward storage
- Webhooks for source/asset events
- Auto-format (WebP/AVIF), auto-quality, auto-compress
- Video processing (separate Video product)
- Asset Manager DAM and Asset Cleanup
finops:
- name: Imgix Finops
  service_category: Image CDN
  slug: imgix-finops
graphqls:
- description: This conceptual GraphQL schema models the Imgix real-time image processing and CDN API. Imgix provides powerful on-the-fly image transformation and optimization through URL parameters, a management AP
  name: Imgix GraphQL Schema
  slug: imgix-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imgix.png
layout: provider
modified: '2026-05-04'
name: Imgix
nav: Providers
network: true
overview: 'Imgix publishes 1 API on the [APIs.io](https://apis.io/) network: Sources API. Tagged areas include CDN, Image Optimization, Image Processing, and Media.


  Imgix''s developer surface includes authentication, documentation, support, engineering blog, and 6 more developer resources.'
plans:
- name: Imgix Plans Pricing
  plan_count: 6
  slug: imgix-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 3
  name: Imgix Rate Limits
  slug: imgix-rate-limits
score:
  band: thin
  composite: 31.1
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 61.2
    developer_ergonomics: 26.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imgix/refs/heads/main/screenshots/imgix-2026-06-20T183253.png
security:
- kind: authentication
  name: Imgix Authentication
  slug: imgix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Imgix Domain Security
  slug: imgix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imgix
tags:
- CDN
- Image Optimization
- Image Processing
- Media
website: https://imgix.com/
---
