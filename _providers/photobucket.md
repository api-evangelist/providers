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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/photobucket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://photobucket.com
- group: start
  title: ''
  type: SignUp
  url: https://app.photobucket.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.photobucket.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://photobucket.com/plans
- group: operate
  title: ''
  type: Support
  url: https://support.photobucket.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://photobucket.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://photobucket.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Photobucket
created: '2026-07-17'
description: 'Photobucket is a consumer image and video hosting service founded in 2003 and now operated by Photobucket Inc. of Seattle. It provides cloud photo/video storage, organization, and private group sharing through subscription plans (My Bucket and +Group Buckets, each including 1TB of storage) alongside a free tier. Historically one of the largest image-hosting platforms on the early social web, Photobucket opened a public developer API in 2008, but no current public/documented API surface could be found during enrichment: the developer portal is bot-blocked, the GitHub organization holds only forks and hiring challenges (no official SDK), and the app runs as a single-page application with no published /.well-known/ discovery documents. Added to the API Evangelist network as a portfolio company of Trinity Ventures.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/photobucket.png
layout: provider
modified: '2026-07-20'
name: Photobucket
nav: Providers
network: true
overview: 'Photobucket is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Photo Sharing, Image Hosting, and Video Sharing.


  Photobucket''s developer surface includes signup flow, pricing, support, and 6 more developer resources.'
random_paper: 44
score:
  band: emerging
  composite: 15.5
  delta: -1.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Photobucket Domain Security
  slug: photobucket-domain-security
  summary_line: TLSv1.3 · DMARC
slug: photobucket
tags:
- Company
- Consumer
- Photo Sharing
- Image Hosting
- Video Sharing
- Cloud Storage
- Media
website: https://photobucket.com
---
