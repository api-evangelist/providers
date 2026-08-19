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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Microsoft Azure Service Bus Agentic Access
  operation_count: 5
  slug: microsoft-azure-service-bus-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 2
apis:
- description: The management REST API enables namespace, queue, topic, and subscription configuration through Azure Resource Manager, including SKU, network rules, authorization rules, and disaster recovery configu
  name: Azure Service Bus Management REST API
  slug: management-api
- description: The Messages API from Azure Service Bus — 3 operation(s) for messages.
  name: Azure Service Bus Messages API
  slug: microsoft-azure-service-bus-messages-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Service Bus REST Messages API
  slug: open-microsoft-azure-service-bus-messages-api
- collection_type: open
  name: Azure Service Bus REST API
  slug: open-microsoft-azure-service-bus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-service-bus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-service-bus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-service-bus-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/service-bus/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quickstart-portal
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dotnet-get-started-with-queues
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/product/service-bus/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azureservicebus
created: '2026-03-13'
description: Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics. It enables decoupling applications and services with reliable asynchronous messaging, supporting sessions, dead-lettering, scheduled delivery, duplicate detection, and transactions.
finops:
- name: Microsoft Azure Service Bus Finops
  service_category: API
  slug: microsoft-azure-service-bus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-service-bus.png
layout: provider
modified: '2026-05-19'
name: Azure Service Bus
nav: Providers
network: true
overview: 'Azure Service Bus publishes 1 API on the [APIs.io](https://apis.io/) network: Messages API. Tagged areas include Enterprise Messaging, Message Broker, Messaging, Publish Subscribe, and Queues.


  Azure Service Bus'' developer surface includes authentication, developer portal, pricing, documentation, getting-started guide, support, engineering blog, and 8 more developer resources.'
plans:
- name: Microsoft Azure Service Bus Plans Pricing
  plan_count: 3
  slug: microsoft-azure-service-bus-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Microsoft Azure Service Bus Rate Limits
  slug: microsoft-azure-service-bus-rate-limits
score:
  band: developing
  composite: 42.1
  delta: -2.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-service-bus/refs/heads/main/screenshots/microsoft-azure-service-bus-2026-06-20T185434.png
security:
- kind: authentication
  name: Microsoft Azure Service Bus Authentication
  slug: microsoft-azure-service-bus-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Azure Service Bus Domain Security
  slug: microsoft-azure-service-bus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-service-bus
tags:
- Enterprise Messaging
- Message Broker
- Messaging
- Publish Subscribe
- Queues
- Topics
website: https://portal.azure.com/
---
