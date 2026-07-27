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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
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
overview: 'GoReplay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, HTTP Traffic, Load Testing, Network Capture, and Open Source.


  GoReplay''s developer surface includes documentation, GitHub presence, getting-started guide, pricing, support, and 2 more developer resources.'
plans:
- name: Goreplay Plans Pricing
  plan_count: 3
  slug: goreplay-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 5
  name: Goreplay Rate Limits
  slug: goreplay-rate-limits
score:
  band: emerging
  composite: 27.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 27.6
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- Open Source
- Traffic Replay
website: https://goreplay.org
---
