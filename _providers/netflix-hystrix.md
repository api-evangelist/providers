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
random_paper: 6
rate_limits:
- limit_count: 5
  name: Netflix Hystrix Rate Limits
  slug: netflix-hystrix-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Netflix Hystrix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: netflix-hystrix-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 50.3
    catalog_earned_first_party: 0.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 8.0
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 28.9
  previous_composite: 20.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
