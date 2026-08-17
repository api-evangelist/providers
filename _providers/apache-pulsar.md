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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Apache Pulsar Agentic Access
  operation_count: 29
  slug: apache-pulsar-agentic-access
  summary_line: 29 operations · 13 acting
api_count: 8
apis:
- description: Pulsar messaging protocol for producing and consuming messages on topics, with support for multiple subscription types (Exclusive, Shared, Failover, Key_Shared), schema enforcement, and both persisten
  name: Apache Pulsar Messaging API
  slug: apache-pulsar-messaging-api
- description: The Brokers API from Apache Pulsar — 2 operation(s) for brokers.
  name: Apache Pulsar Brokers API
  slug: apache-pulsar-brokers-api
- description: The Clusters API from Apache Pulsar — 2 operation(s) for clusters.
  name: Apache Pulsar Clusters API
  slug: apache-pulsar-clusters-api
- description: The Functions API from Apache Pulsar — 3 operation(s) for functions.
  name: Apache Pulsar Functions API
  slug: apache-pulsar-functions-api
- description: The Namespaces API from Apache Pulsar — 3 operation(s) for namespaces.
  name: Apache Pulsar Namespaces API
  slug: apache-pulsar-namespaces-api
- description: The Subscriptions API from Apache Pulsar — 2 operation(s) for subscriptions.
  name: Apache Pulsar Subscriptions API
  slug: apache-pulsar-subscriptions-api
- description: The Tenants API from Apache Pulsar — 2 operation(s) for tenants.
  name: Apache Pulsar Tenants API
  slug: apache-pulsar-tenants-api
- description: The Topics API from Apache Pulsar — 4 operation(s) for topics.
  name: Apache Pulsar Topics API
  slug: apache-pulsar-topics-api
artifact_total: 61
asyncapis:
- description: 'Apache Pulsar is a cloud-native, multi-tenant, high-performance messaging and streaming platform. This spec describes the messaging patterns for producing and consuming messages on Pulsar topics with '
  name: Apache Pulsar Messaging API
  slug: pulsar-messaging
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Pulsar Admin REST Brokers API
  slug: open-apache-pulsar-brokers-api
- collection_type: open
  name: Apache Pulsar Admin REST Brokers Clusters API
  slug: open-apache-pulsar-clusters-api
- collection_type: open
  name: Apache Pulsar Admin REST Brokers Functions API
  slug: open-apache-pulsar-functions-api
- collection_type: open
  name: Apache Pulsar Admin REST Brokers Namespaces API
  slug: open-apache-pulsar-namespaces-api
- collection_type: open
  name: Apache Pulsar Admin REST Brokers Subscriptions API
  slug: open-apache-pulsar-subscriptions-api
- collection_type: open
  name: Apache Pulsar Admin REST Brokers Tenants API
  slug: open-apache-pulsar-tenants-api
- collection_type: open
  name: Apache Pulsar Admin REST Brokers Topics API
  slug: open-apache-pulsar-topics-api
- collection_type: open
  name: Apache Pulsar Admin REST API
  slug: open-pulsar-admin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-pulsar-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-pulsar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-pulsar-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/pulsar
- group: docs
  title: ''
  type: Documentation
  url: https://pulsar.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-pulsar-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-pulsar-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-pulsar-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://pulsar.apache.org/blog/rss.xml
created: '2026-03-16'
description: Apache Pulsar is a cloud-native, distributed messaging and streaming platform that provides server-to-server messaging with multi-tenancy, high performance, and geo-replication. It combines messaging and stream processing in a single platform.
examples:
- key_count: 5
  name: Apache Pulsar Cluster Data Example
  slug: apache-pulsar-cluster-data-example
- key_count: 12
  name: Apache Pulsar Function Config Example
  slug: apache-pulsar-function-config-example
- key_count: 9
  name: Apache Pulsar Policies Example
  slug: apache-pulsar-policies-example
- key_count: 12
  name: Apache Pulsar Pulsar Message Example
  slug: apache-pulsar-pulsar-message-example
- key_count: 2
  name: Apache Pulsar Retention Policies Example
  slug: apache-pulsar-retention-policies-example
- key_count: 2
  name: Apache Pulsar Tenant Info Example
  slug: apache-pulsar-tenant-info-example
- key_count: 9
  name: Apache Pulsar Topic Stats Example
  slug: apache-pulsar-topic-stats-example
features:
- description: Native multi-tenancy with tenant and namespace isolation
  name: Multi-Tenancy
- description: Durable message storage with Apache BookKeeper
  name: Persistent Messaging
- description: Built-in geo-replication across data centers and clouds
  name: Geo-Replication
- description: Lightweight serverless compute natively integrated with messaging
  name: Pulsar Functions
- description: Offload old data to object storage (S3, GCS) for cost efficiency
  name: Tiered Storage
- description: Built-in schema registry for producers and consumers
  name: Schema Registry
- description: Exclusive, Shared, Failover, and Key_Shared subscription modes
  name: Multiple Subscription Types
finops:
- name: Apache Pulsar Finops
  service_category: API
  slug: apache-pulsar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-pulsar.png
json_schemas:
- name: ClusterData
  property_count: 5
  slug: apache-pulsar-cluster-data
- name: FunctionConfig
  property_count: 12
  slug: apache-pulsar-function-config
- name: Policies
  property_count: 9
  slug: apache-pulsar-policies
- name: PulsarMessage
  property_count: 12
  slug: apache-pulsar-pulsar-message
- name: RetentionPolicies
  property_count: 2
  slug: apache-pulsar-retention-policies
- name: TenantInfo
  property_count: 2
  slug: apache-pulsar-tenant-info
- name: TopicStats
  property_count: 9
  slug: apache-pulsar-topic-stats
- name: Apache Pulsar Message
  property_count: 12
  slug: pulsar-message
json_structures:
- name: Apache Pulsar Cluster Data Structure
  property_count: 5
  slug: apache-pulsar-cluster-data-structure
- name: Apache Pulsar Function Config Structure
  property_count: 12
  slug: apache-pulsar-function-config-structure
- name: Apache Pulsar Policies Structure
  property_count: 9
  slug: apache-pulsar-policies-structure
- name: Apache Pulsar Pulsar Message Structure
  property_count: 12
  slug: apache-pulsar-pulsar-message-structure
- name: Apache Pulsar Retention Policies Structure
  property_count: 2
  slug: apache-pulsar-retention-policies-structure
- name: Apache Pulsar Tenant Info Structure
  property_count: 2
  slug: apache-pulsar-tenant-info-structure
- name: Apache Pulsar Topic Stats Structure
  property_count: 9
  slug: apache-pulsar-topic-stats-structure
jsonld:
- class_count: 7
  name: Apache Pulsar Context
  property_count: 51
  slug: apache-pulsar-context
layout: provider
modified: '2026-05-19'
name: Apache Pulsar
nav: Providers
network: true
overview: 'Apache Pulsar publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Messaging API, Brokers API, Clusters API, and 5 more. Tagged areas include Cloud Native, Messaging, Multi-Tenant, Pub-Sub, and Streaming.


  The Apache Pulsar catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Apache Pulsar''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Apache Pulsar Plans Pricing
  plan_count: 3
  slug: apache-pulsar-plans-pricing
random_paper: 126
rate_limits:
- limit_count: 5
  name: Apache Pulsar Rate Limits
  slug: apache-pulsar-rate-limits
rules:
- name: Apache Pulsar API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 3
  slug: apache-pulsar-asyncapi-spectral-rules
- name: Apache Pulsar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-pulsar-jsonschema-spectral-rules
- name: Apache Pulsar API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: apache-pulsar-spectral-rules
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 63.4
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 62.5
    operational_transparency: 13.2
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-pulsar/refs/heads/main/screenshots/apache-pulsar-2026-06-20T172138.png
security:
- kind: domain-security
  name: Apache Pulsar Domain Security
  slug: apache-pulsar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Pulsar Vulnerability Disclosure
  slug: apache-pulsar-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-pulsar
tags:
- Cloud Native
- Messaging
- Multi-Tenant
- Pub-Sub
- Streaming
- Apache
- Open Source
use_cases:
- description: Stream events between microservices with guaranteed delivery
  name: Real-Time Event Streaming
- description: Use Shared subscription as a traditional message queue
  name: Message Queue
- description: Store and replay event streams for event-driven architectures
  name: Event Sourcing
- description: Ingest high-volume IoT telemetry into Pulsar topics
  name: IoT Data Ingestion
---
