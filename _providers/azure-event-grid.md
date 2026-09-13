---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Azure Event Grid Agentic Access
  operation_count: 6
  slug: azure-event-grid-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- description: Data-plane REST API for publishing events and CloudEvents to Event Grid topics and domains, and for managing namespace topics, subscriptions, and event delivery. Authentication uses Microsoft Entra ID
  name: Azure Event Grid Publisher API
  slug: publisher-api
- baseURL: https://{topic-endpoint}.{region}.eventgrid.azure.net
  baseurl_source: declared
  description: Namespace topic publish, receive, acknowledge
  name: Azure Event Grid Namespace Topics API
  slug: azure-event-grid-namespace-topics-api
- baseURL: https://{topic-endpoint}.{region}.eventgrid.azure.net
  baseurl_source: declared
  description: Publish events to a topic
  name: Azure Event Grid Publish API
  slug: azure-event-grid-publish-api
- baseURL: https://{topic}.{region}.eventgrid.azure.net/
  baseurl_source: declared
  description: Operations operations
  name: Azure Event Grid Operations API
  slug: microsoft-azure-event-grid-operations-api
- baseURL: https://{topic}.{region}.eventgrid.azure.net/
  baseurl_source: declared
  description: Topics operations
  name: Azure Event Grid Topics API
  slug: microsoft-azure-event-grid-topics-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Event Grid Publisher Namespace Topics API
  slug: open-azure-event-grid-namespace-topics-api
- collection_type: open
  name: Azure Event Grid Publisher Namespace Topics Publish API
  slug: open-azure-event-grid-publish-api
- collection_type: open
  name: Azure Event Grid Publisher API
  slug: open-azure-event-grid
common:
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-event-grid-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-event-grid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-event-grid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-event-grid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-event-grid-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/event-grid/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/event-grid/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/event-grid/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: agent
  title: ''
  type: LlmsText
  url: https://azure.microsoft.com/llms.txt
created: '2026-05-11'
description: Azure Event Grid is a fully managed event routing service from Microsoft Azure that enables event-driven, reactive programming by ingesting events from Azure services, SaaS providers, and custom sources and delivering them to subscribers such as Azure Functions, Logic Apps, webhooks, and event hubs. It supports both Event Grid topics and the MQTT/CloudEvents-based Event Grid namespaces for IoT and pub-sub workloads. The Event Grid REST APIs and Azure SDKs use Microsoft Entra ID OAuth 2.0 bearer tokens or shared-access keys for authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-event-grid.png
layout: provider
modified: '2026-05-11'
name: Azure Event Grid
nav: Providers
network: true
overview: 'Azure Event Grid publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Namespace Topics API, Publish API, Operations API, and 1 more. Tagged areas include Eventing, Event-Driven, Pub-Sub, Messaging, and Webhook.


  Azure Event Grid''s developer surface includes developer portal, support, authentication, documentation, pricing, signup flow, and 9 more developer resources.'
random_paper: 13
scopes:
- name: Azure Event Grid Scopes
  scope_count: 1
  slug: azure-event-grid-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.1
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 50.7
    developer_ergonomics: 35.7
    discoverability: 83.3
    operational_transparency: 5.3
  previous_composite: 28.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-event-grid/refs/heads/main/screenshots/azure-event-grid-2026-06-20T172903.png
security:
- kind: authentication
  name: Azure Event Grid Authentication
  slug: azure-event-grid-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Azure Event Grid Domain Security
  slug: azure-event-grid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Event Grid Vulnerability Disclosure
  slug: azure-event-grid-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-event-grid
tags:
- Eventing
- Event-Driven
- Pub-Sub
- Messaging
- Webhook
- CloudEvents
- Cloud
- Azure
website: https://azure.microsoft.com/en-us/products/event-grid/
---
