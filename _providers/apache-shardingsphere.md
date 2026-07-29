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
- acting_count: 3
  human_in_the_loop: 0
  name: Apache Shardingsphere Agentic Access
  operation_count: 9
  slug: apache-shardingsphere-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 5
apis:
- description: The Cluster API from Apache ShardingSphere — 1 operation(s) for cluster.
  name: Apache ShardingSphere Cluster API
  slug: apache-shardingsphere-cluster-api
- description: The Databases API from Apache ShardingSphere — 2 operation(s) for databases.
  name: Apache ShardingSphere Databases API
  slug: apache-shardingsphere-databases-api
- description: The DataSources API from Apache ShardingSphere — 1 operation(s) for datasources.
  name: Apache ShardingSphere DataSources API
  slug: apache-shardingsphere-datasources-api
- description: The ReadwriteSplitting API from Apache ShardingSphere — 1 operation(s) for readwritesplitting.
  name: Apache ShardingSphere ReadwriteSplitting API
  slug: apache-shardingsphere-readwritesplitting-api
- description: The ShardingRules API from Apache ShardingSphere — 1 operation(s) for shardingrules.
  name: Apache ShardingSphere ShardingRules API
  slug: apache-shardingsphere-shardingrules-api
artifact_total: 72
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-shardingsphere-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-shardingsphere-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-shardingsphere-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/apache-shardingsphere
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/shardingsphere
- group: docs
  title: ''
  type: Documentation
  url: https://shardingsphere.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-shardingsphere-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-shardingsphere-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-shardingsphere-context.jsonld
created: '2026-03-16'
description: Apache ShardingSphere is an open-source ecosystem for distributed database systems providing data sharding, distributed transactions, and database governance. It supports MySQL, PostgreSQL, and other databases with transparent sharding capabilities.
examples:
- key_count: 2
  name: Apache Shardingsphere Cluster Status Example
  slug: apache-shardingsphere-cluster-status-example
- key_count: 6
  name: Apache Shardingsphere Data Source Example
  slug: apache-shardingsphere-data-source-example
- key_count: 1
  name: Apache Shardingsphere Data Source List Example
  slug: apache-shardingsphere-data-source-list-example
- key_count: 5
  name: Apache Shardingsphere Data Source Request Example
  slug: apache-shardingsphere-data-source-request-example
- key_count: 2
  name: Apache Shardingsphere Database Example
  slug: apache-shardingsphere-database-example
- key_count: 1
  name: Apache Shardingsphere Database List Example
  slug: apache-shardingsphere-database-list-example
- key_count: 1
  name: Apache Shardingsphere Database Request Example
  slug: apache-shardingsphere-database-request-example
- key_count: 4
  name: Apache Shardingsphere Instance Example
  slug: apache-shardingsphere-instance-example
- key_count: 4
  name: Apache Shardingsphere Readwrite Splitting Rule Example
  slug: apache-shardingsphere-readwrite-splitting-rule-example
- key_count: 1
  name: Apache Shardingsphere Readwrite Splitting Rule List Example
  slug: apache-shardingsphere-readwrite-splitting-rule-list-example
- key_count: 3
  name: Apache Shardingsphere Sharding Rule Example
  slug: apache-shardingsphere-sharding-rule-example
- key_count: 1
  name: Apache Shardingsphere Sharding Rule List Example
  slug: apache-shardingsphere-sharding-rule-list-example
- key_count: 3
  name: Apache Shardingsphere Sharding Strategy Example
  slug: apache-shardingsphere-sharding-strategy-example
- key_count: 4
  name: Apache Shardingsphere Sharding Table Example
  slug: apache-shardingsphere-sharding-table-example
features:
- description: Horizontal database sharding with flexible sharding algorithms
  name: Database Sharding
- description: Transparent primary/replica read-write splitting
  name: Read-Write Splitting
- description: XA and BASE distributed transaction support
  name: Distributed Transactions
- description: Transparent data encryption at the SQL layer
  name: Data Encryption
- description: Shadow database for production traffic testing
  name: Shadow Database
- description: SQL-based distributed database management language
  name: DistSQL
- description: Query across heterogeneous database instances
  name: Database Federation
finops:
- name: Apache Shardingsphere Finops
  service_category: API
  slug: apache-shardingsphere-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-shardingsphere.png
integrations:
- description: MySQL-compatible sharding and proxy
  name: MySQL
- description: PostgreSQL protocol support for sharding
  name: PostgreSQL
- description: Cluster coordination and configuration storage
  name: Apache ZooKeeper
- description: ShardingSphere Spring Boot starter for Java applications
  name: Spring Boot
- description: Kubernetes operator for cloud-native deployment
  name: Kubernetes
json_schemas:
- name: ClusterStatus
  property_count: 2
  slug: apache-shardingsphere-cluster-status
- name: DataSourceList
  property_count: 1
  slug: apache-shardingsphere-data-source-list
- name: DataSourceRequest
  property_count: 5
  slug: apache-shardingsphere-data-source-request
- name: DataSource
  property_count: 6
  slug: apache-shardingsphere-data-source
- name: DatabaseList
  property_count: 1
  slug: apache-shardingsphere-database-list
- name: DatabaseRequest
  property_count: 1
  slug: apache-shardingsphere-database-request
- name: Database
  property_count: 2
  slug: apache-shardingsphere-database
- name: Instance
  property_count: 4
  slug: apache-shardingsphere-instance
- name: ReadwriteSplittingRuleList
  property_count: 1
  slug: apache-shardingsphere-readwrite-splitting-rule-list
- name: ReadwriteSplittingRule
  property_count: 4
  slug: apache-shardingsphere-readwrite-splitting-rule
- name: ShardingRuleList
  property_count: 1
  slug: apache-shardingsphere-sharding-rule-list
- name: ShardingRule
  property_count: 3
  slug: apache-shardingsphere-sharding-rule
- name: ShardingStrategy
  property_count: 3
  slug: apache-shardingsphere-sharding-strategy
- name: ShardingTable
  property_count: 4
  slug: apache-shardingsphere-sharding-table
json_structures:
- name: Apache Shardingsphere Cluster Status Structure
  property_count: 2
  slug: apache-shardingsphere-cluster-status-structure
- name: Apache Shardingsphere Data Source List Structure
  property_count: 1
  slug: apache-shardingsphere-data-source-list-structure
- name: Apache Shardingsphere Data Source Request Structure
  property_count: 5
  slug: apache-shardingsphere-data-source-request-structure
- name: Apache Shardingsphere Data Source Structure
  property_count: 6
  slug: apache-shardingsphere-data-source-structure
- name: Apache Shardingsphere Database List Structure
  property_count: 1
  slug: apache-shardingsphere-database-list-structure
- name: Apache Shardingsphere Database Request Structure
  property_count: 1
  slug: apache-shardingsphere-database-request-structure
- name: Apache Shardingsphere Database Structure
  property_count: 2
  slug: apache-shardingsphere-database-structure
- name: Apache Shardingsphere Instance Structure
  property_count: 4
  slug: apache-shardingsphere-instance-structure
- name: Apache Shardingsphere Readwrite Splitting Rule List Structure
  property_count: 1
  slug: apache-shardingsphere-readwrite-splitting-rule-list-structure
- name: Apache Shardingsphere Readwrite Splitting Rule Structure
  property_count: 4
  slug: apache-shardingsphere-readwrite-splitting-rule-structure
- name: Apache Shardingsphere Sharding Rule List Structure
  property_count: 1
  slug: apache-shardingsphere-sharding-rule-list-structure
- name: Apache Shardingsphere Sharding Rule Structure
  property_count: 3
  slug: apache-shardingsphere-sharding-rule-structure
- name: Apache Shardingsphere Sharding Strategy Structure
  property_count: 3
  slug: apache-shardingsphere-sharding-strategy-structure
- name: Apache Shardingsphere Sharding Table Structure
  property_count: 4
  slug: apache-shardingsphere-sharding-table-structure
jsonld:
- class_count: 14
  name: Apache Shardingsphere Context
  property_count: 27
  slug: apache-shardingsphere-context
layout: provider
modified: '2026-04-19'
name: Apache ShardingSphere
nav: Providers
network: true
overview: 'Apache ShardingSphere publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Databases API, DataSources API, and 2 more. Tagged areas include Database, Distributed SQL, Read-Write Splitting, Sharding, and SQL.


  The Apache ShardingSphere catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache ShardingSphere''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Apache Shardingsphere Plans Pricing
  plan_count: 3
  slug: apache-shardingsphere-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Apache Shardingsphere Rate Limits
  slug: apache-shardingsphere-rate-limits
rules:
- name: Apache ShardingSphere API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-shardingsphere-jsonschema-spectral-rules
- name: Apache ShardingSphere API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 7
  slug: apache-shardingsphere-spectral-rules
score:
  band: developing
  composite: 43.1
  delta: -5.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.9
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-shardingsphere/refs/heads/main/screenshots/apache-shardingsphere-2026-06-20T172141.png
security:
- kind: domain-security
  name: Apache Shardingsphere Domain Security
  slug: apache-shardingsphere-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Shardingsphere Vulnerability Disclosure
  slug: apache-shardingsphere-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-shardingsphere
tags:
- Database
- Distributed SQL
- Read-Write Splitting
- Sharding
- SQL
- Apache
- Open Source
use_cases:
- description: Horizontally scale relational databases without changing application code
  name: Database Scale-Out
- description: Shard data by tenant ID for SaaS applications
  name: Multi-Tenant Sharding
- description: Scale read traffic with primary/replica splitting
  name: Read Scaling
- description: Online data migration between database clusters
  name: Data Migration
---
