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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-03'
api_count: 6
apis:
- description: The OTLP gRPC API defines Protocol Buffers service definitions for exporting traces, metrics, and logs over gRPC. It is the primary transport for OpenTelemetry data between SDK instrumentation, the Op
  name: OpenTelemetry Protocol (OTLP) gRPC API
  slug: opentelemetry-protocol-otlp-grpc-api
- description: 'The OpenTelemetry Collector is a vendor-agnostic proxy for receiving, processing, and exporting telemetry data. It exposes HTTP and gRPC endpoints for receiving OTLP data and provides a configuration '
  name: OpenTelemetry Collector API
  slug: opentelemetry-collector-api
- description: The OpenTelemetry SDK API specifies language-level interfaces for instrumentation, including the Tracer, Meter, and Logger APIs used by application code to create spans, record metrics, and emit log r
  name: OpenTelemetry SDK API
  slug: opentelemetry-sdk-api
- description: The Logs API from OpenTelemetry — 1 operation(s) for logs.
  name: OpenTelemetry Logs API
  slug: opentelemetry-logs-api
- description: The Metrics API from OpenTelemetry — 1 operation(s) for metrics.
  name: OpenTelemetry Metrics API
  slug: opentelemetry-metrics-api
- description: The Traces API from OpenTelemetry — 1 operation(s) for traces.
  name: OpenTelemetry Traces API
  slug: opentelemetry-traces-api
artifact_total: 12
asyncapis:
- description: The OpenTelemetry Protocol (OTLP) defines the event-driven telemetry export pipeline through which instrumented applications and OpenTelemetry Collectors push batches of traces, metrics, and logs to o
  name: OpenTelemetry Protocol (OTLP) Telemetry Events
  slug: opentelemetry-otlp-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opentelemetry-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opentelemetry
- group: company
  title: ''
  type: Website
  url: https://opentelemetry.io/
- group: docs
  title: ''
  type: Documentation
  url: https://opentelemetry.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://opentelemetry.io/docs/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/open-telemetry
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/open-telemetry/opentelemetry-specification
- group: build
  title: ''
  type: SDKs
  url: https://opentelemetry.io/docs/languages/
- group: company
  title: ''
  type: Blog
  url: https://opentelemetry.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://opentelemetry.io/community/
- group: operate
  title: ''
  type: Slack
  url: https://cloud-native.slack.com/archives/CJFCJHG4Q
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/open-telemetry
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/open-telemetry/opentelemetry-specification/blob/main/CHANGELOG.md
- group: auth
  title: ''
  type: Security
  url: https://github.com/open-telemetry/opentelemetry-collector/security/policy
- group: agent
  title: ''
  type: LlmsText
  url: https://opentelemetry.io/llms.txt
created: '2025-01-01'
description: Vendor-neutral open-source observability framework for cloud-native software, providing a collection of tools, APIs, and SDKs for instrumenting, generating, collecting, and exporting telemetry data including metrics, logs, and traces.
finops:
- name: Opentelemetry Finops
  service_category: API
  slug: opentelemetry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opentelemetry.png
layout: provider
modified: '2026-04-28'
name: OpenTelemetry
nav: Providers
network: true
overview: 'OpenTelemetry publishes 3 APIs on the [APIs.io](https://apis.io/) network: Logs API, Metrics API, and Traces API. Tagged areas include Cloud Native, Logging, Metrics, Monitoring, and Observability.


  The OpenTelemetry catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  OpenTelemetry''s developer surface includes documentation, getting-started guide, engineering blog, Stack Overflow tag, changelog, and 10 more developer resources.'
plans:
- name: Opentelemetry Plans Pricing
  plan_count: 3
  slug: opentelemetry-plans-pricing
random_paper: 91
rate_limits:
- limit_count: 5
  name: Opentelemetry Rate Limits
  slug: opentelemetry-rate-limits
rules:
- name: OpenTelemetry API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 7
  slug: opentelemetry-asyncapi-spectral-rules
score:
  band: developing
  composite: 53.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 70.5
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 63.2
  previous_composite: 53.7
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opentelemetry/refs/heads/main/screenshots/opentelemetry-2026-06-20T191044.png
security:
- kind: domain-security
  name: Opentelemetry Domain Security
  slug: opentelemetry-domain-security
  summary_line: TLSv1.3 · HSTS
slug: opentelemetry
tags:
- Cloud Native
- Logging
- Metrics
- Monitoring
- Observability
- Open Source
- Tracing
website: https://opentelemetry.io/
---
