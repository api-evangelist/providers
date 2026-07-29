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
- acting_count: 2
  human_in_the_loop: 0
  name: Apache Hudi Agentic Access
  operation_count: 5
  slug: apache-hudi-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 3
apis:
- description: Java API for writing Hudi tables with upserts, inserts, and deletes, plus timeline management, compaction, and Spark/Flink DataSource integration APIs.
  name: Apache Hudi Java API
  slug: apache-hudi-java-api
- description: Hudi table management operations
  name: Apache Hudi Tables API
  slug: apache-hudi-tables-api
- description: Hudi timeline and commit operations
  name: Apache Hudi Timeline API
  slug: apache-hudi-timeline-api
artifact_total: 44
collections:
- collection_type: open
  name: Apache Hudi Timeline Server API
  slug: open-apache-hudi-timeline
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-hudi-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-hudi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-hudi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-hudi
- group: docs
  title: ''
  type: Documentation
  url: https://hudi.apache.org/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://hudi.apache.org/docs/quick-start-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/hudi
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-hudi-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-hudi-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://hudi.apache.org/blog/rss.xml
created: '2026-03-16'
description: Apache Hudi is a data lake platform that provides incremental data processing primitives including upserts and incremental queries. It manages storage of large analytical datasets on distributed file systems with ACID transactions, timeline-based versioning, and integrations for Spark, Flink, and Hive.
examples:
- key_count: 4
  name: Hudi Cleanconfig Example
  slug: hudi-cleanconfig-example
- key_count: 6
  name: Hudi Commitmetadata Example
  slug: hudi-commitmetadata-example
- key_count: 7
  name: Hudi Huditable Example
  slug: hudi-huditable-example
- key_count: 4
  name: Hudi Queryconfig Example
  slug: hudi-queryconfig-example
- key_count: 3
  name: Hudi Timelineinstant Example
  slug: hudi-timelineinstant-example
- key_count: 5
  name: Hudi Writeconfig Example
  slug: hudi-writeconfig-example
features:
- description: Atomically insert or update records in data lake tables with ACID guarantees using record keys.
  name: ACID Upserts
- description: Immutable commit timeline tracking all mutations for time travel, rollback, and incremental queries.
  name: Hudi Timeline
- description: Query only the data changed since a given commit timestamp for efficient streaming ingestion.
  name: Incremental Queries
- description: COW table type rewrites entire Parquet files on upsert for read-optimized query performance.
  name: Copy-On-Write Tables
- description: MOR table type appends delta logs for fast writes with compaction-based read optimization.
  name: Merge-On-Read Tables
- description: Built-in cleaning, compaction, clustering, and indexing services for table maintenance.
  name: Table Services
- description: Read and write Hudi tables from Apache Spark, Flink, Hive, Presto, Trino, and Athena.
  name: Multi-Engine Support
- description: Support for adding, renaming, and dropping columns with backward-compatible schema evolution.
  name: Schema Evolution
finops:
- name: Apache Hudi Finops
  service_category: API
  slug: apache-hudi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-hudi.png
json_schemas:
- name: CleanConfig
  property_count: 4
  slug: hudi-cleanconfig
- name: CommitMetadata
  property_count: 6
  slug: hudi-commitmetadata
- name: HudiTable
  property_count: 7
  slug: hudi-huditable
- name: QueryConfig
  property_count: 4
  slug: hudi-queryconfig
- name: TimelineInstant
  property_count: 3
  slug: hudi-timelineinstant
- name: WriteConfig
  property_count: 5
  slug: hudi-writeconfig
json_structures:
- name: Hudi Cleanconfig Structure
  property_count: 4
  slug: hudi-cleanconfig-structure
- name: Hudi Commitmetadata Structure
  property_count: 6
  slug: hudi-commitmetadata-structure
- name: Hudi Huditable Structure
  property_count: 7
  slug: hudi-huditable-structure
- name: Hudi Queryconfig Structure
  property_count: 4
  slug: hudi-queryconfig-structure
- name: Hudi Timelineinstant Structure
  property_count: 3
  slug: hudi-timelineinstant-structure
- name: Hudi Writeconfig Structure
  property_count: 5
  slug: hudi-writeconfig-structure
jsonld:
- class_count: 25
  name: Apache Hudi Timeline Context
  property_count: 0
  slug: apache-hudi-timeline-context
layout: provider
modified: '2026-05-19'
name: Apache Hudi
nav: Providers
network: true
overview: 'Apache Hudi publishes 2 APIs on the [APIs.io](https://apis.io/) network: Tables API and Timeline API. Tagged areas include ACID, Apache, Big Data, Data Lake, and Incremental Processing.


  The Apache Hudi catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Hudi''s developer surface includes documentation, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Apache Hudi Plans Pricing
  plan_count: 3
  slug: apache-hudi-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Apache Hudi Rate Limits
  slug: apache-hudi-rate-limits
rules:
- name: Apache Hudi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-hudi-jsonschema-spectral-rules
- name: Apache Hudi API Rules
  rule_count: 13
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 9
  slug: apache-hudi-spectral-rules
score:
  band: developing
  composite: 46.6
  delta: -6.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.3
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-hudi/refs/heads/main/screenshots/apache-hudi-2026-06-20T172109.png
security:
- kind: domain-security
  name: Apache Hudi Domain Security
  slug: apache-hudi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Hudi Vulnerability Disclosure
  slug: apache-hudi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-hudi
tags:
- ACID
- Apache
- Big Data
- Data Lake
- Incremental Processing
- Lakehouse
- Open Source
use_cases:
- description: Ingest change data capture (CDC) events from databases into data lake tables with upsert support.
  name: CDC Pipeline Ingestion
- description: Build near-real-time data lake pipelines with Spark Structured Streaming or Flink.
  name: Streaming Data Lake
- description: Manage storage costs with automated cleaning, compaction, and clustering of Hudi tables.
  name: Data Lake Maintenance
- description: Build incremental ETL pipelines that process only changed data since the last run.
  name: Incremental ETL
- description: Implement GDPR right-to-erasure by deleting records from Hudi tables with delete operations.
  name: Regulatory Data Retention
---
