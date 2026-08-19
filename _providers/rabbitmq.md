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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Rabbitmq Agentic Access
  operation_count: 45
  slug: rabbitmq-agentic-access
  summary_line: 45 operations · 19 acting
api_count: 14
apis:
- description: AMQP 0-9-1 messaging protocol for producing and consuming messages via exchanges, queues, and bindings with support for multiple exchange types, message acknowledgment, and consumer groups.
  name: RabbitMQ AMQP Messaging API
  slug: rabbitmq-amqp-messaging-api
- description: The Bindings API from RabbitMQ — 2 operation(s) for bindings.
  name: RabbitMQ Bindings API
  slug: rabbitmq-bindings-api
- description: The Channels API from RabbitMQ — 1 operation(s) for channels.
  name: RabbitMQ Channels API
  slug: rabbitmq-channels-api
- description: The Connections API from RabbitMQ — 2 operation(s) for connections.
  name: RabbitMQ Connections API
  slug: rabbitmq-connections-api
- description: The Definitions API from RabbitMQ — 1 operation(s) for definitions.
  name: RabbitMQ Definitions API
  slug: rabbitmq-definitions-api
- description: The Exchanges API from RabbitMQ — 4 operation(s) for exchanges.
  name: RabbitMQ Exchanges API
  slug: rabbitmq-exchanges-api
- description: The Health API from RabbitMQ — 2 operation(s) for health.
  name: RabbitMQ Health API
  slug: rabbitmq-health-api
- description: The Nodes API from RabbitMQ — 2 operation(s) for nodes.
  name: RabbitMQ Nodes API
  slug: rabbitmq-nodes-api
- description: The Overview API from RabbitMQ — 2 operation(s) for overview.
  name: RabbitMQ Overview API
  slug: rabbitmq-overview-api
- description: The Permissions API from RabbitMQ — 1 operation(s) for permissions.
  name: RabbitMQ Permissions API
  slug: rabbitmq-permissions-api
- description: The Policies API from RabbitMQ — 2 operation(s) for policies.
  name: RabbitMQ Policies API
  slug: rabbitmq-policies-api
- description: The Queues API from RabbitMQ — 5 operation(s) for queues.
  name: RabbitMQ Queues API
  slug: rabbitmq-queues-api
- description: The Users API from RabbitMQ — 3 operation(s) for users.
  name: RabbitMQ Users API
  slug: rabbitmq-users-api
- description: The Virtual Hosts API from RabbitMQ — 2 operation(s) for virtual hosts.
  name: RabbitMQ Virtual Hosts API
  slug: rabbitmq-virtual-hosts-api
artifact_total: 39
asyncapis:
- description: RabbitMQ messaging via AMQP 0-9-1 protocol. Producers publish messages to exchanges which route them to queues based on bindings and routing keys. Consumers subscribe to queues to receive messages.
  name: RabbitMQ AMQP Messaging API
  slug: rabbitmq-messaging
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RabbitMQ Management HTTP Bindings API
  slug: open-rabbitmq-bindings-api
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Channels API
  slug: open-rabbitmq-channels-api
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Connections API
  slug: open-rabbitmq-connections-api
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Definitions API
  slug: open-rabbitmq-definitions-api
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Exchanges API
  slug: open-rabbitmq-exchanges-api
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Health API
  slug: open-rabbitmq-health-api
- collection_type: open
  name: RabbitMQ Management HTTP API
  slug: open-rabbitmq-management
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Nodes API
  slug: open-rabbitmq-nodes-api
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Overview API
  slug: open-rabbitmq-overview-api
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Permissions API
  slug: open-rabbitmq-permissions-api
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Policies API
  slug: open-rabbitmq-policies-api
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Queues API
  slug: open-rabbitmq-queues-api
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Users API
  slug: open-rabbitmq-users-api
- collection_type: open
  name: RabbitMQ Management HTTP Bindings Virtual Hosts API
  slug: open-rabbitmq-virtual-hosts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rabbitmq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rabbitmq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rabbitmq-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rabbitmq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rabbitmq
- group: operate
  title: ''
  type: Community
  url: https://www.rabbitmq.com/community.html
- group: operate
  title: ''
  type: Support
  url: https://www.rabbitmq.com/contact.html
- group: company
  title: ''
  type: Blog
  url: https://www.rabbitmq.com/blog/
- group: company
  title: ''
  type: Website
  url: https://www.rabbitmq.com/
created: '2024-01-01'
description: RabbitMQ is a widely deployed open source message broker. It supports multiple messaging protocols and can be deployed in distributed and federated configurations to meet high-scale, high-availability requirements.
finops:
- name: Rabbitmq Finops
  service_category: API
  slug: rabbitmq-finops
image: https://www.rabbitmq.com/img/rabbitmq-logo.svg
json_schemas:
- name: RabbitMQ Message
  property_count: 6
  slug: rabbitmq-message
layout: provider
modified: '2026-05-19'
name: RabbitMQ
nav: Providers
network: true
overview: 'RabbitMQ publishes 14 APIs on the [APIs.io](https://apis.io/) network, including AMQP Messaging API, Bindings API, Channels API, and 11 more. Tagged areas include AMQP, Distributed Systems, Event Streaming, Message Broker, and Messaging.


  The RabbitMQ catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  RabbitMQ''s developer surface includes authentication, support, engineering blog, and 6 more developer resources.'
plans:
- name: Rabbitmq Plans Pricing
  plan_count: 3
  slug: rabbitmq-plans-pricing
random_paper: 105
rate_limits:
- limit_count: 5
  name: Rabbitmq Rate Limits
  slug: rabbitmq-rate-limits
rules:
- effective_rule_count: 28
  extends:
  - spectral:asyncapi
  name: RabbitMQ API Rules
  rule_count: 1
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 1
  slug: rabbitmq-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: RabbitMQ API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: rabbitmq-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.5
  delta: -5.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 11.4
    contract_quality: 57.5
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 11.4
    operational_transparency: 10.5
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/rabbitmq/refs/heads/main/screenshots/rabbitmq-2026-06-20T192503.png
security:
- kind: authentication
  name: Rabbitmq Authentication
  slug: rabbitmq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rabbitmq Domain Security
  slug: rabbitmq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rabbitmq
tags:
- AMQP
- Distributed Systems
- Event Streaming
- Message Broker
- Messaging
- Queue
website: https://www.rabbitmq.com/
---
