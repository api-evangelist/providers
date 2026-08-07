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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API for managing AdRoll advertisers, campaigns, ads, audience segments, and reporting on the NextRoll platform. Supports OAuth 2.0 flows and Personal Access Tokens with the client API key sent as
  name: NextRoll API for AdRoll
  slug: nextroll-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adroll-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nextroll.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adroll
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adroll
- group: company
  title: ''
  type: Website
  url: https://www.adroll.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.nextroll.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adroll.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.adroll.com/signup
created: '2026-05-11'
description: AdRoll is a display advertising and retargeting platform from NextRoll that helps direct-to-consumer brands run cross-channel display, social, and email campaigns from a single dashboard powered by the BidIQ machine learning bidder. The platform manages audience segmentation, creative serving, and attribution across the open web and major social networks. The NextRoll API for AdRoll exposes campaign, ad, audience, and reporting endpoints using OAuth 2.0 or Personal Access Token authentication.
graphqls:
- description: AdRoll is a performance advertising platform for retargeting and prospecting. Their API covers campaign management, audience segments, ad creative management, attribution, and cross-channel reporting.
  name: AdRoll GraphQL API
  slug: adroll-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adroll.png
layout: provider
modified: '2026-05-11'
name: AdRoll
nav: Providers
network: true
overview: 'AdRoll publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Display Advertising, Retargeting, Marketing, and AdTech.


  AdRoll''s developer surface includes engineering blog, documentation, pricing, signup flow, and 4 more developer resources.'
random_paper: 73
score:
  band: emerging
  composite: 22.6
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 43.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 22.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adroll/refs/heads/main/screenshots/adroll-2026-06-20T165128.png
security:
- kind: domain-security
  name: Adroll Domain Security
  slug: adroll-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: adroll
tags:
- Advertising
- Display Advertising
- Retargeting
- Marketing
- AdTech
- Programmatic
website: https://www.adroll.com
---
