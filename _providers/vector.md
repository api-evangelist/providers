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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Vector Agentic Access
  operation_count: 2
  slug: vector-agentic-access
  summary_line: 2 operations
api_count: 3
apis:
- description: Vector Remap Language (VRL) is a purpose-built expression language for transforming observability data in Vector. Provides 100+ built-in functions for parsing, filtering, enriching, and transforming l
  name: Vector Remap Language (VRL)
  slug: vector-vrl
- description: Official Helm charts for deploying Vector on Kubernetes as a DaemonSet (agent mode) or Deployment (aggregator mode).
  name: Vector Helm Charts
  slug: vector-helm
- baseURL: http://127.0.0.1:8686
  baseurl_source: declared
  description: Health check endpoints for load balancers and Kubernetes probes.
  name: Vector Health API
  slug: vector-health-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vector Observability Health API
  slug: open-vector-health-api
- collection_type: open
  name: Vector Observability API
  slug: open-vector-observability-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/vectordotdev/vrl/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/vectordotdev/vrl/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/vectordotdev/vrl/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/vectordotdev/vrl/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vector-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vector-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vector.dev
- group: docs
  title: ''
  type: Documentation
  url: https://vector.dev/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vectordotdev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/vectordotdev/vector
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://vector.dev/releases/
- group: company
  title: ''
  type: Blog
  url: https://vector.dev/blog/
- group: operate
  title: ''
  type: Forums
  url: https://discord.com/invite/n2yjjZR
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/vector-dev
- group: design
  title: ''
  type: SpectralRules
  url: rules/vector-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vector-vocabulary.yaml
created: '2026-03-25'
description: Vector is an open source high-performance observability data pipeline from Datadog for collecting, transforming, and routing logs, metrics, and traces. Built in Rust for performance and reliability, Vector supports 50+ sources, 20+ transforms, and 80+ sinks. It provides a built-in API for health monitoring and component inspection, plus Vector Remap Language (VRL) for powerful data transformation.
examples:
- key_count: 1
  name: Vector Observability Api Health Response Example
  slug: vector-observability-api-health-response-example
features:
- description: Built in Rust with benchmarks showing 86+ MiB/s throughput for log pipeline workloads.
  name: High-Performance Pipeline
- description: Single binary handles logs, metrics, and traces from collection through routing.
  name: Unified Data Plane
- description: Native integrations for files, Kafka, Kubernetes, AWS S3/CloudWatch, Splunk, and more.
  name: 50+ Sources
- description: Route data to Elasticsearch, Datadog, S3, BigQuery, Splunk, Loki, and many more destinations.
  name: 80+ Sinks
- description: Purpose-built expression language with 100+ functions for transforming observability data.
  name: Vector Remap Language (VRL)
- description: Built-in HTTP/gRPC API for health checks and component inspection (must be explicitly enabled).
  name: Observability API
- description: Deploy as DaemonSet (agent) or Deployment (aggregator) with official Helm charts.
  name: Kubernetes Native
- description: Run as a lightweight agent on each node or as a centralized aggregator for fan-in routing.
  name: Agent and Aggregator Modes
finops:
- name: Vector Finops
  service_category: API
  slug: vector-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vector.png
integrations:
- description: Native Datadog logs and metrics sink; Vector was created and is maintained by Datadog.
  name: Datadog
- description: Elasticsearch sink for forwarding logs and metrics to Elasticsearch clusters.
  name: Elasticsearch
- description: Splunk HTTP Event Collector sink for sending data to Splunk Enterprise and Cloud.
  name: Splunk HEC
- description: Kafka source and sink for consuming and producing observability data streams.
  name: Kafka
- description: S3 sink for archiving logs and metrics to Amazon S3 for long-term storage.
  name: AWS S3
- description: Loki sink for forwarding logs to Grafana's log aggregation system.
  name: Grafana Loki
- description: Prometheus remote write sink and scrape source for metrics pipelines.
  name: Prometheus
- description: Kubernetes source for collecting container logs, pod metadata, and events.
  name: Kubernetes
json_schemas:
- name: HealthResponse
  property_count: 1
  slug: vector-observability-api-health-response
json_structures:
- name: Vector Observability Api Health Response Structure
  property_count: 1
  slug: vector-observability-api-health-response-structure
jsonld:
- class_count: 1
  name: Vector Observability Api Context
  property_count: 1
  slug: vector-observability-api-context
layout: provider
modified: '2026-05-19'
name: Vector
nav: Providers
network: true
overview: 'Vector publishes 1 API on the [APIs.io](https://apis.io/) network: Health API. Tagged areas include Data Pipeline, Logs, Metrics, Observability, and Open-Source.


  The Vector catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vector''s developer surface includes documentation, release notes, engineering blog, Stack Overflow tag, and 12 more developer resources.'
plans:
- name: Vector Plans Pricing
  plan_count: 3
  slug: vector-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Vector Rate Limits
  slug: vector-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Vector API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: vector-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Vector API Rules
  rule_count: 17
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 8
  slug: vector-spectral-rules
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 41.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 22.1
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 40.0
  previous_composite: 24.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vector/refs/heads/main/screenshots/vector-2026-06-20T200848.png
security:
- kind: domain-security
  name: Vector Domain Security
  slug: vector-domain-security
  summary_line: TLSv1.3
slug: vector
tags:
- Data Pipeline
- Logs
- Metrics
- Observability
- Open-Source
- Rust
- Traces
use_cases:
- description: Replace multiple log shippers with a single Vector pipeline for all log collection and routing.
  name: Log Pipeline Unification
- description: Filter, sample, and transform data before sending to expensive SaaS observability platforms.
  name: Observability Cost Reduction
- description: Route observability data to multiple backends simultaneously to facilitate migration.
  name: Vendor Switching
- description: Deploy Vector as a DaemonSet to collect container logs from all Kubernetes nodes.
  name: Kubernetes Log Collection
- description: Parse, enrich, and normalize log events using VRL before routing to downstream systems.
  name: Log Enrichment
- description: Collect host and service metrics using Vector's built-in sources and forward to Prometheus or DataDog.
  name: Metrics Collection
- description: Use Vector to filter and route Splunk data to reduce indexing volume and licensing costs.
  name: Splunk Cost Reduction
website: https://vector.dev
---
