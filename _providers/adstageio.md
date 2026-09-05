---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Pull normalized advertising data of any granularity from many ad networks and marketing analytics tools through a unified HAL+JSON interface (v1 and v2). Access user/organization/advertising-entity da
  name: AdStage Data API
  slug: adstage-data-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://adstage.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adstage
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/adstage/api-documentation
created: '2026-07-17'
description: AdStage was a cross-network advertising management, reporting, and automation platform (a 500 Startups / 500 Global portfolio company, founded 2013) that let marketers pull normalized advertising data from Google Ads, Microsoft/Bing Ads, Facebook, LinkedIn, Twitter, Instagram, Pinterest, Amazon, Google Analytics and more through a single unified interface. Its AdStage Data API (v1 and v2, HAL+JSON over HTTP with bearer-token / OAuth 2 auth) exposed user, organization, and advertising-entity data plus customizable cross-network reports. AdStage was acquired by TapClicks in April 2020 and folded into TapClicks' Marketing Intelligence platform; the standalone AdStage Data API (platform.adstage.io) is now defunct, though the AdStage GitHub organization and its API Blueprint documentation remain public. The adstage.io domain now serves unrelated PPC/advertising content under new ownership.
image: https://avatars.githubusercontent.com/u/2108068?s=200&v=4
layout: provider
modified: '2026-07-17'
name: AdStage.io
nav: Providers
network: true
overview: 'AdStage.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Marketing, and Analytics.


  AdStage.io''s developer surface includes documentation and 2 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 12.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adstageio/refs/heads/main/screenshots/adstageio-2026-07-25T181704.png
security:
- kind: authentication
  name: Adstageio Authentication
  slug: adstageio-authentication
  summary_line: http/oauth2 · 2 schemes
slug: adstageio
tags:
- Company
- Advertising
- AdTech
- Marketing
- Analytics
- Reporting
- Advertising Data
- Cross-Network Advertising
- Acquired
website: https://adstage.io
---
