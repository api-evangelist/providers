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
  title: ''
  type: Packages
  url: packages/atmosplay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/atmosplay-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Atmosplay/AtmosplayAds-Android/wiki/GetStarted
- group: auth
  title: ''
  type: Authentication
  url: authentication/atmosplay-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/atmosplay-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/atmosplay-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/atmosplay-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atmosplay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atmosplay-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/atmosplay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/atmosplay-rate-limits.yml
- group: agent
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
random_paper: 92
rate_limits:
- limit_count: 0
  name: Atmosplay Rate Limits
  slug: atmosplay-rate-limits
score:
  band: emerging
  composite: 17.7
  delta: 0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 17.2
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
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
