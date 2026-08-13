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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apache Hive Agentic Access
  operation_count: 7
  slug: apache-hive-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 4
apis:
- description: JDBC interface to HiveServer2 for standard SQL client connectivity, supporting parameterized queries, result sets, and connection pooling from Java and ODBC-bridge applications.
  name: Apache Hive JDBC API
  slug: apache-hive-jdbc
- description: Database metadata operations
  name: Apache Hive Databases API
  slug: apache-hive-databases-api
- description: Hive job submission and monitoring
  name: Apache Hive Jobs API
  slug: apache-hive-jobs-api
- description: Table metadata operations
  name: Apache Hive Tables API
  slug: apache-hive-tables-api
artifact_total: 45
collections:
- collection_type: open
  name: Apache Hive WebHCat REST API
  slug: open-apache-hive-webhcat
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/hive/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/hive/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-hive-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-hive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-hive-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-hive
- group: docs
  title: ''
  type: Documentation
  url: https://cwiki.apache.org/confluence/display/Hive/Home
- group: start
  title: ''
  type: GettingStarted
  url: https://cwiki.apache.org/confluence/display/Hive/GettingStarted
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/hive
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-hive-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-hive-vocabulary.yaml
created: '2026-03-16'
description: Apache Hive is a data warehouse software that facilitates reading, writing, and managing large datasets residing in distributed storage using SQL. It provides a SQL-like interface called HiveQL for querying data stored in Hadoop, along with a WebHCat REST API for job submission and metastore access.
examples:
- key_count: 3
  name: Hive Webhcat Column Example
  slug: hive-webhcat-column-example
- key_count: 5
  name: Hive Webhcat Database Example
  slug: hive-webhcat-database-example
- key_count: 6
  name: Hive Webhcat Job Example
  slug: hive-webhcat-job-example
- key_count: 5
  name: Hive Webhcat Partition Example
  slug: hive-webhcat-partition-example
- key_count: 4
  name: Hive Webhcat Queryresult Example
  slug: hive-webhcat-queryresult-example
- key_count: 8
  name: Hive Webhcat Table Example
  slug: hive-webhcat-table-example
features:
- description: SQL-like query language for reading, writing, and aggregating data stored in distributed storage.
  name: HiveQL SQL Interface
- description: HTTP REST API (Templeton) for DDL operations, job submission, and metastore metadata access.
  name: WebHCat REST API
- description: Thrift-based server with JDBC and ODBC drivers for standard SQL client connectivity.
  name: HiveServer2 JDBC/ODBC
- description: Central repository for table schema, partition metadata, and storage location information.
  name: Hive Metastore
- description: Partition tables by column values for efficient query pruning and data organization.
  name: Partitioning
- description: Optimized columnar storage formats with predicate pushdown and compression support.
  name: ORC and Parquet Storage
- description: Full ACID transaction support for inserts, updates, and deletes on managed ORC tables.
  name: ACID Transactions
- description: Batch processing of rows in CPU register-width vectors for improved query throughput.
  name: Vectorized Query Execution
finops:
- name: Apache Hive Finops
  service_category: API
  slug: apache-hive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-hive.png
json_schemas:
- name: Column
  property_count: 3
  slug: hive-webhcat-column
- name: Database
  property_count: 5
  slug: hive-webhcat-database
- name: Job
  property_count: 6
  slug: hive-webhcat-job
- name: Partition
  property_count: 5
  slug: hive-webhcat-partition
- name: QueryResult
  property_count: 4
  slug: hive-webhcat-queryresult
- name: Table
  property_count: 8
  slug: hive-webhcat-table
json_structures:
- name: Hive Webhcat Column Structure
  property_count: 3
  slug: hive-webhcat-column-structure
- name: Hive Webhcat Database Structure
  property_count: 5
  slug: hive-webhcat-database-structure
- name: Hive Webhcat Job Structure
  property_count: 6
  slug: hive-webhcat-job-structure
- name: Hive Webhcat Partition Structure
  property_count: 5
  slug: hive-webhcat-partition-structure
- name: Hive Webhcat Queryresult Structure
  property_count: 4
  slug: hive-webhcat-queryresult-structure
- name: Hive Webhcat Table Structure
  property_count: 8
  slug: hive-webhcat-table-structure
jsonld:
- class_count: 21
  name: Apache Hive Webhcat Context
  property_count: 0
  slug: apache-hive-webhcat-context
layout: provider
modified: '2026-05-19'
name: Apache Hive
nav: Providers
network: true
overview: 'Apache Hive publishes 3 APIs on the [APIs.io](https://apis.io/) network: Databases API, Jobs API, and Tables API. Tagged areas include Apache, Big Data, Data Warehouse, ETL, and Hadoop.


  The Apache Hive catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Hive''s developer surface includes documentation, getting-started guide, and 11 more developer resources.'
plans:
- name: Apache Hive Plans Pricing
  plan_count: 3
  slug: apache-hive-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Apache Hive Rate Limits
  slug: apache-hive-rate-limits
rules:
- name: Apache Hive API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-hive-jsonschema-spectral-rules
- name: Apache Hive API Rules
  rule_count: 13
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 9
  slug: apache-hive-spectral-rules
score:
  band: thin
  composite: 39.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 59.5
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 23.7
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-hive/refs/heads/main/screenshots/apache-hive-2026-06-20T172106.png
security:
- kind: domain-security
  name: Apache Hive Domain Security
  slug: apache-hive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Hive Vulnerability Disclosure
  slug: apache-hive-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-hive
tags:
- Apache
- Big Data
- Data Warehouse
- ETL
- Hadoop
- Open Source
- SQL
use_cases:
- description: Run SQL analytics on petabyte-scale datasets stored in HDFS or object storage.
  name: Data Warehouse Analytics
- description: Use HiveQL scripts to transform and load data between raw and curated data lake zones.
  name: ETL Pipeline Orchestration
- description: Query structured data interactively using Beeline or JDBC-connected BI tools.
  name: Ad-Hoc Data Exploration
- description: Parse and aggregate application logs stored as text or JSON in HDFS using Hive SerDes.
  name: Log Analysis
- description: Use the Hive Metastore as a shared schema registry for Spark, Flink, and Presto.
  name: Data Catalog Integration
---
