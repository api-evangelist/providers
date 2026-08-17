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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Lightstep API provides programmatic access to observability data including traces, spans, streams, dashboards, alerting conditions, and service health. It enables teams to manage their observabili
  name: Lightstep API
  slug: lightstep-api
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightstep-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lightstep.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lightstep.com
- group: company
  title: ''
  type: Blog
  url: https://lightstep.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://lightstep.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.lightstep.com
- group: start
  title: ''
  type: Signup
  url: https://app.lightstep.com/signup
- group: operate
  title: ''
  type: Support
  url: https://lightstep.com/support
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lightstep
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightstep
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lightstep.com
- group: start
  title: ''
  type: OpenTelemetry
  url: https://docs.lightstep.com/docs/opentelemetry
created: '2026-03-26'
description: Lightstep, now ServiceNow Cloud Observability, is a distributed tracing and observability platform that helps teams monitor, debug, and optimize microservice performance. It provides deep visibility into distributed systems using OpenTelemetry-based tracing, metrics, and service health monitoring.
features:
- Now ServiceNow Cloud Observability after acquisition
- Community free for evaluation
- 'Enterprise: custom pricing through ServiceNow'
- Distributed tracing with intelligent sampling
- Service maps (Enterprise)
- Anomaly detection with notebooks
- OpenTelemetry-native
- Public API at api.lightstep.com
- Default 600 req/min/org
- Span ingest scales with plan
- Streams (saved span queries)
- Notebooks for collaborative root-cause analysis
- ServiceNow ITSM integration (Enterprise)
- API tokens per project
- Webhooks for streams and conditions
- AWS, GCP, Azure cloud support
finops:
- name: Lightstep Finops
  service_category: Observability
  slug: lightstep-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightstep.png
layout: provider
modified: '2026-05-04'
name: Lightstep
nav: Providers
network: true
overview: 'Lightstep publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include APM, Distributed Tracing, Microservices, Monitoring, and Observability.


  Lightstep''s developer surface includes documentation, engineering blog, pricing, signup flow, support, GitHub presence, and 6 more developer resources.'
plans:
- name: Lightstep Plans Pricing
  plan_count: 2
  slug: lightstep-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 2
  name: Lightstep Rate Limits
  slug: lightstep-rate-limits
score:
  band: emerging
  composite: 27.8
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 32.3
    developer_ergonomics: 15.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 27.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightstep/refs/heads/main/screenshots/lightstep-2026-06-20T184527.png
security:
- kind: domain-security
  name: Lightstep Domain Security
  slug: lightstep-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: lightstep
tags:
- APM
- Distributed Tracing
- Microservices
- Monitoring
- Observability
- OpenTelemetry
website: https://lightstep.com
---
