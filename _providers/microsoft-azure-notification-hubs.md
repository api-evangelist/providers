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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Azure Notification Hubs Agentic Access
  operation_count: 5
  slug: microsoft-azure-notification-hubs-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 3
apis:
- description: The Installations API from Azure Notification Hubs — 1 operation(s) for installations.
  name: Azure Notification Hubs Installations API
  slug: microsoft-azure-notification-hubs-installations-api
- description: The Notifications API from Azure Notification Hubs — 1 operation(s) for notifications.
  name: Azure Notification Hubs Notifications API
  slug: microsoft-azure-notification-hubs-notifications-api
- description: The Registrations API from Azure Notification Hubs — 1 operation(s) for registrations.
  name: Azure Notification Hubs Registrations API
  slug: microsoft-azure-notification-hubs-registrations-api
artifact_total: 10
collections:
- collection_type: open
  name: Azure Notification Hubs REST API
  slug: open-microsoft-azure-notification-hubs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-notification-hubs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-notification-hubs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-notification-hubs-authentication.yml
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
  url: https://azure.microsoft.com/en-us/pricing/details/notification-hubs/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/notification-hubs/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/notification-hubs
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
created: '2026-03-13'
description: Azure Notification Hubs is a massively scalable mobile push notification engine that enables sending push notifications to iOS, Android, Windows, and other platforms. It supports device registration, tag-based routing, template notifications, scheduled sends, and telemetry for tracking delivery metrics.
finops:
- name: Microsoft Azure Notification Hubs Finops
  service_category: API
  slug: microsoft-azure-notification-hubs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-notification-hubs.png
layout: provider
modified: '2026-05-19'
name: Azure Notification Hubs
nav: Providers
network: true
overview: 'Azure Notification Hubs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Installations API, Notifications API, and Registrations API. Tagged areas include Cross-Platform, Messaging, Mobile, Notifications, and Push Notifications.


  Azure Notification Hubs'' developer surface includes authentication, developer portal, pricing, documentation, signup flow, support, and 7 more developer resources.'
plans:
- name: Microsoft Azure Notification Hubs Plans Pricing
  plan_count: 3
  slug: microsoft-azure-notification-hubs-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Microsoft Azure Notification Hubs Rate Limits
  slug: microsoft-azure-notification-hubs-rate-limits
score:
  band: developing
  composite: 48.2
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 53.1
    developer_ergonomics: 32.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 48.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-notification-hubs/refs/heads/main/screenshots/microsoft-azure-notification-hubs-2026-06-20T185428.png
security:
- kind: authentication
  name: Microsoft Azure Notification Hubs Authentication
  slug: microsoft-azure-notification-hubs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Azure Notification Hubs Domain Security
  slug: microsoft-azure-notification-hubs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-notification-hubs
tags:
- Cross-Platform
- Messaging
- Mobile
- Notifications
- Push Notifications
website: https://azure.microsoft.com/en-us/products/notification-hubs
---
