---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Real-time and historical US equity quotes, intraday and historical prices, OHLCV charts, news, dividends, splits, options chains, fundamentals, and corporate actions. Pricing was message-based: each e'
  name: IEX Cloud Core Data API (sunset)
  slug: core-data-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iex-cloud-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iexcloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/iex-cloud
- group: start
  title: ''
  type: Portal
  url: https://www.iexcloud.io/
- group: other
  title: ''
  type: Sunset Notice
  url: https://iexcloud.io/community/blog/iex-cloud-end-of-life-announcement
- group: docs
  title: ''
  type: Documentation
  url: https://web.archive.org/web/20241003164023/https://iexcloud.io/docs/api/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/iex-cloud-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.iexapis.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://web.archive.org/web/20240611120824/https://iexcloud.io/docs/api-basics/deprecation
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/iex-cloud-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iex-cloud-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/iex-cloud-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/iex-cloud-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/iex-cloud-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iex-cloud-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/iex-cloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iex-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/iex-cloud-finops.yml
created: '2026-05-08'
description: IEX Cloud was a cloud-based financial data platform from IEX Group offering market data, fundamentals, news, options, and reference APIs at https://cloud.iexapis.com/v1. The service was sunset on August 31, 2024 by IEX Group. The entry below is preserved as historical reference for migration patterns; endpoints are no longer reachable.
finops:
- name: Iex Cloud Finops
  service_category: Fintech
  slug: iex-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iex-cloud.png
layout: provider
modified: '2026-07-22'
name: IEX Cloud
nav: Providers
network: true
overview: 'IEX Cloud publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Market Data, Stocks, Reference, and Sunset.


  IEX Cloud''s developer surface includes developer portal, documentation, changelog, authentication, and 14 more developer resources.'
plans:
- name: Iex Cloud Plans Pricing
  plan_count: 4
  slug: iex-cloud-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Iex Cloud Rate Limits
  slug: iex-cloud-rate-limits
score:
  band: thin
  composite: 33.0
  delta: 0.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 76.3
  previous_composite: 32.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iex-cloud/refs/heads/main/screenshots/iex-cloud-2026-06-20T183213.png
security:
- kind: authentication
  name: Iex Cloud Authentication
  slug: iex-cloud-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Iex Cloud Domain Security
  slug: iex-cloud-domain-security
  summary_line: TLSv1.3
slug: iex-cloud
tags:
- Fintech
- Market Data
- Stocks
- Reference
- Sunset
- Historical
website: https://www.iexcloud.io/
---
