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
api_count: 0
artifact_total: 3
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Atmosplay
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Atmosplay/Help-Center-for-Publisher
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/packages/atmosplay-packages.yml
  title: ''
  type: Packages
  url: packages/atmosplay-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/packages/atmosplay-packages.yml
  title: ''
  type: SDKs
  url: packages/atmosplay-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Atmosplay/AtmosplayAds-Android/wiki/GetStarted
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/authentication/atmosplay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atmosplay-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/errors/atmosplay-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/atmosplay-error-codes.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/sandbox/atmosplay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/atmosplay-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/changelog/atmosplay-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/atmosplay-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/lifecycle/atmosplay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/atmosplay-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/conformance/atmosplay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atmosplay-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/plans/atmosplay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atmosplay-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/rate-limits/atmosplay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/atmosplay-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/llms/atmosplay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atmosplay-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Atmosplay was acquired by ZPLAY Information Technology on 2018-01-01 and its domain has since been released — atmosplay.com now serves a HugeDomains "AtmosPlay.com is for sale" parking page that answers HTTP 200 with the same 44,825-byte HTML on every path and every subdomain (api., docs., sdk., dev., developer., platform., console., ads.), while atmosplay.net no longer resolves at all, leaving the frozen GitHub SDK organization as the only first-party surface and no callable API anywhere.
  evidence:
  - status: 200
    url: https://atmosplay.com
  - status: 200
    url: https://atmosplay.com/openapi.json
  - status: 200
    url: https://atmosplay.com/.well-known/agent-card.json
  - status: 0
    url: https://atmosplay.net
  - status: 404
    url: https://repo1.maven.org/maven2/com/atmosplayads/
  - status: 200
    url: https://github.com/Atmosplay
  reason: defunct
  state: none
created: '2026-07-17'
description: Atmosplay was a mobile advertising technology company, founded in 2014 in Budapest, Hungary, that built interactive 3D "playable" ads and an ad-monetization platform for mobile game publishers. Its ATMIQ cloud gameplay engine let users try a game inside an ad without installing it, and its self-serve builder produced playable creatives for 3D and action games. Atmosplay shipped first-party mobile SDKs (Unity, iOS, Android) plus AdMob and MoPub mediation adapters for publishers to integrate interstitial, banner, and rewarded-video formats. Speedinvest led its Series A in 2016; the company was acquired by ZPLAY Information Technology on 2018-01-01. Its websites (atmosplay.com / atmosplay.net) are no longer operational; the surviving public developer surface is its GitHub organization of SDK and adapter repositories. This profile is maintained for network completeness as an acquired/inactive portfolio lead.
image: https://avatars.githubusercontent.com/u/12141997?v=4
layout: provider
modified: '2026-08-12'
name: Atmosplay
nav: Providers
network: true
overview: 'Atmosplay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Mobile, and Playable Ads.


  Atmosplay''s developer surface includes documentation, getting-started guide, authentication, sandbox, changelog, and 9 more developer resources.'
plans:
- name: Atmosplay Plans Pricing
  plan_count: 0
  slug: atmosplay-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Atmosplay Rate Limits
  slug: atmosplay-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/atmosplay/refs/heads/main/screenshots/atmosplay-2026-07-25T201559.png
security:
- kind: authentication
  name: Atmosplay Authentication
  slug: atmosplay-authentication
  summary_line: 0 schemes
slug: atmosplay
tags:
- Company
- Advertising
- AdTech
- Mobile
- Playable Ads
- Ad Monetization
- Gaming
- SDK
---
