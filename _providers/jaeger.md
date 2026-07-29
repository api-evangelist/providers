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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Jaeger Agentic Access
  operation_count: 9
  slug: jaeger-agentic-access
  summary_line: 9 operations
api_count: 7
apis:
- description: The Jaeger Collector API receives trace spans from instrumented applications and SDKs. Since Jaeger v1.11 the primary protocol is the jaeger.api_v2.CollectorService gRPC endpoint; the collector also a
  name: Jaeger Collector API
  slug: jaeger-collector-api
- description: The Jaeger Remote Storage API is a gRPC-based interface that allows extending Jaeger with custom storage backends. Any backend implementing this API can be deployed as a remote gRPC server and plugged
  name: Jaeger Remote Storage API
  slug: jaeger-remote-storage-api
- description: The Jaeger Remote Sampling API provides HTTP and gRPC endpoints that SDKs use to retrieve sampling strategies for distributed trace collection. It is implemented by the jaeger-collector and defined in
  name: Jaeger Remote Sampling API
  slug: jaeger-remote-sampling-api
- description: Endpoints for retrieving service dependency graphs.
  name: Jaeger Dependencies API
  slug: jaeger-dependencies-api
- description: Endpoints for retrieving service performance metrics including latency, call rates, and error rates.
  name: Jaeger Metrics API
  slug: jaeger-metrics-api
- description: Endpoints for listing services and their operations.
  name: Jaeger Services API
  slug: jaeger-services-api
- description: Endpoints for searching and retrieving distributed traces.
  name: Jaeger Traces API
  slug: jaeger-traces-api
artifact_total: 14
collections:
- collection_type: open
  name: Jaeger Query API
  slug: open-jaeger-query-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jaeger-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jaeger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jaegertracing.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jaegertracing.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.jaegertracing.io/docs/latest/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jaegertracing
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jaegertracing/jaeger
- group: company
  title: ''
  type: Blog
  url: https://www.jaegertracing.io/news/
- group: operate
  title: ''
  type: Community
  url: https://www.jaegertracing.io/get-involved/
- group: operate
  title: ''
  type: Support
  url: https://www.jaegertracing.io/get-in-touch/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/jaegertracing/jaeger/blob/main/CHANGELOG.md
- group: design
  title: ''
  type: JSONLD
  url: json-ld/jaeger-trace.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/jaeger-trace.yml
created: '2025-01-01'
description: Jaeger is an open source, end-to-end distributed tracing system for monitoring and troubleshooting microservices-based architectures. Jaeger provides visibility into distributed system behavior through trace collection, storage, and visualization.
finops:
- name: Jaeger Finops
  service_category: API
  slug: jaeger-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jaeger.png
layout: provider
modified: '2026-05-19'
name: Jaeger
nav: Providers
network: true
overview: 'Jaeger publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Dependencies API, Metrics API, Services API, and 1 more. Tagged areas include Distributed Tracing, Microservices, Monitoring, and Observability.


  The Jaeger catalog on APIs.io includes 1 Spectral governance ruleset.


  Jaeger''s developer surface includes documentation, getting-started guide, engineering blog, support, changelog, and 8 more developer resources.'
plans:
- name: Jaeger Plans Pricing
  plan_count: 3
  slug: jaeger-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Jaeger Rate Limits
  slug: jaeger-rate-limits
rules:
- name: Jaeger API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: jaeger-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.4
  delta: -4.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.5
    developer_ergonomics: 26.1
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jaeger/refs/heads/main/screenshots/jaeger-2026-06-20T183651.png
security:
- kind: domain-security
  name: Jaeger Domain Security
  slug: jaeger-domain-security
  summary_line: TLSv1.3 · HSTS
slug: jaeger
tags:
- Distributed Tracing
- Microservices
- Monitoring
- Observability
website: https://www.jaegertracing.io/
---
