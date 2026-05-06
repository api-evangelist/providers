---
aid: apache-skywalking
name: Apache SkyWalking
description: Apache SkyWalking is an open-source APM (Application Performance Monitoring) system that provides monitoring, tracing, and diagnosing capabilities for distributed systems in cloud native architectures. It supports auto-instrumentation for Java, .NET, Python, Go, Node.js, PHP, and Ruby, offering distributed tracing, metrics collection, log aggregation, and continuous profiling through a unified observability platform governed by the Apache Software Foundation.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - APM
  - Application Performance Monitoring
  - Cloud Native
  - Distributed Tracing
  - Monitoring
  - Observability
  - Open Source
  - Tracing
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-skywalking/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-skywalking:apache-skywalking-graphql-query-api
    name: Apache SkyWalking GraphQL Query API
    description: The SkyWalking GraphQL Query API provides a comprehensive query interface for retrieving observability data including traces, metrics, logs, alarms, topology maps, and profiling results. It supports metadata queries (services, instances, endpoints), topology queries, metrics via SkyWalking Metrics Query Expression (MQE), log queries, trace queries, alarm queries, and profiling queries. The API is served on port 12800 and consumed by the native UI and CLI tools.
    humanURL: https://github.com/apache/skywalking-query-protocol
    tags:
      - GraphQL
      - Metrics
      - Observability
      - Tracing
      - Logs
      - Alarms
      - Profiling
    properties:
      - type: Documentation
        url: https://skywalking.apache.org/docs/main/next/en/api/query-protocol/
      - type: GitHubRepository
        url: https://github.com/apache/skywalking-query-protocol
  - aid: apache-skywalking:apache-skywalking-rest-api
    name: Apache SkyWalking REST API
    description: The SkyWalking HTTP REST API exposes endpoints on port 12800 for health checks, PromQL-compatible metrics queries (Prometheus Query Language), LogQL log queries, and dynamic configuration management. PromQL support enables integration with Grafana and other Prometheus-compatible visualization tools. LogQL support enables integration with Grafana Loki-compatible tooling.
    humanURL: https://skywalking.apache.org/docs/main/next/en/api/promql-service/
    tags:
      - REST
      - HTTP
      - PromQL
      - LogQL
      - Health Check
      - Metrics
    properties:
      - type: Documentation
        url: https://skywalking.apache.org/docs/main/next/en/api/promql-service/
      - type: Documentation
        url: https://skywalking.apache.org/docs/main/next/en/api/logql-service/
  - aid: apache-skywalking:apache-skywalking-grpc-data-collect-protocol
    name: Apache SkyWalking gRPC Data Collect Protocol
    description: The SkyWalking data collection protocol defines gRPC service definitions for telemetry data ingestion from language agents and service mesh proxies. It covers trace data (v3), JVM metrics, meter protocol, event reporting, browser performance data, instance properties, continuous profiling, eBPF profiling, and log data protocols. Agents report data to OAP server on port 11800.
    humanURL: https://github.com/apache/skywalking-data-collect-protocol
    tags:
      - gRPC
      - Protocol Buffers
      - Telemetry
      - Agents
      - Tracing
      - Metrics
    properties:
      - type: Documentation
        url: https://skywalking.apache.org/docs/main/next/en/api/trace-data-protocol-v3/
      - type: GitHubRepository
        url: https://github.com/apache/skywalking-data-collect-protocol
common:
  - type: GitHubOrganization
    url: https://github.com/apache?q=skywalking
  - type: GitHubRepository
    url: https://github.com/apache/skywalking
  - type: Documentation
    url: https://skywalking.apache.org/docs/
  - type: Portal
    url: https://skywalking.apache.org/
  - type: Blog
    url: https://skywalking.apache.org/blog/
  - type: ReleaseNotes
    url: https://github.com/apache/skywalking/releases
  - type: Support
    url: https://skywalking.apache.org/community/
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: SDK
    url: https://github.com/apache/skywalking-java
    title: Java Agent SDK
  - type: SDK
    url: https://github.com/apache/skywalking-python
    title: Python Agent SDK
  - type: SDK
    url: https://github.com/apache/skywalking-go
    title: Go Agent SDK
  - type: SDK
    url: https://github.com/apache/skywalking-nodejs
    title: Node.js Agent SDK
  - type: SDK
    url: https://github.com/apache/skywalking-php
    title: PHP Agent SDK
  - type: SDK
    url: https://github.com/apache/skywalking-ruby
    title: Ruby Agent SDK
  - type: SDK
    url: https://github.com/apache/skywalking-rust
    title: Rust Agent SDK
  - type: SDK
    url: https://github.com/apache/skywalking-client-js
    title: JavaScript Browser Agent SDK
  - type: Features
    data:
      - name: Distributed Tracing
        description: Auto-instrumented distributed tracing across 10+ languages with trace correlation and cross-service propagation.
      - name: Metrics Collection
        description: Service, instance, and endpoint metrics with SkyWalking Metrics Query Expression (MQE) engine.
      - name: Log Aggregation
        description: Centralized log collection and search with LAL (Log Analysis Language) rules.
      - name: Service Topology
        description: Automatic service dependency mapping and topology visualization.
      - name: Alarm System
        description: Rule-based alerting on metrics thresholds with webhook and notification integrations.
      - name: Continuous Profiling
        description: CPU, memory, and network profiling via async-profiler, pprof, and eBPF.
      - name: eBPF Network Profiling
        description: Out-of-process network performance profiling using eBPF without code instrumentation.
      - name: PromQL Compatibility
        description: Prometheus Query Language API for Grafana and other Prometheus-compatible tools.
      - name: BanyanDB Storage
        description: Native observability database optimized for time-series and trace data storage.
      - name: Multi-Layer Service Model
        description: Hierarchical service model supporting mesh, Kubernetes, APISIX gateway, and custom layers.
  - type: UseCases
    data:
      - name: Microservices Observability
        description: End-to-end monitoring and tracing for microservices architectures in Kubernetes.
      - name: Service Mesh Monitoring
        description: Integration with Istio and other service meshes for traffic and performance monitoring.
      - name: Root Cause Analysis
        description: Trace-based root cause analysis for distributed system failures and latency issues.
      - name: SLA Monitoring
        description: Service level agreement monitoring with metrics dashboards and alerting.
      - name: Continuous Profiling
        description: Always-on profiling for performance optimization without overhead in production.
  - type: Integrations
    data:
      - name: Kubernetes
        description: Native Kubernetes monitoring via skywalking-kubernetes Helm charts and event integration.
      - name: Grafana
        description: PromQL-compatible metrics API enables native Grafana dashboard integration.
      - name: Istio
        description: Service mesh telemetry collection from Istio-managed service traffic.
      - name: APISIX
        description: API Gateway integration for monitoring API traffic through Apache APISIX.
      - name: Elasticsearch
        description: Elasticsearch and OpenSearch backend storage for trace and log data.
      - name: BanyanDB
        description: Native high-performance observability database built for SkyWalking.
      - name: Kafka
        description: Kafka-based data pipeline for high-throughput telemetry ingestion.
      - name: OpenTelemetry
        description: OpenTelemetry receiver for ingesting OTLP traces, metrics, and logs.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
