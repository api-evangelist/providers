---
access_model:
  confidence: medium
  label: Partner
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.stnvideo.com/resources/our-wordpress-ovp-plugin/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The public oEmbed 1.0 provider endpoint for STN Video (formerly SendtoNews), Minute Media's online video platform. A GET with a URL-encoded `url` naming an embed.sendtonews.com resource that carries a
  name: STN Video oEmbed API
  slug: stn-video-oembed-api
- description: The credential-gated publisher API behind the STN Online Video Platform. Every operation is a POST to https://api.sendtonews.com/api/v1/ carrying a `cid` (Company ID) and `authcode` (Authentication Co
  name: STN Video Publisher API
  slug: stn-video-publisher-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/minute-media-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/minute-media-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/minute-media-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/minute-media-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/minute-media-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/minute-media-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/minute-media-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/minute-media-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/minute-media-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/minute-media-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/minute-media-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.minutemedia.com
- group: other
  title: ''
  type: Company
  url: https://www.minutemedia.com/company/about-us
- group: docs
  title: ''
  type: Documentation
  url: https://www.stnvideo.com/resources/our-wordpress-ovp-plugin/
- group: operate
  title: ''
  type: Support
  url: https://www.minutemedia.com/company/contact
- group: company
  title: ''
  type: Blog
  url: https://www.stnvideo.com/category/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/minutemedia
- group: start
  title: ''
  type: SignUp
  url: https://pub.stnvideo.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.minutemedia.com/policies/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.minutemedia.com/policies/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.minutemedia.com/policies/cookie-policy
- group: other
  title: ''
  type: TakedownPolicy
  url: https://www.minutemedia.com/policies/takedown-policy
- group: company
  title: ''
  type: Careers
  url: https://www.minutemedia.com/company/careers
created: '2026-07-17'
description: 'Minute Media is a global technology, media, and advertising company that builds and operates digital sports and entertainment content brands while licensing publishing and monetization technology to third parties. Its owned-and-operated properties include Sports Illustrated, The Players'' Tribune, 90min, Mental Floss, FanSided, The Big Lead, and DBLTAP, reaching a reported 200+ million monthly users. On the technology side it offers the STN Online Video Platform (OVP) for video publishing and monetization, a Minute Media SSP for programmatic advertising, and ad-management solutions for publishers. Minute Media was surfaced as a portfolio company of Battery Ventures and added to the API Evangelist network for enrichment. The company publishes no developer portal, no API reference and no machine-readable API definition, but two real API surfaces are live and were verified by probe: a public oEmbed 1.0 endpoint at embed.sendtonews.com that any publisher can call unauthenticated,
  and a credential-gated STN Video Publisher API at api.sendtonews.com/api/v1 whose only public client is Minute Media''s own WordPress plugin. Both hosts still carry the pre-acquisition SendtoNews brand two renames later.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/minute-media.png
layout: provider
modified: '2026-08-12'
name: Minute Media
nav: Providers
network: true
overview: 'Minute Media publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Sports, Advertising, and Video.


  Minute Media''s developer surface includes authentication, documentation, support, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Minute Media Plans Pricing
  plan_count: 0
  slug: minute-media-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Minute Media Rate Limits
  slug: minute-media-rate-limits
score:
  band: emerging
  composite: 21.4
  delta: -0.4
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.8
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/minute-media/refs/heads/main/screenshots/minute-media-2026-08-07T183655.png
security:
- kind: authentication
  name: Minute Media Authentication
  slug: minute-media-authentication
  summary_line: none/custom-credential-pair · 2 schemes
- kind: domain-security
  name: Minute Media Domain Security
  slug: minute-media-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: minute-media
tags:
- Company
- Media
- Sports
- Advertising
- Video
- Publishing
- AdTech
- Content
- oEmbed
- Online Video Platform
website: https://www.minutemedia.com
---
