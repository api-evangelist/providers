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
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: REST API enabling publishers to pull programmatic and direct sell reporting data for their native ad placements, including impressions, revenue, and performance metrics, using token-based authenticati
  name: Sharethrough Publisher Reporting API
  slug: sharethrough-publisher-reporting-api
- description: OpenRTB-based bidder adapter integration enabling SSP/DSP connections through the Prebid.js header bidding framework for native, display, and video ad formats with support for placement keys and first
  name: Sharethrough Header Bidding (Prebid) API
  slug: sharethrough-header-bidding-prebid-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sharethrough-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sharethrough.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.sharethrough.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sharethrough
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sharethrough
- group: company
  title: ''
  type: Blog
  url: https://www.sharethrough.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sharethrough.com/publishers
- group: other
  title: ''
  type: X
  url: https://x.com/sharethrough
- group: commercial
  title: ''
  type: Plans
  url: plans/sharethrough-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sharethrough-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sharethrough-finops.yml
created: '2026-06-13'
description: Sharethrough is a human-centric programmatic advertising platform and one of the largest independent omnichannel ad exchanges, offering REST APIs for publishers and advertisers to manage native, display, and video ad placements through SSP/DSP integrations, real-time bidding via OpenRTB, programmatic reporting, and sustainability-focused media buying with Scope3 Climate Shield certification.
finops:
- name: Sharethrough Finops
  service_category: ''
  slug: sharethrough-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sharethrough.png
jsonld:
- class_count: 7
  name: Sharethrough Context
  property_count: 12
  slug: sharethrough-context
layout: provider
modified: '2026-06-13'
name: Sharethrough
nav: Providers
network: true
overview: 'Sharethrough publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Native Advertising, Programmatic Advertising, SSP, DSP, and OpenRTB.


  The Sharethrough catalog on APIs.io includes 1 JSON-LD context.


  Sharethrough''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Sharethrough Plans Pricing
  plan_count: 2
  slug: sharethrough-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 0
  name: Sharethrough Rate Limits
  slug: sharethrough-rate-limits
score:
  band: emerging
  composite: 22.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 17.7
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 22.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sharethrough/refs/heads/main/screenshots/sharethrough-2026-06-20T193746.png
security:
- kind: domain-security
  name: Sharethrough Domain Security
  slug: sharethrough-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sharethrough
tags:
- Native Advertising
- Programmatic Advertising
- SSP
- DSP
- OpenRTB
- Ad Exchange
- Header Bidding
- Sustainability
website: https://www.sharethrough.com
---
