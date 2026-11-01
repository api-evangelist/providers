---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'User lookup API: retrieve full profile details for any Twitter/X username. Flat-rate $0.0002 per request, flexible rate limits and no subscriptions.'
  name: SocialData API
  slug: socialdata-api
- baseURL: https://api.socialdata.tools
  baseurl_source: declared
  description: Endpoints for retrieving data from Twitter
  name: socialdata-tools Data API
  slug: socialdata-tools-data-api-api
- baseURL: https://api.socialdata.tools
  baseurl_source: declared
  description: Endpoints for creating and managing your monitors
  name: socialdata-tools Monitoring API
  slug: socialdata-tools-monitoring-api-api
- baseURL: https://api.socialdata.tools
  baseurl_source: declared
  description: Endpoints for validating social actions Twitter
  name: socialdata-tools Social Actions API
  slug: socialdata-tools-social-actions-api-api
- baseURL: https://api.socialdata.tools
  baseurl_source: declared
  description: Endpoints for managing your SocialData account
  name: socialdata-tools SocialData Account Management API
  slug: socialdata-tools-socialdata-account-management-api
artifact_total: 11
common:
- group: auth
  href: https://artifacts.apis.io/socialdata-tools/security/socialdata-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/socialdata-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://socialdata.tools/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.socialdata.tools/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.socialdata.tools/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.socialdata.tools/getting-started/overview/
- group: operate
  title: ''
  type: Support
  url: https://docs.socialdata.tools/getting-started/getting-help/
- group: commercial
  title: ''
  type: Pricing
  url: https://socialdata.tools/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://socialdata.tools/signup
created: '2026-10-31'
description: SocialData builds developer APIs for reading public data from X (formerly Twitter). It offers a read‑only Twitter/X API that provides access to tweets, user profiles, followers, and search results without requiring an X developer account. Pricing is pay‑per‑result at $0.20 per 1,000 results, with real‑time data and no subscription. The service includes an MCP endpoint for AI assistants and comprehensive documentation.
image: https://docs.socialdata.tools/android-chrome-512x512.png
layout: provider
modified: '2026-10-31'
name: socialdata-tools
nav: Providers
network: true
overview: 'socialdata-tools publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data API, Monitoring API, Social Actions API, and 2 more. Tagged areas include API, Data, Social Media, X, and Twitter.


  socialdata-tools'' developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, and 2 more developer resources.'
plans:
- name: Socialdata Tools Plans Pricing
  plan_count: 0
  slug: socialdata-tools-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Socialdata Tools Rate Limits
  slug: socialdata-tools-rate-limits
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 44.2
    catalog_earned_first_party: 0.0
    catalog_gap: 70.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 48.1
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 18.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Socialdata Tools Authentication
  slug: socialdata-tools-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Socialdata Tools Domain Security
  slug: socialdata-tools-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: get-tweet
  slug: get-tweet
- name: get-user-profile
  slug: get-user-profile
slug: socialdata-tools
tags:
- API
- Data
- Social Media
- X
- Twitter
website: https://socialdata.tools/
---
