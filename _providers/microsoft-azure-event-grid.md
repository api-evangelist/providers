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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Event Grid Agentic Access
  operation_count: 7
  slug: microsoft-azure-event-grid-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Operations operations
  name: Azure Event Grid Operations API
  slug: microsoft-azure-event-grid-operations-api
- description: Topics operations
  name: Azure Event Grid Topics API
  slug: microsoft-azure-event-grid-topics-api
artifact_total: 10
collections:
- collection_type: open
  name: Azure Event Grid REST API
  slug: open-microsoft-azure-event-grid
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-event-grid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-event-grid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-event-grid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-event-grid-scopes.yml
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
  url: https://azure.microsoft.com/en-us/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/
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
created: '2024-01-01'
description: Azure Event Grid provides APIs for publishing events to custom topics, managing event subscriptions with filtering, and configuring event delivery to endpoints including webhooks, Azure Functions, Event Hubs, and Storage Queues. It supports dead-lettering, retry policies, and custom event schemas.
finops:
- name: Microsoft Azure Event Grid Finops
  service_category: API
  slug: microsoft-azure-event-grid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-event-grid.png
layout: provider
modified: '2026-05-19'
name: Azure Event Grid
nav: Providers
network: true
overview: 'Azure Event Grid publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Topics API. Tagged areas include Events, Event-Driven, Pub-Sub, and Serverless.


  Azure Event Grid''s developer surface includes authentication, developer portal, pricing, documentation, support, and 6 more developer resources.'
plans:
- name: Microsoft Azure Event Grid Plans Pricing
  plan_count: 3
  slug: microsoft-azure-event-grid-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Microsoft Azure Event Grid Rate Limits
  slug: microsoft-azure-event-grid-rate-limits
scopes:
- name: Microsoft Azure Event Grid Scopes
  scope_count: 1
  slug: microsoft-azure-event-grid-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.8
    developer_ergonomics: 32.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-event-grid/refs/heads/main/screenshots/microsoft-azure-event-grid-2026-06-20T185413.png
security:
- kind: authentication
  name: Microsoft Azure Event Grid Authentication
  slug: microsoft-azure-event-grid-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Event Grid Domain Security
  slug: microsoft-azure-event-grid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-event-grid
tags:
- Events
- Event-Driven
- Pub-Sub
- Serverless
website: https://portal.azure.com/
---
