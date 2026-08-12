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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Netflix Hystrix is a latency and fault tolerance library designed to isolate points of access to remote systems, services, and third-party libraries, stop cascading failure, and enable resilience in c
  name: Netflix Hystrix
  slug: netflix-hystrix
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/Netflix/Hystrix
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Netflix/Hystrix/wiki
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Netflix/Hystrix/wiki/Getting-Started
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Netflix
- group: other
  title: ''
  type: Javadoc
  url: http://netflix.github.com/Hystrix/javadoc
- group: operate
  title: ''
  type: Issues
  url: https://github.com/Netflix/Hystrix/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/Netflix/Hystrix/releases
created: '2026-03-26'
description: Netflix Hystrix is a latency and fault tolerance library designed to isolate points of access to remote systems, services, and third-party libraries, stop cascading failure, and enable resilience in complex distributed systems where failure is inevitable. Now in maintenance mode, with Resilience4j recommended as a replacement.
finops:
- name: Netflix Hystrix Finops
  service_category: API
  slug: netflix-hystrix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netflix-hystrix.png
json_schemas:
- name: Netflix Hystrix Command Configuration
  property_count: 1
  slug: hystrix-command-configuration
layout: provider
modified: '2026-03-26'
name: Netflix Hystrix
nav: Providers
network: true
overview: 'Netflix Hystrix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Circuit Breaker, Fault Tolerance, Java, Latency, and Maintenance Mode.


  The Netflix Hystrix catalog on APIs.io includes 1 Spectral governance ruleset.


  Netflix Hystrix''s developer surface includes documentation, getting-started guide, release notes, and 4 more developer resources.'
plans:
- name: Netflix Hystrix Plans Pricing
  plan_count: 3
  slug: netflix-hystrix-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 5
  name: Netflix Hystrix Rate Limits
  slug: netflix-hystrix-rate-limits
rules:
- name: Netflix Hystrix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: netflix-hystrix-jsonschema-spectral-rules
score:
  band: emerging
  composite: 26.2
  delta: -7.8
  facets:
    commercial_clarity: 15.8
    contract_quality: 9.7
    developer_ergonomics: 19.6
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 34.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/netflix-hystrix/refs/heads/main/screenshots/netflix-hystrix-2026-06-20T190155.png
slug: netflix-hystrix
tags:
- Circuit Breaker
- Fault Tolerance
- Java
- Latency
- Maintenance Mode
- Microservices
- Netflix
- Resilience
---
