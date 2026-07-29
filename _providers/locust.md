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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Open source distributed load testing tool. Tests are written in Python by defining User classes and tasks; tests can be run from a web UI, the command line, or embedded as a library.
  name: Locust
  slug: locust
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/locust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://locust.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.locust.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/locustio
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/locustio/locust
- group: commercial
  title: ''
  type: License
  url: https://github.com/locustio/locust/blob/master/LICENSE
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.locust.io/llms.txt
created: '2026-03-25'
description: Locust is an open source load testing tool written in Python that lets you define user behavior with code and swarm your system with millions of simultaneous users. Supports HTTP, WebSocket, MQTT, SocketIO, PostgreSQL, MongoDB, and other protocols via pluggable user classes, with a real-time web UI for orchestrating tests.
finops:
- name: Locust Finops
  service_category: API
  slug: locust-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/locust.png
layout: provider
modified: '2026-04-28'
name: Locust
nav: Providers
network: true
overview: 'Locust publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Load Testing, Performance Testing, Open Source, Python, and Testing.


  Locust''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Locust Plans Pricing
  plan_count: 3
  slug: locust-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 5
  name: Locust Rate Limits
  slug: locust-rate-limits
score:
  band: emerging
  composite: 20.4
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/locust/refs/heads/main/screenshots/locust-2026-06-20T184648.png
security:
- kind: domain-security
  name: Locust Domain Security
  slug: locust-domain-security
  summary_line: TLSv1.3 · HSTS
slug: locust
tags:
- Load Testing
- Performance Testing
- Open Source
- Python
- Testing
website: https://locust.io
---
