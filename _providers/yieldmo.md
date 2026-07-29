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
api_count: 4
apis:
- description: JavaScript SDK providing publisher-side API methods for managing ad placements and requesting page views in single-page applications and infinite scroll implementations. Enables dynamic ad loading wit
  name: Yieldmo JavaScript SDK API
  slug: yieldmo-javascript-sdk-api
- description: Header bidding integration adapter for Prebid.js enabling publishers to receive bids from Yieldmo's exchange for display and video inventory. Supports placement-based targeting with optional bid floor
  name: Yieldmo Prebid.js Bid Adapter
  slug: yieldmo-prebidjs-bid-adapter
- description: Prebid.js module enabling publishers to integrate Yieldmo Synthetic Outstream ads by automatically creating placements and injecting the Yieldmo SDK. Requires a Yieldmo placement ID and Google Ad Mana
  name: Yieldmo Synthetic Inventory Module
  slug: yieldmo-synthetic-inventory-module
- description: Proprietary programmatic exchange and creative intelligence platform offering curated inventory access, contextual targeting, attention analytics, and deal management for advertisers and demand-side p
  name: Yieldmo YMax Platform API
  slug: yieldmo-ymax-platform-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yieldmo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yieldmo.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/yieldmo/yieldmo-js-sdk/wiki
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/yieldmo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yieldmo
- group: company
  title: ''
  type: Blog
  url: https://yieldmo.com/category/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://yieldmo.com/solutions/
- group: operate
  title: ''
  type: StatusPage
  url: https://yieldmo.com
- group: other
  title: ''
  type: X
  url: https://x.com/yieldmo
- group: commercial
  title: ''
  type: Plans
  url: plans/yieldmo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yieldmo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yieldmo-finops.yml
created: '2026-06-13'
description: Yieldmo is a programmatic native advertising marketplace and smart exchange that differentiates and enhances the value of ad inventory for buyers and sellers. The platform provides REST APIs and JavaScript SDKs for managing ad placements, proprietary ad formats, contextual targeting, publisher inventory monetization, and campaign performance analytics powered by attention data and machine learning.
finops:
- name: Yieldmo Finops
  service_category: ''
  slug: yieldmo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yieldmo.png
jsonld:
- class_count: 0
  name: Yieldmo Context
  property_count: 0
  slug: yieldmo
layout: provider
modified: '2026-06-13'
name: Yieldmo
nav: Providers
network: true
overview: 'Yieldmo publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Programmatic, Native Advertising, Ad Exchange, and Publisher Monetization.


  The Yieldmo catalog on APIs.io includes 1 JSON-LD context.


  Yieldmo''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Yieldmo Plans Pricing
  plan_count: 3
  slug: yieldmo-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 0
  name: Yieldmo Rate Limits
  slug: yieldmo-rate-limits
score:
  band: emerging
  composite: 24.4
  delta: -2.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 27.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yieldmo/refs/heads/main/screenshots/yieldmo-2026-06-20T201742.png
security:
- kind: domain-security
  name: Yieldmo Domain Security
  slug: yieldmo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: yieldmo
tags:
- Advertising
- Programmatic
- Native Advertising
- Ad Exchange
- Publisher Monetization
- Header Bidding
- Contextual Targeting
- Ad Formats
- Supply-Side Platform
- SSP
website: https://yieldmo.com
---
