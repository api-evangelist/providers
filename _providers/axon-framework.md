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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Axon Framework Agentic Access
  operation_count: 20
  slug: axon-framework-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 9
apis:
- description: The Applications API from Axon Framework — 1 operation(s) for applications.
  name: Axon Framework Applications API
  slug: axon-framework-applications-api
- description: The Cluster API from Axon Framework — 2 operation(s) for cluster.
  name: Axon Framework Cluster API
  slug: axon-framework-cluster-api
- description: The Commands API from Axon Framework — 1 operation(s) for commands.
  name: Axon Framework Commands API
  slug: axon-framework-commands-api
- description: The Contexts API from Axon Framework — 2 operation(s) for contexts.
  name: Axon Framework Contexts API
  slug: axon-framework-contexts-api
- description: The Event Processors API from Axon Framework — 3 operation(s) for event processors.
  name: Axon Framework Event Processors API
  slug: axon-framework-event-processors-api
- description: The Events API from Axon Framework — 2 operation(s) for events.
  name: Axon Framework Events API
  slug: axon-framework-events-api
- description: The Queries API from Axon Framework — 1 operation(s) for queries.
  name: Axon Framework Queries API
  slug: axon-framework-queries-api
- description: The Snapshots API from Axon Framework — 1 operation(s) for snapshots.
  name: Axon Framework Snapshots API
  slug: axon-framework-snapshots-api
- description: The Users API from Axon Framework — 2 operation(s) for users.
  name: Axon Framework Users API
  slug: axon-framework-users-api
artifact_total: 66
collections:
- collection_type: open
  name: Axon Server REST API
  slug: open-axon-server-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/axon-framework-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axon-framework-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axoniq
- group: company
  title: ''
  type: Website
  url: https://www.axoniq.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.axoniq.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.axoniq.io/axon-framework/getting-started
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/AxonFramework/AxonFramework
- group: company
  title: ''
  type: Blog
  url: https://www.axoniq.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.axoniq.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.axoniq.io/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.axoniq.io/
- group: design
  title: ''
  type: SpectralRules
  url: rules/axon-framework-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/axon-framework-vocabulary.yaml
created: '2026-03-26'
description: Axon Framework is a Java framework for building event-driven microservices using CQRS (Command Query Responsibility Segregation) and event sourcing patterns, providing the building blocks to implement scalable and maintainable distributed systems.
examples:
- key_count: 3
  name: Axon Application Example
  slug: axon-application-example
- key_count: 3
  name: Axon Clusternode Example
  slug: axon-clusternode-example
- key_count: 3
  name: Axon Commandhandler Example
  slug: axon-commandhandler-example
- key_count: 3
  name: Axon Context Example
  slug: axon-context-example
- key_count: 3
  name: Axon Createcontextrequest Example
  slug: axon-createcontextrequest-example
- key_count: 3
  name: Axon Createuserrequest Example
  slug: axon-createuserrequest-example
- key_count: 3
  name: Axon Event Example
  slug: axon-event-example
- key_count: 3
  name: Axon Eventprocessor Example
  slug: axon-eventprocessor-example
- key_count: 3
  name: Axon Queryhandler Example
  slug: axon-queryhandler-example
- key_count: 3
  name: Axon User Example
  slug: axon-user-example
features:
- description: Separate command and query models for scalable, maintainable architecture.
  name: CQRS Pattern
- description: Store application state as a sequence of events for full audit trail and time-travel debugging.
  name: Event Sourcing
- description: First-class support for DDD patterns including aggregates, sagas, and bounded contexts.
  name: Domain-Driven Design
- description: Zero-configuration event store and message router with Axon Server.
  name: Axon Server Integration
- description: Built-in routing for commands, events, and queries across distributed services.
  name: Distributed Systems Support
- description: Seamless Spring Boot auto-configuration for rapid application development.
  name: Spring Boot Integration
- description: Built-in testing fixtures for validating aggregate behavior without infrastructure.
  name: Testing Support
- description: Manage long-running business processes with durable saga state.
  name: Saga Management
finops:
- name: Axon Framework Finops
  service_category: API
  slug: axon-framework-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axon-framework.png
integrations:
- description: Auto-configuration and starter dependency for Spring Boot integration.
  name: Spring Boot
- description: Route events through Kafka as an alternative to Axon Server.
  name: Apache Kafka
- description: Route commands and events through AMQP with RabbitMQ extension.
  name: RabbitMQ
- description: Persist saga state and event-sourced entities with JPA.
  name: JPA/Hibernate
- description: Expose framework metrics via Micrometer for Prometheus and Grafana.
  name: Micrometer
json_schemas:
- name: Application
  property_count: 4
  slug: axon-application
- name: ClusterNode
  property_count: 7
  slug: axon-clusternode
- name: CommandHandler
  property_count: 3
  slug: axon-commandhandler
- name: Context
  property_count: 3
  slug: axon-context
- name: CreateContextRequest
  property_count: 3
  slug: axon-createcontextrequest
- name: CreateUserRequest
  property_count: 3
  slug: axon-createuserrequest
- name: Event
  property_count: 9
  slug: axon-event
- name: EventProcessor
  property_count: 9
  slug: axon-eventprocessor
- name: QueryHandler
  property_count: 4
  slug: axon-queryhandler
- name: User
  property_count: 2
  slug: axon-user
json_structures:
- name: Axon Application Structure
  property_count: 0
  slug: axon-application-structure
- name: Axon Clusternode Structure
  property_count: 0
  slug: axon-clusternode-structure
- name: Axon Commandhandler Structure
  property_count: 0
  slug: axon-commandhandler-structure
- name: Axon Context Structure
  property_count: 0
  slug: axon-context-structure
- name: Axon Createcontextrequest Structure
  property_count: 0
  slug: axon-createcontextrequest-structure
- name: Axon Createuserrequest Structure
  property_count: 0
  slug: axon-createuserrequest-structure
- name: Axon Event Structure
  property_count: 0
  slug: axon-event-structure
- name: Axon Eventprocessor Structure
  property_count: 0
  slug: axon-eventprocessor-structure
- name: Axon Queryhandler Structure
  property_count: 0
  slug: axon-queryhandler-structure
- name: Axon User Structure
  property_count: 0
  slug: axon-user-structure
jsonld:
- class_count: 10
  name: Axon Framework Context
  property_count: 0
  slug: axon-framework-context
layout: provider
modified: '2026-04-19'
name: Axon Framework
nav: Providers
network: true
overview: 'Axon Framework publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Cluster API, Commands API, and 6 more. Tagged areas include CQRS, Event Sourcing, Event-Driven, Java, and Messaging.


  The Axon Framework catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Axon Framework''s developer surface includes documentation, getting-started guide, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Axon Framework Plans Pricing
  plan_count: 3
  slug: axon-framework-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Axon Framework Rate Limits
  slug: axon-framework-rate-limits
rules:
- name: Axon Framework API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: axon-framework-jsonschema-spectral-rules
- name: Axon Framework API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 6
  slug: axon-framework-spectral-rules
score:
  band: developing
  composite: 54.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.5
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 47.4
  previous_composite: 54.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axon-framework/refs/heads/main/screenshots/axon-framework-2026-06-20T172816.png
security:
- kind: domain-security
  name: Axon Framework Domain Security
  slug: axon-framework-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: axon-framework
tags:
- CQRS
- Event Sourcing
- Event-Driven
- Java
- Messaging
- Microservices
use_cases:
- description: Build event-driven microservices with reliable message routing.
  name: Microservices Architecture
- description: Maintain complete audit trails by storing all state changes as events.
  name: Audit Trail
- description: Reconstruct system state at any point in time from the event store.
  name: Temporal Queries
- description: Build complex collaborative domains with CQRS separation.
  name: Collaborative Domains
- description: Automate multi-step business workflows with event-driven sagas.
  name: Workflow Automation
website: https://www.axoniq.io/
---
