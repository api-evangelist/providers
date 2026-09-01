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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Apache Kafka Agentic Access
  operation_count: 34
  slug: apache-kafka-agentic-access
  summary_line: 34 operations · 16 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: The core Kafka messaging protocol for producing and consuming records to/from topics using the native Kafka binary protocol, supporting exactly-once semantics, compaction, and partitioned log storage.
  name: Apache Kafka Messaging API
  slug: kafka-messaging-api
- description: The ACL API from Apache Kafka — 1 operation(s) for acl.
  name: Apache Kafka ACL API
  slug: apache-kafka-acl-api
- description: The Broker API from Apache Kafka — 1 operation(s) for broker.
  name: Apache Kafka Broker API
  slug: apache-kafka-broker-api
- description: The Cluster API from Apache Kafka — 3 operation(s) for cluster.
  name: Apache Kafka Cluster API
  slug: apache-kafka-cluster-api
- description: The Connectors API from Apache Kafka — 8 operation(s) for connectors.
  name: Apache Kafka Connectors API
  slug: apache-kafka-connectors-api
- description: The Consumer Group API from Apache Kafka — 2 operation(s) for consumer group.
  name: Apache Kafka Consumer Group API
  slug: apache-kafka-consumer-group-api
- description: The Offsets API from Apache Kafka — 1 operation(s) for offsets.
  name: Apache Kafka Offsets API
  slug: apache-kafka-offsets-api
- description: The Partition API from Apache Kafka — 1 operation(s) for partition.
  name: Apache Kafka Partition API
  slug: apache-kafka-partition-api
- description: The Plugins API from Apache Kafka — 2 operation(s) for plugins.
  name: Apache Kafka Plugins API
  slug: apache-kafka-plugins-api
- description: The Records API from Apache Kafka — 1 operation(s) for records.
  name: Apache Kafka Records API
  slug: apache-kafka-records-api
- description: The Tasks API from Apache Kafka — 3 operation(s) for tasks.
  name: Apache Kafka Tasks API
  slug: apache-kafka-tasks-api
- description: The Topic API from Apache Kafka — 2 operation(s) for topic.
  name: Apache Kafka Topic API
  slug: apache-kafka-topic-api
arazzos:
- description: Read the current config, validate the replacement, apply it, restart, and confirm.
  name: Apache Kafka Update a Connector Configuration
  slug: apache-kafka-connector-config-update-workflow
- description: Capture a connector's config and offsets, stop it cleanly, delete it, and verify it is gone.
  name: Apache Kafka Decommission a Connector
  slug: apache-kafka-connector-decommission-workflow
- description: Find the connector, read its status, drill into the failing task, and restart what is broken.
  name: Apache Kafka Triage a Failed Connector
  slug: apache-kafka-connector-health-triage-workflow
- description: Pause a connector for a maintenance window, confirm it stopped, then resume it and confirm recovery.
  name: Apache Kafka Pause and Resume a Connector for Maintenance
  slug: apache-kafka-connector-maintenance-pause-resume-workflow
- description: Stop a connector, snapshot its offsets, wipe them entirely, and resume from a clean slate.
  name: Apache Kafka Reset Connector Offsets
  slug: apache-kafka-connector-offset-reset-workflow
- description: Stop a connector, capture its offsets, rewind them to a chosen position, and resume.
  name: Apache Kafka Rewind Connector Offsets
  slug: apache-kafka-connector-offset-rewind-workflow
- description: Check the worker, confirm the plugin is installed, validate the config, then create the connector.
  name: Apache Kafka Validate and Deploy a Connector
  slug: apache-kafka-connector-validate-deploy-workflow
- description: Resolve the cluster, list the consumer groups, and pull the lag summary and assignment for one group.
  name: Apache Kafka Review Consumer Group Lag
  slug: apache-kafka-consumer-group-lag-review-workflow
- description: Resolve the cluster, confirm the topic, audit existing ACLs, grant read access, and verify the grant.
  name: Apache Kafka Grant a Principal Access to a Topic
  slug: apache-kafka-topic-acl-grant-workflow
- description: Walk a cluster from brokers to topics to the partition and replica layout of one topic.
  name: Apache Kafka Review Cluster and Topic Capacity
  slug: apache-kafka-topic-capacity-review-workflow
- description: Confirm the topic, check for active consumer groups and bound ACLs, then delete it.
  name: Apache Kafka Decommission a Topic
  slug: apache-kafka-topic-decommission-workflow
- description: Resolve the cluster, create a topic with explicit partitioning, read it back, and produce a first record.
  name: Apache Kafka Provision a Topic and Produce a Record
  slug: apache-kafka-topic-provision-produce-workflow
artifact_total: 125
asyncapis:
- description: 'Apache Kafka is a distributed event streaming platform capable of handling trillions of events a day. This spec describes the core messaging protocol for producing and consuming records to/from Kafka '
  name: Apache Kafka Messaging API
  slug: kafka-messaging
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kafka Connect REST ACL API
  slug: open-apache-kafka-acl-api
- collection_type: open
  name: Kafka Connect REST ACL Broker API
  slug: open-apache-kafka-broker-api
- collection_type: open
  name: Kafka Connect REST ACL Cluster API
  slug: open-apache-kafka-cluster-api
- collection_type: open
  name: Kafka Connect REST ACL Connectors API
  slug: open-apache-kafka-connectors-api
- collection_type: open
  name: Kafka Connect REST ACL Consumer Group API
  slug: open-apache-kafka-consumer-group-api
- collection_type: open
  name: Kafka Connect REST ACL Offsets API
  slug: open-apache-kafka-offsets-api
- collection_type: open
  name: Kafka Connect REST ACL Partition API
  slug: open-apache-kafka-partition-api
- collection_type: open
  name: Kafka Connect REST ACL Plugins API
  slug: open-apache-kafka-plugins-api
- collection_type: open
  name: Kafka Connect REST ACL Records API
  slug: open-apache-kafka-records-api
- collection_type: open
  name: Kafka Connect REST ACL Tasks API
  slug: open-apache-kafka-tasks-api
- collection_type: open
  name: Kafka Connect REST ACL Topic API
  slug: open-apache-kafka-topic-api
- collection_type: open
  name: Kafka Connect REST API
  slug: open-kafka-connect
- collection_type: open
  name: Confluent Kafka REST Proxy API
  slug: open-kafka-rest-proxy
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/apache-kafka-kafka-connect-overlay.yaml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/kafka/blob/trunk/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/kafka/blob/trunk/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/kafka/blob/trunk/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-kafka-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/apache-kafka-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/apache-kafka-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apache-kafka-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apache-kafka-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/apache-kafka-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/apache-kafka-security.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apache-kafka-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apache-kafka-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apache-kafka-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apache-kafka-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apache-kafka-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apache-kafka-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-kafka-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-kafka-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apachekafka
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/kafka
- group: docs
  title: ''
  type: Documentation
  url: https://kafka.apache.org/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://kafka.apache.org/quickstart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: Versioning
  url: https://kafka.apache.org/downloads
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-kafka-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-kafka-vocabulary.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-connector-validate-deploy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-connector-health-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-connector-config-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-connector-maintenance-pause-resume-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-connector-offset-rewind-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-connector-offset-reset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-connector-decommission-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-topic-provision-produce-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-topic-capacity-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-consumer-group-lag-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-topic-acl-grant-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-kafka-topic-decommission-workflow.yml
- group: company
  title: ''
  type: Blog
  url: https://www.confluent.io/rss.xml
created: '2025-06-05'
description: Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications. It provides a REST Proxy API, Kafka Connect REST API, and AsyncAPI for event streaming.
examples:
- key_count: 4
  name: Kafka Connect Config Validation Result Example
  slug: kafka-connect-config-validation-result-example
- key_count: 4
  name: Kafka Connect Connector Info Example
  slug: kafka-connect-connector-info-example
- key_count: 3
  name: Kafka Connect Connector Plugin Example
  slug: kafka-connect-connector-plugin-example
- key_count: 4
  name: Kafka Connect Connector Status Example
  slug: kafka-connect-connector-status-example
- key_count: 2
  name: Kafka Connect Create Connector Request Example
  slug: kafka-connect-create-connector-request-example
- key_count: 2
  name: Kafka Connect Task Info Example
  slug: kafka-connect-task-info-example
- key_count: 4
  name: Kafka Connect Task Status Example
  slug: kafka-connect-task-status-example
- key_count: 10
  name: Kafka Rest Proxy Acl Example
  slug: kafka-rest-proxy-acl-example
- key_count: 6
  name: Kafka Rest Proxy Broker Example
  slug: kafka-rest-proxy-broker-example
- key_count: 6
  name: Kafka Rest Proxy Cluster Example
  slug: kafka-rest-proxy-cluster-example
- key_count: 10
  name: Kafka Rest Proxy Consumer Group Example
  slug: kafka-rest-proxy-consumer-group-example
- key_count: 7
  name: Kafka Rest Proxy Create Acl Request Example
  slug: kafka-rest-proxy-create-acl-request-example
- key_count: 4
  name: Kafka Rest Proxy Create Topic Request Example
  slug: kafka-rest-proxy-create-topic-request-example
- key_count: 7
  name: Kafka Rest Proxy Partition Example
  slug: kafka-rest-proxy-partition-example
- key_count: 4
  name: Kafka Rest Proxy Produce Request Example
  slug: kafka-rest-proxy-produce-request-example
- key_count: 6
  name: Kafka Rest Proxy Produce Response Example
  slug: kafka-rest-proxy-produce-response-example
- key_count: 9
  name: Kafka Rest Proxy Topic Example
  slug: kafka-rest-proxy-topic-example
features:
- description: Handle millions of messages per second with low latency at massive scale.
  name: High Throughput
- description: Guarantee exactly-once message delivery with idempotent producers and transactional APIs.
  name: Exactly-Once Semantics
- description: Automatic replication across brokers for fault tolerance and high availability.
  name: Distributed Replication
- description: Real-time stream processing via Kafka Streams library and KSQL.
  name: Stream Processing
- description: 200+ pre-built Kafka Connect connectors for databases, clouds, and SaaS.
  name: Connector Ecosystem
- description: Retain the latest value for each key with topic log compaction.
  name: Log Compaction
- description: Horizontally scalable consumers with automatic partition rebalancing.
  name: Consumer Groups
finops:
- name: Apache Kafka Finops
  service_category: API
  slug: apache-kafka-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-kafka.png
integrations:
- description: Spark Structured Streaming integration for batch and streaming analytics.
  name: Apache Spark
- description: Native Flink Kafka connector for low-latency stream processing.
  name: Apache Flink
- description: CDC platform using Kafka Connect to capture database change events.
  name: Debezium
- description: Kafka Connect Elasticsearch sink for indexing event data.
  name: Elasticsearch
- description: Kafka Connect S3 sink for archiving event streams to object storage.
  name: Amazon S3
- description: HDFS sink connector for streaming data into Hadoop data lake.
  name: Apache Hadoop
json_schemas:
- name: ConfigValidationResult
  property_count: 4
  slug: kafka-connect-config-validation-result
- name: ConnectorInfo
  property_count: 4
  slug: kafka-connect-connector-info
- name: ConnectorPlugin
  property_count: 3
  slug: kafka-connect-connector-plugin
- name: ConnectorStatus
  property_count: 4
  slug: kafka-connect-connector-status
- name: CreateConnectorRequest
  property_count: 2
  slug: kafka-connect-create-connector-request
- name: TaskInfo
  property_count: 2
  slug: kafka-connect-task-info
- name: TaskStatus
  property_count: 4
  slug: kafka-connect-task-status
- name: Kafka Record
  property_count: 8
  slug: kafka-record
- name: Acl
  property_count: 10
  slug: kafka-rest-proxy-acl
- name: Broker
  property_count: 6
  slug: kafka-rest-proxy-broker
- name: Cluster
  property_count: 6
  slug: kafka-rest-proxy-cluster
- name: ConsumerGroup
  property_count: 10
  slug: kafka-rest-proxy-consumer-group
- name: CreateAclRequest
  property_count: 7
  slug: kafka-rest-proxy-create-acl-request
- name: CreateTopicRequest
  property_count: 4
  slug: kafka-rest-proxy-create-topic-request
- name: Partition
  property_count: 7
  slug: kafka-rest-proxy-partition
- name: ProduceRequest
  property_count: 4
  slug: kafka-rest-proxy-produce-request
- name: ProduceResponse
  property_count: 6
  slug: kafka-rest-proxy-produce-response
- name: Topic
  property_count: 9
  slug: kafka-rest-proxy-topic
- name: Kafka Topic Configuration
  property_count: 4
  slug: kafka-topic-config
json_structures:
- name: Kafka Connect Config Validation Result Structure
  property_count: 4
  slug: kafka-connect-config-validation-result-structure
- name: Kafka Connect Connector Info Structure
  property_count: 4
  slug: kafka-connect-connector-info-structure
- name: Kafka Connect Connector Plugin Structure
  property_count: 3
  slug: kafka-connect-connector-plugin-structure
- name: Kafka Connect Connector Status Structure
  property_count: 4
  slug: kafka-connect-connector-status-structure
- name: Kafka Connect Create Connector Request Structure
  property_count: 2
  slug: kafka-connect-create-connector-request-structure
- name: Kafka Connect Task Info Structure
  property_count: 2
  slug: kafka-connect-task-info-structure
- name: Kafka Connect Task Status Structure
  property_count: 4
  slug: kafka-connect-task-status-structure
- name: Kafka Rest Proxy Acl Structure
  property_count: 10
  slug: kafka-rest-proxy-acl-structure
- name: Kafka Rest Proxy Broker Structure
  property_count: 6
  slug: kafka-rest-proxy-broker-structure
- name: Kafka Rest Proxy Cluster Structure
  property_count: 6
  slug: kafka-rest-proxy-cluster-structure
- name: Kafka Rest Proxy Consumer Group Structure
  property_count: 10
  slug: kafka-rest-proxy-consumer-group-structure
- name: Kafka Rest Proxy Create Acl Request Structure
  property_count: 7
  slug: kafka-rest-proxy-create-acl-request-structure
- name: Kafka Rest Proxy Create Topic Request Structure
  property_count: 4
  slug: kafka-rest-proxy-create-topic-request-structure
- name: Kafka Rest Proxy Partition Structure
  property_count: 7
  slug: kafka-rest-proxy-partition-structure
- name: Kafka Rest Proxy Produce Request Structure
  property_count: 4
  slug: kafka-rest-proxy-produce-request-structure
- name: Kafka Rest Proxy Produce Response Structure
  property_count: 6
  slug: kafka-rest-proxy-produce-response-structure
- name: Kafka Rest Proxy Topic Structure
  property_count: 9
  slug: kafka-rest-proxy-topic-structure
jsonld:
- class_count: 2
  name: Apache Kafka Kafka Connect Config Context
  property_count: 3
  slug: apache-kafka-kafka-connect-config-context
- class_count: 5
  name: Apache Kafka Kafka Connect Connector Context
  property_count: 7
  slug: apache-kafka-kafka-connect-connector-context
- class_count: 2
  name: Apache Kafka Kafka Connect Create Context
  property_count: 1
  slug: apache-kafka-kafka-connect-create-context
- class_count: 2
  name: Apache Kafka Kafka Connect Task Context
  property_count: 7
  slug: apache-kafka-kafka-connect-task-context
- class_count: 10
  name: Apache Kafka Kafka Rest Proxy Context
  property_count: 41
  slug: apache-kafka-kafka-rest-proxy-context
layout: provider
mcp_servers:
- description: ''
  name: Apache Kafka MCP Server
  slug: apache-kafka-mcp-server
modified: '2026-06-20'
name: Apache Kafka
nav: Providers
network: true
overview: 'Apache Kafka publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Messaging API, ACL API, Broker API, and 9 more. Tagged areas include Distributed Systems, Event Streaming, Messaging, Open-Source, and Pub-Sub.


  The Apache Kafka catalog on APIs.io includes 1 event-driven AsyncAPI specification, 5 JSON-LD contexts, and 3 Spectral governance rulesets.


  Apache Kafka''s developer surface includes CLI, changelog, documentation, getting-started guide, engineering blog, and 37 more developer resources.'
plans:
- name: Apache Kafka Plans Pricing
  plan_count: 3
  slug: apache-kafka-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Apache Kafka Rate Limits
  slug: apache-kafka-rate-limits
rules:
- effective_rule_count: 29
  extends:
  - spectral:asyncapi
  name: Apache Kafka API Rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 1
  slug: apache-kafka-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Apache Kafka API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: apache-kafka-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: Apache Kafka API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 5
    warn: 6
  slug: apache-kafka-spectral-rules
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 29
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 33.3
    contract_quality: 57.2
    developer_ergonomics: 31.0
    discoverability: 66.7
    governance: 33.3
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 75.0
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-kafka/refs/heads/main/screenshots/apache-kafka-2026-06-20T172115.png
security:
- kind: domain-security
  name: Apache Kafka Domain Security
  slug: apache-kafka-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Kafka Vulnerability Disclosure
  slug: apache-kafka-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-kafka
tags:
- Distributed Systems
- Event Streaming
- Messaging
- Open-Source
- Pub-Sub
use_cases:
- description: Build event-driven microservices with reliable message delivery.
  name: Event-Driven Architecture
- description: Move data between systems at scale with exactly-once delivery guarantees.
  name: Data Pipeline
- description: Process and analyze event streams in real time with Kafka Streams.
  name: Real-Time Analytics
- description: Centralize application and infrastructure logs for analysis and alerting.
  name: Log Aggregation
- description: Capture database changes and stream them to data warehouses and caches.
  name: CDC (Change Data Capture)
---
