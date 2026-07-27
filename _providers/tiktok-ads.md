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
  band: human-only
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'RESTful Marketing API for managing TikTok ad accounts, campaigns, ad groups, ads, creatives, audiences, conversions, pixels, and reporting. Authentication uses OAuth 2.0 with access tokens issued via '
  name: TikTok Marketing API
  slug: marketing-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiktok-ads-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tiktok.com/business/
- group: docs
  title: ''
  type: Documentation
  url: https://business-api.tiktok.com/portal/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://business-api.tiktok.com/portal
- group: start
  title: ''
  type: Signup
  url: https://ads.tiktok.com/i18n/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tiktok.com/business/en/pricing
- group: build
  title: ''
  type: GitHub SDK
  url: https://github.com/tiktok/tiktok-business-api-sdk
- group: operate
  title: ''
  type: Support
  url: https://ads.tiktok.com/help/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/tiktokforbusiness/
- group: company
  title: ''
  type: Blog
  url: https://ads.tiktok.com/business/en/blog
created: '2026-05-11'
description: TikTok for Business is TikTok's advertising platform that enables brands, agencies, and advertisers to create, manage, and optimize ad campaigns across TikTok and its family of apps. The TikTok Marketing API (business-api.tiktok.com) is a RESTful API that uses OAuth 2.0 authentication and lets developers programmatically manage advertiser accounts, campaigns, ad groups, ads, creatives, audiences, reporting, conversions, and pixel/events for performance marketing and measurement.
graphqls:
- description: TikTok Marketing API covers campaign management, ad groups, creatives, audiences, targeting options, pixel events, attribution, and reporting for TikTok advertising.
  name: TikTok Marketing API GraphQL API
  slug: tiktok-ads-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tiktok-ads.png
layout: provider
modified: '2026-05-11'
name: TikTok Marketing API
nav: Providers
network: true
overview: 'TikTok Marketing API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Marketing, Social Media, Ad Campaigns, and Performance Marketing.


  TikTok Marketing API''s developer surface includes documentation, signup flow, pricing, support, engineering blog, and 5 more developer resources.'
random_paper: 67
score:
  band: emerging
  composite: 16.1
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tiktok-ads/refs/heads/main/screenshots/tiktok-ads-2026-06-20T195404.png
security:
- kind: domain-security
  name: Tiktok Ads Domain Security
  slug: tiktok-ads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tiktok-ads
tags:
- Advertising
- Marketing
- Social Media
- Ad Campaigns
- Performance Marketing
- Conversion Tracking
website: https://www.tiktok.com/business/
---
