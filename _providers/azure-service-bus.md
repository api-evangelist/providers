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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Azure Service Bus Agentic Access
  operation_count: 17
  slug: azure-service-bus-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 4
apis:
- description: Service Bus namespace operations
  name: Azure Service Bus Namespaces API
  slug: azure-service-bus-namespaces-api
- description: Service Bus queue operations
  name: Azure Service Bus Queues API
  slug: azure-service-bus-queues-api
- description: Service Bus topic subscription operations
  name: Azure Service Bus Subscriptions API
  slug: azure-service-bus-subscriptions-api
- description: Service Bus topic operations
  name: Azure Service Bus Topics API
  slug: azure-service-bus-topics-api
artifact_total: 64
asyncapis:
- description: 'Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics. This AsyncAPI spec describes the messaging patterns for sending and receiving messages '
  name: Azure Service Bus Messaging
  slug: azure-service-bus-asyncapi
collections:
- collection_type: postman
  name: Azure Service Bus Management Namespaces API
  slug: postman-azure-service-bus-namespaces-api
- collection_type: postman
  name: Azure Service Bus Management Namespaces Queues API
  slug: postman-azure-service-bus-queues-api
- collection_type: postman
  name: Azure Service Bus Management Namespaces Subscriptions API
  slug: postman-azure-service-bus-subscriptions-api
- collection_type: postman
  name: Azure Service Bus Management Namespaces Topics API
  slug: postman-azure-service-bus-topics-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Service Bus Management Namespaces API
  slug: open-azure-service-bus-namespaces-api
- collection_type: open
  name: Azure Service Bus Management Namespaces Queues API
  slug: open-azure-service-bus-queues-api
- collection_type: open
  name: Azure Service Bus Management Namespaces Subscriptions API
  slug: open-azure-service-bus-subscriptions-api
- collection_type: open
  name: Azure Service Bus Management Namespaces Topics API
  slug: open-azure-service-bus-topics-api
- collection_type: open
  name: Azure Service Bus Management API
  slug: open-azure-service-bus
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Azure/azure-sdk-for-net/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Azure/azure-sdk-for-net/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/azure-sdk-for-net/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Azure/azure-sdk-for-net/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Azure/azure-sdk-for-net/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-service-bus/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-service-bus-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-service-bus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-service-bus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-service-bus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-service-bus-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://azure.microsoft.com/en-us/products/service-bus
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quickstart-portal
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/service-bus/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/servicebus
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: agent
  title: ''
  type: LlmsText
  url: https://azure.microsoft.com/llms.txt
created: '2026-03-26'
description: Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics, providing reliable message delivery for decoupling applications and services in cloud and hybrid environments.
examples:
- key_count: 7
  name: Azure Service Bus Sb Namespace Example
  slug: azure-service-bus-sb-namespace-example
- key_count: 2
  name: Azure Service Bus Sb Namespace List Result Example
  slug: azure-service-bus-sb-namespace-list-result-example
- key_count: 4
  name: Azure Service Bus Sb Queue Example
  slug: azure-service-bus-sb-queue-example
- key_count: 2
  name: Azure Service Bus Sb Queue List Result Example
  slug: azure-service-bus-sb-queue-list-result-example
- key_count: 4
  name: Azure Service Bus Sb Subscription Example
  slug: azure-service-bus-sb-subscription-example
- key_count: 2
  name: Azure Service Bus Sb Subscription List Result Example
  slug: azure-service-bus-sb-subscription-list-result-example
- key_count: 4
  name: Azure Service Bus Sb Topic Example
  slug: azure-service-bus-sb-topic-example
- key_count: 2
  name: Azure Service Bus Sb Topic List Result Example
  slug: azure-service-bus-sb-topic-list-result-example
features:
- description: Point-to-point messaging with FIFO delivery, sessions, dead-lettering, and duplicate detection for reliable asynchronous communication.
  name: Message Queues
- description: One-to-many messaging with topic subscriptions, filters, and actions for event-driven architectures.
  name: Publish-Subscribe Topics
- description: Automatic routing of undeliverable or failed messages to a secondary queue for inspection and reprocessing.
  name: Dead-Letter Queue
- description: Schedule messages for future delivery at a specified time without requiring sender availability.
  name: Scheduled Delivery
- description: ACID transaction support for grouping multiple operations across queues and topics into atomic units.
  name: Transactions
- description: Automatically forward messages from one queue or subscription to another entity for chaining processing stages.
  name: Auto-Forwarding
finops:
- name: Azure Service Bus Finops
  service_category: API
  slug: azure-service-bus-finops
image: /assets/icons/azure-service-bus.png
integrations:
- description: Trigger serverless functions automatically when messages arrive in queues or topic subscriptions.
  name: Azure Functions
- description: Build automated workflows that send and receive Service Bus messages with no-code connectors.
  name: Azure Logic Apps
- description: Route Service Bus events to other Azure services for real-time event processing and monitoring.
  name: Azure Event Grid
json_schemas:
- name: SBNamespaceListResult
  property_count: 2
  slug: azure-service-bus-sb-namespace-list-result
- name: SBNamespace
  property_count: 7
  slug: azure-service-bus-sb-namespace
- name: SBQueueListResult
  property_count: 2
  slug: azure-service-bus-sb-queue-list-result
- name: SBQueue
  property_count: 4
  slug: azure-service-bus-sb-queue
- name: SBSubscriptionListResult
  property_count: 2
  slug: azure-service-bus-sb-subscription-list-result
- name: SBSubscription
  property_count: 4
  slug: azure-service-bus-sb-subscription
- name: SBTopicListResult
  property_count: 2
  slug: azure-service-bus-sb-topic-list-result
- name: SBTopic
  property_count: 4
  slug: azure-service-bus-sb-topic
json_structures:
- name: Azure Service Bus Sb Namespace List Result Structure
  property_count: 2
  slug: azure-service-bus-sb-namespace-list-result-structure
- name: Azure Service Bus Sb Namespace Structure
  property_count: 7
  slug: azure-service-bus-sb-namespace-structure
- name: Azure Service Bus Sb Queue List Result Structure
  property_count: 2
  slug: azure-service-bus-sb-queue-list-result-structure
- name: Azure Service Bus Sb Queue Structure
  property_count: 4
  slug: azure-service-bus-sb-queue-structure
- name: Azure Service Bus Sb Subscription List Result Structure
  property_count: 2
  slug: azure-service-bus-sb-subscription-list-result-structure
- name: Azure Service Bus Sb Subscription Structure
  property_count: 4
  slug: azure-service-bus-sb-subscription-structure
- name: Azure Service Bus Sb Topic List Result Structure
  property_count: 2
  slug: azure-service-bus-sb-topic-list-result-structure
- name: Azure Service Bus Sb Topic Structure
  property_count: 4
  slug: azure-service-bus-sb-topic-structure
jsonld:
- class_count: 0
  name: Azure Service Bus Context
  property_count: 0
  slug: azure-service-bus-context
layout: provider
modified: '2026-05-19'
name: Azure Service Bus
nav: Providers
network: true
overview: 'Azure Service Bus publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Namespaces API, Queues API, Subscriptions API, and 1 more. Tagged areas include Azure, Cloud, Enterprise, Message Broker, and Messaging.


  The Azure Service Bus catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Azure Service Bus'' developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Azure Service Bus Plans Pricing
  plan_count: 3
  slug: azure-service-bus-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 5
  name: Azure Service Bus Rate Limits
  slug: azure-service-bus-rate-limits
rules:
- name: Azure Service Bus API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 2
  slug: azure-service-bus-asyncapi-spectral-rules
- name: Azure Service Bus API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-service-bus-jsonschema-spectral-rules
- name: Azure Service Bus API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: azure-service-bus-spectral-rules
scopes:
- name: Azure Service Bus Scopes
  scope_count: 1
  slug: azure-service-bus-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 52.2
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 76.7
    developer_ergonomics: 45.7
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 34.2
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-service-bus/refs/heads/main/screenshots/azure-service-bus-2026-06-20T172908.png
security:
- kind: authentication
  name: Azure Service Bus Authentication
  slug: azure-service-bus-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Service Bus Domain Security
  slug: azure-service-bus-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Azure Service Bus Vulnerability Disclosure
  slug: azure-service-bus-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-service-bus
tags:
- Azure
- Cloud
- Enterprise
- Message Broker
- Messaging
- Pub/Sub
- Queues
use_cases:
- description: Decouple microservices and distributed applications using asynchronous messaging for independent scaling and deployment.
  name: Application Decoupling
- description: Buffer incoming requests during traffic spikes to protect backend services from overload.
  name: Load Leveling
- description: Build event-driven systems using publish-subscribe topics to broadcast events to multiple subscribers.
  name: Event-Driven Architecture
- description: Coordinate multi-step business processes using message sessions and scheduled delivery for reliable workflow execution.
  name: Workflow Orchestration
website: https://azure.microsoft.com/en-us/products/service-bus
---
