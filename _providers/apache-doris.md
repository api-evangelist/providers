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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Apache Doris provides a MySQL-compatible protocol for SQL queries, a REST API for cluster management and monitoring, Stream Load HTTP API for real-time bulk data ingestion, Routine Load for continuous
  name: Apache Doris
  slug: apache-doris
artifact_total: 36
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/doris/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/doris/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/doris/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/doris/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/doris/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/doris/blob/master/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-doris-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-doris-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://doris.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://doris.apache.org/docs/dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://doris.apache.org/docs/dev/install/
- group: company
  title: ''
  type: Blog
  url: https://doris.apache.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/doris
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/apache-doris
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/vocabulary/apache-doris-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://doris.apache.org/llms.txt
created: '2026-03-16'
description: Apache Doris is a high-performance, real-time analytical database based on MPP (Massively Parallel Processing) architecture, governed by the Apache Software Foundation. It provides MySQL-protocol-compatible SQL queries, sub-second query latency on large-scale data, columnar storage with vectorized execution, real-time upsert via Stream Load and Routine Load APIs, and federated querying over data lakes (Hive, Iceberg, Hudi). It supports both shared-nothing and storage/compute-separated deployment modes.
examples:
- key_count: 13
  name: Apache Doris Routine Load Job Example
  slug: apache-doris-routine-load-job-example
- key_count: 17
  name: Apache Doris Stream Load Response Example
  slug: apache-doris-stream-load-response-example
- key_count: 7
  name: Apache Doris Table Schema Example
  slug: apache-doris-table-schema-example
features:
- description: Massively parallel processing with columnar storage and vectorized execution engine for high-concurrency sub-second analytical queries.
  name: MPP Columnar Analytics
- description: HTTP-based bulk data ingestion API that loads CSV, JSON, and Parquet data in real time with transactional guarantees.
  name: Stream Load API
- description: Fully MySQL-wire-protocol compatible, enabling use of standard MySQL clients, drivers, and BI tools without modification.
  name: MySQL Protocol Compatibility
- description: Query external data in Hive, Iceberg, Hudi, and Delta Lake tables without data movement using Multi-Catalog.
  name: Federated Data Lakehouse Queries
- description: Primary key based upsert model supports real-time CDC data ingestion with micro-second latency row-level updates.
  name: Real-Time Upsert (Unique Key Model)
- description: Continuous data ingestion from Apache Kafka topics with automatic offset management and exactly-once semantics.
  name: Routine Load from Kafka
- description: Hot/warm/cold data tiering with object storage (S3, HDFS) for cost-optimized storage at scale.
  name: Tiered Storage
- description: Model Context Protocol (MCP) server enabling AI agents to query Doris databases through natural language.
  name: MCP Server
finops:
- name: Apache Doris Finops
  service_category: API
  slug: apache-doris-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-doris.png
integrations:
- description: Official Flink Connector for reading from and writing to Doris in real-time Flink streaming pipelines.
  name: Apache Flink
- description: Official Spark Connector for batch ETL and analytics workflows using Apache Spark.
  name: Apache Spark
- description: Kafka Connector and Routine Load for continuous real-time data ingestion from Kafka topics.
  name: Apache Kafka
- description: Multi-Catalog feature enables federated queries over Iceberg, Hudi, and Hive Metastore data lakes.
  name: Apache Iceberg / Hudi / Hive
- description: Official Kubernetes Operator for automated Doris cluster lifecycle management.
  name: Kubernetes
- description: OpenTelemetry demo integration for observability and tracing in Doris deployments.
  name: OpenTelemetry
json_schemas:
- name: RoutineLoadJob
  property_count: 13
  slug: apache-doris-routine-load-job
- name: StreamLoadResponse
  property_count: 17
  slug: apache-doris-stream-load-response
- name: TableSchema
  property_count: 7
  slug: apache-doris-table-schema
json_structures:
- name: Apache Doris Routine Load Job Structure
  property_count: 13
  slug: apache-doris-routine-load-job-structure
- name: Apache Doris Stream Load Response Structure
  property_count: 17
  slug: apache-doris-stream-load-response-structure
- name: Apache Doris Table Schema Structure
  property_count: 7
  slug: apache-doris-table-schema-structure
jsonld:
- class_count: 4
  name: Apache Doris Context
  property_count: 38
  slug: apache-doris-context
layout: provider
modified: '2026-04-19'
name: Apache Doris
nav: Providers
network: true
overview: 'Apache Doris publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Apache, Database, Lakehouse, and MPP.


  The Apache Doris catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apache Doris'' developer surface includes developer portal, documentation, getting-started guide, engineering blog, Stack Overflow tag, and 12 more developer resources.'
plans:
- name: Apache Doris Plans Pricing
  plan_count: 3
  slug: apache-doris-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Apache Doris Rate Limits
  slug: apache-doris-rate-limits
rules:
- name: Apache Doris API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-doris-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.6
  delta: -3.6
  facets:
    commercial_clarity: 15.8
    contract_quality: 29.0
    developer_ergonomics: 30.4
    discoverability: 66.7
    governance: 68.8
    operational_transparency: 39.5
  previous_composite: 40.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/screenshots/apache-doris-2026-06-20T172056.png
security:
- kind: domain-security
  name: Apache Doris Domain Security
  slug: apache-doris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Doris Vulnerability Disclosure
  slug: apache-doris-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-doris
tags:
- Analytics
- Apache
- Database
- Lakehouse
- MPP
- OLAP
- Open Source
- Real-Time
- SQL
use_cases:
- description: Power business intelligence dashboards with sub-second query latency on live data updated continuously.
  name: Real-Time Dashboards and Reporting
- description: Ingest and analyze high-volume log, metric, and event data in real time using inverted indexes and full-text search.
  name: Log and Event Analytics
- description: Consolidate customer behavioral and transactional data from multiple sources for real-time segmentation and analytics.
  name: Customer Data Platform
- description: Federate queries across data lake (Hive, Iceberg) and operational databases without ETL movement.
  name: Data Lakehouse Analytics
- description: Enable data analysts to run complex exploratory SQL queries on petabyte-scale datasets with fast response times.
  name: Ad-Hoc Analytics
website: https://doris.apache.org/
---
