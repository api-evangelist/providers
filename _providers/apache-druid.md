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
- acting_count: 11
  human_in_the_loop: 0
  name: Apache Druid Agentic Access
  operation_count: 13
  slug: apache-druid-agentic-access
  summary_line: 13 operations · 11 acting
api_count: 1
apis:
- description: The Druid API from Apache Druid — 10 operation(s) for druid.
  name: Apache Druid Druid API
  slug: apache-druid-druid-api
artifact_total: 42
collections:
- collection_type: open
  name: Apache Druid REST API
  slug: open-apache-druid
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-druid-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-druid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-druid-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://druid.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://druid.apache.org/docs/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://druid.apache.org/docs/latest/tutorials/
- group: company
  title: ''
  type: Blog
  url: https://druid.apache.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/druid
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/druid
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/vocabulary/apache-druid-vocabulary.yaml
created: '2026-03-16'
description: Apache Druid is a high-performance, real-time analytics database governed by the Apache Software Foundation, designed for fast slice-and-dice OLAP queries on event-time data. It features a distributed, column-oriented storage engine with automatic rollup, supports both streaming (Kafka, Kinesis) and batch (S3, HDFS, local) data ingestion, and provides a SQL query interface plus a native JSON query API via REST. Druid is optimized for sub-second queries at petabyte scale with high concurrency.
examples:
- key_count: 9
  name: Apache Druid Ingestion Task Example
  slug: apache-druid-ingestion-task-example
- key_count: 7
  name: Apache Druid Sql Query Request Example
  slug: apache-druid-sql-query-request-example
- key_count: 5
  name: Apache Druid Sql Query Response Example
  slug: apache-druid-sql-query-response-example
- key_count: 8
  name: Apache Druid Supervisor Example
  slug: apache-druid-supervisor-example
features:
- description: Columnar storage with bitmap indexes, dictionary encoding, and pre-aggregation (rollup) enables sub-second queries on billions of events.
  name: Sub-Second OLAP Queries
- description: REST endpoint for submitting standard SQL queries with ANSI SQL support, time-based filtering, and streaming response options.
  name: Druid SQL API
- description: Druid-native query format (Timeseries, TopN, GroupBy, Scan, Search) for maximum control and performance.
  name: Native JSON Query API
- description: Real-time data ingestion from Apache Kafka and Amazon Kinesis with supervisor-managed offset tracking and exactly-once semantics.
  name: Streaming Ingestion
- description: Parallel batch indexing tasks from local files, S3, GCS, HDFS, and other external storage systems.
  name: Batch Ingestion
- description: Pre-aggregates metrics at ingestion time to reduce storage and query time, configurable per datasource.
  name: Automatic Rollup
- description: All data is partitioned by time interval (segments), enabling efficient time-range query pruning.
  name: Time-Based Partitioning
- description: Query isolation and resource management via query lanes, scheduler priorities, and row-level access control.
  name: Multi-Tenancy
finops:
- name: Apache Druid Finops
  service_category: API
  slug: apache-druid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-druid.png
integrations:
- description: KafkaSupervisor for real-time continuous ingestion from Kafka topics into Druid datasources.
  name: Apache Kafka
- description: KinesisSupervisor for real-time data ingestion from AWS Kinesis data streams.
  name: Amazon Kinesis
- description: Native Hadoop batch indexing task for bulk loading data from HDFS or MapReduce job outputs.
  name: Apache Hadoop / HDFS
- description: Batch and streaming ingestion from object storage (S3, GCS, Azure Blob) using index tasks.
  name: Amazon S3 / GCS
- description: Druid-Hive integration for querying Druid datasources from HiveQL and performing joins.
  name: Apache Hive
- description: Official Kubernetes operator for deploying and managing Druid clusters on Kubernetes.
  name: Kubernetes
- description: Imply provides a commercial managed Druid service with additional features and enterprise support.
  name: Imply (Commercial)
json_schemas:
- name: IngestionTask
  property_count: 9
  slug: apache-druid-ingestion-task
- name: SqlQueryRequest
  property_count: 7
  slug: apache-druid-sql-query-request
- name: SqlQueryResponse
  property_count: 5
  slug: apache-druid-sql-query-response
- name: Supervisor
  property_count: 8
  slug: apache-druid-supervisor
json_structures:
- name: Apache Druid Ingestion Task Structure
  property_count: 9
  slug: apache-druid-ingestion-task-structure
- name: Apache Druid Sql Query Request Structure
  property_count: 7
  slug: apache-druid-sql-query-request-structure
- name: Apache Druid Sql Query Response Structure
  property_count: 5
  slug: apache-druid-sql-query-response-structure
- name: Apache Druid Supervisor Structure
  property_count: 8
  slug: apache-druid-supervisor-structure
jsonld:
- class_count: 5
  name: Apache Druid Context
  property_count: 32
  slug: apache-druid-context
layout: provider
modified: '2026-05-19'
name: Apache Druid
nav: Providers
network: true
overview: 'Apache Druid publishes 1 API on the [APIs.io](https://apis.io/) network: Druid API. Tagged areas include Analytics, Apache, Database, Kafka, and OLAP.


  The Apache Druid catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apache Druid''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, Stack Overflow tag, and 6 more developer resources.'
plans:
- name: Apache Druid Plans Pricing
  plan_count: 3
  slug: apache-druid-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 5
  name: Apache Druid Rate Limits
  slug: apache-druid-rate-limits
rules:
- name: Apache Druid API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-druid-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.9
  delta: -4.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.7
    developer_ergonomics: 30.4
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/screenshots/apache-druid-2026-06-20T172055.png
security:
- kind: domain-security
  name: Apache Druid Domain Security
  slug: apache-druid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Druid Vulnerability Disclosure
  slug: apache-druid-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-druid
tags:
- Analytics
- Apache
- Database
- Kafka
- OLAP
- Open Source
- Real-Time
- SQL
- Time Series
use_cases:
- description: Analyze click streams, IoT events, application logs, and user behavior data with sub-second query latency.
  name: Real-Time Event Analytics
- description: Power interactive BI dashboards with high-concurrency low-latency queries backed by Druid's columnar engine.
  name: Business Intelligence Dashboards
- description: Ingest and analyze network flow data and security events in real time for threat detection and capacity planning.
  name: Network and Security Monitoring
- description: Process advertising impression, click, and conversion events at high volume with real-time aggregation.
  name: Ad Tech Analytics
- description: Monitor application performance metrics and operational data with drilldown and filtering capabilities.
  name: Operational Analytics
website: https://druid.apache.org/
---
