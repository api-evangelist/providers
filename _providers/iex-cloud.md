---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Real-time and historical US equity quotes, intraday and historical prices, OHLCV charts, news, dividends, splits, options chains, fundamentals, and corporate actions. Pricing was message-based: each e'
  name: IEX Cloud Core Data API (sunset)
  slug: core-data-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://iexcloud.io
- group: auth
  href: https://artifacts.apis.io/iex-cloud/security/iex-cloud-domain-security.yml
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
  href: https://artifacts.apis.io/iex-cloud/lifecycle/iex-cloud-lifecycle.yml
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
  href: https://artifacts.apis.io/iex-cloud/changelog/iex-cloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/iex-cloud-changelog.yml
- group: auth
  href: https://artifacts.apis.io/iex-cloud/authentication/iex-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iex-cloud-authentication.yml
- group: build
  href: https://artifacts.apis.io/iex-cloud/packages/iex-cloud-packages.yml
  title: ''
  type: Packages
  url: packages/iex-cloud-packages.yml
- group: build
  href: https://artifacts.apis.io/iex-cloud/packages/iex-cloud-packages.yml
  title: ''
  type: SDKs
  url: packages/iex-cloud-packages.yml
- group: agent
  href: https://artifacts.apis.io/iex-cloud/well-known/iex-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/iex-cloud-well-known.yml
- group: agent
  href: https://artifacts.apis.io/iex-cloud/llms/iex-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iex-cloud-llms.txt
- group: commercial
  href: https://artifacts.apis.io/iex-cloud/plans/iex-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iex-cloud-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/iex-cloud/rate-limits/iex-cloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iex-cloud-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/iex-cloud/finops/iex-cloud-finops.yml
  title: ''
  type: FinOps
  url: finops/iex-cloud-finops.yml
created: '2026-05-08'
description: IEX Cloud was a cloud-based financial data platform from IEX Group offering market data, fundamentals, news, options, and reference APIs at https://cloud.iexapis.com/v1. The service was sunset on August 31, 2024 by IEX Group. The entry below is preserved as historical reference for migration patterns; endpoints are no longer reachable.
finops:
- has_sources: true
  method: generated
  name: Iex Cloud Finops
  primary_unit: ''
  service_category: Fintech
  slug: iex-cloud-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iex-cloud.png
layout: provider
modified: '2026-09-16'
name: IEX Cloud
nav: Providers
network: true
overview: 'IEX Cloud is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Market Data, Stocks, Reference, and Historical.


  IEX Cloud''s developer surface includes developer portal, documentation, changelog, authentication, and 15 more developer resources.'
plans:
- name: Iex Cloud Plans Pricing
  plan_count: 4
  slug: iex-cloud-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Iex Cloud Rate Limits
  slug: iex-cloud-rate-limits
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  previous_composite: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/iex-cloud/iex-cloud-2026-06-20T183213.png
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
- Historical
- Defunct
website: https://iexcloud.io
---
