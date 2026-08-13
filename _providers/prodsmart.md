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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-12'
api_count: 16
apis:
- description: The Authorization API from Prodsmart — 1 operation(s) for authorization.
  name: Prodsmart Authorization API
  slug: prodsmart-authorization-api
- description: The Changes Feed API from Prodsmart — 1 operation(s) for changes feed.
  name: Prodsmart Changes Feed API
  slug: prodsmart-changes-feed-api
- description: The Clients API from Prodsmart — 2 operation(s) for clients.
  name: Prodsmart Clients API
  slug: prodsmart-clients-api
- description: The Downtime API from Prodsmart — 1 operation(s) for downtime.
  name: Prodsmart Downtime API
  slug: prodsmart-downtime-api
- description: The Inventory API from Prodsmart — 3 operation(s) for inventory.
  name: Prodsmart Inventory API
  slug: prodsmart-inventory-api
- description: The Machines API from Prodsmart — 2 operation(s) for machines.
  name: Prodsmart Machines API
  slug: prodsmart-machines-api
- description: The Product Families API from Prodsmart — 2 operation(s) for product families.
  name: Prodsmart Product Families API
  slug: prodsmart-product-families-api
- description: The Production Orders API from Prodsmart — 6 operation(s) for production orders.
  name: Prodsmart Production Orders API
  slug: prodsmart-production-orders-api
- description: The Productions API from Prodsmart — 2 operation(s) for productions.
  name: Prodsmart Productions API
  slug: prodsmart-productions-api
- description: The Products API from Prodsmart — 5 operation(s) for products.
  name: Prodsmart Products API
  slug: prodsmart-products-api
- description: The Punch Clock API from Prodsmart — 1 operation(s) for punch clock.
  name: Prodsmart Punch Clock API
  slug: prodsmart-punch-clock-api
- description: The Purchase Orders API from Prodsmart — 4 operation(s) for purchase orders.
  name: Prodsmart Purchase Orders API
  slug: prodsmart-purchase-orders-api
- description: The Reports API from Prodsmart — 1 operation(s) for reports.
  name: Prodsmart Reports API
  slug: prodsmart-reports-api
- description: The Sales Orders API from Prodsmart — 4 operation(s) for sales orders.
  name: Prodsmart Sales Orders API
  slug: prodsmart-sales-orders-api
- description: The Suppliers API from Prodsmart — 2 operation(s) for suppliers.
  name: Prodsmart Suppliers API
  slug: prodsmart-suppliers-api
- description: The Task Durations API from Prodsmart — 2 operation(s) for task durations.
  name: Prodsmart Task Durations API
  slug: prodsmart-task-durations-api
artifact_total: 20
asyncapis:
- description: ''
  name: Prodsmart Webhooks
  slug: prodsmart-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/prodsmart-v1-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://prodsmart.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.fusionoperations.autodesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.fusionoperations.autodesk.com/en/articles/8106718-api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://fusionoperations.autodesk.com/api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://help.fusionoperations.autodesk.com/en/articles/7257724-autodesk-fusion-operations-api
- group: operate
  title: ''
  type: Support
  url: https://help.fusionoperations.autodesk.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/prodsmart-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prodsmart-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/prodsmart-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prodsmart-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/prodsmart-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/prodsmart-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prodsmart-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prodsmart-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prodsmart-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/prodsmart-data-model.yml
created: '2026-07-17'
description: Prodsmart is a cloud manufacturing execution system (MES) and production management platform for small and mid-sized manufacturers, covering production tracking, inventory, sales and purchasing, quality, scheduling and material requirements, asset maintenance, and shop-floor analytics across mobile and desktop. Founded as Prodsmart and acquired by Autodesk in 2021, it is now offered as Autodesk Fusion Operations. It exposes a documented REST API (a deprecated v1 surface at fusionoperations.autodesk.com/api/v1 and a current v2 API on Autodesk Platform Services), authenticated with an API Key/Secret via HTTP Basic that mints a 2-hour token, plus webhooks, a Changes Feed, and Zapier and Power BI integrations. This profile was surfaced as a portfolio company of 500 Global and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prodsmart.png
layout: provider
mcp_servers:
- description: ''
  name: prodsmart-mcp.yml
  slug: prodsmart-mcpyml
modified: '2026-07-20'
name: Prodsmart
nav: Providers
network: true
overview: 'Prodsmart publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Changes Feed API, Clients API, and 13 more. Tagged areas include Company, Manufacturing, Manufacturing Execution System, Production Management, and Inventory.


  The Prodsmart catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Prodsmart''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, and 11 more developer resources.'
random_paper: 28
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 60.4
    developer_ergonomics: 52.2
    discoverability: 81.5
    governance: 8.3
    operational_transparency: 31.6
  previous_composite: 38.8
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Prodsmart Authentication
  slug: prodsmart-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Prodsmart Domain Security
  slug: prodsmart-domain-security
  summary_line: TLSv1.2 · DMARC
slug: prodsmart
tags:
- Company
- Manufacturing
- Manufacturing Execution System
- Production Management
- Inventory
- Shop Floor
- Autodesk
- Industry 4.0
website: https://prodsmart.com
---
