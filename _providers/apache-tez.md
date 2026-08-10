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
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: The Tez DAG API provides a Java programming model for defining and submitting directed-acyclic-graph (DAG) computation jobs to Apache YARN. It allows building DAGs composed of Vertex (processing units
  name: Apache Tez DAG API
  slug: apache-tez-dag-api
- description: The Tez UI and YARN Application History Server expose REST endpoints for monitoring Tez application history, DAG details, vertex and task statistics. The Tez Timeline Server integration provides histo
  name: Apache Tez UI REST API
  slug: apache-tez-ui-rest-api
artifact_total: 19
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-tez-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-tez-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/tez
- group: docs
  title: ''
  type: Documentation
  url: https://tez.apache.org/
- group: start
  title: ''
  type: Portal
  url: https://tez.apache.org/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/tez/releases
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
created: '2026-03-16'
description: Apache Tez is an application framework that allows for complex directed-acyclic-graph (DAG) based processing of data built on Apache Hadoop YARN. It is designed as a successor to MapReduce for executing Hive and Pig queries, providing a flexible API for creating DAG execution pipelines, in-memory data passing between tasks, and session reuse for reduced startup latency. Apache Tez is an Apache Software Foundation top-level project.
features:
- description: Flexible DAG computation model replacing MapReduce for complex multi-stage pipelines.
  name: DAG-Based Execution
- description: Direct in-memory data transfer between connected vertices eliminating HDFS I/O.
  name: In-Memory Data Passing
- description: Tez sessions reuse container allocations across DAG submissions for reduced latency.
  name: Session Reuse
- description: Runtime DAG modification based on actual data statistics during execution.
  name: Dynamic Optimization
- description: Native YARN resource management with fine-grained resource requests per vertex.
  name: YARN Integration
finops:
- name: Apache Tez Finops
  service_category: API
  slug: apache-tez-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-tez.png
integrations:
- description: Native YARN resource manager integration for cluster resource allocation.
  name: Apache Hadoop YARN
- description: Default execution engine for Hive queries in HDP and CDH distributions.
  name: Apache Hive
- description: Tez execution backend for Apache Pig script compilation and execution.
  name: Apache Pig
- description: Input/output storage for Tez job data via Hadoop Distributed File System.
  name: Apache HDFS
layout: provider
modified: '2026-04-19'
name: Apache Tez
nav: Providers
network: true
overview: 'Apache Tez publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Big Data, DAG, Execution Engine, Hadoop, and YARN.


  Apache Tez''s developer surface includes documentation, developer portal, release notes, and 4 more developer resources.'
plans:
- name: Apache Tez Plans Pricing
  plan_count: 3
  slug: apache-tez-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Apache Tez Rate Limits
  slug: apache-tez-rate-limits
score:
  band: emerging
  composite: 25.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 25.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-tez/refs/heads/main/screenshots/apache-tez-2026-06-20T172151.png
security:
- kind: domain-security
  name: Apache Tez Domain Security
  slug: apache-tez-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Tez Vulnerability Disclosure
  slug: apache-tez-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-tez
tags:
- Big Data
- DAG
- Execution Engine
- Hadoop
- YARN
- Open Source
use_cases:
- description: Tez is the default execution engine for Apache Hive queries replacing MapReduce.
  name: Apache Hive Query Execution
- description: Execute Apache Pig Latin scripts as optimized Tez DAGs.
  name: Apache Pig Script Execution
- description: Multi-stage data transformation pipelines with in-memory data passing.
  name: Complex ETL Pipelines
website: https://tez.apache.org/
---
