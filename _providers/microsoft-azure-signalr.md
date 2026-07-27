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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Signalr Agentic Access
  operation_count: 7
  slug: microsoft-azure-signalr-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Operations operations
  name: Azure SignalR Service Operations API
  slug: microsoft-azure-signalr-operations-api
- description: SignalR operations
  name: Azure SignalR Service SignalR API
  slug: microsoft-azure-signalr-signalr-api
artifact_total: 10
collections:
- collection_type: open
  name: Azure SignalR Service REST API
  slug: open-microsoft-azure-signalr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-signalr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-signalr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-signalr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-signalr-scopes.yml
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
  url: https://azure.microsoft.com/en-us/pricing/details/signalr-service/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-signalr/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-quickstart-azure-signalr-service-arm-template
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
  url: https://azure.microsoft.com/en-us/blog/product/azure-signalr-service/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-signalr
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure SignalR Service REST API enables management of real-time web communication services. It supports creating SignalR instances, managing connections, sending messages to clients and groups, and configuring upstream endpoints for serverless real-time messaging.
finops:
- name: Microsoft Azure Signalr Finops
  service_category: API
  slug: microsoft-azure-signalr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-signalr.png
layout: provider
modified: '2026-05-19'
name: Azure SignalR Service
nav: Providers
network: true
overview: 'Azure SignalR Service publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and SignalR API. Tagged areas include Real-Time, WebSockets, SignalR, Messaging, and Push.


  Azure SignalR Service''s developer surface includes authentication, developer portal, pricing, documentation, getting-started guide, support, engineering blog, and 9 more developer resources.'
plans:
- name: Microsoft Azure Signalr Plans Pricing
  plan_count: 3
  slug: microsoft-azure-signalr-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: Microsoft Azure Signalr Rate Limits
  slug: microsoft-azure-signalr-rate-limits
scopes:
- name: Microsoft Azure Signalr Scopes
  scope_count: 1
  slug: microsoft-azure-signalr-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 52.7
  delta: 3.2
  facets:
    commercial_clarity: 71.1
    contract_quality: 53.1
    developer_ergonomics: 45.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 49.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-signalr/refs/heads/main/screenshots/microsoft-azure-signalr-2026-06-20T185437.png
security:
- kind: authentication
  name: Microsoft Azure Signalr Authentication
  slug: microsoft-azure-signalr-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Signalr Domain Security
  slug: microsoft-azure-signalr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-signalr
tags:
- Real-Time
- WebSockets
- SignalR
- Messaging
- Push
website: https://portal.azure.com/
---
