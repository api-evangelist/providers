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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nats Agentic Access
  operation_count: 10
  slug: nats-agentic-access
  summary_line: 10 operations
api_count: 15
apis:
- description: HTTP monitoring API providing real-time server status, connection information, route details, subscription statistics, JetStream metrics, and health check endpoints for observability and operations.
  name: NATS Monitoring API
  slug: nats-monitoring-api
- description: Asynchronous messaging API supporting core pub-sub, request-reply, queue groups, and JetStream persistent messaging with streams, consumers, key-value stores, and object stores.
  name: NATS Messaging API
  slug: nats-messaging-api
- description: 'The JetStream wire API provides a protocol-level management interface for configuring and operating JetStream streams, consumers, key-value buckets, and object stores. Requests are made by publishing '
  name: NATS JetStream Management API
  slug: nats-jetstream-api
- description: The NATS Key-Value Store API is a JetStream-backed abstraction that provides immediately consistent, persistent associative array semantics. Clients can create buckets, get, put, delete, and watch key
  name: NATS Key-Value Store API
  slug: nats-kv-api
- description: The NATS Object Store API is a JetStream-backed abstraction for storing and retrieving arbitrarily large binary objects using a chunking mechanism. Objects are identified by a bucket and a name, and t
  name: NATS Object Store API
  slug: nats-object-store-api
- description: The Accounts API from NATS — 1 operation(s) for accounts.
  name: NATS Accounts API
  slug: nats-accounts-api
- description: Cluster, gateway, and leaf node endpoints
  name: NATS Clustering API
  slug: nats-clustering-api
- description: The Connections API from NATS — 1 operation(s) for connections.
  name: NATS Connections API
  slug: nats-connections-api
- description: The Gateways API from NATS — 1 operation(s) for gateways.
  name: NATS Gateways API
  slug: nats-gateways-api
- description: The Health API from NATS — 1 operation(s) for health.
  name: NATS Health API
  slug: nats-health-api
- description: The JetStream API from NATS — 1 operation(s) for jetstream.
  name: NATS JetStream API
  slug: nats-jetstream-api
- description: The Leaf Nodes API from NATS — 1 operation(s) for leaf nodes.
  name: NATS Leaf Nodes API
  slug: nats-leaf-nodes-api
- description: The Routes API from NATS — 1 operation(s) for routes.
  name: NATS Routes API
  slug: nats-routes-api
- description: The Server API from NATS — 2 operation(s) for server.
  name: NATS Server API
  slug: nats-server-api
- description: The Subscriptions API from NATS — 1 operation(s) for subscriptions.
  name: NATS Subscriptions API
  slug: nats-subscriptions-api
artifact_total: 25
asyncapis:
- description: NATS provides cloud-native messaging with core pub-sub, request-reply, and queue group patterns, plus JetStream for persistent streaming with streams, consumers, key-value stores, and object stores.
  name: NATS Core and JetStream Messaging API
  slug: nats-messaging
collections:
- collection_type: open
  name: NATS Monitoring HTTP API
  slug: open-nats-monitoring
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nats-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nats-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nats.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nats.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nats.io/running-a-nats-service/introduction/installation
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/nats-io/nats-server
- group: company
  title: ''
  type: Blog
  url: https://nats.io/blog/
- group: operate
  title: ''
  type: Slack
  url: https://slack.nats.io
- group: operate
  title: ''
  type: Issues
  url: https://github.com/nats-io/nats-server/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/nats-io/nats-server/releases
- group: build
  title: ''
  type: Examples
  url: https://natsbyexample.com
- group: build
  title: ''
  type: CLI
  url: https://docs.nats.io/using-nats/nats-tools/nats_cli
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nats-io
- group: docs
  title: ''
  type: JSONSchema
  url: properties/nats-server-config-json-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: properties/nats-jetstream-config-json-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: properties/nats-kv-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: properties/nats-object-store-schema.json
- group: design
  title: ''
  type: JSONLD
  url: properties/nats-context-jsonld.json
- group: operate
  title: ''
  type: Support
  url: https://nats.io/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nats.io/privacy/
- group: operate
  title: ''
  type: Community
  url: https://nats.io/community/
- group: build
  title: ''
  type: SDKs
  url: https://docs.nats.io/using-nats/developer
- group: other
  title: ''
  type: Download
  url: https://nats.io/download/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.nats.io/llms.txt
created: '2025-01-01'
description: A high-performance, cloud-native messaging system for microservices, IoT, and edge computing. Provides pub-sub, request-reply, and queue-based messaging patterns with at-most-once and at-least-once delivery guarantees.
finops:
- name: Nats Finops
  service_category: Messaging + Streaming
  slug: nats-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nats.png
json_schemas:
- name: NATS JetStream Stream Configuration
  property_count: 19
  slug: nats-stream-config
layout: provider
modified: '2026-05-19'
name: NATS
nav: Providers
network: true
overview: 'NATS publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Monitoring API, Messaging API, JetStream Management API, and 10 more. Tagged areas include Cloud Native, IoT, Message Broker, Microservices, and Pub Sub.


  The NATS catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  NATS''s developer surface includes documentation, getting-started guide, engineering blog, changelog, code examples, CLI, support, and 17 more developer resources.'
plans:
- name: Nats Plans Pricing
  plan_count: 8
  slug: nats-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 8
  name: Nats Rate Limits
  slug: nats-rate-limits
rules:
- name: NATS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: nats-asyncapi-spectral-rules
- name: NATS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nats-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.1
    developer_ergonomics: 39.1
    discoverability: 67.5
    governance: 65.8
    operational_transparency: 52.6
  previous_composite: 53.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nats/refs/heads/main/screenshots/nats-2026-06-20T190052.png
security:
- kind: domain-security
  name: Nats Domain Security
  slug: nats-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nats
tags:
- Cloud Native
- IoT
- Message Broker
- Microservices
- Pub Sub
website: https://nats.io
---
