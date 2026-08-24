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
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Apache Pig Agentic Access
  operation_count: 6
  slug: apache-pig-agentic-access
  summary_line: 6 operations · 3 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The Jobs API from Apache Pig — 3 operation(s) for jobs.
  name: Apache Pig Jobs API
  slug: apache-pig-jobs-api
- description: The Scripts API from Apache Pig — 1 operation(s) for scripts.
  name: Apache Pig Scripts API
  slug: apache-pig-scripts-api
artifact_total: 50
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Pig Jobs API
  slug: open-apache-pig-jobs-api
- collection_type: open
  name: Apache Pig Jobs Scripts API
  slug: open-apache-pig-scripts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-pig-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-pig-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-pig-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/pig
- group: docs
  title: ''
  type: Documentation
  url: https://pig.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-pig-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-pig-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-pig-context.jsonld
created: '2026-03-16'
description: Apache Pig is a platform for analyzing large data sets that provides a high-level language (Pig Latin) for expressing data analysis programs. It compiles Pig Latin programs into MapReduce/Tez jobs and runs them on Hadoop clusters.
examples:
- key_count: 8
  name: Apache Pig Job Example
  slug: apache-pig-job-example
- key_count: 2
  name: Apache Pig Job List Example
  slug: apache-pig-job-list-example
- key_count: 2
  name: Apache Pig Job Logs Example
  slug: apache-pig-job-logs-example
- key_count: 4
  name: Apache Pig Job Request Example
  slug: apache-pig-job-request-example
- key_count: 1
  name: Apache Pig Script Request Example
  slug: apache-pig-script-request-example
- key_count: 4
  name: Apache Pig Validation Error Example
  slug: apache-pig-validation-error-example
- key_count: 2
  name: Apache Pig Validation Result Example
  slug: apache-pig-validation-result-example
features:
- description: High-level dataflow language for expressing data transformations
  name: Pig Latin Language
- description: Compiles Pig Latin to MapReduce or Apache Tez execution plans
  name: MapReduce/Tez Backend
- description: User-defined functions in Java, Python, JavaScript, and Ruby
  name: UDF Support
- description: Process data through external programs using STREAM operator
  name: Streaming
- description: Flexible schema handling for semi-structured data
  name: Schema Evolution
- description: Automatic logical and physical plan optimization
  name: Optimization
finops:
- name: Apache Pig Finops
  service_category: API
  slug: apache-pig-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-pig.png
integrations:
- description: Native MapReduce execution on YARN/HDFS
  name: Apache Hadoop
- description: High-performance Tez execution engine support
  name: Apache Tez
- description: HBase storage handler for reading/writing HBase tables
  name: Apache HBase
- description: HCatalog integration for Hive metastore access
  name: Apache Hive
- description: S3 input/output for cloud-based data processing
  name: Amazon S3
json_schemas:
- name: JobList
  property_count: 2
  slug: apache-pig-job-list
- name: JobLogs
  property_count: 2
  slug: apache-pig-job-logs
- name: JobRequest
  property_count: 4
  slug: apache-pig-job-request
- name: Job
  property_count: 8
  slug: apache-pig-job
- name: ScriptRequest
  property_count: 1
  slug: apache-pig-script-request
- name: ValidationError
  property_count: 4
  slug: apache-pig-validation-error
- name: ValidationResult
  property_count: 2
  slug: apache-pig-validation-result
json_structures:
- name: Apache Pig Job List Structure
  property_count: 2
  slug: apache-pig-job-list-structure
- name: Apache Pig Job Logs Structure
  property_count: 2
  slug: apache-pig-job-logs-structure
- name: Apache Pig Job Request Structure
  property_count: 4
  slug: apache-pig-job-request-structure
- name: Apache Pig Job Structure
  property_count: 8
  slug: apache-pig-job-structure
- name: Apache Pig Script Request Structure
  property_count: 1
  slug: apache-pig-script-request-structure
- name: Apache Pig Validation Error Structure
  property_count: 4
  slug: apache-pig-validation-error-structure
- name: Apache Pig Validation Result Structure
  property_count: 2
  slug: apache-pig-validation-result-structure
jsonld:
- class_count: 7
  name: Apache Pig Context
  property_count: 19
  slug: apache-pig-context
layout: provider
modified: '2026-05-19'
name: Apache Pig
nav: Providers
network: true
overview: 'Apache Pig publishes 2 APIs on the [APIs.io](https://apis.io/) network: Jobs API and Scripts API. Tagged areas include Big Data, Data Analysis, ETL, Hadoop, and Scripting.


  The Apache Pig catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Pig''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Apache Pig Plans Pricing
  plan_count: 3
  slug: apache-pig-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Apache Pig Rate Limits
  slug: apache-pig-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Pig API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-pig-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Apache Pig API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 5
  slug: apache-pig-spectral-rules
score:
  band: emerging
  composite: 20.6
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 19.2
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 20.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-pig/refs/heads/main/screenshots/apache-pig-2026-06-20T172132.png
security:
- kind: domain-security
  name: Apache Pig Domain Security
  slug: apache-pig-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Pig Vulnerability Disclosure
  slug: apache-pig-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-pig
tags:
- Big Data
- Data Analysis
- ETL
- Hadoop
- Scripting
- Apache
- Open-Source
use_cases:
- description: Build data transformation pipelines from raw logs to structured data
  name: ETL Pipelines
- description: Analyze large datasets with ad-hoc Pig Latin queries
  name: Ad-hoc Data Analysis
- description: Clean and prepare data for machine learning workflows
  name: Data Preparation
- description: Process and aggregate web server and application logs
  name: Log Processing
---
