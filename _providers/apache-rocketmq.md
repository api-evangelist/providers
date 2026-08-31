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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Apache Rocketmq Agentic Access
  operation_count: 10
  slug: apache-rocketmq-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- description: The Brokers API from Apache RocketMQ — 1 operation(s) for brokers.
  name: Apache RocketMQ Brokers API
  slug: apache-rocketmq-brokers-api
- description: The ConsumerGroups API from Apache RocketMQ — 1 operation(s) for consumergroups.
  name: Apache RocketMQ ConsumerGroups API
  slug: apache-rocketmq-consumergroups-api
- description: The Messages API from Apache RocketMQ — 3 operation(s) for messages.
  name: Apache RocketMQ Messages API
  slug: apache-rocketmq-messages-api
- description: The Topics API from Apache RocketMQ — 2 operation(s) for topics.
  name: Apache RocketMQ Topics API
  slug: apache-rocketmq-topics-api
artifact_total: 75
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache RocketMQ REST Brokers API
  slug: open-apache-rocketmq-brokers-api
- collection_type: open
  name: Apache RocketMQ REST Brokers ConsumerGroups API
  slug: open-apache-rocketmq-consumergroups-api
- collection_type: open
  name: Apache RocketMQ REST Brokers Messages API
  slug: open-apache-rocketmq-messages-api
- collection_type: open
  name: Apache RocketMQ REST Brokers Topics API
  slug: open-apache-rocketmq-topics-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-rocketmq-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-rocketmq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-rocketmq-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/rocketmq
- group: docs
  title: ''
  type: Documentation
  url: https://rocketmq.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-rocketmq-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-rocketmq-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-rocketmq-context.jsonld
created: '2026-03-16'
description: Apache RocketMQ is a distributed messaging and streaming platform with low latency, high performance, and reliability. It provides trillion-level message capacity with rich message types including normal, transactional, delayed, and ordered messages.
examples:
- key_count: 3
  name: Apache Rocketmq Ack Request Example
  slug: apache-rocketmq-ack-request-example
- key_count: 5
  name: Apache Rocketmq Broker Example
  slug: apache-rocketmq-broker-example
- key_count: 1
  name: Apache Rocketmq Broker List Example
  slug: apache-rocketmq-broker-list-example
- key_count: 4
  name: Apache Rocketmq Consumer Group Example
  slug: apache-rocketmq-consumer-group-example
- key_count: 2
  name: Apache Rocketmq Consumer Group List Example
  slug: apache-rocketmq-consumer-group-list-example
- key_count: 3
  name: Apache Rocketmq Consumer Group Request Example
  slug: apache-rocketmq-consumer-group-request-example
- key_count: 8
  name: Apache Rocketmq Message Example
  slug: apache-rocketmq-message-example
- key_count: 6
  name: Apache Rocketmq Message Request Example
  slug: apache-rocketmq-message-request-example
- key_count: 4
  name: Apache Rocketmq Receive Request Example
  slug: apache-rocketmq-receive-request-example
- key_count: 1
  name: Apache Rocketmq Receive Result Example
  slug: apache-rocketmq-receive-result-example
- key_count: 5
  name: Apache Rocketmq Send Result Example
  slug: apache-rocketmq-send-result-example
- key_count: 5
  name: Apache Rocketmq Topic Example
  slug: apache-rocketmq-topic-example
- key_count: 2
  name: Apache Rocketmq Topic List Example
  slug: apache-rocketmq-topic-list-example
- key_count: 4
  name: Apache Rocketmq Topic Request Example
  slug: apache-rocketmq-topic-request-example
features:
- description: Billion-level message throughput with low latency
  name: High Throughput
- description: Normal, ordered, delayed, transactional, and batch messages
  name: Multiple Message Types
- description: Server-side tag and SQL expression filtering
  name: Message Filtering
- description: Transactional messages for exactly-once delivery
  name: Exactly-Once Semantics
- description: Schedule messages with configurable delay levels
  name: Delayed Messages
- description: Automatic dead letter queue for failed messages
  name: Dead Letter Queue
- description: End-to-end message tracing for debugging and monitoring
  name: Message Tracing
finops:
- name: Apache Rocketmq Finops
  service_category: API
  slug: apache-rocketmq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-rocketmq.png
integrations:
- description: RocketMQ Spring Boot starter for easy integration
  name: Spring Boot
- description: Flink connector for stream processing from RocketMQ
  name: Apache Flink
- description: Spark Streaming connector for RocketMQ
  name: Apache Spark
- description: RocketMQ Operator for Kubernetes-native deployment
  name: Kubernetes
json_schemas:
- name: AckRequest
  property_count: 3
  slug: apache-rocketmq-ack-request
- name: BrokerList
  property_count: 1
  slug: apache-rocketmq-broker-list
- name: Broker
  property_count: 5
  slug: apache-rocketmq-broker
- name: ConsumerGroupList
  property_count: 2
  slug: apache-rocketmq-consumer-group-list
- name: ConsumerGroupRequest
  property_count: 3
  slug: apache-rocketmq-consumer-group-request
- name: ConsumerGroup
  property_count: 4
  slug: apache-rocketmq-consumer-group
- name: MessageRequest
  property_count: 6
  slug: apache-rocketmq-message-request
- name: Message
  property_count: 8
  slug: apache-rocketmq-message
- name: ReceiveRequest
  property_count: 4
  slug: apache-rocketmq-receive-request
- name: ReceiveResult
  property_count: 1
  slug: apache-rocketmq-receive-result
- name: SendResult
  property_count: 5
  slug: apache-rocketmq-send-result
- name: TopicList
  property_count: 2
  slug: apache-rocketmq-topic-list
- name: TopicRequest
  property_count: 4
  slug: apache-rocketmq-topic-request
- name: Topic
  property_count: 5
  slug: apache-rocketmq-topic
json_structures:
- name: Apache Rocketmq Ack Request Structure
  property_count: 3
  slug: apache-rocketmq-ack-request-structure
- name: Apache Rocketmq Broker List Structure
  property_count: 1
  slug: apache-rocketmq-broker-list-structure
- name: Apache Rocketmq Broker Structure
  property_count: 5
  slug: apache-rocketmq-broker-structure
- name: Apache Rocketmq Consumer Group List Structure
  property_count: 2
  slug: apache-rocketmq-consumer-group-list-structure
- name: Apache Rocketmq Consumer Group Request Structure
  property_count: 3
  slug: apache-rocketmq-consumer-group-request-structure
- name: Apache Rocketmq Consumer Group Structure
  property_count: 4
  slug: apache-rocketmq-consumer-group-structure
- name: Apache Rocketmq Message Request Structure
  property_count: 6
  slug: apache-rocketmq-message-request-structure
- name: Apache Rocketmq Message Structure
  property_count: 8
  slug: apache-rocketmq-message-structure
- name: Apache Rocketmq Receive Request Structure
  property_count: 4
  slug: apache-rocketmq-receive-request-structure
- name: Apache Rocketmq Receive Result Structure
  property_count: 1
  slug: apache-rocketmq-receive-result-structure
- name: Apache Rocketmq Send Result Structure
  property_count: 5
  slug: apache-rocketmq-send-result-structure
- name: Apache Rocketmq Topic List Structure
  property_count: 2
  slug: apache-rocketmq-topic-list-structure
- name: Apache Rocketmq Topic Request Structure
  property_count: 4
  slug: apache-rocketmq-topic-request-structure
- name: Apache Rocketmq Topic Structure
  property_count: 5
  slug: apache-rocketmq-topic-structure
jsonld:
- class_count: 14
  name: Apache Rocketmq Context
  property_count: 34
  slug: apache-rocketmq-context
layout: provider
modified: '2026-05-19'
name: Apache RocketMQ
nav: Providers
network: true
overview: 'Apache RocketMQ publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Brokers API, ConsumerGroups API, Messages API, and 1 more. Tagged areas include Cloud-Native, Messaging, Message Queue, Pub-Sub, and Streaming.


  The Apache RocketMQ catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache RocketMQ''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Apache Rocketmq Plans Pricing
  plan_count: 3
  slug: apache-rocketmq-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Apache Rocketmq Rate Limits
  slug: apache-rocketmq-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache RocketMQ API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-rocketmq-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Apache RocketMQ API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 6
  slug: apache-rocketmq-spectral-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 52.9
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-rocketmq/refs/heads/main/screenshots/apache-rocketmq-2026-06-20T172138.png
security:
- kind: domain-security
  name: Apache Rocketmq Domain Security
  slug: apache-rocketmq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Rocketmq Vulnerability Disclosure
  slug: apache-rocketmq-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-rocketmq
tags:
- Cloud-Native
- Messaging
- Message Queue
- Pub-Sub
- Streaming
- Apache
- Open-Source
use_cases:
- description: Ensure ordered processing of e-commerce order events
  name: Order Processing
- description: Decouple microservices with reliable asynchronous messaging
  name: Event-Driven Microservices
- description: Aggregate application logs from distributed services
  name: Log Aggregation
- description: Reliable transactional messaging for financial systems
  name: Financial Transactions
---
