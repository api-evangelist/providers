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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.6
  scored_at: '2026-08-24'
api_count: 7
apis:
- description: JWT-authenticated API for partner vendors (drop-off locations, scan events) to exchange an API key for a 24-hour access token and query shipment tracking status and event history.
  name: UniUni Partner API
  slug: uniuni-partner-api
- description: Legacy enterprise integration API documented as a public Postman collection — token-based authorization, freight estimation, sorting information, batch management, shipment creation/cancellation, labe
  name: UniUni Integration API
  slug: uniuni-integration-api
- description: Group purchased shipments into batches for drop-off or pickup.
  name: UniUni Batches API
  slug: uniuni-batches-api
- description: Retrieve shipping and batch labels as Base64-encoded PDFs.
  name: UniUni Labels API
  slug: uniuni-labels-api
- description: Create, retrieve, list, purchase, refund, and delete shipments.
  name: UniUni Shipments API
  slug: uniuni-shipments-api
- description: Track shipment status and scan events.
  name: UniUni Tracking API
  slug: uniuni-tracking-api
- description: Receive real-time shipment status updates.
  name: UniUni Webhooks API
  slug: uniuni-webhooks-api
artifact_total: 17
asyncapis:
- description: ''
  name: Uniuni Webhooks
  slug: uniuni-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UniUni Platform Client Batches API
  slug: open-uniuni-batches-api
- collection_type: open
  name: UniUni Platform Client Batches Labels API
  slug: open-uniuni-labels-api
- collection_type: open
  name: UniUni Platform Client Batches Shipments API
  slug: open-uniuni-shipments-api
- collection_type: open
  name: UniUni Platform Client Batches Tracking API
  slug: open-uniuni-tracking-api
- collection_type: open
  name: UniUni Platform Client Batches Webhooks API
  slug: open-uniuni-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/uniuni-platform-client-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.uniuni.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ship.uniuni.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.ship.uniuni.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.ship.uniuni.com/en/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ship.uniuni.com/en/getting-started/welcome
- group: operate
  title: ''
  type: Support
  url: https://www.uniuni.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.uniuni.com/news/
- group: start
  title: ''
  type: SignUp
  url: https://ship.uniuni.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.ship.uniuni.com/en/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uniuni.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://docs.uniuni.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uniuni-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uniuni-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uniuni-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/uniuni-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uniuni-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uniuni-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uniuni-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uniuni-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uniuni-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/uniuni-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uniuni-domain-security.yml
created: '2026-07-17'
description: UniUni is a Canadian last-mile delivery carrier serving ecommerce businesses across Canada and the United States, delivering parcels through a crowdsourced driver network with hubs, stores, and partner drop-off locations. The UniUni Platform gives merchants shipment creation, label purchase, batching, wallet billing, tracking, and Shopify/ShipStation/WooCommerce integrations, alongside a REST Client API, a Partner API for vendor tracking updates, and a legacy Integration API for enterprise shippers.
image: https://mintcdn.com/uniexpressinc/YvoYth8Wg7rezp7U/logo/light.svg
layout: provider
mcp_servers:
- description: ''
  name: UniUni MCP Server
  slug: uniuni-mcp-server
modified: '2026-07-21'
name: UniUni
nav: Providers
network: true
overview: 'UniUni publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Batches API, Labels API, Shipments API, and 2 more. Tagged areas include Company, Logistics, Shipping, Last Mile Delivery, and E-Commerce.


  The UniUni catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  UniUni''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 49.3
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 68.4
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 7.9
  previous_composite: 49.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uniuni/refs/heads/main/screenshots/uniuni-2026-08-17T082619.png
security:
- kind: authentication
  name: Uniuni Authentication
  slug: uniuni-authentication
  summary_line: http-bearer/apiKey · 3 schemes
- kind: domain-security
  name: Uniuni Domain Security
  slug: uniuni-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uniuni
tags:
- Company
- Logistics
- Shipping
- Last Mile Delivery
- E-Commerce
- Tracking
- Delivery
website: https://www.uniuni.com/
---
