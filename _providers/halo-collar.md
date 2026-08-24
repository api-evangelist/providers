---
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/halo-collar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.halocollar.com/
- group: company
  title: ''
  type: About
  url: https://www.halocollar.com/about/
- group: operate
  title: ''
  type: Support
  url: https://support.halocollar.com/hc/en-us
- group: operate
  title: ''
  type: FAQ
  url: https://www.halocollar.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://www.halocollar.com/blog/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.halocollar.com/press/
- group: company
  title: ''
  type: Careers
  url: https://www.halocollar.com/careers/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.halocollar.com/plans/
- group: start
  title: ''
  type: SignUp
  url: https://www.halocollar.com/signup/
- group: start
  title: ''
  type: Login
  url: https://www.halocollar.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.halocollar.com/unified-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.halocollar.com/privacy-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/halocollar
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/halocollar
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@halocollar
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@halocollar
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/halo-collar/id1476830649
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.paws.haloapp
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/halo-collar_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/halo-collar-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/halo-collar-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/halo-collar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/halo-collar-rate-limits.yml
coverage:
  checked: '2026-08-22'
  detail: 'Halo sells an end-user GPS dog collar and app: its only API host, api.halocollar.com, is the private ASP.NET backend for the mobile app (it answers 200 with a "Halo.Web.Api" service banner and a JSON 404 envelope on every other path), and there is no developer portal, no API reference, no SDK and no docs./developer. host in DNS at all.'
  evidence:
  - status: 200
    url: https://api.halocollar.com/
  - status: 404
    url: https://api.halocollar.com/openapi.json
  - status: 404
    url: https://api.halocollar.com/swagger/v1/swagger.json
  - status: 404
    url: https://api.halocollar.com/graphql
  - status: 0
    url: https://developer.halocollar.com/
  - status: 404
    url: https://www.halocollar.com/llms.txt
  - status: 404
    url: https://www.halocollar.com/.well-known/agent-card.json
  - status: 0
    url: https://halo-api.agents.halocollar.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: 'Halo Collar is the consumer GPS dog-fence and dog-tracking product built by Protect Animals With Satellites LLC (d/b/a Halo), founded in 2017 by Ken Ehrman, Michael Ehrman and dog behaviorist Cesar Millan. The product pairs a cellular- and GPS-connected smart collar (currently Halo Collar 5, with Halo Collar 4 still sold) with a companion iOS/Android app that lets an owner draw virtual GPS fences, watch real-time location, trigger Cesar Millan-designed training feedback, and read activity reports. The service runs on a required Pack Membership subscription in Bronze, Silver and Gold tiers that carries unlimited cellular data, an increasing virtual-fence allowance, accessory discounts and third-party partner perks. Halo publishes no public developer program: the app is served by a first-party, undocumented backend at api.halocollar.com (an ASP.NET service that self-identifies as Halo.Web.Api), and there is no developer portal, API reference, OpenAPI/AsyncAPI/GraphQL contract,
  SDK or webhook surface anywhere on the company''s public web properties.'
image: https://d252xzqwj6utz.cloudfront.net/static/owls-home/halo-logo-light.svg
layout: provider
modified: '2026-08-22'
name: Halo Collar
nav: Providers
network: true
overview: 'Halo Collar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pet Tech, Consumer IoT, GPS Tracking, and Geofencing.


  Halo Collar''s developer surface includes support, FAQ, engineering blog, pricing, signup flow, YouTube channel, and 18 more developer resources.'
plans:
- name: Halo Collar Plans Pricing
  plan_count: 3
  slug: halo-collar-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Halo Collar Rate Limits
  slug: halo-collar-rate-limits
score:
  band: emerging
  composite: 22.4
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: domain-security
  name: Halo Collar Domain Security
  slug: halo-collar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: halo-collar
tags:
- Company
- Pet Tech
- Consumer IoT
- GPS Tracking
- Geofencing
- Wearables
- Connected Devices
- Mobile Apps
- Subscription Service
- Consumer Hardware
website: https://www.halocollar.com/
---
