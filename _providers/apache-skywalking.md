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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 3
apis:
- description: The SkyWalking GraphQL Query API provides a comprehensive query interface for retrieving observability data including traces, metrics, logs, alarms, topology maps, and profiling results. It supports m
  name: Apache SkyWalking GraphQL Query API
  slug: apache-skywalking-graphql-query-api
- description: 'The SkyWalking HTTP REST API exposes endpoints on port 12800 for health checks, PromQL-compatible metrics queries (Prometheus Query Language), LogQL log queries, and dynamic configuration management. '
  name: Apache SkyWalking REST API
  slug: apache-skywalking-rest-api
- description: The SkyWalking data collection protocol defines gRPC service definitions for telemetry data ingestion from language agents and service mesh proxies. It covers trace data (v3), JVM metrics, meter proto
  name: Apache SkyWalking gRPC Data Collect Protocol
  slug: apache-skywalking-grpc-data-collect-protocol
artifact_total: 32
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-skywalking-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-skywalking-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache?q=skywalking
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/skywalking
- group: docs
  title: ''
  type: Documentation
  url: https://skywalking.apache.org/docs/
- group: start
  title: ''
  type: Portal
  url: https://skywalking.apache.org/
- group: company
  title: ''
  type: Blog
  url: https://skywalking.apache.org/blog/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/skywalking/releases
- group: operate
  title: ''
  type: Support
  url: https://skywalking.apache.org/community/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: build
  title: Java Agent SDK
  type: SDKs
  url: https://github.com/apache/skywalking-java
- group: build
  title: Python Agent SDK
  type: SDKs
  url: https://github.com/apache/skywalking-python
- group: build
  title: Go Agent SDK
  type: SDKs
  url: https://github.com/apache/skywalking-go
- group: build
  title: Node.js Agent SDK
  type: SDKs
  url: https://github.com/apache/skywalking-nodejs
- group: build
  title: PHP Agent SDK
  type: SDKs
  url: https://github.com/apache/skywalking-php
- group: build
  title: Ruby Agent SDK
  type: SDKs
  url: https://github.com/apache/skywalking-ruby
- group: build
  title: Rust Agent SDK
  type: SDKs
  url: https://github.com/apache/skywalking-rust
- group: build
  title: JavaScript Browser Agent SDK
  type: SDKs
  url: https://github.com/apache/skywalking-client-js
created: '2026-03-16'
description: Apache SkyWalking is an open-source APM (Application Performance Monitoring) system that provides monitoring, tracing, and diagnosing capabilities for distributed systems in cloud native architectures. It supports auto-instrumentation for Java, .NET, Python, Go, Node.js, PHP, and Ruby, offering distributed tracing, metrics collection, log aggregation, and continuous profiling through a unified observability platform governed by the Apache Software Foundation.
features:
- description: Auto-instrumented distributed tracing across 10+ languages with trace correlation and cross-service propagation.
  name: Distributed Tracing
- description: Service, instance, and endpoint metrics with SkyWalking Metrics Query Expression (MQE) engine.
  name: Metrics Collection
- description: Centralized log collection and search with LAL (Log Analysis Language) rules.
  name: Log Aggregation
- description: Automatic service dependency mapping and topology visualization.
  name: Service Topology
- description: Rule-based alerting on metrics thresholds with webhook and notification integrations.
  name: Alarm System
- description: CPU, memory, and network profiling via async-profiler, pprof, and eBPF.
  name: Continuous Profiling
- description: Out-of-process network performance profiling using eBPF without code instrumentation.
  name: eBPF Network Profiling
- description: Prometheus Query Language API for Grafana and other Prometheus-compatible tools.
  name: PromQL Compatibility
- description: Native observability database optimized for time-series and trace data storage.
  name: BanyanDB Storage
- description: Hierarchical service model supporting mesh, Kubernetes, APISIX gateway, and custom layers.
  name: Multi-Layer Service Model
finops:
- name: Apache Skywalking Finops
  service_category: API
  slug: apache-skywalking-finops
graphqls:
- description: The SkyWalking GraphQL Query API provides a comprehensive query interface for retrieving observability data including traces, metrics, logs, alarms, topology maps, and profiling results. It supports m
  name: Apache SkyWalking GraphQL API
  slug: apache-skywalking-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-skywalking.png
integrations:
- description: Native Kubernetes monitoring via skywalking-kubernetes Helm charts and event integration.
  name: Kubernetes
- description: PromQL-compatible metrics API enables native Grafana dashboard integration.
  name: Grafana
- description: Service mesh telemetry collection from Istio-managed service traffic.
  name: Istio
- description: API Gateway integration for monitoring API traffic through Apache APISIX.
  name: APISIX
- description: Elasticsearch and OpenSearch backend storage for trace and log data.
  name: Elasticsearch
- description: Native high-performance observability database built for SkyWalking.
  name: BanyanDB
- description: Kafka-based data pipeline for high-throughput telemetry ingestion.
  name: Kafka
- description: OpenTelemetry receiver for ingesting OTLP traces, metrics, and logs.
  name: OpenTelemetry
layout: provider
modified: '2026-04-19'
name: Apache SkyWalking
nav: Providers
network: true
overview: 'Apache SkyWalking publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include APM, Application Performance Monitoring, Cloud Native, Distributed Tracing, and Monitoring.


  Apache SkyWalking''s developer surface includes documentation, developer portal, engineering blog, release notes, support, and 13 more developer resources.'
plans:
- name: Apache Skywalking Plans Pricing
  plan_count: 3
  slug: apache-skywalking-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Apache Skywalking Rate Limits
  slug: apache-skywalking-rate-limits
score:
  band: thin
  composite: 33.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 33.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-skywalking/refs/heads/main/screenshots/apache-skywalking-2026-06-20T172144.png
security:
- kind: domain-security
  name: Apache Skywalking Domain Security
  slug: apache-skywalking-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Skywalking Vulnerability Disclosure
  slug: apache-skywalking-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-skywalking
tags:
- APM
- Application Performance Monitoring
- Cloud Native
- Distributed Tracing
- Monitoring
- Observability
- Open Source
- Tracing
use_cases:
- description: End-to-end monitoring and tracing for microservices architectures in Kubernetes.
  name: Microservices Observability
- description: Integration with Istio and other service meshes for traffic and performance monitoring.
  name: Service Mesh Monitoring
- description: Trace-based root cause analysis for distributed system failures and latency issues.
  name: Root Cause Analysis
- description: Service level agreement monitoring with metrics dashboards and alerting.
  name: SLA Monitoring
- description: Always-on profiling for performance optimization without overhead in production.
  name: Continuous Profiling
website: https://skywalking.apache.org/
---
