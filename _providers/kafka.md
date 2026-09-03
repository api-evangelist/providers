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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.5
  scored_at: '2026-09-03'
api_count: 5
apis:
- description: API for publishing streams of records to Kafka topics.
  name: Kafka Producer API
  slug: producer-api
- description: API for subscribing to topics and processing streams of records.
  name: Kafka Consumer API
  slug: consumer-api
- description: API for building stream processing applications and microservices on top of Kafka.
  name: Kafka Streams API
  slug: streams-api
- description: REST API for integrating Kafka with external systems through connectors.
  name: Kafka Connect REST API
  slug: connect-api
- description: API for managing and inspecting topics, brokers, configurations, and ACLs.
  name: Kafka Admin API
  slug: admin-api
artifact_total: 12
asyncapis:
- description: 'Generic AsyncAPI 2.6 reference template for Apache Kafka. Apache Kafka is a distributed event streaming platform where producers publish records to topics partitioned across a cluster of brokers, and '
  name: Apache Kafka
  slug: kafka-asyncapi
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kafka-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kafka-domain-security.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/kafka/refs/heads/main/asyncapi/kafka-asyncapi.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apachekafka
- group: company
  title: ''
  type: Website
  url: https://kafka.apache.org
- group: docs
  title: ''
  type: Documentation
  url: https://kafka.apache.org/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://kafka.apache.org/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/kafka
- group: company
  title: ''
  type: Blog
  url: https://kafka.apache.org/blog
- group: operate
  title: ''
  type: Community
  url: https://kafka.apache.org/contact
created: '2024-01-01'
description: Apache Kafka is a distributed event streaming platform for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications. It provides high-throughput, fault-tolerant, publish-subscribe messaging.
finops:
- name: Kafka Finops
  service_category: API
  slug: kafka-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kafka.png
layout: provider
modified: '2026-05-30'
name: Apache Kafka
nav: Providers
network: true
overview: 'Apache Kafka publishes 2 APIs on the [APIs.io](https://apis.io/) network: Kafka Producer API and Kafka Consumer API. Tagged areas include Distributed Systems, Event-Driven, Messaging, Real-Time, and Streaming.


  The Apache Kafka catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Apache Kafka''s developer surface includes documentation, getting-started guide, engineering blog, and 7 more developer resources.'
plans:
- name: Kafka Plans Pricing
  plan_count: 3
  slug: kafka-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Kafka Rate Limits
  slug: kafka-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Apache Kafka API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: kafka-asyncapi-spectral-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 66.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 45.8
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 29.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kafka/refs/heads/main/screenshots/kafka-2026-06-20T183849.png
security:
- kind: domain-security
  name: Kafka Domain Security
  slug: kafka-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kafka Vulnerability Disclosure
  slug: kafka-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kafka
tags:
- Distributed Systems
- Event-Driven
- Messaging
- Real-Time
- Streaming
website: https://kafka.apache.org
---
