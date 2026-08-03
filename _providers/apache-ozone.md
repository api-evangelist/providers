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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Apache Ozone Agentic Access
  operation_count: 9
  slug: apache-ozone-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 2
apis:
- description: The Buckets API from Apache Ozone — 2 operation(s) for buckets.
  name: Apache Ozone Buckets API
  slug: apache-ozone-buckets-api
- description: The Objects API from Apache Ozone — 1 operation(s) for objects.
  name: Apache Ozone Objects API
  slug: apache-ozone-objects-api
artifact_total: 41
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-ozone-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-ozone-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-ozone-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/ozone
- group: docs
  title: ''
  type: Documentation
  url: https://ozone.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-ozone-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-ozone-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-ozone-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://ozone.apache.org/blog/rss.xml
created: '2026-03-16'
description: Apache Ozone is a scalable, redundant, and distributed object store optimized for big data workloads. It provides an S3-compatible interface and a Hadoop-compatible file system interface for seamless integration with existing big data tools.
examples:
- key_count: 3
  name: Apache Ozone Bucket Example
  slug: apache-ozone-bucket-example
- key_count: 2
  name: Apache Ozone List All My Buckets Result Example
  slug: apache-ozone-list-all-my-buckets-result-example
- key_count: 6
  name: Apache Ozone List Objects Result Example
  slug: apache-ozone-list-objects-result-example
- key_count: 6
  name: Apache Ozone Object Example
  slug: apache-ozone-object-example
- key_count: 2
  name: Apache Ozone Owner Example
  slug: apache-ozone-owner-example
features:
- description: Fully compatible with Amazon S3 API for object storage operations
  name: S3-Compatible API
- description: Hadoop-compatible file system interface (o3fs, ofs) for existing Hadoop workloads
  name: HDFS-Compatible
- description: Volume/bucket hierarchy with multi-tenant access controls
  name: Multi-Tenant
- description: Configurable replication for data durability
  name: Replication
- description: Erasure coding support for storage efficiency
  name: Erasure Coding
- description: Scale to billions of files with petabytes of data
  name: Scalability
finops:
- name: Apache Ozone Finops
  service_category: API
  slug: apache-ozone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-ozone.png
integrations:
- description: Native HDFS-compatible file system integration
  name: Apache Hadoop
- description: Direct Spark data source for reading and writing ORC/Parquet
  name: Apache Spark
- description: Hive metastore integration for data lake querying
  name: Apache Hive
- description: Compatible with AWS SDK for S3 operations
  name: Amazon S3 SDK
- description: Container-native deployment with CSI driver support
  name: Kubernetes
json_schemas:
- name: Bucket
  property_count: 3
  slug: apache-ozone-bucket
- name: ListAllMyBucketsResult
  property_count: 2
  slug: apache-ozone-list-all-my-buckets-result
- name: ListObjectsResult
  property_count: 6
  slug: apache-ozone-list-objects-result
- name: Object
  property_count: 6
  slug: apache-ozone-object
- name: Owner
  property_count: 2
  slug: apache-ozone-owner
json_structures:
- name: Apache Ozone Bucket Structure
  property_count: 3
  slug: apache-ozone-bucket-structure
- name: Apache Ozone List All My Buckets Result Structure
  property_count: 2
  slug: apache-ozone-list-all-my-buckets-result-structure
- name: Apache Ozone List Objects Result Structure
  property_count: 6
  slug: apache-ozone-list-objects-result-structure
- name: Apache Ozone Object Structure
  property_count: 6
  slug: apache-ozone-object-structure
- name: Apache Ozone Owner Structure
  property_count: 2
  slug: apache-ozone-owner-structure
jsonld:
- class_count: 5
  name: Apache Ozone Context
  property_count: 16
  slug: apache-ozone-context
layout: provider
modified: '2026-05-19'
name: Apache Ozone
nav: Providers
network: true
overview: 'Apache Ozone publishes 2 APIs on the [APIs.io](https://apis.io/) network: Buckets API and Objects API. Tagged areas include Distributed Storage, Hadoop, Object Storage, S3-Compatible, and Apache.


  The Apache Ozone catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Ozone''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Apache Ozone Plans Pricing
  plan_count: 3
  slug: apache-ozone-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Apache Ozone Rate Limits
  slug: apache-ozone-rate-limits
rules:
- name: Apache Ozone API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-ozone-jsonschema-spectral-rules
- name: Apache Ozone API Rules
  rule_count: 13
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 5
  slug: apache-ozone-spectral-rules
score:
  band: thin
  composite: 34.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 21.7
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-ozone/refs/heads/main/screenshots/apache-ozone-2026-06-20T172131.png
security:
- kind: domain-security
  name: Apache Ozone Domain Security
  slug: apache-ozone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Ozone Vulnerability Disclosure
  slug: apache-ozone-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-ozone
tags:
- Distributed Storage
- Hadoop
- Object Storage
- S3-Compatible
- Apache
- Open Source
use_cases:
- description: Store raw data in a highly scalable and S3-compatible data lake
  name: Data Lake Storage
- description: Replace HDFS with Ozone for petabyte-scale Hadoop clusters
  name: Hadoop Migration
- description: Use S3-compatible API for application file and media storage
  name: Application Object Storage
- description: Cost-effective backup and long-term data archival
  name: Backup and Archive
---
