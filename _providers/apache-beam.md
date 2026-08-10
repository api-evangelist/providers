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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: The Apache Beam SDK provides the programming model for constructing data processing pipelines. Available in Java, Python, and Go, it provides PCollections, PTransforms, and Runners for batch and strea
  name: Apache Beam SDK
  slug: apache-beam-sdk
- description: The Beam Job Service API provides a gRPC-based interface for submitting, managing, and monitoring Apache Beam pipeline jobs on supported runners. It is part of the Beam portability framework and enabl
  name: Apache Beam Job Service API
  slug: apache-beam-job-service
artifact_total: 30
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-beam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-beam-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-beam
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/beam
- group: docs
  title: ''
  type: Documentation
  url: https://beam.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://beam.apache.org/get-started/
- group: learn
  title: ''
  type: Tutorials
  url: https://beam.apache.org/get-started/wordcount-example/
- group: operate
  title: ''
  type: Support
  url: https://beam.apache.org/community/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: operate
  title: ''
  type: ChangeLog
  url: https://beam.apache.org/blog/
- group: build
  title: Python SDK (PyPI)
  type: SDKs
  url: https://pypi.org/project/apache-beam/
- group: build
  title: Java SDK (Maven)
  type: SDKs
  url: https://search.maven.org/artifact/org.apache.beam/beam-sdks-java-core
- group: build
  title: Go SDK
  type: SDKs
  url: https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam
- group: company
  title: ''
  type: Blog
  url: https://beam.apache.org/feed.xml
created: '2026-03-16'
description: Apache Beam is a unified, open-source programming model developed by the Apache Software Foundation for defining both batch and streaming data processing pipelines. It provides a portable API layer that lets developers write pipeline logic once in Java, Python, or Go and deploy it to multiple execution engines (runners) including Apache Flink, Apache Spark, Google Cloud Dataflow, and the direct runner for local testing. The Beam portability framework enables cross-language pipelines and runner-agnostic execution.
features:
- description: Single programming model for both batch and streaming data processing with consistent semantics.
  name: Unified Batch and Streaming
- description: Write pipeline logic once and execute on Apache Flink, Spark, Google Dataflow, Samza, or the local direct runner.
  name: Runner Portability
- description: Native SDKs for Java, Python, and Go with cross-language transform support for mixing languages.
  name: Multi-Language Support
- description: Flexible windowing (fixed, sliding, session, global) and trigger strategies for streaming data processing.
  name: Windowing and Triggers
- description: Built-in connectors for BigQuery, Kafka, Pub/Sub, GCS, HDFS, databases, and many other sources and sinks.
  name: I/O Connectors
- description: SQL-based data processing on Beam PCollections using Apache Calcite for query planning.
  name: Beam SQL
- description: RunInference transform for integrating ML model inference into Beam pipelines with TensorFlow, PyTorch, and sklearn.
  name: ML Integration
- description: Schema inference and typed PCollections for structured data processing with automatic serialization.
  name: Schema-Aware Processing
- description: Call Java transforms from Python pipelines and vice versa via the Beam portability framework.
  name: Cross-Language Transforms
- description: Built-in metrics API and integration with runner-specific monitoring dashboards.
  name: Metrics and Monitoring
finops:
- name: Apache Beam Finops
  service_category: API
  slug: apache-beam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-beam.png
integrations:
- description: Managed Apache Beam runner on Google Cloud with autoscaling and monitoring.
  name: Google Cloud Dataflow
- description: Apache Flink runner for stateful stream processing with exactly-once semantics.
  name: Apache Flink
- description: Apache Spark runner for batch and streaming processing on Spark clusters.
  name: Apache Spark
- description: Kafka I/O connector for reading and writing Kafka topics in Beam pipelines.
  name: Apache Kafka
- description: BigQuery I/O connector for reading and writing BigQuery tables in Beam pipelines.
  name: Google BigQuery
- description: HDFS I/O connector for reading and writing files on Hadoop HDFS.
  name: Apache Hadoop
- description: TFX uses Beam as the runtime for ML data validation and preprocessing components.
  name: TensorFlow Extended (TFX)
layout: provider
modified: '2026-04-19'
name: Apache Beam
nav: Providers
network: true
overview: 'Apache Beam publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Apache, Batch Processing, Data Pipeline, ETL, and Open Source.


  Apache Beam''s developer surface includes documentation, getting-started guide, support, changelog, engineering blog, and 10 more developer resources.'
plans:
- name: Apache Beam Plans Pricing
  plan_count: 3
  slug: apache-beam-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Apache Beam Rate Limits
  slug: apache-beam-rate-limits
score:
  band: thin
  composite: 31.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 31.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-beam/refs/heads/main/screenshots/apache-beam-2026-06-20T172044.png
security:
- kind: domain-security
  name: Apache Beam Domain Security
  slug: apache-beam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Beam Vulnerability Disclosure
  slug: apache-beam-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-beam
tags:
- Apache
- Batch Processing
- Data Pipeline
- ETL
- Open Source
- Python
- Streaming
- Unified Model
use_cases:
- description: Extract, transform, and load data between storage systems using portable, reusable pipeline components.
  name: ETL Pipelines
- description: Process high-throughput event streams with low-latency windowing and triggering strategies.
  name: Real-Time Stream Processing
- description: Compute aggregate statistics, joins, and group-by operations on large historical datasets.
  name: Batch Data Analytics
- description: Run ML model inference in distributed pipelines using the RunInference transform.
  name: ML Model Inference at Scale
- description: Parse, filter, and enrich log events from Kafka or Pub/Sub for operational analytics.
  name: Log and Event Processing
- description: Migrate data between cloud providers and storage systems using Beam's portable I/O connectors.
  name: Data Migration
---
