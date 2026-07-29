---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
- acting_count: 33
  human_in_the_loop: 1
  name: Dapr Agentic Access
  operation_count: 49
  slug: dapr-agentic-access
  summary_line: 49 operations · 33 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Virtual actor operations including state, timers, and reminders.
  name: Dapr Actors API
  slug: dapr-actors-api
- description: Input and output binding operations.
  name: Dapr Bindings API
  slug: dapr-bindings-api
- description: Configuration management operations.
  name: Dapr Configuration API
  slug: dapr-configuration-api
- description: Cryptographic operations.
  name: Dapr Cryptography API
  slug: dapr-cryptography-api
- description: Distributed locking operations.
  name: Dapr DistributedLock API
  slug: dapr-distributedlock-api
- description: Health check operations.
  name: Dapr Health API
  slug: dapr-health-api
- description: Job scheduling operations.
  name: Dapr Jobs API
  slug: dapr-jobs-api
- description: Sidecar metadata operations.
  name: Dapr Metadata API
  slug: dapr-metadata-api
- description: Publish and subscribe messaging operations.
  name: Dapr PubSub API
  slug: dapr-pubsub-api
- description: Secret management operations.
  name: Dapr Secrets API
  slug: dapr-secrets-api
- description: Service-to-service invocation operations.
  name: Dapr ServiceInvocation API
  slug: dapr-serviceinvocation-api
- description: State management operations.
  name: Dapr State API
  slug: dapr-state-api
- description: Workflow orchestration operations.
  name: Dapr Workflow API
  slug: dapr-workflow-api
artifact_total: 45
asyncapis:
- description: The Dapr Pub/Sub AsyncAPI defines the event-driven messaging interfaces for Dapr publish and subscribe operations. Applications publish events to topics and subscribe to receive events using the Cloud
  name: Dapr Pub/Sub Messaging API
  slug: dapr-pubsub-asyncapi
collections:
- collection_type: open
  name: Dapr Actors API
  slug: open-dapr-actors
- collection_type: open
  name: Dapr Bindings API
  slug: open-dapr-bindings
- collection_type: open
  name: Dapr Configuration API
  slug: open-dapr-configuration
- collection_type: open
  name: Dapr Cryptography API
  slug: open-dapr-cryptography
- collection_type: open
  name: Dapr Distributed Lock API
  slug: open-dapr-distributed-lock
- collection_type: open
  name: Dapr Health API
  slug: open-dapr-health
- collection_type: open
  name: Dapr Jobs API
  slug: open-dapr-jobs
- collection_type: open
  name: Dapr Metadata API
  slug: open-dapr-metadata
- collection_type: open
  name: Dapr Pub/Sub API
  slug: open-dapr-pubsub
- collection_type: open
  name: Dapr Secrets API
  slug: open-dapr-secrets
- collection_type: open
  name: Dapr Service Invocation API
  slug: open-dapr-service-invocation
- collection_type: open
  name: Dapr State Management API
  slug: open-dapr-state-management
- collection_type: open
  name: Dapr Workflow API
  slug: open-dapr-workflow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dapr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dapr-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/daprdev
- group: company
  title: ''
  type: Website
  url: https://dapr.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dapr.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dapr.io/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://blog.dapr.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dapr
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/dapr/dapr
- group: build
  title: ''
  type: SDKs
  url: https://docs.dapr.io/sdks/
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/ptHhX6jc34
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/dapr/dapr/blob/master/CHANGELOG.md
- group: auth
  title: ''
  type: Security
  url: https://github.com/dapr/dapr/security/policy
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/dapr
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dapr-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dapr-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/dapr-rules.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/dapr-capabilities.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://dapr.io/llms.txt
created: '2025-01-08'
description: Dapr (Distributed Application Runtime) is a portable, event-driven runtime that makes it easy for developers to build resilient, stateless, and stateful applications that run on the cloud and edge. It provides building block APIs for state management, pub/sub messaging, service invocation, bindings, actors, workflows, secrets, configuration, distributed locks, cryptography, jobs scheduling, health checks, and metadata.
finops:
- name: Dapr Finops
  service_category: Developer Tools
  slug: dapr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dapr.png
json_schemas:
- name: Dapr Actor
  property_count: 4
  slug: actor
- name: Dapr Binding
  property_count: 3
  slug: binding
- name: Dapr CloudEvent
  property_count: 13
  slug: cloud-event
- name: Dapr ConfigurationItem
  property_count: 4
  slug: configuration-item
- name: Dapr Job
  property_count: 6
  slug: job
- name: Dapr Metadata
  property_count: 9
  slug: metadata
- name: Dapr Secret
  property_count: 4
  slug: secret
- name: Dapr StateItem
  property_count: 5
  slug: state-item
- name: Dapr Workflow
  property_count: 6
  slug: workflow
jsonld:
- class_count: 0
  name: Dapr Context
  property_count: 9
  slug: dapr-context
layout: provider
modified: '2026-05-19'
name: Dapr
nav: Providers
network: true
overview: 'Dapr publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Actors API, Bindings API, Configuration API, and 10 more. Tagged areas include Distributed Systems, Microservices, Platform, Pub/Sub, and State Management.


  The Dapr catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Dapr''s developer surface includes documentation, getting-started guide, engineering blog, changelog, Stack Overflow tag, and 14 more developer resources.'
plans:
- name: Dapr Plans Pricing
  plan_count: 1
  slug: dapr-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Dapr Rate Limits
  slug: dapr-rate-limits
rules:
- name: Dapr API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: dapr-asyncapi-spectral-rules
- name: Dapr API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dapr-jsonschema-spectral-rules
- name: Dapr API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: dapr-rules
score:
  band: developing
  composite: 51.1
  delta: -5.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 71.3
    developer_ergonomics: 32.6
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/screenshots/dapr-2026-06-20T175454.png
security:
- kind: domain-security
  name: Dapr Domain Security
  slug: dapr-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dapr
tags:
- Distributed Systems
- Microservices
- Platform
- Pub/Sub
- State Management
- Workflows
website: https://dapr.io/
---
