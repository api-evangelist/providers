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
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: The Apache Calcite Java API provides SQL parsing, validation, query planning, and optimization capabilities for embedding in JVM applications. It exposes a relational algebra framework and pluggable o
  name: Apache Calcite Java API
  slug: apache-calcite-java-api
- description: 'The Apache Calcite JDBC adapter provides a standard JDBC interface over heterogeneous data sources. Applications use it to issue SQL queries across multiple data formats and storage systems through a '
  name: Apache Calcite JDBC API
  slug: apache-calcite-jdbc-api
- description: Apache Avatica is a framework for building database drivers derived from Apache Calcite. It provides a JSON/Protobuf-over-HTTP remote protocol for JDBC clients to connect to Calcite-based query engine
  name: Apache Calcite Avatica API
  slug: apache-calcite-avatica-api
artifact_total: 30
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/calcite/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/calcite/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-calcite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-calcite-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/calcite
- group: docs
  title: ''
  type: Documentation
  url: https://calcite.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://calcite.apache.org/docs/tutorial.html
- group: operate
  title: ''
  type: Support
  url: https://calcite.apache.org/community/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/apache/calcite/releases
- group: build
  title: Java SDK (Maven)
  type: SDKs
  url: https://search.maven.org/artifact/org.apache.calcite/calcite-core
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-calcite-vocabulary.yaml
created: '2026-03-16'
description: Apache Calcite is a dynamic data management framework developed by the Apache Software Foundation that provides SQL parsing, query planning and optimization, and data federation capabilities. It serves as the SQL engine and query optimizer for many big data systems including Apache Hive, Druid, Flink, Kafka Streams, and others. Calcite provides a Java API for embedding SQL capabilities into applications, a JDBC adapter for connecting heterogeneous data sources, and an extensible relational algebra framework for building custom query optimizers.
features:
- description: Parse and validate SQL queries using an extensible SQL grammar with support for SQL:2003 and beyond.
  name: SQL Parsing and Validation
- description: Cost-based and rule-based query optimization using a volcano-style optimizer with pluggable optimization rules.
  name: Query Optimization
- description: Extensible relational algebra framework for representing and transforming query plans as expression trees.
  name: Relational Algebra
- description: Federate queries across heterogeneous data sources including CSV, JSON, JDBC databases, and Elasticsearch.
  name: Data Federation
- description: Pluggable adapter API for connecting new data sources to the Calcite SQL engine.
  name: Adapter Framework
- description: Automatic materialized view recognition and query rewriting for query acceleration.
  name: Materialized Views
- description: SQL extensions for querying streaming data sources with window functions and temporal predicates.
  name: Streaming SQL
- description: Summary table recommendation and query rewriting using lattice structures for OLAP workloads.
  name: Lattices and Tiles
- description: Standard JDBC driver for issuing SQL queries against Calcite-connected data sources.
  name: JDBC Driver
- description: JSON/Protobuf-over-HTTP remote JDBC protocol for connecting clients to Calcite-based query servers.
  name: Avatica Remote Protocol
finops:
- name: Apache Calcite Finops
  service_category: API
  slug: apache-calcite-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-calcite.png
integrations:
- description: Flink uses Calcite for SQL parsing and query optimization in Flink SQL and Table API.
  name: Apache Flink
- description: Hive uses Calcite for cost-based query optimization in HiveQL query planning.
  name: Apache Hive
- description: Druid uses Calcite for SQL query parsing and planning against its time-series data store.
  name: Apache Druid
- description: ksqlDB and Kafka Streams use Calcite for SQL stream processing query planning.
  name: Apache Kafka
- description: Beam SQL uses Calcite for query planning on PCollection-based streaming and batch pipelines.
  name: Apache Beam
- description: Calcite provides a SQL adapter for querying Elasticsearch indices using standard SQL.
  name: Elasticsearch
- description: Kylin uses Calcite as its SQL engine for OLAP cube query planning and execution.
  name: Apache Kylin
layout: provider
modified: '2026-04-19'
name: Apache Calcite
nav: Providers
network: true
overview: 'Apache Calcite publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Apache, Data Federation, Framework, Open Source, and Query Optimization.


  Apache Calcite''s developer surface includes documentation, getting-started guide, support, changelog, and 10 more developer resources.'
plans:
- name: Apache Calcite Plans Pricing
  plan_count: 3
  slug: apache-calcite-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Apache Calcite Rate Limits
  slug: apache-calcite-rate-limits
score:
  band: emerging
  composite: 24.2
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 10.4
    operational_transparency: 39.5
  previous_composite: 24.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-calcite/refs/heads/main/screenshots/apache-calcite-2026-06-20T172045.png
security:
- kind: domain-security
  name: Apache Calcite Domain Security
  slug: apache-calcite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Calcite Vulnerability Disclosure
  slug: apache-calcite-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-calcite
tags:
- Apache
- Data Federation
- Framework
- Open Source
- Query Optimization
- SQL
use_cases:
- description: Add SQL querying capability to Java applications using the Calcite Java API without a full database.
  name: Embedding SQL in Applications
- description: Use Calcite as the SQL parsing and optimization layer in custom query engine implementations.
  name: Building Query Engines
- description: Federate queries across multiple heterogeneous data sources using Calcite adapters.
  name: Data Virtualization
- description: Accelerate analytical queries using materialized view rewriting and lattice-based summary tables.
  name: OLAP Query Optimization
- description: Parse SQL in one dialect and transpile it to another using Calcite's SQL generation framework.
  name: SQL Dialect Translation
---
