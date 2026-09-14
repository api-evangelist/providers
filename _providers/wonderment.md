---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - '{''url'': ''https://www.wonderment.com/'', ''status'': 302, ''note'': ''declared website redirects to https://www.loopreturns.com/wonderment-is-now-loop-tracking/ — a different registrable domain (wonderment.com -> loopreturns.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wonderment Agentic Access
  operation_count: 4
  slug: wonderment-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.wonderment.com
  baseurl_source: declared
  description: Delivery-date predictions for shipping methods.
  name: Wonderment Delivery Promise API
  slug: wonderment-delivery-promise-api
- baseURL: https://api.wonderment.com
  baseurl_source: declared
  description: List and download shipment report exports.
  name: Wonderment Reports API
  slug: wonderment-reports-api
- baseURL: https://api.wonderment.com
  baseurl_source: declared
  description: Search shipments and tracking events for the authenticated shop.
  name: Wonderment Shipments API
  slug: wonderment-shipments-api
arazzos:
- description: List the authenticated shop's shipment report exports and download the most recent finished, non-expired report.
  name: Wonderment — export and download a shipment report
  slug: wonderment-report-export
artifact_total: 12
asyncapis:
- description: ''
  name: Wonderment Webhooks
  slug: wonderment-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wonderment Delivery Promise API
  slug: open-wonderment-delivery-promise-api
- collection_type: open
  name: Wonderment Delivery Promise Reports API
  slug: open-wonderment-reports-api
- collection_type: open
  name: Wonderment Delivery Promise Shipments API
  slug: open-wonderment-shipments-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/wonderment-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/wonderment-openapi-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: Wonderment
nav: Providers
network: true
overview: 'Wonderment publishes 3 APIs on the [APIs.io](https://apis.io/) network: Delivery Promise API, Reports API, and Shipments API. Tagged areas include Company, E-Commerce, Order Tracking, Post-Purchase, and Shipping.


  The Wonderment catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wonderment''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 17 more developer resources.'
random_paper: 20
screenshot: https://raw.githubusercontent.com/api-evangelist/wonderment/refs/heads/main/screenshots/wonderment-2026-09-02T170915.png
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
- E-Commerce
- Order Tracking
- Post-Purchase
- Shipping
- Logistics
- Shopify
- Webhook
website: https://www.wonderment.com/
---
