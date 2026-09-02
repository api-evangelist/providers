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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apache Zipkin Agentic Access
  operation_count: 9
  slug: apache-zipkin-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- description: Tag key/value autocompletion
  name: Apache Zipkin autocomplete API
  slug: apache-zipkin-autocomplete-api
- description: Service discovery and dependency links
  name: Apache Zipkin services API
  slug: apache-zipkin-services-api
- description: Ingest spans and query span names
  name: Apache Zipkin spans API
  slug: apache-zipkin-spans-api
- description: Query trace data
  name: Apache Zipkin traces API
  slug: apache-zipkin-traces-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zipkin autocomplete API
  slug: open-apache-zipkin-autocomplete-api
- collection_type: open
  name: Zipkin autocomplete services API
  slug: open-apache-zipkin-services-api
- collection_type: open
  name: Zipkin autocomplete spans API
  slug: open-apache-zipkin-spans-api
- collection_type: open
  name: Zipkin autocomplete traces API
  slug: open-apache-zipkin-traces-api
- collection_type: open
  name: Zipkin API
  slug: open-apache-zipkin
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/openzipkin/zipkin/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/openzipkin/zipkin/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/openzipkin/zipkin/blob/master/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/openzipkin/zipkin/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-zipkin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-zipkin-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openzipkin/zipkin
- group: docs
  title: ''
  type: Documentation
  url: https://zipkin.io/pages/documentation.html
- group: start
  title: ''
  type: Portal
  url: https://zipkin.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://zipkin.io/pages/quickstart.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/openzipkin/zipkin/releases
- group: operate
  title: ''
  type: Support
  url: https://gitter.im/openzipkin/zipkin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: build
  title: Python SDK
  type: SDKs
  url: https://pypi.org/project/py_zipkin/
- group: build
  title: Java SDK
  type: SDKs
  url: https://search.maven.org/search?q=io.zipkin
created: '2026-03-16'
description: Apache Zipkin is a distributed tracing system that helps gather timing data needed to troubleshoot latency problems in service architectures. It manages both the collection and lookup of tracing data through a collector and query service. Zipkin provides a REST API, web UI, and multiple storage backends (Cassandra, Elasticsearch, MySQL). It supports the B3 propagation format and is compatible with OpenZipkin instrumentation libraries. Originally created at Twitter, it is now maintained as an open-source project.
features:
- description: Collect timing and metadata for distributed service calls with B3 propagation headers.
  name: Distributed Trace Collection
- description: Web UI and REST API for searching and visualizing distributed traces with latency analysis.
  name: Trace Query and Visualization
- description: Automatic service call graph generation from collected trace data.
  name: Service Dependency Graph
- description: Cassandra, Elasticsearch, and MySQL storage backends for different scale requirements.
  name: Multiple Storage Backends
- description: Accepts OTLP/Zipkin spans from OpenTelemetry instrumented services.
  name: OpenTelemetry Compatible
- description: Standard B3 trace propagation headers for distributed context passing across services.
  name: B3 Propagation
finops:
- name: Apache Zipkin Finops
  service_category: API
  slug: apache-zipkin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-zipkin.png
integrations:
- description: Spring Boot auto-instrumentation for trace propagation and Zipkin reporting.
  name: Spring Cloud Sleuth
- description: Java instrumentation library (Brave) for adding Zipkin tracing to Java applications.
  name: Brave
- description: Elasticsearch storage backend for scalable trace data storage and search.
  name: Elasticsearch
- description: Cassandra storage backend for high-volume trace data.
  name: Apache Cassandra
- description: OpenTelemetry Zipkin exporter for reporting OTLP traces to Zipkin.
  name: OpenTelemetry
- description: Kafka collector for ingesting spans from high-throughput microservice architectures.
  name: Kafka
layout: provider
modified: '2026-04-19'
name: Apache Zipkin
nav: Providers
network: true
overview: 'Apache Zipkin publishes 4 APIs on the [APIs.io](https://apis.io/) network, including autocomplete API, services API, spans API, and 1 more. Tagged areas include Distributed Tracing, Microservices, Monitoring, Observability, and Open-Source.


  Apache Zipkin''s developer surface includes documentation, developer portal, getting-started guide, release notes, support, and 10 more developer resources.'
plans:
- name: Apache Zipkin Plans Pricing
  plan_count: 3
  slug: apache-zipkin-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Apache Zipkin Rate Limits
  slug: apache-zipkin-rate-limits
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 43.4
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 85.0
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-zipkin/refs/heads/main/screenshots/apache-zipkin-2026-06-20T172158.png
security:
- kind: domain-security
  name: Apache Zipkin Domain Security
  slug: apache-zipkin-domain-security
  summary_line: TLSv1.3
slug: apache-zipkin
tags:
- Distributed Tracing
- Microservices
- Monitoring
- Observability
- Open-Source
use_cases:
- description: Identify bottlenecks and slow service calls in distributed architectures.
  name: Microservices Latency Troubleshooting
- description: Automatically discover and visualize service-to-service call graphs.
  name: Service Dependency Mapping
- description: Compare trace data before and after deployments to detect performance regressions.
  name: Performance Regression Detection
- description: Follow distributed call chains to identify the root cause of errors and failures.
  name: Root Cause Analysis
website: https://zipkin.io/
---
