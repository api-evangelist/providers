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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Apache Hbase Agentic Access
  operation_count: 13
  slug: apache-hbase-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- description: Java client API for all HBase data operations including table administration, filters, coprocessors, batch operations, and async client for high-throughput workloads.
  name: Apache HBase Java Client API
  slug: apache-hbase-java-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Region information
  name: Apache HBase Regions API
  slug: apache-hbase-regions-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Row and cell operations
  name: Apache HBase Rows API
  slug: apache-hbase-rows-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Table scanning operations
  name: Apache HBase Scans API
  slug: apache-hbase-scans-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Table management operations
  name: Apache HBase Tables API
  slug: apache-hbase-tables-api
artifact_total: 62
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache HBase REST Regions API
  slug: open-apache-hbase-regions-api
- collection_type: open
  name: Apache HBase REST API
  slug: open-apache-hbase-rest
- collection_type: open
  name: Apache HBase REST Regions Rows API
  slug: open-apache-hbase-rows-api
- collection_type: open
  name: Apache HBase REST Regions Scans API
  slug: open-apache-hbase-scans-api
- collection_type: open
  name: Apache HBase REST Regions Tables API
  slug: open-apache-hbase-tables-api
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/hbase/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/hbase/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/hbase/blob/master/LICENSE
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


  Apache HBase''s developer surface includes documentation, getting-started guide, and 11 more developer resources.'
plans:
- name: Apache Hbase Plans Pricing
  plan_count: 3
  slug: apache-hbase-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Apache Hbase Rate Limits
  slug: apache-hbase-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache HBase API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-hbase-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Apache HBase API Rules
  rule_count: 14
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 9
  slug: apache-hbase-spectral-rules
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 53.7
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 75.0
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Open-Source
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
