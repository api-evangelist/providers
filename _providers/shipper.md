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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: HTTP-based API (v3) for interacting with Shipper's location, pricing, and shipment features — search location by keyword and administrative area, retrieve domestic multi-courier pricing, create orders
  name: Shipper Logistics API
  slug: shipper-logistics-api
artifact_total: 5
asyncapis:
- description: ''
  name: Shipper Webhooks
  slug: shipper-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://shipper.id/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://logistics-docs.shipper.id/
- group: docs
  title: ''
  type: Documentation
  url: https://logistics-docs.shipper.id/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://logistics-docs.shipper.id/
- group: start
  title: ''
  type: GettingStarted
  url: https://logistics-docs.shipper.id/docs/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/shipper-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shipper-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shipper-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shipper-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shipper-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shipper-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shipper-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shipper-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipper-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shipper-conformance.yml
- group: start
  title: ''
  type: SignUp
  url: https://bos.sandbox.shipper.id
- group: operate
  title: ''
  type: Support
  url: http://faq.shipper.id/
- group: company
  title: ''
  type: Blog
  url: https://shipper.id/en/blog/
created: '2026-07-17'
description: Shipper is an Indonesian technology-driven logistics aggregator that connects merchants and e-commerce sellers to hundreds of third-party courier and last-mile delivery partners through a single platform. Its services span a logistics aggregator (multi-courier rate check, order creation, pickup and tracking), nationwide fulfillment and warehousing, contract logistics, international freight forwarding, and e-commerce enablement. Developers integrate via the HTTP-based Shipper Logistics API (v3), which exposes location search, domestic pricing, order creation (including COD), shipping label and receipt generation, pickup request, and shipment status tracking, with real-time delivery-status webhooks. Backed by Lightspeed Venture Partners, Partech, and Prosus Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shipper.png
layout: provider
mcp_servers:
- description: ''
  name: Shipper MCP Server
  slug: shipper-mcp-server
modified: '2026-07-21'
name: Shipper
nav: Providers
network: true
overview: 'Shipper publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Shipping, Fulfillment, and Supply Chain.


  The Shipper catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Shipper''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, signup flow, support, and 11 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 51.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 32.4
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shipper/refs/heads/main/screenshots/shipper-2026-09-02T155228.png
security:
- kind: authentication
  name: Shipper Authentication
  slug: shipper-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shipper Domain Security
  slug: shipper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shipper
tags:
- Company
- Logistics
- Shipping
- Fulfillment
- Supply Chain
- E-Commerce
- Last Mile Delivery
- Couriers
- Indonesia
website: https://shipper.id/
---
