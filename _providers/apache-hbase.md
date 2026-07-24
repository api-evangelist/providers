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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Apache Hbase Agentic Access
  operation_count: 13
  slug: apache-hbase-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 5
apis:
- description: Java client API for all HBase data operations including table administration, filters, coprocessors, batch operations, and async client for high-throughput workloads.
  name: Apache HBase Java Client API
  slug: apache-hbase-java-api
- description: Region information
  name: Apache HBase Regions API
  slug: apache-hbase-regions-api
- description: Row and cell operations
  name: Apache HBase Rows API
  slug: apache-hbase-rows-api
- description: Table scanning operations
  name: Apache HBase Scans API
  slug: apache-hbase-scans-api
- description: Table management operations
  name: Apache HBase Tables API
  slug: apache-hbase-tables-api
artifact_total: 57
collections:
- collection_type: open
  name: Apache HBase REST API
  slug: open-apache-hbase-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-hbase-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-hbase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-hbase-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://hbase.apache.org/book.html
- group: start
  title: ''
  type: GettingStarted
  url: https://hbase.apache.org/book.html#quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/hbase
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-hbase-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-hbase-vocabulary.yaml
created: '2026-03-16'
description: Apache HBase is an open-source, distributed, versioned, non-relational database modeled after Google's Bigtable. It provides random, real-time read/write access to big data and runs on top of Apache Hadoop HDFS, offering a REST API (Stargate), Thrift API, and Java client API for table and cell-level operations.
examples:
- key_count: 3
  name: Hbase Rest Cell Example
  slug: hbase-rest-cell-example
- key_count: 1
  name: Hbase Rest Cellset Example
  slug: hbase-rest-cellset-example
- key_count: 5
  name: Hbase Rest Clusterversion Example
  slug: hbase-rest-clusterversion-example
- key_count: 5
  name: Hbase Rest Columnfamily Example
  slug: hbase-rest-columnfamily-example
- key_count: 4
  name: Hbase Rest Scanner Example
  slug: hbase-rest-scanner-example
- key_count: 1
  name: Hbase Rest Tablelist Example
  slug: hbase-rest-tablelist-example
- key_count: 2
  name: Hbase Rest Tableregions Example
  slug: hbase-rest-tableregions-example
- key_count: 2
  name: Hbase Rest Tableschema Example
  slug: hbase-rest-tableschema-example
features:
- description: Store sparse, semi-structured data in a distributed wide-column table model inspired by Google Bigtable.
  name: Wide-Column NoSQL Storage
- description: HTTP REST gateway for language-agnostic table and row operations using JSON or XML.
  name: REST API (Stargate)
- description: High-performance Thrift interface for cross-language HBase access with compact binary encoding.
  name: Thrift API
- description: Strong consistency guarantees for single-row get, put, and delete operations.
  name: Row-Level Consistency
- description: Server-side coprocessor framework for custom observers and endpoints analogous to stored procedures.
  name: Coprocessors
- description: JRuby-based interactive shell for administrative and data manipulation operations.
  name: HBase Shell
- description: Flexible server-side scan API with filters, time ranges, and column family projections.
  name: Scanner API
- description: Asynchronous multi-cluster replication for disaster recovery and geographic distribution.
  name: Replication
finops:
- name: Apache Hbase Finops
  service_category: API
  slug: apache-hbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-hbase.png
integrations:
- description: HBase uses HDFS as its underlying distributed file system for WAL and HFile storage.
  name: Apache Hadoop HDFS
- description: SQL skin over HBase providing JDBC access, secondary indexes, and query optimization.
  name: Apache Phoenix
- description: Spark-HBase connector for reading and writing HBase tables as Spark DataFrames.
  name: Apache Spark
- description: HBase storage handler for using HBase tables as external Hive tables.
  name: Apache Hive
- description: Flink HBase connector for reading and writing HBase tables in streaming pipelines.
  name: Apache Flink
json_schemas:
- name: Cell
  property_count: 3
  slug: hbase-rest-cell
- name: CellSet
  property_count: 1
  slug: hbase-rest-cellset
- name: ClusterVersion
  property_count: 5
  slug: hbase-rest-clusterversion
- name: ColumnFamily
  property_count: 5
  slug: hbase-rest-columnfamily
- name: Scanner
  property_count: 4
  slug: hbase-rest-scanner
- name: TableList
  property_count: 1
  slug: hbase-rest-tablelist
- name: TableRegions
  property_count: 2
  slug: hbase-rest-tableregions
- name: TableSchema
  property_count: 2
  slug: hbase-rest-tableschema
json_structures:
- name: Hbase Rest Cell Structure
  property_count: 3
  slug: hbase-rest-cell-structure
- name: Hbase Rest Cellset Structure
  property_count: 1
  slug: hbase-rest-cellset-structure
- name: Hbase Rest Clusterversion Structure
  property_count: 5
  slug: hbase-rest-clusterversion-structure
- name: Hbase Rest Columnfamily Structure
  property_count: 5
  slug: hbase-rest-columnfamily-structure
- name: Hbase Rest Scanner Structure
  property_count: 4
  slug: hbase-rest-scanner-structure
- name: Hbase Rest Tablelist Structure
  property_count: 1
  slug: hbase-rest-tablelist-structure
- name: Hbase Rest Tableregions Structure
  property_count: 2
  slug: hbase-rest-tableregions-structure
- name: Hbase Rest Tableschema Structure
  property_count: 2
  slug: hbase-rest-tableschema-structure
jsonld:
- class_count: 26
  name: Apache Hbase Rest Context
  property_count: 0
  slug: apache-hbase-rest-context
layout: provider
modified: '2026-05-19'
name: Apache HBase
nav: Providers
network: true
overview: 'Apache HBase publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Regions API, Rows API, Scans API, and 1 more. Tagged areas include Apache, Big Data, Bigtable, Database, and Hadoop.


  The Apache HBase catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache HBase''s developer surface includes documentation, getting-started guide, and 7 more developer resources.'
plans:
- name: Apache Hbase Plans Pricing
  plan_count: 3
  slug: apache-hbase-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 5
  name: Apache Hbase Rate Limits
  slug: apache-hbase-rate-limits
rules:
- name: Apache HBase API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-hbase-jsonschema-spectral-rules
- name: Apache HBase API Rules
  rule_count: 14
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 9
  slug: apache-hbase-spectral-rules
score:
  band: developing
  composite: 48.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 48.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-hbase/refs/heads/main/screenshots/apache-hbase-2026-06-20T172109.png
security:
- kind: domain-security
  name: Apache Hbase Domain Security
  slug: apache-hbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Hbase Vulnerability Disclosure
  slug: apache-hbase-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-hbase
tags:
- Apache
- Big Data
- Bigtable
- Database
- Hadoop
- NoSQL
- Open Source
- Wide Column
use_cases:
- description: Store high-velocity time-series sensor or log data with row keys designed for time range scans.
  name: Time-Series Data Storage
- description: Persist event streams from web applications or IoT devices for analytics and audit.
  name: Event Logging
- description: Store sparse user profile attributes at scale with efficient random access by user ID.
  name: User Profile Storage
- description: Use HBase as a backend storage engine for graph databases like Apache TinkerPop/JanusGraph.
  name: Graph Storage Backend
- description: Store and serve pre-computed ML features at low latency for online prediction.
  name: Machine Learning Feature Store
---
