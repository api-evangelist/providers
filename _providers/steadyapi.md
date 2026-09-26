---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-25'
api_count: 2
apis:
- baseURL: https://api.steadyapi.com
  baseurl_source: declared
  description: REST/JSON API providing stock market, options, crypto, real estate, sports, e-commerce, social media, travel, and web-scraping data. Bearer-token or apikey auth, 15 req/sec rate limit.
  name: SteadyAPI
  slug: steadyapi
- description: REST/JSON API for fetching Reddit posts, comments, voting data, subreddit statistics, and user activity. Endpoints under /v1/reddit/ include /search, /posts, /post, /subreddit/popular, /subreddit/info
  name: Reddit Data API
  slug: reddit-data-api
artifact_total: 6
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/steadyapi/refs/heads/main/rate-limits/steadyapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/steadyapi-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/steadyapi/refs/heads/main/plans/steadyapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/steadyapi-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/steadyapi/refs/heads/main/conventions/steadyapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/steadyapi-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/steadyapi/refs/heads/main/authentication/steadyapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/steadyapi-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/steadyapi/refs/heads/main/lifecycle/steadyapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/steadyapi-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/steadyapi/refs/heads/main/errors/steadyapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/steadyapi-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/steadyapi/refs/heads/main/llms/steadyapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/steadyapi-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://steadyapi.com/pages/terms-and-conditions
- group: start
  title: ''
  type: Login
  url: https://steadyapi.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/steadyapi/refs/heads/main/security/steadyapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/steadyapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://steadyapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.steadyapi.com
- group: commercial
  title: ''
  type: Pricing
  url: https://steadyapi.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://steadyapi.com/pages/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://steadyapi.com/pages/contact
created: '2026-09-21'
description: SteadyAPI is a multi-domain data-as-a-service platform exposing a single REST/JSON API across finance (real-time and historical stock, options and crypto market data), real estate, sports (MLB, NHL), e-commerce (Amazon, AliExpress), travel (Booking.com), and social/web data (Reddit, Twitter/X, Instagram, vehicles/VIN, and web scraping). Endpoints are versioned in the URL path (v1/v2/v3), authenticated with a personal access token via a Bearer header or apikey query parameter, rate limited to 15 requests per second, and sold on four subscription tiers by monthly request volume.
image: https://steadyapi.com/logo/steadyapi-white-api.svg
layout: provider
modified: '2026-09-21'
name: SteadyAPI
nav: Providers
network: true
overview: 'SteadyAPI publishes 2 APIs on the [APIs.io](https://apis.io/) network, including SteadyAPI, and 1 more. Tagged areas include Data, Finance, Stock Market, Social Media, and Reddit.


  SteadyAPI''s developer surface includes authentication, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Steadyapi Plans Pricing
  plan_count: 4
  slug: steadyapi-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Steadyapi Rate Limits
  slug: steadyapi-rate-limits
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 54.0
    catalog_earned_first_party: 20.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 32.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Steadyapi Authentication
  slug: steadyapi-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Steadyapi Domain Security
  slug: steadyapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: steadyapi
tags:
- Data
- Finance
- Stock Market
- Social Media
- Reddit
- Data as a Service
- Web Data
- Alternative Data
website: https://steadyapi.com
---
