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
    asyncapi_events: true
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
  score: 27.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Apache Event Mesh Agentic Access
  operation_count: 10
  slug: apache-event-mesh-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 7
apis:
- description: Event-driven messaging via TCP, HTTP, and gRPC protocols. Events follow the CloudEvents specification. Supports pub-sub, request-reply, and broadcast messaging patterns.
  name: Apache EventMesh Messaging API
  slug: eventmesh-messaging-api
- description: The Client API from Apache EventMesh — 1 operation(s) for client.
  name: Apache EventMesh Client API
  slug: apache-event-mesh-client-api
- description: The Event API from Apache EventMesh — 2 operation(s) for event.
  name: Apache EventMesh Event API
  slug: apache-event-mesh-event-api
- description: The Monitoring API from Apache EventMesh — 2 operation(s) for monitoring.
  name: Apache EventMesh Monitoring API
  slug: apache-event-mesh-monitoring-api
- description: The Registry API from Apache EventMesh — 1 operation(s) for registry.
  name: Apache EventMesh Registry API
  slug: apache-event-mesh-registry-api
- description: The Subscription API from Apache EventMesh — 1 operation(s) for subscription.
  name: Apache EventMesh Subscription API
  slug: apache-event-mesh-subscription-api
- description: The Topic API from Apache EventMesh — 3 operation(s) for topic.
  name: Apache EventMesh Topic API
  slug: apache-event-mesh-topic-api
artifact_total: 47
asyncapis:
- description: Apache EventMesh provides event-driven messaging via multiple protocols including TCP, HTTP, and gRPC. Events follow the CloudEvents specification. EventMesh decouples event producers and consumers, s
  name: Apache EventMesh Messaging API
  slug: eventmesh-messaging
collections:
- collection_type: open
  name: Apache EventMesh Admin API
  slug: open-eventmesh-admin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-event-mesh-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-event-mesh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-event-mesh-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://eventmesh.apache.org/docs/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://eventmesh.apache.org/docs/instruction/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/eventmesh
- group: company
  title: ''
  type: Blog
  url: https://eventmesh.apache.org/blog
- group: operate
  title: ''
  type: Support
  url: https://eventmesh.apache.org/community
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-event-mesh-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-event-mesh-vocabulary.yaml
created: '2026-03-26'
description: Apache EventMesh is a dynamic event-driven application runtime used to decouple the application and backend middleware layer, providing a serverless platform for building distributed event-driven architectures with support for CloudEvents and multiple messaging protocols including HTTP, TCP, and gRPC.
examples:
- key_count: 2
  name: Eventmesh Admin Api Response Example
  slug: eventmesh-admin-api-response-example
- key_count: 8
  name: Eventmesh Admin Client Example
  slug: eventmesh-admin-client-example
- key_count: 10
  name: Eventmesh Admin Cloud Event Example
  slug: eventmesh-admin-cloud-event-example
- key_count: 4
  name: Eventmesh Admin Subscription Example
  slug: eventmesh-admin-subscription-example
features:
- description: Native CloudEvents specification support for standardized event envelopes across all messaging protocols.
  name: CloudEvents Support
- description: Support for HTTP, TCP, and gRPC messaging protocols enabling flexible client connectivity.
  name: Multi-Protocol Messaging
- description: Publish-subscribe messaging pattern with topic-based routing for event-driven architectures.
  name: Pub-Sub Messaging
- description: Synchronous request-reply messaging over asynchronous infrastructure for RPC-style interactions.
  name: Request-Reply Pattern
- description: Durable event storage with replay capability for reliable event delivery and audit trails.
  name: Event Store
- description: Event-driven workflow engine for coordinating distributed business processes and sagas.
  name: Workflow Orchestration
- description: Pluggable connector model supporting Kafka, RocketMQ, Pulsar, and other messaging backends.
  name: Multi-Runtime Support
finops:
- name: Apache Event Mesh Finops
  service_category: API
  slug: apache-event-mesh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-event-mesh.png
integrations:
- description: Kafka connector for event streaming with durable storage and consumer groups.
  name: Apache Kafka
- description: RocketMQ connector for high-throughput message queueing and topic management.
  name: Apache RocketMQ
- description: Pulsar connector for multi-tenant event streaming with geo-replication.
  name: Apache Pulsar
- description: Cloud-native deployment on Kubernetes with operator support for cluster management.
  name: Kubernetes
json_schemas:
- name: CloudEvents v1.0
  property_count: 10
  slug: cloudevent
- name: ApiResponse
  property_count: 2
  slug: eventmesh-admin-api-response
- name: Client
  property_count: 8
  slug: eventmesh-admin-client
- name: CloudEvent
  property_count: 10
  slug: eventmesh-admin-cloud-event
- name: Subscription
  property_count: 4
  slug: eventmesh-admin-subscription
json_structures:
- name: Eventmesh Admin Api Response Structure
  property_count: 2
  slug: eventmesh-admin-api-response-structure
- name: Eventmesh Admin Client Structure
  property_count: 8
  slug: eventmesh-admin-client-structure
- name: Eventmesh Admin Cloud Event Structure
  property_count: 10
  slug: eventmesh-admin-cloud-event-structure
- name: Eventmesh Admin Subscription Structure
  property_count: 4
  slug: eventmesh-admin-subscription-structure
jsonld:
- class_count: 5
  name: Apache Event Mesh Admin Context
  property_count: 21
  slug: apache-event-mesh-admin-context
layout: provider
modified: '2026-05-19'
name: Apache EventMesh
nav: Providers
network: true
overview: 'Apache EventMesh publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Messaging API, Client API, Event API, and 4 more. Tagged areas include Apache, CloudEvents, Event-Driven, Messaging, and Open Source.


  The Apache EventMesh catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Apache EventMesh''s developer surface includes documentation, getting-started guide, engineering blog, support, and 7 more developer resources.'
plans:
- name: Apache Event Mesh Plans Pricing
  plan_count: 3
  slug: apache-event-mesh-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Apache Event Mesh Rate Limits
  slug: apache-event-mesh-rate-limits
rules:
- name: Apache EventMesh API Rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 2
  slug: apache-event-mesh-asyncapi-spectral-rules
- name: Apache EventMesh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: apache-event-mesh-jsonschema-spectral-rules
- name: Apache EventMesh API Rules
  rule_count: 14
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 9
  slug: apache-event-mesh-spectral-rules
score:
  band: developing
  composite: 44.0
  delta: -8.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.8
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 62.5
    operational_transparency: 36.8
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-event-mesh/refs/heads/main/screenshots/apache-event-mesh-2026-06-20T172059.png
security:
- kind: domain-security
  name: Apache Event Mesh Domain Security
  slug: apache-event-mesh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Event Mesh Vulnerability Disclosure
  slug: apache-event-mesh-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-event-mesh
tags:
- Apache
- CloudEvents
- Event-Driven
- Messaging
- Open Source
- Pub-Sub
- Serverless
use_cases:
- description: Decouple microservices through asynchronous event-driven communication reducing direct service dependencies.
  name: Microservices Decoupling
- description: Build scalable event streaming pipelines with durable delivery and replay capabilities.
  name: Event Streaming Pipelines
- description: Orchestrate distributed business processes using event-driven saga and choreography patterns.
  name: Distributed Workflows
- description: Ingest and process high-volume IoT device events through standardized CloudEvents format.
  name: IoT Event Ingestion
---
