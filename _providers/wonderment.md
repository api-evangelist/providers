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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wonderment Agentic Access
  operation_count: 4
  slug: wonderment-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: Delivery-date predictions for shipping methods.
  name: Wonderment Delivery Promise API
  slug: wonderment-delivery-promise-api
- description: List and download shipment report exports.
  name: Wonderment Reports API
  slug: wonderment-reports-api
- description: Search shipments and tracking events for the authenticated shop.
  name: Wonderment Shipments API
  slug: wonderment-shipments-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: List the authenticated shop's shipment report exports and download the most recent finished, non-expired report.
  name: Wonderment — export and download a shipment report
  slug: wonderment-report-export
artifact_total: 10
asyncapis:
- description: ''
  name: Wonderment Webhooks
  slug: wonderment-webhooks
common:
- group: docs
  title: ''
  type: Documentation
  url: https://wonderment.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://wonderment.readme.io/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://help.wonderment.com/en/categories/1026689-getting-started-with-track
- group: operate
  title: ''
  type: Support
  url: https://help.wonderment.com/
- group: start
  title: ''
  type: Login
  url: https://app.wonderment.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wonderment-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wonderment-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wonderment-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wonderment-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wonderment-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wonderment-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wonderment-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wonderment-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wonderment-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/wonderment-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wonderment-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wonderment-report-export.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wonderment-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wonderment.com/
created: '2026-07-17'
description: Wonderment is a post-purchase order-tracking and shipment-visibility platform for ecommerce brands (built for Shopify), now part of Loop as Loop Tracking. It ingests carrier tracking data, surfaces proactive delivery updates, powers branded self-serve tracking pages, and reports on shipment performance. The public REST API (versioned 2022-10, hosted at api.wonderment.com) lets merchants search shipments by order name or tracking code, list and download shipment report exports, and fetch delivery-date predictions for shipping methods, plus webhooks for shipping events. Originally a CRV-backed company, added to the API Evangelist network and enriched from its ReadMe developer hub.
image: https://www.wonderment.com/
layout: provider
mcp_servers:
- description: ''
  name: wonderment-mcp.yml
  slug: wonderment-mcpyml
modified: '2026-07-21'
name: Wonderment
nav: Providers
network: true
overview: 'Wonderment publishes 3 APIs on the [APIs.io](https://apis.io/) network: Delivery Promise API, Reports API, and Shipments API. Tagged areas include Company, Ecommerce, Order Tracking, Post-Purchase, and Shipping.


  The Wonderment catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wonderment''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 15 more developer resources.'
random_paper: 64
score:
  band: thin
  composite: 39.9
  delta: -2.5
  facets:
    commercial_clarity: 13.2
    contract_quality: 70.9
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wonderment Authentication
  slug: wonderment-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wonderment Domain Security
  slug: wonderment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wonderment
tags:
- Company
- Ecommerce
- Order Tracking
- Post-Purchase
- Shipping
- Logistics
- Shopify
- Webhooks
website: https://www.wonderment.com/
---
