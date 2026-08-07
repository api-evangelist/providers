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
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Azure Queue Storage Agentic Access
  operation_count: 7
  slug: microsoft-azure-queue-storage-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- description: Queues operations
  name: Azure Queue Storage Queues API
  slug: microsoft-azure-queue-storage-queues-api
artifact_total: 8
collections:
- collection_type: open
  name: Azure Queue Storage REST API
  slug: open-microsoft-azure-queue-storage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-queue-storage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-queue-storage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-queue-storage-authentication.yml
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
  url: https://azure.microsoft.com/en-us/pricing/details/storage/queues/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/storage/queues/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/storage/queues/storage-quickstart-queues-portal
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction
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
  url: https://azure.microsoft.com/en-us/blog/product/storage/
created: '2026-03-13'
description: Azure Queue Storage is a Microsoft cloud service for storing large numbers of messages, enabling decoupled and asynchronous communication between application components. Messages can be accessed via authenticated HTTP/HTTPS calls and support visibility timeouts, peeking, and metadata for reliable processing.
finops:
- name: Microsoft Azure Queue Storage Finops
  service_category: API
  slug: microsoft-azure-queue-storage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-queue-storage.png
layout: provider
modified: '2026-05-19'
name: Azure Queue Storage
nav: Providers
network: true
overview: 'Azure Queue Storage publishes 1 API on the [APIs.io](https://apis.io/) network: Queues API. Tagged areas include Asynchronous Processing, Cloud Storage, Messaging, Queue, and Storage.


  Azure Queue Storage''s developer surface includes authentication, developer portal, pricing, documentation, getting-started guide, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Azure Queue Storage Plans Pricing
  plan_count: 3
  slug: microsoft-azure-queue-storage-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Microsoft Azure Queue Storage Rate Limits
  slug: microsoft-azure-queue-storage-rate-limits
score:
  band: developing
  composite: 48.8
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 56.6
    developer_ergonomics: 52.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-queue-storage/refs/heads/main/screenshots/microsoft-azure-queue-storage-2026-06-20T185432.png
security:
- kind: authentication
  name: Microsoft Azure Queue Storage Authentication
  slug: microsoft-azure-queue-storage-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Microsoft Azure Queue Storage Domain Security
  slug: microsoft-azure-queue-storage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-queue-storage
tags:
- Asynchronous Processing
- Cloud Storage
- Messaging
- Queue
- Storage
website: https://portal.azure.com/
---
