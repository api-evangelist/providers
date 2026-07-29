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
api_count: 3
apis:
- description: REST API for brands to manage partnership campaigns, track conversions, process commissions, manage contracts, and report on partnership performance.
  name: Impact Brand API
  slug: brand-api
- description: REST API for media partners and publishers to access campaigns, report on content performance, manage commission tracking, and query earning reports.
  name: Impact Partner API
  slug: partner-api
- description: REST API for agencies to manage multiple client accounts, consolidate reporting across brands, and automate partnership operations at scale.
  name: Impact Agency API
  slug: agency-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/impact-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/impact-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://impact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://integrations.impact.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ImpactInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/impactdotcom
- group: company
  title: ''
  type: Blog
  url: https://impact.com/press-releases/
- group: commercial
  title: ''
  type: Pricing
  url: https://impact.com/pricing/
- group: other
  title: ''
  type: X
  url: https://x.com/impactdotcom
- group: commercial
  title: ''
  type: Plans
  url: plans/impact-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/impact-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/impact-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/impact-context.jsonld
created: '2026-06-13'
description: Partnership management platform with a REST API for managing affiliate relationships, tracking conversions, paying partners, and reporting on partnership performance across brands.
finops:
- name: Impact Finops
  service_category: ''
  slug: impact-finops
graphqls:
- description: This document describes the conceptual GraphQL schema for the Impact partnership automation platform (impact.com). Impact provides REST APIs for brands, publishers, and agencies to manage affiliate an
  name: Impact GraphQL Schema
  slug: impact-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/impact.png
jsonld:
- class_count: 0
  name: Impact Context
  property_count: 2
  slug: impact-context
layout: provider
modified: '2026-06-13'
name: Impact
nav: Providers
network: true
overview: 'Impact publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Affiliate, Partnerships, Performance Marketing, Commission, and Tracking.


  The Impact catalog on APIs.io includes 1 JSON-LD context.


  Impact''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Impact Plans Pricing
  plan_count: 4
  slug: impact-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 0
  name: Impact Rate Limits
  slug: impact-rate-limits
score:
  band: thin
  composite: 31.7
  delta: 7.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 49.4
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/impact/refs/heads/main/screenshots/impact-2026-06-20T183254.png
security:
- kind: domain-security
  name: Impact Domain Security
  slug: impact-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Impact Vulnerability Disclosure
  slug: impact-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: impact
tags:
- Affiliate
- Partnerships
- Performance Marketing
- Commission
- Tracking
- Creator Economy
- Partner Management
website: https://impact.com/
---
