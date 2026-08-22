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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Apache Seatunnel Agentic Access
  operation_count: 6
  slug: apache-seatunnel-agentic-access
  summary_line: 6 operations · 2 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The Jobs API from Apache SeaTunnel — 4 operation(s) for jobs.
  name: Apache SeaTunnel Jobs API
  slug: apache-seatunnel-jobs-api
- description: The Monitoring API from Apache SeaTunnel — 2 operation(s) for monitoring.
  name: Apache SeaTunnel Monitoring API
  slug: apache-seatunnel-monitoring-api
artifact_total: 59
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache SeaTunnel REST Jobs API
  slug: open-apache-seatunnel-jobs-api
- collection_type: open
  name: Apache SeaTunnel REST Jobs Monitoring API
  slug: open-apache-seatunnel-monitoring-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-seatunnel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-seatunnel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-seatunnel-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/seatunnel
- group: docs
  title: ''
  type: Documentation
  url: https://seatunnel.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-seatunnel-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-seatunnel-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-seatunnel-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://seatunnel.apache.org/blog/rss.xml
created: '2026-03-16'
description: Apache SeaTunnel is a high-performance, distributed data integration platform that supports real-time and batch data synchronization. It provides a connector API with support for over 100 data sources and sinks.
examples:
- key_count: 7
  name: Apache Seatunnel Cluster Overview Example
  slug: apache-seatunnel-cluster-overview-example
- key_count: 8
  name: Apache Seatunnel Job Detail Example
  slug: apache-seatunnel-job-detail-example
- key_count: 5
  name: Apache Seatunnel Job Info Example
  slug: apache-seatunnel-job-info-example
- key_count: 2
  name: Apache Seatunnel Job List Example
  slug: apache-seatunnel-job-list-example
- key_count: 4
  name: Apache Seatunnel Job Metrics Example
  slug: apache-seatunnel-job-metrics-example
- key_count: 2
  name: Apache Seatunnel Job Stop Request Example
  slug: apache-seatunnel-job-stop-request-example
- key_count: 3
  name: Apache Seatunnel Job Stop Result Example
  slug: apache-seatunnel-job-stop-result-example
- key_count: 3
  name: Apache Seatunnel Job Submit Request Example
  slug: apache-seatunnel-job-submit-request-example
- key_count: 2
  name: Apache Seatunnel Job Submit Result Example
  slug: apache-seatunnel-job-submit-result-example
- key_count: 6
  name: Apache Seatunnel System Info Example
  slug: apache-seatunnel-system-info-example
features:
- description: Over 200 built-in connectors for databases, warehouses, and file systems
  name: 200+ Connectors
- description: Unified API for both batch ETL and real-time streaming jobs
  name: Batch and Streaming
- description: Automatic schema detection and evolution support
  name: Schema Evolution
- description: Zeta execution engine with no external dependencies
  name: Distributed Execution
- description: Change Data Capture for real-time database synchronization
  name: CDC Support
- description: Built-in SQL and custom transform functions
  name: Transform Layer
finops:
- name: Apache Seatunnel Finops
  service_category: API
  slug: apache-seatunnel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-seatunnel.png
integrations:
- description: Kafka source and sink connector for streaming pipelines
  name: Apache Kafka
- description: Run SeaTunnel jobs on Flink execution engine
  name: Apache Flink
- description: Run SeaTunnel jobs on Spark execution engine
  name: Apache Spark
- description: High-performance ClickHouse sink connector
  name: ClickHouse
- description: Apache Doris connector for analytical workloads
  name: Doris
json_schemas:
- name: ClusterOverview
  property_count: 7
  slug: apache-seatunnel-cluster-overview
- name: JobDetail
  property_count: 8
  slug: apache-seatunnel-job-detail
- name: JobInfo
  property_count: 5
  slug: apache-seatunnel-job-info
- name: JobList
  property_count: 2
  slug: apache-seatunnel-job-list
- name: JobMetrics
  property_count: 4
  slug: apache-seatunnel-job-metrics
- name: JobStopRequest
  property_count: 2
  slug: apache-seatunnel-job-stop-request
- name: JobStopResult
  property_count: 3
  slug: apache-seatunnel-job-stop-result
- name: JobSubmitRequest
  property_count: 3
  slug: apache-seatunnel-job-submit-request
- name: JobSubmitResult
  property_count: 2
  slug: apache-seatunnel-job-submit-result
- name: SystemInfo
  property_count: 6
  slug: apache-seatunnel-system-info
json_structures:
- name: Apache Seatunnel Cluster Overview Structure
  property_count: 7
  slug: apache-seatunnel-cluster-overview-structure
- name: Apache Seatunnel Job Detail Structure
  property_count: 8
  slug: apache-seatunnel-job-detail-structure
- name: Apache Seatunnel Job Info Structure
  property_count: 5
  slug: apache-seatunnel-job-info-structure
- name: Apache Seatunnel Job List Structure
  property_count: 2
  slug: apache-seatunnel-job-list-structure
- name: Apache Seatunnel Job Metrics Structure
  property_count: 4
  slug: apache-seatunnel-job-metrics-structure
- name: Apache Seatunnel Job Stop Request Structure
  property_count: 2
  slug: apache-seatunnel-job-stop-request-structure
- name: Apache Seatunnel Job Stop Result Structure
  property_count: 3
  slug: apache-seatunnel-job-stop-result-structure
- name: Apache Seatunnel Job Submit Request Structure
  property_count: 3
  slug: apache-seatunnel-job-submit-request-structure
- name: Apache Seatunnel Job Submit Result Structure
  property_count: 2
  slug: apache-seatunnel-job-submit-result-structure
- name: Apache Seatunnel System Info Structure
  property_count: 6
  slug: apache-seatunnel-system-info-structure
jsonld:
- class_count: 10
  name: Apache Seatunnel Context
  property_count: 32
  slug: apache-seatunnel-context
layout: provider
modified: '2026-05-19'
name: Apache SeaTunnel
nav: Providers
network: true
overview: 'Apache SeaTunnel publishes 2 APIs on the [APIs.io](https://apis.io/) network: Jobs API and Monitoring API. Tagged areas include Data Integration, ETL, ELT, Batch, and Streaming.


  The Apache SeaTunnel catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache SeaTunnel''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Apache Seatunnel Plans Pricing
  plan_count: 3
  slug: apache-seatunnel-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Apache Seatunnel Rate Limits
  slug: apache-seatunnel-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache SeaTunnel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-seatunnel-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Apache SeaTunnel API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 6
  slug: apache-seatunnel-spectral-rules
score:
  band: thin
  composite: 29.6
  delta: -6.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 54.9
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-seatunnel/refs/heads/main/screenshots/apache-seatunnel-2026-06-20T172141.png
security:
- kind: domain-security
  name: Apache Seatunnel Domain Security
  slug: apache-seatunnel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Seatunnel Vulnerability Disclosure
  slug: apache-seatunnel-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-seatunnel
tags:
- Data Integration
- ETL
- ELT
- Batch
- Streaming
- Apache
- Open Source
use_cases:
- description: Migrate data between databases with schema mapping
  name: Database Migration
- description: Load and sync data into data warehouses
  name: Data Warehouse Loading
- description: CDC-based real-time sync between source and target systems
  name: Real-Time Synchronization
- description: Ingest data from multiple sources into a data lake
  name: Data Lake Ingestion
---
