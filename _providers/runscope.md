---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: REST API for the Runscope (now BlazeMeter API Monitoring) platform. Manages buckets, API tests, environments, scheduled runs, and test results, plus account administration. Authenticated with OAuth2 b
  name: Runscope API Monitoring API
  slug: runscope-api-monitoring-api
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.blazemeter.com/product/api-monitoring
- group: docs
  title: ''
  type: Documentation
  url: https://help.blazemeter.com/apidocs/api-monitoring/index.htm
- group: docs
  title: ''
  type: APIReference
  url: https://help.blazemeter.com/apidocs/api-monitoring/index.htm
- group: operate
  title: ''
  type: Support
  url: https://help.blazemeter.com
- group: company
  title: ''
  type: Blog
  url: https://www.blazemeter.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blazemeter.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blazemeter.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/runscope-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/runscope-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runscope-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/runscope-lifecycle.yml
created: '2026-07-17'
description: Runscope is an API monitoring and testing platform that lets teams create, schedule, and run automated tests against their APIs to catch performance problems, uptime issues, and functional regressions before customers do. Originally an independent, a16z-backed startup, Runscope was acquired by CA Technologies in 2017 and is now delivered as the API Monitoring capability of BlazeMeter (a Perforce company). The product exposes a REST API for managing buckets, tests, environments, and test results, along with scheduled runs, integrations, and real-user Radar monitoring.
image: https://www.blazemeter.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Runscope
nav: Providers
network: true
overview: 'Runscope publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Monitoring, API Testing, Observability, and Synthetic Monitoring.


  Runscope''s developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, and 5 more developer resources.'
random_paper: 39
score:
  band: emerging
  composite: 19.3
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 19.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Runscope Authentication
  slug: runscope-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Runscope Domain Security
  slug: runscope-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: runscope
tags:
- Company
- API Monitoring
- API Testing
- Observability
- Synthetic Monitoring
- Developer Tools
- Quality Assurance
website: https://www.blazemeter.com/product/api-monitoring
---
