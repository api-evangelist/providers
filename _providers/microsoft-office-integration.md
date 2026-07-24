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
- acting_count: 2
  human_in_the_loop: 1
  name: Microsoft Office Integration Agentic Access
  operation_count: 10
  slug: microsoft-office-integration-agentic-access
  summary_line: 10 operations · 2 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The CurrentStatus API from Microsoft Office Integration — 1 operation(s) for currentstatus.
  name: Microsoft Office Integration CurrentStatus API
  slug: microsoft-office-integration-currentstatus-api
- description: The HistoricalStatus API from Microsoft Office Integration — 1 operation(s) for historicalstatus.
  name: Microsoft Office Integration HistoricalStatus API
  slug: microsoft-office-integration-historicalstatus-api
- description: The Messages API from Microsoft Office Integration — 1 operation(s) for messages.
  name: Microsoft Office Integration Messages API
  slug: microsoft-office-integration-messages-api
- description: The Resources API from Microsoft Office Integration — 1 operation(s) for resources.
  name: Microsoft Office Integration Resources API
  slug: microsoft-office-integration-resources-api
- description: The Services API from Microsoft Office Integration — 1 operation(s) for services.
  name: Microsoft Office Integration Services API
  slug: microsoft-office-integration-services-api
- description: The Subscriptions API from Microsoft Office Integration — 5 operation(s) for subscriptions.
  name: Microsoft Office Integration Subscriptions API
  slug: microsoft-office-integration-subscriptions-api
artifact_total: 23
collections:
- collection_type: open
  name: Microsoft Office Integration Microsoft Office 365 Management Activity API
  slug: open-microsoft-office-management-activity-api
- collection_type: open
  name: Microsoft Office Integration Microsoft Office 365 Service Communications API
  slug: open-microsoft-office-service-communications-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-office-integration-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-office-integration-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-office-integration-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-office-integration-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/office/office-365-management-api/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/office/office-365-management-api/get-started-with-office-365-management-apis
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/graph
created: '2025-01-01'
description: APIs for Microsoft Office Integration, connecting Microsoft Office components and systems for seamless data exchange and end-to-end workflows across multiple technologies and platforms. The Office 365 Management APIs provide a single extensibility platform for management tasks including service communications, security, compliance, reporting, and auditing, using common industry-standard approaches including OAuth v2, OData v4, and JSON.
finops:
- name: Microsoft Office Integration Finops
  service_category: API
  slug: microsoft-office-integration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-office-integration.png
json_schemas:
- name: ActivityRecord
  property_count: 12
  slug: activity-record
- name: ContentBlob
  property_count: 5
  slug: content-blob
- name: Message
  property_count: 13
  slug: message
- name: Service
  property_count: 3
  slug: service
- name: Subscription
  property_count: 3
  slug: subscription
- name: WorkloadStatus
  property_count: 7
  slug: workload-status
jsonld:
- class_count: 0
  name: Microsoft Office Integration Context
  property_count: 6
  slug: microsoft-office-integration-context
layout: provider
modified: '2026-05-19'
name: Microsoft Office Integration
nav: Providers
network: true
overview: 'Microsoft Office Integration publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CurrentStatus API, HistoricalStatus API, Messages API, and 3 more. Tagged areas include Microsoft 365, Microsoft Office Integration, and Office 365.


  The Microsoft Office Integration catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Office Integration''s developer surface includes authentication, documentation, getting-started guide, developer portal, and 5 more developer resources.'
plans:
- name: Microsoft Office Integration Plans Pricing
  plan_count: 3
  slug: microsoft-office-integration-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 5
  name: Microsoft Office Integration Rate Limits
  slug: microsoft-office-integration-rate-limits
rules:
- name: Microsoft Office Integration API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-office-integration-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.3
    developer_ergonomics: 39.1
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 49.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-office-integration/refs/heads/main/screenshots/microsoft-office-integration-2026-06-20T185512.png
security:
- kind: authentication
  name: Microsoft Office Integration Authentication
  slug: microsoft-office-integration-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Office Integration Domain Security
  slug: microsoft-office-integration-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Office Integration Vulnerability Disclosure
  slug: microsoft-office-integration-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-office-integration
tags:
- Microsoft 365
- Microsoft Office Integration
- Office 365
website: https://developer.microsoft.com/en-us/graph
---
