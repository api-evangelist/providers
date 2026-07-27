---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-07-27'
api_count: 7
apis:
- description: Comprehensive reporting API for querying account and campaign performance data with flexible filtering, metrics selection, and date range specification.
  name: Rokt Query API
  slug: rokt-query-api
- description: Enables sending conversion data and client events to Rokt to close the attribution loop for campaign performance tracking.
  name: Rokt Event API
  slug: rokt-event-api
- description: Supports integration of Rokt into ecommerce transaction flows, enabling placement of personalized offers during the checkout and confirmation moment.
  name: Rokt Cart API
  slug: rokt-cart-api
- description: Allows importing custom audience segments into Rokt for targeted offer delivery and campaign personalization.
  name: Rokt Custom Audience Import API
  slug: rokt-custom-audience-import-api
- description: Manages data removal requests within Rokt systems to support privacy compliance and data governance requirements.
  name: Rokt Data Deletion API
  slug: rokt-data-deletion-api
- description: Handles unsubscribe management for Rokt nurture campaigns, enabling partners to honor customer opt-outs.
  name: Rokt Nurture Unsubscribe API
  slug: rokt-nurture-unsubscribe-api
- description: Supports third-party integrations including mParticle for connecting Rokt with partner data platforms.
  name: Rokt Partnerships API
  slug: rokt-partnerships-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rokt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rokt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rokt.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rokt.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ROKT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rokt
- group: company
  title: ''
  type: Blog
  url: https://www.rokt.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rokt.com/products/product-overview
- group: other
  title: ''
  type: X
  url: https://x.com/rokt
- group: commercial
  title: ''
  type: Plans
  url: plans/rokt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rokt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rokt-finops.yml
created: '2026-06-13'
description: Rokt is an eCommerce technology platform that uses AI and machine learning to serve personalized non-endemic offers and ads during transaction moments. APIs cover ecommerce placement integrations, conversion event tracking, reporting and analytics, custom audience management, and data governance.
finops:
- name: Rokt Finops
  service_category: ''
  slug: rokt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rokt.png
jsonld:
- class_count: 36
  name: Rokt Context
  property_count: 8
  slug: rokt-context
layout: provider
modified: '2026-06-13'
name: Rokt
nav: Providers
network: true
overview: 'Rokt publishes 1 API on the [APIs.io](https://apis.io/) network: Query API. Tagged areas include eCommerce, Advertising, Transaction Moment, Personalization, and Offers.


  The Rokt catalog on APIs.io includes 1 JSON-LD context.


  Rokt''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Rokt Plans Pricing
  plan_count: 0
  slug: rokt-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 2
  name: Rokt Rate Limits
  slug: rokt-rate-limits
score:
  band: thin
  composite: 32.5
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 52.8
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rokt/refs/heads/main/screenshots/rokt-2026-06-20T193204.png
security:
- kind: domain-security
  name: Rokt Domain Security
  slug: rokt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rokt Vulnerability Disclosure
  slug: rokt-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rokt
tags:
- eCommerce
- Advertising
- Transaction Moment
- Personalization
- Offers
- Analytics
- Reporting
website: https://www.rokt.com
---
