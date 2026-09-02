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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Asyncapi Agentic Access
  operation_count: 7
  slug: asyncapi-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- description: The AsyncAPI Specification is an open standard for describing asynchronous and event-driven APIs. It provides a machine-readable format for defining messaging interfaces across protocols like Kafka, M
  name: AsyncAPI Specification
  slug: asyncapi-spec
- description: The Bundle API from AsyncAPI — 1 operation(s) for bundle.
  name: AsyncAPI Bundle API
  slug: asyncapi-bundle-api
- description: The Convert API from AsyncAPI — 1 operation(s) for convert.
  name: AsyncAPI Convert API
  slug: asyncapi-convert-api
- description: The Diff API from AsyncAPI — 1 operation(s) for diff.
  name: AsyncAPI Diff API
  slug: asyncapi-diff-api
- description: The Generate API from AsyncAPI — 1 operation(s) for generate.
  name: AsyncAPI Generate API
  slug: asyncapi-generate-api
- description: The Help API from AsyncAPI — 1 operation(s) for help.
  name: AsyncAPI Help API
  slug: asyncapi-help-api
- description: The Parse API from AsyncAPI — 1 operation(s) for parse.
  name: AsyncAPI Parse API
  slug: asyncapi-parse-api
- description: The Validate API from AsyncAPI — 1 operation(s) for validate.
  name: AsyncAPI Validate API
  slug: asyncapi-validate-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AsyncAPI Server Bundle API
  slug: open-asyncapi-bundle-api
- collection_type: open
  name: AsyncAPI Server Bundle Convert API
  slug: open-asyncapi-convert-api
- collection_type: open
  name: AsyncAPI Server Bundle Diff API
  slug: open-asyncapi-diff-api
- collection_type: open
  name: AsyncAPI Server Bundle Generate API
  slug: open-asyncapi-generate-api
- collection_type: open
  name: AsyncAPI Server Bundle Help API
  slug: open-asyncapi-help-api
- collection_type: open
  name: AsyncAPI Server Bundle Parse API
  slug: open-asyncapi-parse-api
- collection_type: open
  name: AsyncAPI Server Bundle Validate API
  slug: open-asyncapi-validate-api
- collection_type: open
  name: AsyncAPI Server API
  slug: open-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/asyncapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/asyncapi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/asyncapi
- group: start
  title: AsyncAPI Website
  type: Portal
  url: https://www.asyncapi.com/
- group: docs
  title: Documentation
  type: Documentation
  url: https://www.asyncapi.com/docs
- group: build
  title: AsyncAPI GitHub Organization
  type: GitHubOrganization
  url: https://github.com/asyncapi
- group: company
  title: Blog
  type: Blog
  url: https://www.asyncapi.com/blog
created: '2026-03-16'
description: AsyncAPI is a Linux Foundation project that improves the state of event-driven architectures by providing an open specification and tooling ecosystem for defining asynchronous and event-driven APIs. It enables developers to document, validate, generate code, and manage message-driven APIs across protocols including Kafka, MQTT, WebSocket, AMQP, and others. The AsyncAPI specification serves as the industry standard for describing asynchronous messaging interfaces, similar to how OpenAPI serves REST APIs.
features:
- description: An open specification standard for describing asynchronous and event-driven APIs, supporting multiple messaging protocols including Kafka, MQTT, WebSocket, AMQP, and more.
  name: AsyncAPI Specification
- description: Code and documentation generation tool that uses AsyncAPI definitions to produce boilerplate code, documentation, and other artifacts in multiple programming languages.
  name: AsyncAPI Generator
- description: Command-line interface tool for working with AsyncAPI files including validation, generation, and conversion operations from the terminal.
  name: AsyncAPI CLI
- description: Web-based editor and visualization tool for creating, editing, and previewing AsyncAPI specification documents with real-time validation.
  name: AsyncAPI Studio
- description: Broad protocol support covering Kafka, MQTT, WebSocket, AMQP, NATS, JMS, and other messaging protocols through a unified specification format.
  name: Protocol Support
finops:
- name: Asyncapi Finops
  service_category: API
  slug: asyncapi-finops
- name: Asyncapi Funding
  service_category: ''
  slug: asyncapi-funding
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/asyncapi.png
integrations:
- description: AsyncAPI supports defining Kafka-based event-driven APIs with topic, message schema, and broker configuration documentation.
  name: Apache Kafka
- description: IoT and messaging platforms using MQTT can document their pub/sub interfaces using AsyncAPI specifications for device and service integration.
  name: MQTT Brokers
- description: AsyncAPI CLI integrates into continuous integration pipelines for automated validation and linting of AsyncAPI specification files.
  name: CI/CD Pipelines
layout: provider
modified: '2026-04-19'
name: AsyncAPI
nav: Providers
network: true
overview: 'AsyncAPI publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Specification, Bundle API, Convert API, and 5 more. Tagged areas include Event-Driven, Linux Foundation, Messaging, Standards, and Specification.


  AsyncAPI''s developer surface includes developer portal, documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Asyncapi Plans Pricing
  plan_count: 3
  slug: asyncapi-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Asyncapi Rate Limits
  slug: asyncapi-rate-limits
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.9
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/asyncapi/refs/heads/main/screenshots/asyncapi-2026-06-20T172514.png
security:
- kind: domain-security
  name: Asyncapi Domain Security
  slug: asyncapi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: asyncapi
tags:
- Event-Driven
- Linux Foundation
- Messaging
- Standards
- Specification
use_cases:
- description: Development teams use AsyncAPI to create machine-readable documentation for their message-driven APIs, making it easier for consumers to understand and integrate with event streams.
  name: Event-Driven API Documentation
- description: Engineers generate boilerplate code for Kafka consumers, MQTT publishers, and other messaging clients directly from AsyncAPI specifications to accelerate development.
  name: Code Generation for Messaging
- description: Platform teams apply AsyncAPI specifications to enforce standards and governance across microservices architectures using event-driven communication.
  name: API Governance for Event-Driven Systems
website: https://www.asyncapi.com/
---
