---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Community-accessible interface to HowLongToBeat game completion time data. Provides search-by-game-name and game-detail lookups returning main story, main story plus extras, completionist, and all-sty
  name: HowLongToBeat API
  slug: howlongtobeat-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/howlongtobeat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://howlongtobeat.com
- group: docs
  title: ''
  type: Documentation
  url: https://howlongtobeat.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/topics/howlongtobeat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ign-entertainment
- group: company
  title: ''
  type: Blog
  url: https://howlongtobeat.com
- group: commercial
  title: ''
  type: Pricing
  url: https://howlongtobeat.com
- group: operate
  title: ''
  type: StatusPage
  url: https://howlongtobeat.com
- group: other
  title: ''
  type: X
  url: https://x.com/HowLongToBeat
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/howlongtobeat/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/howlongtobeat/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/howlongtobeat/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: HowLongToBeat is a game completion time database that tracks how long it takes to finish thousands of video games. Community-sourced data provides average completion times across multiple play styles including main story, main story plus extras, completionist, and all styles. The site is owned by IGN Entertainment (Ziff Davis) and does not publish an official public API; all programmatic access relies on community-built wrappers that query the website directly.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/howlongtobeat.png
layout: provider
modified: '2026-06-13'
name: HowLongToBeat
nav: Providers
network: true
overview: 'HowLongToBeat publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Games, Video Games, Game Completion Times, Game Database, and Community Data.


  HowLongToBeat''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 64
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 19.9
  delta: 0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/howlongtobeat/refs/heads/main/screenshots/howlongtobeat-2026-06-20T182851.png
security:
- kind: domain-security
  name: Howlongtobeat Domain Security
  slug: howlongtobeat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: howlongtobeat
tags:
- Games
- Video Games
- Game Completion Times
- Game Database
- Community Data
website: https://howlongtobeat.com
---
