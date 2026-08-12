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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Apache Oozie Agentic Access
  operation_count: 16
  slug: apache-oozie-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 4
apis:
- description: System administration, configuration, and monitoring
  name: Apache Oozie Admin API
  slug: apache-oozie-admin-api
- description: Single job lifecycle management and information retrieval
  name: Apache Oozie Job API
  slug: apache-oozie-job-api
- description: Job submission and bulk management
  name: Apache Oozie Jobs API
  slug: apache-oozie-jobs-api
- description: Supported protocol version discovery
  name: Apache Oozie Versions API
  slug: apache-oozie-versions-api
artifact_total: 59
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/oozie/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-oozie-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-oozie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-oozie-domain-security.yml
- group: build
  title: Apache Oozie GitHub Repository
  type: GitHubRepository
  url: https://github.com/apache/oozie
- group: build
  title: Apache Software Foundation GitHub
  type: GitHubOrganization
  url: https://github.com/apache
- group: docs
  title: Apache Oozie Documentation
  type: Documentation
  url: https://oozie.apache.org/docs/5.2.1/
- group: start
  title: Oozie Quick Start Guide
  type: GettingStarted
  url: https://oozie.apache.org/docs/5.2.1/DG_QuickStart.html
- group: learn
  title: Oozie Examples
  type: Tutorials
  url: https://oozie.apache.org/docs/5.2.1/DG_Examples.html
- group: operate
  title: Oozie Release Log
  type: ReleaseNotes
  url: https://github.com/apache/oozie/blob/master/release-log.txt
- group: commercial
  title: Apache License 2.0
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: operate
  title: Mailing Lists
  type: Support
  url: https://oozie.apache.org/mailing-lists.html
- group: operate
  title: Oozie on Stack Overflow
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/oozie
- group: design
  title: Apache Oozie Spectral Rules
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/rules/apache-oozie-spectral-rules.yml
- group: design
  title: Apache Oozie Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/vocabulary/apache-oozie-vocabulary.yaml
- group: design
  title: Apache Oozie JSON-LD Context
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/json-ld/apache-oozie-context.jsonld
created: '2026-03-16'
description: Apache Oozie is a workflow scheduler system for managing Apache Hadoop jobs. It enables users to define workflows as directed acyclic graphs (DAGs) of actions including MapReduce, Pig, Hive, Sqoop, and custom Java/shell steps. Coordinator jobs trigger workflows based on time schedules or data availability, while bundle jobs group multiple coordinators. Oozie provides a REST API for job submission, lifecycle management, monitoring, and system administration. Governed by the Apache Software Foundation under the Apache License 2.0, written in Java.
examples:
- key_count: 1
  name: Apache Oozie Build Version Example
  slug: apache-oozie-build-version-example
- key_count: 6
  name: Apache Oozie Job Action Example
  slug: apache-oozie-job-action-example
- key_count: 1
  name: Apache Oozie Job Id Example
  slug: apache-oozie-job-id-example
- key_count: 12
  name: Apache Oozie Job Info Example
  slug: apache-oozie-job-info-example
- key_count: 6
  name: Apache Oozie Job List Example
  slug: apache-oozie-job-list-example
- key_count: 3
  name: Apache Oozie System Metrics Example
  slug: apache-oozie-system-metrics-example
- key_count: 1
  name: Apache Oozie System Status Example
  slug: apache-oozie-system-status-example
- key_count: 1
  name: Apache Oozie Validation Result Example
  slug: apache-oozie-validation-result-example
features:
- description: Define complex data processing pipelines as DAGs of actions executed on Apache Hadoop.
  name: Directed Acyclic Graph Workflows
- description: Schedule recurring workflows triggered by time intervals or data availability conditions in HDFS.
  name: Coordinator Jobs
- description: Group multiple coordinator jobs into a single bundle for coordinated lifecycle management.
  name: Bundle Jobs
- description: Full REST API for job submission, lifecycle control, monitoring, and system administration.
  name: REST API Management
- description: Built-in support for MapReduce, Pig, Hive, Sqoop, Distcp, and custom Java/shell actions.
  name: Native Hadoop Action Types
- description: Define and monitor service level agreements on workflow and coordinator actions with alert capabilities.
  name: SLA Management
- description: Generate PNG, SVG, or DOT graph visualizations of workflow DAGs for debugging and documentation.
  name: DAG Visualization
- description: Retrieve execution logs, error logs, and audit trails for jobs via REST API with filtering support.
  name: Log Retrieval
- description: Built-in HA support with multiple Oozie server instances and distributed state management.
  name: High Availability
- description: Manage shared Hadoop libraries across workflows for consistent classpath management.
  name: Shared Library Support
finops:
- name: Apache Oozie Finops
  service_category: API
  slug: apache-oozie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-oozie.png
integrations:
- description: Core integration with HDFS for data storage and YARN for resource management.
  name: Apache Hadoop
- description: Native Hive action type for executing HiveQL queries as workflow steps.
  name: Apache Hive
- description: Native Pig action type for data transformation scripts in workflow pipelines.
  name: Apache Pig
- description: Native Sqoop action type for importing and exporting data between Hadoop and RDBMS.
  name: Apache Sqoop
- description: Spark action type for running Spark jobs within Oozie workflows.
  name: Apache Spark
- description: Native MapReduce action type as the foundational Hadoop computation framework.
  name: Apache MapReduce
json_schemas:
- name: BuildVersion
  property_count: 1
  slug: apache-oozie-build-version
- name: JobAction
  property_count: 8
  slug: apache-oozie-job-action
- name: JobId
  property_count: 1
  slug: apache-oozie-job-id
- name: JobInfo
  property_count: 12
  slug: apache-oozie-job-info
- name: JobList
  property_count: 6
  slug: apache-oozie-job-list
- name: SystemMetrics
  property_count: 3
  slug: apache-oozie-system-metrics
- name: SystemStatus
  property_count: 1
  slug: apache-oozie-system-status
- name: ValidationResult
  property_count: 1
  slug: apache-oozie-validation-result
json_structures:
- name: Apache Oozie Build Version Structure
  property_count: 1
  slug: apache-oozie-build-version-structure
- name: Apache Oozie Job Action Structure
  property_count: 8
  slug: apache-oozie-job-action-structure
- name: Apache Oozie Job Id Structure
  property_count: 1
  slug: apache-oozie-job-id-structure
- name: Apache Oozie Job Info Structure
  property_count: 12
  slug: apache-oozie-job-info-structure
- name: Apache Oozie Job List Structure
  property_count: 6
  slug: apache-oozie-job-list-structure
- name: Apache Oozie System Metrics Structure
  property_count: 3
  slug: apache-oozie-system-metrics-structure
- name: Apache Oozie System Status Structure
  property_count: 1
  slug: apache-oozie-system-status-structure
- name: Apache Oozie Validation Result Structure
  property_count: 1
  slug: apache-oozie-validation-result-structure
jsonld:
- class_count: 9
  name: Apache Oozie Context
  property_count: 27
  slug: apache-oozie-context
layout: provider
modified: '2026-05-19'
name: Apache Oozie
nav: Providers
network: true
overview: 'Apache Oozie publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Job API, Jobs API, and 1 more. Tagged areas include Workflow, Hadoop, Orchestration, Scheduling, and Big Data.


  The Apache Oozie catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Oozie''s developer surface includes documentation, getting-started guide, release notes, support, Stack Overflow tag, and 12 more developer resources.'
plans:
- name: Apache Oozie Plans Pricing
  plan_count: 3
  slug: apache-oozie-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Apache Oozie Rate Limits
  slug: apache-oozie-rate-limits
rules:
- name: Apache Oozie API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-oozie-jsonschema-spectral-rules
- name: Apache Oozie API Rules
  rule_count: 33
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 18
  slug: apache-oozie-spectral-rules
score:
  band: developing
  composite: 45.2
  delta: -8.4
  facets:
    commercial_clarity: 26.3
    contract_quality: 66.5
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/screenshots/apache-oozie-2026-06-20T172126.png
security:
- kind: domain-security
  name: Apache Oozie Domain Security
  slug: apache-oozie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Oozie Vulnerability Disclosure
  slug: apache-oozie-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-oozie
tags:
- Workflow
- Hadoop
- Orchestration
- Scheduling
- Big Data
- Apache
- Java
- Open Source
use_cases:
- description: Orchestrate multi-step ETL pipelines combining Hive queries, MapReduce jobs, and data transfers on Hadoop.
  name: ETL Pipeline Orchestration
- description: Run recurring Hadoop batch jobs on time-based schedules using coordinator jobs.
  name: Scheduled Data Processing
- description: Trigger workflows automatically when new data arrives in HDFS using coordinator data-in conditions.
  name: Data-Triggered Workflows
- description: Automate ML model training and evaluation pipelines on Hadoop with dependency chaining.
  name: Machine Learning Pipeline Automation
- description: Orchestrate large-scale data migration, compaction, and archival workflows across Hadoop clusters.
  name: Data Migration and Archival
- description: Coordinate workflows that span multiple Hadoop clusters using Distcp and remote actions.
  name: Multi-Cluster Coordination
---
