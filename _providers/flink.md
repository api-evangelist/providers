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
- acting_count: 7
  human_in_the_loop: 2
  name: Flink Agentic Access
  operation_count: 29
  slug: flink-agentic-access
  summary_line: 29 operations · 7 acting · 2 human-in-the-loop
api_count: 7
apis:
- description: Checkpoint configuration, status, and details.
  name: Apache Flink Checkpoints API
  slug: flink-checkpoints-api
- description: Cluster lifecycle and configuration.
  name: Apache Flink Cluster API
  slug: flink-cluster-api
- description: Cluster dataset listing and deletion.
  name: Apache Flink Datasets API
  slug: flink-datasets-api
- description: JAR upload, listing, run, and delete.
  name: Apache Flink JARs API
  slug: flink-jars-api
- description: JobManager configuration, environment, logs, metrics, and threads.
  name: Apache Flink JobManager API
  slug: flink-jobmanager-api
- description: Job lifecycle and inspection.
  name: Apache Flink Jobs API
  slug: flink-jobs-api
- description: TaskManager listing and inspection.
  name: Apache Flink TaskManagers API
  slug: flink-taskmanagers-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flink-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flink.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://nightlies.apache.org/flink/flink-docs-stable/
- group: docs
  title: ''
  type: RESTAPIDocumentation
  url: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/rest_api/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/flink
- group: company
  title: ''
  type: Blog
  url: https://flink.apache.org/posts/
- group: operate
  title: ''
  type: Community
  url: https://flink.apache.org/community/
created: '2025-01-01'
description: Apache Flink is an open-source framework and distributed processing engine for stateful computations over unbounded and bounded data streams. It is designed to run in all common cluster environments and to perform computations at in-memory speed and at any scale. Flink exposes a REST API on the JobManager Dispatcher that allows external systems to query cluster status, submit and manage jobs, trigger savepoints and checkpoints, upload and run JARs, and inspect metrics, accumulators, and exception histories. The same REST endpoints power the Flink Web UI.
finops:
- name: Flink Finops
  service_category: API
  slug: flink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flink.png
layout: provider
modified: '2026-05-19'
name: Apache Flink
nav: Providers
network: true
overview: 'Apache Flink publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Checkpoints API, Cluster API, Datasets API, and 4 more. Tagged areas include Big Data, Distributed Computing, Real-Time Analytics, Stream Processing, and Workflows.


  Apache Flink''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Flink Plans Pricing
  plan_count: 3
  slug: flink-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 5
  name: Flink Rate Limits
  slug: flink-rate-limits
score:
  band: thin
  composite: 31.7
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 40.7
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flink/refs/heads/main/screenshots/flink-2026-06-20T181313.png
security:
- kind: domain-security
  name: Flink Domain Security
  slug: flink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flink Vulnerability Disclosure
  slug: flink-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: flink
tags:
- Big Data
- Distributed Computing
- Real-Time Analytics
- Stream Processing
- Workflows
website: https://flink.apache.org/
---
