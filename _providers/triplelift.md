---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
api_count: 2
apis:
- description: Real-time bidding API implementing OpenRTB 2.x and Native Ads 1.2 specifications for demand partners to participate in native, banner, and video ad auctions. Supports bid request and response objects,
  name: TripleLift Exchange (TLX) API
  slug: triplelift-exchange-tlx-api
- description: REST API for supply partners and publishers to access network reporting, connected TV publisher network reports, and integration management. Provides synchronous and asynchronous query capabilities wi
  name: TripleLift Supply Publisher API
  slug: triplelift-supply-publisher-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/triplelift-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://triplelift.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.triplelift.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/triplelift
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triplelift/
- group: company
  title: ''
  type: Blog
  url: https://triplelift.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://triplelift.com/contact-us/
- group: other
  title: ''
  type: X
  url: https://twitter.com/TripleLiftHQ
- group: commercial
  title: ''
  type: Plans
  url: plans/triplelift-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/triplelift-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/triplelift-finops.yml
created: '2026-06-13'
description: TripleLift is a programmatic advertising company specializing in native inventory with APIs for managing native ad units, deals, targeting, viewability measurement, and creative quality. The platform provides OpenRTB-compliant exchange APIs for demand and supply partners, publisher network reporting, connected TV (CTV) advertising, and mobile SDKs for iOS and Android.
finops:
- name: Triplelift Finops
  service_category: ''
  slug: triplelift-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/triplelift.png
jsonld:
- class_count: 62
  name: Triplelift Context
  property_count: 0
  slug: triplelift-context
layout: provider
modified: '2026-06-13'
name: TripleLift
nav: Providers
network: true
overview: 'TripleLift publishes 2 APIs on the [APIs.io](https://apis.io/) network: Exchange (TLX) API and Supply Publisher API. Tagged areas include Programmatic Advertising, Native Advertising, Ad Exchange, OpenRTB, and Header Bidding.


  The TripleLift catalog on APIs.io includes 1 JSON-LD context.


  TripleLift''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Triplelift Plans Pricing
  plan_count: 2
  slug: triplelift-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 0
  name: Triplelift Rate Limits
  slug: triplelift-rate-limits
score:
  band: thin
  composite: 28.9
  delta: -4.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 33.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/triplelift/refs/heads/main/screenshots/triplelift-2026-06-20T195728.png
security:
- kind: domain-security
  name: Triplelift Domain Security
  slug: triplelift-domain-security
  summary_line: TLSv1.3 · DMARC
slug: triplelift
tags:
- Programmatic Advertising
- Native Advertising
- Ad Exchange
- OpenRTB
- Header Bidding
- Connected TV
- Supply Side Platform
- Demand Side Platform
website: https://triplelift.com
---
