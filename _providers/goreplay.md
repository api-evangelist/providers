---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: GoReplay captures and replays live HTTP traffic, enabling developers to test APIs and applications with real production traffic patterns without impacting production systems.
  name: GoReplay
  slug: goreplay-tool
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goreplay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goreplay.org
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/buger/goreplay/wiki
- group: build
  title: ''
  type: GitHub
  url: https://github.com/buger/goreplay
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/buger/goreplay/wiki/Getting-Started
- group: commercial
  title: ''
  type: Pricing
  url: https://goreplay.org/pro.html
- group: operate
  title: ''
  type: Support
  url: https://github.com/buger/goreplay/issues
created: '2026-03-26'
description: GoReplay is an open source network traffic capture and replay tool that allows teams to record live HTTP traffic and replay it in test environments, enabling realistic load testing and API testing with real production data.
finops:
- name: Goreplay Finops
  service_category: API
  slug: goreplay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goreplay.png
layout: provider
modified: '2026-04-28'
name: GoReplay
nav: Providers
network: true
overview: 'GoReplay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, HTTP Traffic, Load Testing, Network Capture, and Open-Source.


  GoReplay''s developer surface includes documentation, GitHub presence, getting-started guide, pricing, support, and 2 more developer resources.'
plans:
- name: Goreplay Plans Pricing
  plan_count: 3
  slug: goreplay-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Goreplay Rate Limits
  slug: goreplay-rate-limits
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 18.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/screenshots/goreplay-2026-06-20T182250.png
security:
- kind: domain-security
  name: Goreplay Domain Security
  slug: goreplay-domain-security
  summary_line: TLSv1.3
slug: goreplay
tags:
- API Testing
- HTTP Traffic
- Load Testing
- Network Capture
- Open-Source
- Traffic Replay
website: https://goreplay.org
---
