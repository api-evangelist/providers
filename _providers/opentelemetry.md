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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 16
asyncapis:
- description: The OpenTelemetry Protocol (OTLP) defines the event-driven telemetry export pipeline through which instrumented applications and OpenTelemetry Collectors push batches of traces, metrics, and logs to o
  name: OpenTelemetry Protocol (OTLP) Telemetry Events
  slug: opentelemetry-otlp-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenTelemetry Protocol (OTLP) HTTP Logs API
  slug: open-opentelemetry-logs-api
- collection_type: open
  name: OpenTelemetry Protocol (OTLP) HTTP Metrics API
  slug: open-opentelemetry-metrics-api
- collection_type: open
  name: OpenTelemetry Protocol (OTLP) HTTP Traces API
  slug: open-opentelemetry-traces-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/open-telemetry/opentelemetry-proto/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/open-telemetry/opentelemetry-proto/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/open-telemetry/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/open-telemetry/opentelemetry-proto/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/open-telemetry/opentelemetry-proto/blob/main/LICENSE
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
overview: 'OpenTelemetry publishes 3 APIs on the [APIs.io](https://apis.io/) network: Logs API, Metrics API, and Traces API. Tagged areas include Cloud-Native, Logging, Metrics, Monitoring, and Observability.


  The OpenTelemetry catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  OpenTelemetry''s developer surface includes documentation, getting-started guide, engineering blog, Stack Overflow tag, changelog, and 15 more developer resources.'
plans:
- name: Opentelemetry Plans Pricing
  plan_count: 3
  slug: opentelemetry-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Opentelemetry Rate Limits
  slug: opentelemetry-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: OpenTelemetry API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 7
  slug: opentelemetry-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 63.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 63.1
    developer_ergonomics: 42.9
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 65.0
  previous_composite: 43.5
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opentelemetry/refs/heads/main/screenshots/opentelemetry-2026-06-20T191044.png
security:
- kind: domain-security
  name: Opentelemetry Domain Security
  slug: opentelemetry-domain-security
  summary_line: TLSv1.3 · HSTS
slug: opentelemetry
tags:
- Cloud-Native
- Logging
- Metrics
- Monitoring
- Observability
- Open-Source
- Tracing
website: https://opentelemetry.io/
---
