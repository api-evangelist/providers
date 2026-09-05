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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://bybit-exchange.github.io/docs/linear/#t-introduction
  baseurl_source: declared
  description: Cryptocurrency data feed and algorithmic trading
  name: Bybit
  slug: bybit
artifact_total: 3
asyncapis:
- description: 'AsyncAPI definition for the Bybit V5 WebSocket API. Bybit exposes five public WebSocket endpoints split by product (spot, linear, inverse, option, spread) plus a single authenticated private endpoint '
  name: Bybit V5 WebSocket API
  slug: bybit-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://bybit-exchange.github.io/docs/linear/#t-introduction
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Cryptocurrency data feed and algorithmic trading
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bybit.png
layout: provider
modified: '2026-05-29'
name: Bybit
nav: Providers
network: true
overview: 'Bybit publishes 1 API on the [APIs.io](https://apis.io/) network: Bybit. Tagged areas include Cryptocurrency and Public APIs.


  The Bybit catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 13
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Bybit API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: bybit-asyncapi-spectral-rules
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 45.8
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 0.0
  previous_composite: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
slug: bybit
tags:
- Cryptocurrency
- Public APIs
website: https://bybit-exchange.github.io/docs/linear/#t-introduction
---
