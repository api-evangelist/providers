---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Microsoft Azure Event Hubs Agentic Access
  operation_count: 37
  slug: microsoft-azure-event-hubs-agentic-access
  summary_line: 37 operations · 22 acting
api_count: 10
apis:
- description: Event-driven messaging API for publishing and consuming events via AMQP 1.0, Kafka, and HTTPS protocols. Supports partitioned event streams, consumer groups, and publisher policies.
  name: Azure Event Hubs Messaging API
  slug: azure-event-hubs-messaging-api
- description: Client libraries for various programming languages to interact with Event Hubs.
  name: Azure Event Hubs SDK
  slug: azure-event-hubs-sdk
- description: Operations for managing authorization rules and access keys.
  name: Azure Event Hubs Authorization Rules API
  slug: microsoft-azure-event-hubs-authorization-rules-api
- description: Operations for managing consumer groups within an event hub.
  name: Azure Event Hubs Consumer Groups API
  slug: microsoft-azure-event-hubs-consumer-groups-api
- description: Operations for managing disaster recovery (Geo-DR) configurations.
  name: Azure Event Hubs Disaster Recovery Configs API
  slug: microsoft-azure-event-hubs-disaster-recovery-configs-api
- description: Operations for managing event hubs within a namespace.
  name: Azure Event Hubs Event Hubs API
  slug: microsoft-azure-event-hubs-event-hubs-api
- description: Operations for sending events to Azure Event Hubs, including single events, batch events, partition-specific events, and events with publisher identity.
  name: Azure Event Hubs Events API
  slug: microsoft-azure-event-hubs-events-api
- description: Operations for managing Event Hubs namespaces.
  name: Azure Event Hubs Namespaces API
  slug: microsoft-azure-event-hubs-namespaces-api
- description: Operations for listing available Event Hub REST API operations.
  name: Azure Event Hubs Operations API
  slug: microsoft-azure-event-hubs-operations-api
- description: Operations for managing schema groups in the Schema Registry.
  name: Azure Event Hubs Schema Registry API
  slug: microsoft-azure-event-hubs-schema-registry-api
arazzos:
- description: Create a Geo-DR alias pairing a primary namespace to a secondary, then poll the configuration until replication provisioning succeeds.
  name: Microsoft Azure Event Hubs Configure Geo-Disaster Recovery Pairing
  slug: microsoft-azure-event-hubs-configure-disaster-recovery-pairing-workflow
- description: Create an event hub with Avro capture enabled to an Azure Blob container, then read it back to confirm capture is active.
  name: Microsoft Azure Event Hubs Configure Event Hub Capture to Blob Storage
  slug: microsoft-azure-event-hubs-configure-event-hub-capture-workflow
- description: Create an event hub in an existing namespace, add a consumer group, and confirm the consumer group is listed.
  name: Microsoft Azure Event Hubs Create an Event Hub with a Consumer Group
  slug: microsoft-azure-event-hubs-create-event-hub-with-consumer-group-workflow
- description: Apply a default-deny network rule set with an IP allow rule to a namespace, then read it back to confirm the deny posture.
  name: Microsoft Azure Event Hubs Lock Down a Namespace Network
  slug: microsoft-azure-event-hubs-lock-down-namespace-network-workflow
- description: Create a namespace shared access authorization rule with the requested rights, then fetch its connection strings and keys.
  name: Microsoft Azure Event Hubs Provision an Authorization Rule and Retrieve Keys
  slug: microsoft-azure-event-hubs-provision-authorization-rule-and-keys-workflow
- description: Create an Event Hubs namespace, wait for it to finish provisioning, then create an event hub inside it.
  name: Microsoft Azure Event Hubs Provision a Namespace with an Event Hub
  slug: microsoft-azure-event-hubs-provision-namespace-with-event-hub-workflow
- description: Create an Avro schema group in a namespace's schema registry with a compatibility mode, then read it back to confirm registration.
  name: Microsoft Azure Event Hubs Register a Schema Registry Group
  slug: microsoft-azure-event-hubs-register-schema-group-workflow
- description: Capture the current connection strings for an authorization rule, regenerate one of the keys, and read back the new credentials.
  name: Microsoft Azure Event Hubs Rotate Namespace Keys
  slug: microsoft-azure-event-hubs-rotate-namespace-keys-workflow
artifact_total: 38
asyncapis:
- description: Azure Event Hubs is a big data streaming platform and event ingestion service that can receive and process millions of events per second. This AsyncAPI specification describes the event-driven messagi
  name: Azure Event Hubs Messaging API
  slug: azure-event-hubs-messaging-asyncapi
collections:
- collection_type: postman
  name: Azure Event Hubs Data Plane REST API
  slug: postman-azure-event-hubs-data-plane
- collection_type: postman
  name: Azure Event Hubs Management REST API
  slug: postman-azure-event-hubs-management
- collection_type: open
  name: Azure Event Hubs Data Plane REST API
  slug: open-azure-event-hubs-data-plane
- collection_type: open
  name: Azure Event Hubs Management REST API
  slug: open-azure-event-hubs-management
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-event-hubs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-event-hubs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-event-hubs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-event-hubs-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-event-hubs/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-event-hubs-configure-disaster-recovery-pairing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-event-hubs-configure-event-hub-capture-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-event-hubs-create-event-hub-with-consumer-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-event-hubs-lock-down-namespace-network-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-event-hubs-provision-authorization-rule-and-keys-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-event-hubs-provision-namespace-with-event-hub-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-event-hubs-register-schema-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-event-hubs-rotate-namespace-keys-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.EventHub%2Fnamespaces
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-quickstart-portal
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/event-hubs/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://azure.microsoft.com/en-us/support/legal/sla/event-hubs/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/event-hubs/authenticate-application
- group: other
  title: ''
  type: Best Practices
  url: https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-best-practices
- group: build
  title: ''
  type: Samples
  url: https://github.com/Azure/azure-event-hubs/tree/master/samples
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/messaging-on-azure-and-net/bg-p/MessagingonAzureBlog
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/event-hubs/
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-quotas
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/event-hubs/sdks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/services/event-hubs/
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: operate
  title: ''
  type: Community
  url: https://learn.microsoft.com/en-us/answers/tags/165/azure-event-hubs/
- group: auth
  title: ''
  type: Security
  url: https://learn.microsoft.com/en-us/azure/event-hubs/network-security
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/azure-event-hubs-namespace.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/azure-event-hubs-eventhub.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/azure-event-hubs-consumer-group.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/azure-event-hubs-event-data.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/azure-event-hubs-schema-group.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/azure-event-hubs-context.jsonld
created: '2024-01-01'
description: Azure Event Hubs is a big data streaming platform and event ingestion service that can receive and process millions of events per second. It provides a distributed stream processing platform with low latency and seamless integration with Azure data and analytics services.
finops:
- name: Microsoft Azure Event Hubs Finops
  service_category: Messaging / Event Streaming
  slug: microsoft-azure-event-hubs-finops
image: https://azure.microsoft.com/svghandler/event-hubs/
json_schemas:
- name: Azure Event Hubs Consumer Group
  property_count: 6
  slug: azure-event-hubs-consumer-group
- name: Azure Event Hubs Event Data
  property_count: 3
  slug: azure-event-hubs-event-data
- name: Azure Event Hub
  property_count: 6
  slug: azure-event-hubs-eventhub
- name: Azure Event Hubs Namespace
  property_count: 9
  slug: azure-event-hubs-namespace
- name: Azure Event Hubs Schema Group
  property_count: 5
  slug: azure-event-hubs-schema-group
jsonld:
- class_count: 0
  name: Azure Event Hubs Context
  property_count: 15
  slug: azure-event-hubs-context
layout: provider
modified: '2026-05-19'
name: Azure Event Hubs
nav: Providers
network: true
overview: 'Azure Event Hubs publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Messaging API, Authorization Rules API, Consumer Groups API, and 6 more. Tagged areas include Big Data, Event Streaming, IoT, Message Ingestion, and Real-Time Processing.


  The Azure Event Hubs catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Azure Event Hubs'' developer surface includes authentication, developer portal, getting-started guide, pricing, support, engineering blog, documentation, and 33 more developer resources.'
plans:
- name: Microsoft Azure Event Hubs Plans Pricing
  plan_count: 4
  slug: microsoft-azure-event-hubs-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 7
  name: Microsoft Azure Event Hubs Rate Limits
  slug: microsoft-azure-event-hubs-rate-limits
rules:
- name: Azure Event Hubs API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 7
  slug: microsoft-azure-event-hubs-asyncapi-spectral-rules
- name: Azure Event Hubs API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-azure-event-hubs-jsonschema-spectral-rules
scopes:
- name: Microsoft Azure Event Hubs Scopes
  scope_count: 1
  slug: microsoft-azure-event-hubs-scopes
  summary_line: 1 scope · implicit
score:
  band: exemplar
  composite: 70.5
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 76.1
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 63.2
  previous_composite: 70.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-event-hubs/refs/heads/main/screenshots/microsoft-azure-event-hubs-2026-06-20T185412.png
security:
- kind: authentication
  name: Microsoft Azure Event Hubs Authentication
  slug: microsoft-azure-event-hubs-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Microsoft Azure Event Hubs Domain Security
  slug: microsoft-azure-event-hubs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-event-hubs
tags:
- Big Data
- Event Streaming
- IoT
- Message Ingestion
- Real-Time Processing
website: https://azure.microsoft.com/en-us/services/event-hubs/
---
