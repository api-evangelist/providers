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
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: 'The DolphinScheduler REST API enables programmatic management of projects, workflow definitions (DAGs), workflow instances, task types, schedules, resources, data sources, alerts, tenants, and users. '
  name: Apache DolphinScheduler REST API
  slug: apache-dolphinscheduler-rest-api
artifact_total: 40
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-dolphinscheduler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-dolphinscheduler-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-dolphinscheduler
- group: start
  title: ''
  type: Portal
  url: https://dolphinscheduler.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://dolphinscheduler.apache.org/en-us/docs/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://dolphinscheduler.apache.org/en-us/docs/latest/user_doc/start/quick-start.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/dolphinscheduler
- group: build
  title: PyDolphinScheduler Python SDK
  type: SDKs
  url: https://github.com/apache/dolphinscheduler-sdk-python
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/vocabulary/apache-dolphinscheduler-vocabulary.yaml
created: '2026-03-16'
description: Apache DolphinScheduler is a modern distributed and extensible data orchestration platform governed by the Apache Software Foundation. It provides a DAG-based visual workflow designer, multi-master/multi-worker architecture for horizontal scaling, and a comprehensive REST API for programmatic control. It supports dozens of task types (Shell, Spark, Flink, SQL, Python, HTTP, etc.), multi-cloud deployments, multi-tenancy, backfill, and a Python SDK (PyDolphinScheduler).
examples:
- key_count: 9
  name: Apache Dolphinscheduler Schedule Example
  slug: apache-dolphinscheduler-schedule-example
- key_count: 12
  name: Apache Dolphinscheduler Task Definition Example
  slug: apache-dolphinscheduler-task-definition-example
- key_count: 12
  name: Apache Dolphinscheduler Workflow Definition Example
  slug: apache-dolphinscheduler-workflow-definition-example
- key_count: 10
  name: Apache Dolphinscheduler Workflow Instance Example
  slug: apache-dolphinscheduler-workflow-instance-example
features:
- description: Web-based drag-and-drop interface for building directed acyclic graph (DAG) workflows with real-time execution visualization.
  name: DAG Visual Workflow Designer
- description: Comprehensive REST API for all platform operations including workflow management, scheduling, resource management, and administration.
  name: REST Open API
- description: Decentralized architecture with horizontal scaling support, capable of processing tens of millions of tasks per day.
  name: Multi-Master/Worker Architecture
- description: Built-in task types including Shell, Spark, Flink, SQL, Python, HTTP, DataX, Seatunnel, Jupyter, and custom task plugins.
  name: Rich Task Types
- description: Supports multiple tenants with isolated resource quotas, permissions, and workflow namespaces.
  name: Multi-Tenancy
- description: Version control for workflow definitions and instances, enabling rollback and auditing of workflow changes.
  name: Workflow Versioning
- description: Unified data source management supporting MySQL, PostgreSQL, Hive, Trino, Spark, ClickHouse, and many other databases.
  name: Data Source Management
- description: PyDolphinScheduler allows defining and managing workflows programmatically in Python with code-first workflow authoring.
  name: Python SDK
finops:
- name: Apache Dolphinscheduler Finops
  service_category: API
  slug: apache-dolphinscheduler-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-dolphinscheduler.png
integrations:
- description: Native Spark task type for submitting Spark batch and streaming jobs from DolphinScheduler workflows.
  name: Apache Spark
- description: Native Flink task type for submitting Flink stream processing jobs.
  name: Apache Flink
- description: Hive data source and task type for SQL-on-Hadoop workloads.
  name: Apache Hive
- description: Kubernetes deployment mode and K8s task type for container-native workflow execution.
  name: Kubernetes
- description: Official Docker images and Docker Compose configuration for rapid deployment.
  name: Docker
- description: Native task types for DataX and SeaTunnel data integration frameworks.
  name: DataX / SeaTunnel
- description: An Airflow provider package allows triggering DolphinScheduler workflows from Airflow DAGs.
  name: Apache Airflow
json_schemas:
- name: Schedule
  property_count: 9
  slug: apache-dolphinscheduler-schedule
- name: TaskDefinition
  property_count: 12
  slug: apache-dolphinscheduler-task-definition
- name: WorkflowDefinition
  property_count: 12
  slug: apache-dolphinscheduler-workflow-definition
- name: WorkflowInstance
  property_count: 10
  slug: apache-dolphinscheduler-workflow-instance
json_structures:
- name: Apache Dolphinscheduler Schedule Structure
  property_count: 9
  slug: apache-dolphinscheduler-schedule-structure
- name: Apache Dolphinscheduler Task Definition Structure
  property_count: 12
  slug: apache-dolphinscheduler-task-definition-structure
- name: Apache Dolphinscheduler Workflow Definition Structure
  property_count: 12
  slug: apache-dolphinscheduler-workflow-definition-structure
- name: Apache Dolphinscheduler Workflow Instance Structure
  property_count: 10
  slug: apache-dolphinscheduler-workflow-instance-structure
jsonld:
- class_count: 6
  name: Apache Dolphinscheduler Context
  property_count: 29
  slug: apache-dolphinscheduler-context
layout: provider
modified: '2026-04-19'
name: Apache DolphinScheduler
nav: Providers
network: true
overview: 'Apache DolphinScheduler publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apache, DAG, Data Pipeline, Open Source, and Orchestration.


  The Apache DolphinScheduler catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apache DolphinScheduler''s developer surface includes developer portal, documentation, getting-started guide, and 7 more developer resources.'
plans:
- name: Apache Dolphinscheduler Plans Pricing
  plan_count: 3
  slug: apache-dolphinscheduler-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 5
  name: Apache Dolphinscheduler Rate Limits
  slug: apache-dolphinscheduler-rate-limits
rules:
- name: Apache DolphinScheduler API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-dolphinscheduler-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 33.9
    developer_ergonomics: 34.8
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 42.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/screenshots/apache-dolphinscheduler-2026-06-20T172053.png
security:
- kind: domain-security
  name: Apache Dolphinscheduler Domain Security
  slug: apache-dolphinscheduler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Dolphinscheduler Vulnerability Disclosure
  slug: apache-dolphinscheduler-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-dolphinscheduler
tags:
- Apache
- DAG
- Data Pipeline
- Open Source
- Orchestration
- Python
- Scheduling
- Workflow
use_cases:
- description: Orchestrate complex ETL/ELT data pipelines with dependencies, retries, and monitoring across distributed systems.
  name: Data Pipeline Orchestration
- description: Schedule and manage ML model training, evaluation, and deployment pipelines with task dependencies.
  name: Machine Learning Workflows
- description: Orchestrate workflows spanning multiple cloud providers and data centers with unified scheduling.
  name: Multi-Cloud Data Workflows
- description: Schedule recurring SQL queries, reports, and analytics jobs against multiple data sources.
  name: SQL and Analytics Scheduling
- description: Automate deployment workflows, data quality checks, and operational tasks with DolphinScheduler DAGs.
  name: DevOps and CI/CD Pipelines
website: https://dolphinscheduler.apache.org/
---
