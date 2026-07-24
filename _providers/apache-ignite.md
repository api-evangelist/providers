---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 22
  human_in_the_loop: 7
  name: Apache Ignite Agentic Access
  operation_count: 50
  slug: apache-ignite-agentic-access
  summary_line: 50 operations · 22 acting · 7 human-in-the-loop
api_count: 15
apis:
- description: The Ignite Java client API provides native Java access to Ignite clusters for table operations, SQL queries, transactions, and compute task execution.
  name: Apache Ignite Java Client API
  slug: java-api
- description: The Ignite .NET client API provides native C# and .NET access to Ignite clusters for table operations, SQL queries, and distributed computing.
  name: Apache Ignite .NET Client API
  slug: dotnet-api
- description: The clusterConfiguration API from Apache Ignite — 2 operation(s) for clusterconfiguration.
  name: Apache Ignite clusterConfiguration API
  slug: apache-ignite-clusterconfiguration-api
- description: The clusterManagement API from Apache Ignite — 2 operation(s) for clustermanagement.
  name: Apache Ignite clusterManagement API
  slug: apache-ignite-clustermanagement-api
- description: The clusterMetric API from Apache Ignite — 3 operation(s) for clustermetric.
  name: Apache Ignite clusterMetric API
  slug: apache-ignite-clustermetric-api
- description: The compute API from Apache Ignite — 3 operation(s) for compute.
  name: Apache Ignite compute API
  slug: apache-ignite-compute-api
- description: The deployment API from Apache Ignite — 6 operation(s) for deployment.
  name: Apache Ignite deployment API
  slug: apache-ignite-deployment-api
- description: The nodeConfiguration API from Apache Ignite — 2 operation(s) for nodeconfiguration.
  name: Apache Ignite nodeConfiguration API
  slug: apache-ignite-nodeconfiguration-api
- description: The nodeManagement API from Apache Ignite — 3 operation(s) for nodemanagement.
  name: Apache Ignite nodeManagement API
  slug: apache-ignite-nodemanagement-api
- description: The nodeMetric API from Apache Ignite — 4 operation(s) for nodemetric.
  name: Apache Ignite nodeMetric API
  slug: apache-ignite-nodemetric-api
- description: The recovery API from Apache Ignite — 12 operation(s) for recovery.
  name: Apache Ignite recovery API
  slug: apache-ignite-recovery-api
- description: The sql API from Apache Ignite — 3 operation(s) for sql.
  name: Apache Ignite sql API
  slug: apache-ignite-sql-api
- description: The system API from Apache Ignite — 2 operation(s) for system.
  name: Apache Ignite system API
  slug: apache-ignite-system-api
- description: The topology API from Apache Ignite — 2 operation(s) for topology.
  name: Apache Ignite topology API
  slug: apache-ignite-topology-api
- description: The transactions API from Apache Ignite — 2 operation(s) for transactions.
  name: Apache Ignite transactions API
  slug: apache-ignite-transactions-api
artifact_total: 160
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-ignite-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-ignite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-ignite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-ignite-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/apache-ignite
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/ignite-3
- group: docs
  title: ''
  type: Documentation
  url: https://ignite.apache.org/docs/ignite3/3.1.0/
- group: start
  title: ''
  type: GettingStarted
  url: https://ignite.apache.org/docs/ignite3/3.1.0/getting-started/quick-start
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: Versioning
  url: https://ignite.apache.org/releases/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-ignite-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-ignite-vocabulary.yaml
created: '2026-03-16'
description: Apache Ignite is a distributed database for mission-critical high-velocity applications requiring in-memory performance. It provides ACID transactions, SQL queries, key-value storage, compute grid, and backpressured streaming across distributed clusters. Governed by the Apache Software Foundation under the Apache 2.0 license.
examples:
- key_count: 4
  name: Rest Api Cluster Node Example
  slug: rest-api-cluster-node-example
- key_count: 5
  name: Rest Api Cluster State Example
  slug: rest-api-cluster-state-example
- key_count: 2
  name: Rest Api Cluster Tag Example
  slug: rest-api-cluster-tag-example
- key_count: 0
  name: Rest Api Deploy Mode Example
  slug: rest-api-deploy-mode-example
- key_count: 0
  name: Rest Api Deployment Status Example
  slug: rest-api-deployment-status-example
- key_count: 6
  name: Rest Api Global Partition State Response Example
  slug: rest-api-global-partition-state-response-example
- key_count: 1
  name: Rest Api Global Partition States Response Example
  slug: rest-api-global-partition-states-response-example
- key_count: 3
  name: Rest Api Global Zone Partition State Response Example
  slug: rest-api-global-zone-partition-state-response-example
- key_count: 1
  name: Rest Api Global Zone Partition States Response Example
  slug: rest-api-global-zone-partition-states-response-example
- key_count: 4
  name: Rest Api Init Command Example
  slug: rest-api-init-command-example
- key_count: 2
  name: Rest Api Invalid Param Example
  slug: rest-api-invalid-param-example
- key_count: 5
  name: Rest Api Job State Example
  slug: rest-api-job-state-example
- key_count: 0
  name: Rest Api Job Status Example
  slug: rest-api-job-status-example
- key_count: 8
  name: Rest Api Local Partition State Response Example
  slug: rest-api-local-partition-state-response-example
- key_count: 1
  name: Rest Api Local Partition States Response Example
  slug: rest-api-local-partition-states-response-example
- key_count: 5
  name: Rest Api Local Zone Partition State Response Example
  slug: rest-api-local-zone-partition-state-response-example
- key_count: 1
  name: Rest Api Local Zone Partition States Response Example
  slug: rest-api-local-zone-partition-states-response-example
- key_count: 2
  name: Rest Api Metric Example
  slug: rest-api-metric-example
- key_count: 2
  name: Rest Api Metric Set Example
  slug: rest-api-metric-set-example
- key_count: 2
  name: Rest Api Metric Source Example
  slug: rest-api-metric-source-example
- key_count: 6
  name: Rest Api Migrate Request Example
  slug: rest-api-migrate-request-example
- key_count: 2
  name: Rest Api Network Address Example
  slug: rest-api-network-address-example
- key_count: 2
  name: Rest Api Node Info Example
  slug: rest-api-node-info-example
- key_count: 3
  name: Rest Api Node Metadata Example
  slug: rest-api-node-metadata-example
- key_count: 2
  name: Rest Api Node Metric Sources Example
  slug: rest-api-node-metric-sources-example
- key_count: 2
  name: Rest Api Node State Example
  slug: rest-api-node-state-example
- key_count: 2
  name: Rest Api Node Version Example
  slug: rest-api-node-version-example
- key_count: 8
  name: Rest Api Problem Example
  slug: rest-api-problem-example
- key_count: 2
  name: Rest Api Reset Cluster Request Example
  slug: rest-api-reset-cluster-request-example
- key_count: 3
  name: Rest Api Reset Partitions Request Example
  slug: rest-api-reset-partitions-request-example
- key_count: 2
  name: Rest Api Reset Zone Partitions Request Example
  slug: rest-api-reset-zone-partitions-request-example
- key_count: 4
  name: Rest Api Restart Partitions Request Example
  slug: rest-api-restart-partitions-request-example
- key_count: 3
  name: Rest Api Restart Zone Partitions Request Example
  slug: rest-api-restart-zone-partitions-request-example
- key_count: 7
  name: Rest Api Sql Query Example
  slug: rest-api-sql-query-example
- key_count: 0
  name: Rest Api State Example
  slug: rest-api-state-example
- key_count: 6
  name: Rest Api Transaction Example
  slug: rest-api-transaction-example
- key_count: 2
  name: Rest Api Unit Status Example
  slug: rest-api-unit-status-example
- key_count: 2
  name: Rest Api Unit Version Status Example
  slug: rest-api-unit-version-status-example
- key_count: 1
  name: Rest Api Update Job Priority Body Example
  slug: rest-api-update-job-priority-body-example
features:
- description: Memory-first storage with MVCC for consistent high-velocity performance.
  name: In-Memory Speed
- description: Full ACID transactions across distributed cluster nodes.
  name: ACID Transactions
- description: ANSI SQL-compliant queries across distributed tables with JDBC/ODBC drivers.
  name: SQL Support
- description: Native key-value API for direct cache access without SQL overhead.
  name: Key-Value Storage
- description: Distributed compute tasks co-located with data for low-latency processing.
  name: Compute Grid
- description: Native clients for Java, .NET, C++, and Python.
  name: Multi-Language Clients
- description: Online schema changes without cluster downtime.
  name: Schema Evolution
- description: Event stream ingestion and enrichment with flow control.
  name: Backpressured Streaming
finops:
- name: Apache Ignite Finops
  service_category: API
  slug: apache-ignite-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-ignite.png
integrations:
- description: Native Spring Boot integration for Ignite cluster connectivity.
  name: Spring Boot
- description: Stream data from Kafka topics into Ignite tables for real-time processing.
  name: Apache Kafka
- description: Standard JDBC driver for connecting SQL tools to Ignite clusters.
  name: JDBC
- description: ODBC driver for BI tool integration with Ignite SQL engine.
  name: ODBC
- type: Blog
  url: https://ignite.apache.org/blog/rss.xml
json_schemas:
- name: ClusterNode
  property_count: 4
  slug: rest-api-cluster-node
- name: ClusterState
  property_count: 5
  slug: rest-api-cluster-state
- name: ClusterTag
  property_count: 2
  slug: rest-api-cluster-tag
- name: deployMode
  property_count: 0
  slug: rest-api-deploy-mode
- name: DeploymentStatus
  property_count: 0
  slug: rest-api-deployment-status
- name: GlobalPartitionStateResponse
  property_count: 6
  slug: rest-api-global-partition-state-response
- name: GlobalPartitionStatesResponse
  property_count: 1
  slug: rest-api-global-partition-states-response
- name: GlobalZonePartitionStateResponse
  property_count: 3
  slug: rest-api-global-zone-partition-state-response
- name: GlobalZonePartitionStatesResponse
  property_count: 1
  slug: rest-api-global-zone-partition-states-response
- name: InitCommand
  property_count: 4
  slug: rest-api-init-command
- name: InvalidParam
  property_count: 2
  slug: rest-api-invalid-param
- name: JobState
  property_count: 5
  slug: rest-api-job-state
- name: JobStatus
  property_count: 0
  slug: rest-api-job-status
- name: LocalPartitionStateResponse
  property_count: 8
  slug: rest-api-local-partition-state-response
- name: LocalPartitionStatesResponse
  property_count: 1
  slug: rest-api-local-partition-states-response
- name: LocalZonePartitionStateResponse
  property_count: 5
  slug: rest-api-local-zone-partition-state-response
- name: LocalZonePartitionStatesResponse
  property_count: 1
  slug: rest-api-local-zone-partition-states-response
- name: Metric
  property_count: 2
  slug: rest-api-metric
- name: MetricSet
  property_count: 2
  slug: rest-api-metric-set
- name: MetricSource
  property_count: 2
  slug: rest-api-metric-source
- name: MigrateRequest
  property_count: 6
  slug: rest-api-migrate-request
- name: NetworkAddress
  property_count: 2
  slug: rest-api-network-address
- name: NodeInfo
  property_count: 2
  slug: rest-api-node-info
- name: NodeMetadata
  property_count: 3
  slug: rest-api-node-metadata
- name: NodeMetricSources
  property_count: 2
  slug: rest-api-node-metric-sources
- name: NodeState
  property_count: 2
  slug: rest-api-node-state
- name: NodeVersion
  property_count: 2
  slug: rest-api-node-version
- name: Problem
  property_count: 8
  slug: rest-api-problem
- name: ResetClusterRequest
  property_count: 2
  slug: rest-api-reset-cluster-request
- name: ResetPartitionsRequest
  property_count: 3
  slug: rest-api-reset-partitions-request
- name: ResetZonePartitionsRequest
  property_count: 2
  slug: rest-api-reset-zone-partitions-request
- name: RestartPartitionsRequest
  property_count: 4
  slug: rest-api-restart-partitions-request
- name: RestartZonePartitionsRequest
  property_count: 3
  slug: rest-api-restart-zone-partitions-request
- name: SqlQuery
  property_count: 7
  slug: rest-api-sql-query
- name: State
  property_count: 0
  slug: rest-api-state
- name: Transaction
  property_count: 6
  slug: rest-api-transaction
- name: UnitStatus
  property_count: 2
  slug: rest-api-unit-status
- name: UnitVersionStatus
  property_count: 2
  slug: rest-api-unit-version-status
- name: UpdateJobPriorityBody
  property_count: 1
  slug: rest-api-update-job-priority-body
json_structures:
- name: Rest Api Cluster Node Structure
  property_count: 4
  slug: rest-api-cluster-node-structure
- name: Rest Api Cluster State Structure
  property_count: 5
  slug: rest-api-cluster-state-structure
- name: Rest Api Cluster Tag Structure
  property_count: 2
  slug: rest-api-cluster-tag-structure
- name: Rest Api Deploy Mode Structure
  property_count: 0
  slug: rest-api-deploy-mode-structure
- name: Rest Api Deployment Status Structure
  property_count: 0
  slug: rest-api-deployment-status-structure
- name: Rest Api Global Partition State Response Structure
  property_count: 6
  slug: rest-api-global-partition-state-response-structure
- name: Rest Api Global Partition States Response Structure
  property_count: 1
  slug: rest-api-global-partition-states-response-structure
- name: Rest Api Global Zone Partition State Response Structure
  property_count: 3
  slug: rest-api-global-zone-partition-state-response-structure
- name: Rest Api Global Zone Partition States Response Structure
  property_count: 1
  slug: rest-api-global-zone-partition-states-response-structure
- name: Rest Api Init Command Structure
  property_count: 4
  slug: rest-api-init-command-structure
- name: Rest Api Invalid Param Structure
  property_count: 2
  slug: rest-api-invalid-param-structure
- name: Rest Api Job State Structure
  property_count: 5
  slug: rest-api-job-state-structure
- name: Rest Api Job Status Structure
  property_count: 0
  slug: rest-api-job-status-structure
- name: Rest Api Local Partition State Response Structure
  property_count: 8
  slug: rest-api-local-partition-state-response-structure
- name: Rest Api Local Partition States Response Structure
  property_count: 1
  slug: rest-api-local-partition-states-response-structure
- name: Rest Api Local Zone Partition State Response Structure
  property_count: 5
  slug: rest-api-local-zone-partition-state-response-structure
- name: Rest Api Local Zone Partition States Response Structure
  property_count: 1
  slug: rest-api-local-zone-partition-states-response-structure
- name: Rest Api Metric Set Structure
  property_count: 2
  slug: rest-api-metric-set-structure
- name: Rest Api Metric Source Structure
  property_count: 2
  slug: rest-api-metric-source-structure
- name: Rest Api Metric Structure
  property_count: 2
  slug: rest-api-metric-structure
- name: Rest Api Migrate Request Structure
  property_count: 6
  slug: rest-api-migrate-request-structure
- name: Rest Api Network Address Structure
  property_count: 2
  slug: rest-api-network-address-structure
- name: Rest Api Node Info Structure
  property_count: 2
  slug: rest-api-node-info-structure
- name: Rest Api Node Metadata Structure
  property_count: 3
  slug: rest-api-node-metadata-structure
- name: Rest Api Node Metric Sources Structure
  property_count: 2
  slug: rest-api-node-metric-sources-structure
- name: Rest Api Node State Structure
  property_count: 2
  slug: rest-api-node-state-structure
- name: Rest Api Node Version Structure
  property_count: 2
  slug: rest-api-node-version-structure
- name: Rest Api Problem Structure
  property_count: 8
  slug: rest-api-problem-structure
- name: Rest Api Reset Cluster Request Structure
  property_count: 2
  slug: rest-api-reset-cluster-request-structure
- name: Rest Api Reset Partitions Request Structure
  property_count: 3
  slug: rest-api-reset-partitions-request-structure
- name: Rest Api Reset Zone Partitions Request Structure
  property_count: 2
  slug: rest-api-reset-zone-partitions-request-structure
- name: Rest Api Restart Partitions Request Structure
  property_count: 4
  slug: rest-api-restart-partitions-request-structure
- name: Rest Api Restart Zone Partitions Request Structure
  property_count: 3
  slug: rest-api-restart-zone-partitions-request-structure
- name: Rest Api Sql Query Structure
  property_count: 7
  slug: rest-api-sql-query-structure
- name: Rest Api State Structure
  property_count: 0
  slug: rest-api-state-structure
- name: Rest Api Transaction Structure
  property_count: 6
  slug: rest-api-transaction-structure
- name: Rest Api Unit Status Structure
  property_count: 2
  slug: rest-api-unit-status-structure
- name: Rest Api Unit Version Status Structure
  property_count: 2
  slug: rest-api-unit-version-status-structure
- name: Rest Api Update Job Priority Body Structure
  property_count: 1
  slug: rest-api-update-job-priority-body-structure
jsonld:
- class_count: 37
  name: Apache Ignite Rest Api Context
  property_count: 53
  slug: apache-ignite-rest-api-context
layout: provider
modified: '2026-05-19'
name: Apache Ignite
nav: Providers
network: true
overview: 'Apache Ignite publishes 13 APIs on the [APIs.io](https://apis.io/) network, including clusterConfiguration API, clusterManagement API, clusterMetric API, and 10 more. Tagged areas include Caching, Compute Grid, Distributed Database, In-Memory, and Open Source.


  The Apache Ignite catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Ignite''s developer surface includes authentication, documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Apache Ignite Plans Pricing
  plan_count: 3
  slug: apache-ignite-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Apache Ignite Rate Limits
  slug: apache-ignite-rate-limits
rules:
- name: Apache Ignite API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-ignite-jsonschema-spectral-rules
- name: Apache Ignite API Rules
  rule_count: 27
  severity_counts:
    error: 10
    hint: 0
    info: 5
    warn: 12
  slug: apache-ignite-spectral-rules
score:
  band: developing
  composite: 58.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.1
    developer_ergonomics: 30.4
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 58.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-ignite/refs/heads/main/screenshots/apache-ignite-2026-06-20T172109.png
security:
- kind: authentication
  name: Apache Ignite Authentication
  slug: apache-ignite-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Ignite Domain Security
  slug: apache-ignite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Ignite Vulnerability Disclosure
  slug: apache-ignite-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-ignite
tags:
- Caching
- Compute Grid
- Distributed Database
- In-Memory
- Open Source
- SQL
use_cases:
- description: Ingest, enrich, and process high-velocity event streams with in-memory speed.
  name: Event Stream Processing
- description: Distributed state store for microservices with ACID guarantees.
  name: Microservices State Management
- description: High-speed session caching for web applications.
  name: Session Management
- description: Low-latency feature serving for machine learning model inference.
  name: AI/ML Feature Store
- description: SQL analytics over continuously updated distributed datasets.
  name: Real-Time Analytics
---
