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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Integration Services Agentic Access
  operation_count: 7
  slug: microsoft-azure-integration-services-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 6
apis:
- description: Azure Logic Apps is a cloud-based platform for creating and running automated workflows that integrate apps, data, services, and systems. It provides a visual designer and hundreds of pre-built connec
  name: Azure Logic Apps
  slug: azure-logic-apps
- description: Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics. It decouples applications and services from each other, providing reliable asynchronous
  name: Azure Service Bus
  slug: azure-service-bus
- description: Azure Event Grid is a highly scalable, fully managed publish-subscribe event distribution service. It enables event-driven architectures by routing events from Azure services and custom sources to eve
  name: Azure Event Grid
  slug: azure-event-grid
- description: Azure Event Hubs is a big data streaming platform and event ingestion service capable of receiving and processing millions of events per second. It is used for telemetry ingestion, application logging
  name: Azure Event Hubs
  slug: azure-event-hubs
- description: Operations operations
  name: Microsoft Azure Integration Services Operations API
  slug: microsoft-azure-integration-services-operations-api
- description: Services operations
  name: Microsoft Azure Integration Services Services API
  slug: microsoft-azure-integration-services-services-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure API Management REST Operations API
  slug: open-microsoft-azure-integration-services-operations-api
- collection_type: open
  name: Azure API Management REST Operations Services API
  slug: open-microsoft-azure-integration-services-services-api
- collection_type: open
  name: Azure API Management REST API
  slug: open-microsoft-azure-integration-services
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-integration-services-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-integration-services-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-integration-services-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-integration-services-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/category/integration
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/?product=integration
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/integration-services/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/integrationsonazureblog
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
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
  type: GitHubOrganization
  url: https://github.com/Azure
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@MicrosoftAzure
- group: operate
  title: ''
  type: Community
  url: https://techcommunity.microsoft.com/category/azure
- group: start
  title: ''
  type: Console
  url: https://portal.azure.com/
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
created: '2026-03-16'
description: Microsoft Azure Integration Services is a collection of cloud-based integration capabilities that connect applications, data, and processes across cloud and on-premises environments. It includes API Management, Logic Apps, Service Bus, Event Grid, and Event Hubs to enable enterprise integration, messaging, and event-driven architectures.
finops:
- name: Microsoft Azure Integration Services Finops
  service_category: API
  slug: microsoft-azure-integration-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-integration-services.png
layout: provider
modified: '2026-05-19'
name: Microsoft Azure Integration Services
nav: Providers
network: true
overview: 'Microsoft Azure Integration Services publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Services API. Tagged areas include API Management, Enterprise, Event-Driven, Integration, and Messaging.


  Microsoft Azure Integration Services'' developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, support, and 13 more developer resources.'
plans:
- name: Microsoft Azure Integration Services Plans Pricing
  plan_count: 3
  slug: microsoft-azure-integration-services-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Microsoft Azure Integration Services Rate Limits
  slug: microsoft-azure-integration-services-rate-limits
scopes:
- name: Microsoft Azure Integration Services Scopes
  scope_count: 1
  slug: microsoft-azure-integration-services-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 48.0
  delta: 1.4
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 64.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-integration-services/refs/heads/main/screenshots/microsoft-azure-integration-services-2026-06-20T185419.png
security:
- kind: authentication
  name: Microsoft Azure Integration Services Authentication
  slug: microsoft-azure-integration-services-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Integration Services Domain Security
  slug: microsoft-azure-integration-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-integration-services
tags:
- API Management
- Enterprise
- Event-Driven
- Integration
- Messaging
website: https://azure.microsoft.com/en-us/products/category/integration
---
