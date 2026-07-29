---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Prometheus Io Agentic Access
  operation_count: 57
  slug: prometheus-io-agentic-access
  summary_line: 57 operations · 22 acting
api_count: 21
apis:
- description: Remote Write is Prometheus' push protocol for shipping scraped samples to long-term storage and analysis backends (Cortex, Thanos, Mimir, VictoriaMetrics, InfluxDB, Datadog, etc.). Snappy-compressed p
  name: Prometheus Remote Write
  slug: prometheus-remote-write
- description: The text-based exposition format that every instrumented target exposes (typically on /metrics) and that the Prometheus server scrapes over HTTP. The format evolved into OpenMetrics, a CNCF Sandbox sp
  name: Prometheus Exposition Format / OpenMetrics
  slug: prometheus-exposition-format
- description: Optional OpenTelemetry Protocol metrics receiver exposed on /api/v1/otlp/v1/metrics when the Prometheus server is started with --web.enable-otlp-receiver. Accepts OTLP/HTTP protobuf payloads from Open
  name: Prometheus OTLP Metrics Receiver
  slug: prometheus-otlp-receiver
- description: Administrative operations for TSDB management.
  name: Prometheus admin API
  slug: prometheus-io-admin-api
- description: Everything related to Alertmanager alerts
  name: Prometheus alert API
  slug: prometheus-io-alert-api
- description: The alertgroup API from Prometheus — 1 operation(s) for alertgroup.
  name: Prometheus alertgroup API
  slug: prometheus-io-alertgroup-api
- description: Query active alerts and alertmanager discovery.
  name: Prometheus alerts API
  slug: prometheus-io-alerts-api
- description: Query enabled features.
  name: Prometheus features API
  slug: prometheus-io-features-api
- description: General Alertmanager operations
  name: Prometheus general API
  slug: prometheus-io-general-api
- description: Query label names and values.
  name: Prometheus labels API
  slug: prometheus-io-labels-api
- description: Retrieve metric metadata such as type and unit.
  name: Prometheus metadata API
  slug: prometheus-io-metadata-api
- description: Server notifications and events.
  name: Prometheus notifications API
  slug: prometheus-io-notifications-api
- description: OpenTelemetry Protocol metrics ingestion.
  name: Prometheus otlp API
  slug: prometheus-io-otlp-api
- description: Query and evaluate PromQL expressions.
  name: Prometheus query API
  slug: prometheus-io-query-api
- description: Everything related to Alertmanager receivers
  name: Prometheus receiver API
  slug: prometheus-io-receiver-api
- description: Remote read and write endpoints.
  name: Prometheus remote API
  slug: prometheus-io-remote-api
- description: Query recording and alerting rules.
  name: Prometheus rules API
  slug: prometheus-io-rules-api
- description: Query and manage time series.
  name: Prometheus series API
  slug: prometheus-io-series-api
- description: Everything related to Alertmanager silences
  name: Prometheus silence API
  slug: prometheus-io-silence-api
- description: Retrieve server status and configuration.
  name: Prometheus status API
  slug: prometheus-io-status-api
- description: Retrieve target and scrape pool information.
  name: Prometheus targets API
  slug: prometheus-io-targets-api
artifact_total: 34
collections:
- collection_type: open
  name: Alertmanager API
  slug: open-prometheus-alertmanager-api
- collection_type: open
  name: Prometheus API
  slug: open-prometheus-server-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prometheus-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prometheus-io-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://prometheus.io/
- group: docs
  title: ''
  type: Documentation
  url: https://prometheus.io/docs/introduction/overview/
- group: docs
  title: ''
  type: Documentation
  url: https://prometheus.io/docs/prometheus/latest/querying/api/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/prometheus
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/prometheus/prometheus
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/prometheus/prometheus/releases
- group: other
  title: ''
  type: Download
  url: https://prometheus.io/download/
- group: operate
  title: ''
  type: Forums
  url: https://prometheus.io/community/
- group: docs
  title: ''
  type: Documentation
  url: https://prometheus.io/docs/introduction/glossary/
- group: company
  title: ''
  type: Blog
  url: https://prometheus.io/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/cncf/foundation/blob/main/charter.md
- group: docs
  title: ''
  type: Documentation
  url: https://www.cncf.io/projects/prometheus/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/prometheus/governance
- group: commercial
  title: ''
  type: License
  url: https://github.com/prometheus/prometheus/blob/main/LICENSE
- group: auth
  title: ''
  type: Security
  url: https://github.com/prometheus/prometheus/security/policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/prometheus/prometheus/blob/main/CHANGELOG.md
- group: build
  title: ''
  type: SDKs
  url: https://github.com/prometheus/client_golang
- group: build
  title: ''
  type: SDKs
  url: https://github.com/prometheus/client_python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/prometheus/client_java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/prometheus/client_ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/prometheus/client_rust
- group: build
  title: ''
  type: SDKs
  url: https://github.com/siimon/prom-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jupp0r/prometheus-cpp
- group: build
  title: ''
  type: Tools
  url: https://github.com/prometheus/alertmanager
- group: build
  title: ''
  type: Tools
  url: https://github.com/prometheus/node_exporter
- group: build
  title: ''
  type: Tools
  url: https://github.com/prometheus/blackbox_exporter
- group: build
  title: ''
  type: Tools
  url: https://github.com/prometheus/snmp_exporter
- group: build
  title: ''
  type: Tools
  url: https://github.com/prometheus/statsd_exporter
- group: build
  title: ''
  type: Tools
  url: https://github.com/prometheus/jmx_exporter
- group: build
  title: ''
  type: Tools
  url: https://github.com/prometheus/mysqld_exporter
- group: build
  title: ''
  type: Tools
  url: https://github.com/prometheus/cloudwatch_exporter
- group: build
  title: ''
  type: Tools
  url: https://github.com/prometheus/pushgateway
- group: build
  title: ''
  type: Tools
  url: https://github.com/prometheus/promlens
- group: build
  title: ''
  type: Tools
  url: https://github.com/prometheus/prom2json
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/prometheus/OpenMetrics
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/prometheus/proposals
- group: docs
  title: ''
  type: Documentation
  url: https://prometheus.io/docs/prometheus/latest/installation/
- group: other
  title: ''
  type: ContainerImage
  url: https://hub.docker.com/r/prom/prometheus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloud-native-computing-foundation/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/PrometheusIO
created: 2026-05-25 00:00:00+00:00
description: Prometheus is a Cloud Native Computing Foundation graduated open source systems monitoring and alerting toolkit. A Prometheus server scrapes metrics over HTTP from instrumented targets, stores them in an embedded time series database, and lets operators query, alert, and aggregate them with the PromQL query language. The project pairs the Prometheus server with Alertmanager for alert routing and silencing, official client libraries for Go, Java, Python, Ruby, and Rust, and a large ecosystem of exporters (node, blackbox, snmp, statsd, jmx, mysqld, cloudwatch, consul, graphite, memcached, pushgateway, etc.) for pulling metrics out of existing systems. Prometheus also drives the OpenMetrics exposition format and an experimental Remote Write 2.0 protocol for shipping samples to long-term storage backends.
examples:
- key_count: 2
  name: Prometheus Query Example
  slug: prometheus-query-example
- key_count: 2
  name: Prometheus Query Range Example
  slug: prometheus-query-range-example
- key_count: 2
  name: Prometheus Targets Example
  slug: prometheus-targets-example
graphqls:
- description: This directory contains a conceptual GraphQL schema that maps the Prometheus HTTP API to GraphQL types and queries. Prometheus itself exposes a REST/PromQL HTTP API — this schema is a structural repre
  name: Prometheus GraphQL Schema
  slug: prometheus-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prometheus-io.png
json_schemas:
- name: Prometheus Query Result
  property_count: 6
  slug: prometheus-query-result
- name: Prometheus Scrape Target
  property_count: 2
  slug: prometheus-target
jsonld:
- class_count: 48
  name: Prometheus Io Context
  property_count: 6
  slug: prometheus-io-context
layout: provider
modified: 2026-05-25 00:00:00+00:00
name: Prometheus
nav: Providers
network: true
overview: 'Prometheus publishes 18 APIs on the [APIs.io](https://apis.io/) network, including admin API, alert API, alertgroup API, and 15 more. Tagged areas include Monitoring, Metrics, Observability, Time Series, and Alerting.


  The Prometheus catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Prometheus'' developer surface includes developer portal, documentation, changelog, engineering blog, tooling, and 37 more developer resources.'
random_paper: 65
rules:
- name: Prometheus API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: prometheus-io-jsonschema-spectral-rules
- name: Prometheus API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: prometheus-io-rules
score:
  band: developing
  composite: 43.0
  delta: -4.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 70.4
    developer_ergonomics: 34.8
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prometheus-io/refs/heads/main/screenshots/prometheus-io-2026-06-20T192153.png
security:
- kind: domain-security
  name: Prometheus Io Domain Security
  slug: prometheus-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: prometheus-io
tags:
- Monitoring
- Metrics
- Observability
- Time Series
- Alerting
- Cloud Native
- CNCF
- Open Source
- PromQL
- Telemetry
website: https://prometheus.io/
---
