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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Apache Orc Agentic Access
  operation_count: 6
  slug: apache-orc-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 3
apis:
- description: The Conversion API from Apache ORC — 1 operation(s) for conversion.
  name: Apache ORC Conversion API
  slug: apache-orc-conversion-api
- description: The Files API from Apache ORC — 4 operation(s) for files.
  name: Apache ORC Files API
  slug: apache-orc-files-api
- description: The Operations API from Apache ORC — 1 operation(s) for operations.
  name: Apache ORC Operations API
  slug: apache-orc-operations-api
artifact_total: 63
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-orc-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-orc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-orc-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/orc
- group: docs
  title: ''
  type: Documentation
  url: https://orc.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-orc-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-orc-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-orc-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://orc.apache.org/news/
created: '2026-03-16'
description: Apache ORC is a self-describing, type-aware columnar file format designed for Hadoop workloads. It provides high compression ratios and fast read performance for large-scale data processing with support for complex data types.
examples:
- key_count: 7
  name: Apache Orc Column Statistics Example
  slug: apache-orc-column-statistics-example
- key_count: 2
  name: Apache Orc Column Statistics Response Example
  slug: apache-orc-column-statistics-response-example
- key_count: 4
  name: Apache Orc Column Type Example
  slug: apache-orc-column-type-example
- key_count: 5
  name: Apache Orc Conversion Request Example
  slug: apache-orc-conversion-request-example
- key_count: 4
  name: Apache Orc Conversion Result Example
  slug: apache-orc-conversion-result-example
- key_count: 4
  name: Apache Orc File Info Example
  slug: apache-orc-file-info-example
- key_count: 1
  name: Apache Orc File List Example
  slug: apache-orc-file-list-example
- key_count: 9
  name: Apache Orc File Metadata Example
  slug: apache-orc-file-metadata-example
- key_count: 2
  name: Apache Orc Merge Request Example
  slug: apache-orc-merge-request-example
- key_count: 3
  name: Apache Orc Operation Result Example
  slug: apache-orc-operation-result-example
- key_count: 2
  name: Apache Orc Orc Schema Example
  slug: apache-orc-orc-schema-example
- key_count: 4
  name: Apache Orc Stripe Info Example
  slug: apache-orc-stripe-info-example
features:
- description: Stores data by column for efficient compression and query performance
  name: Columnar Storage
- description: Skip reading data that does not match query predicates
  name: Predicate Pushdown
- description: Read only the columns needed for a query
  name: Column Projection
- description: Full ACID transactional support when used with Apache Hive
  name: ACID Support
- description: Add, rename, and remove columns while preserving backward compatibility
  name: Schema Evolution
- description: Supports ZLIB, Snappy, LZO, LZ4, and ZSTD compression codecs
  name: Compression
finops:
- name: Apache Orc Finops
  service_category: API
  slug: apache-orc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-orc.png
integrations:
- description: Native ORC support as default Hive storage format
  name: Apache Hive
- description: ORC data source support in Spark SQL
  name: Apache Spark
- description: Fast ORC reading with native vectorized reader
  name: Presto/Trino
- description: ORC file format support for batch and streaming
  name: Apache Flink
- description: ORC to Arrow conversion for in-memory analytics
  name: Apache Arrow
json_schemas:
- name: ColumnStatisticsResponse
  property_count: 2
  slug: apache-orc-column-statistics-response
- name: ColumnStatistics
  property_count: 7
  slug: apache-orc-column-statistics
- name: ColumnType
  property_count: 4
  slug: apache-orc-column-type
- name: ConversionRequest
  property_count: 5
  slug: apache-orc-conversion-request
- name: ConversionResult
  property_count: 4
  slug: apache-orc-conversion-result
- name: FileInfo
  property_count: 4
  slug: apache-orc-file-info
- name: FileList
  property_count: 1
  slug: apache-orc-file-list
- name: FileMetadata
  property_count: 9
  slug: apache-orc-file-metadata
- name: MergeRequest
  property_count: 2
  slug: apache-orc-merge-request
- name: OperationResult
  property_count: 3
  slug: apache-orc-operation-result
- name: OrcSchema
  property_count: 2
  slug: apache-orc-orc-schema
- name: StripeInfo
  property_count: 4
  slug: apache-orc-stripe-info
json_structures:
- name: Apache Orc Column Statistics Response Structure
  property_count: 2
  slug: apache-orc-column-statistics-response-structure
- name: Apache Orc Column Statistics Structure
  property_count: 7
  slug: apache-orc-column-statistics-structure
- name: Apache Orc Column Type Structure
  property_count: 4
  slug: apache-orc-column-type-structure
- name: Apache Orc Conversion Request Structure
  property_count: 5
  slug: apache-orc-conversion-request-structure
- name: Apache Orc Conversion Result Structure
  property_count: 4
  slug: apache-orc-conversion-result-structure
- name: Apache Orc File Info Structure
  property_count: 4
  slug: apache-orc-file-info-structure
- name: Apache Orc File List Structure
  property_count: 1
  slug: apache-orc-file-list-structure
- name: Apache Orc File Metadata Structure
  property_count: 9
  slug: apache-orc-file-metadata-structure
- name: Apache Orc Merge Request Structure
  property_count: 2
  slug: apache-orc-merge-request-structure
- name: Apache Orc Operation Result Structure
  property_count: 3
  slug: apache-orc-operation-result-structure
- name: Apache Orc Orc Schema Structure
  property_count: 2
  slug: apache-orc-orc-schema-structure
- name: Apache Orc Stripe Info Structure
  property_count: 4
  slug: apache-orc-stripe-info-structure
jsonld:
- class_count: 12
  name: Apache Orc Context
  property_count: 37
  slug: apache-orc-context
layout: provider
modified: '2026-05-19'
name: Apache ORC
nav: Providers
network: true
overview: 'Apache ORC publishes 3 APIs on the [APIs.io](https://apis.io/) network: Conversion API, Files API, and Operations API. Tagged areas include Big Data, Columnar Storage, Compression, File Format, and Hadoop.


  The Apache ORC catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache ORC''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Apache Orc Plans Pricing
  plan_count: 3
  slug: apache-orc-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 5
  name: Apache Orc Rate Limits
  slug: apache-orc-rate-limits
rules:
- name: Apache ORC API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-orc-jsonschema-spectral-rules
- name: Apache ORC API Rules
  rule_count: 14
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 7
  slug: apache-orc-spectral-rules
score:
  band: emerging
  composite: 26.9
  delta: -8.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 20.6
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-orc/refs/heads/main/screenshots/apache-orc-2026-06-20T172130.png
security:
- kind: domain-security
  name: Apache Orc Domain Security
  slug: apache-orc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Orc Vulnerability Disclosure
  slug: apache-orc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-orc
tags:
- Big Data
- Columnar Storage
- Compression
- File Format
- Hadoop
- Apache
- Open Source
use_cases:
- description: Store Hive tables in highly efficient ORC format
  name: Hive Data Warehousing
- description: Process large ORC datasets with Apache Spark SQL
  name: Spark Analytics
- description: Fast analytical queries over ORC files with Presto or Trino
  name: Presto/Trino Queries
- description: Efficient columnar storage for data lake architectures
  name: Data Lake Storage
---
