---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Shipmonk Agentic Access
  operation_count: 19
  slug: shipmonk-agentic-access
  summary_line: 19 operations · 9 acting
api_count: 7
apis:
- description: 'The ShipMonk event surface: four HTTP callback events (order shipment notification, order status change, return status change, receiving status change) declared in the OpenAPI 3.1 webhooks block. Deli'
  name: ShipMonk Webhooks
  slug: shipmonk-webhooks
- description: 'A live Model Context Protocol endpoint served from ShipMonk''s own developer-docs host. tools/list responds anonymously with five spec-driven tools: four OpenAPI introspection tools plus execute-reques'
  name: ShipMonk MCP Server
  slug: shipmonk-mcp
- description: The Orders API from ShipMonk — 5 operation(s) for orders.
  name: ShipMonk Orders API
  slug: shipmonk-orders-api
- description: The Products API from ShipMonk — 4 operation(s) for products.
  name: ShipMonk Products API
  slug: shipmonk-products-api
- description: The Receivings API from ShipMonk — 4 operation(s) for receivings.
  name: ShipMonk Receivings API
  slug: shipmonk-receivings-api
- description: The Returns API from ShipMonk — 3 operation(s) for returns.
  name: ShipMonk Returns API
  slug: shipmonk-returns-api
- description: The Warehouses API from ShipMonk — 1 operation(s) for warehouses.
  name: ShipMonk Warehouses API
  slug: shipmonk-warehouses-api
artifact_total: 21
asyncapis:
- description: AsyncAPI 3.0 model of the ShipMonk webhook event surface, derived from the `webhooks` block of ShipMonk's own OpenAPI 3.1 document (https://apidocs.shipmonk.com/openapi/public_api.json) plus the publi
  name: ShipMonk Webhooks
  slug: shipmonk-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ShipMonk Orders API
  slug: open-shipmonk-orders-api
- collection_type: open
  name: ShipMonk Products API
  slug: open-shipmonk-products-api
- collection_type: open
  name: ShipMonk Receivings API
  slug: open-shipmonk-receivings-api
- collection_type: open
  name: ShipMonk Returns API
  slug: open-shipmonk-returns-api
- collection_type: open
  name: ShipMonk Warehouses API
  slug: open-shipmonk-warehouses-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/shipmonk-orders-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.shipmonk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.shipmonk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.shipmonk.com/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.shipmonk.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.shipmonk.com/reference/common
- group: docs
  title: ''
  type: OpenAPI
  url: https://apidocs.shipmonk.com/openapi/public_api.json
- group: operate
  title: ''
  type: Support
  url: https://support.shipmonk.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.shipmonk.com/resources/content-hub
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shipmonk-rnd
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shipmonk.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.shipmonk.com/get-a-quote
- group: start
  title: ''
  type: Login
  url: https://app.shipmonk.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shipmonk.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shipmonk.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shipmonk.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.shipmonk.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shipmonk-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.shipmonk.com/resources/content-hub/soc-2-type-ii-compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/shipmonk-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://app.shipmonk.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shipmonk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/shipmonk-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipmonk-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shipmonk-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/shipmonk-api-catalog.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/shipmonk-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shipmonk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/shipmonk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shipmonk-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shipmonk-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shipmonk-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shipmonk-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shipmonk-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shipmonk-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/shipmonk-packages.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/shipmonk-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: https://apidocs.shipmonk.com/reference/webhooks
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shipmonk-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/shipmonk-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shipmonk-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shipmonk-llms.txt
created: '2026-08-02'
description: ShipMonk is a Florida-headquartered third-party logistics (3PL) and ecommerce fulfillment provider operating a network of fulfillment centres across the United States, Canada, Mexico, the United Kingdom and Czechia. It runs an order management system for direct-to-consumer, retail/B2B and marketplace brands covering inbound receiving, inventory and lot control, pick-and-pack fulfillment, multi-carrier shipping and returns. Its public API is a single REST surface at api.shipmonk.com, described by a self-published OpenAPI 3.1 document covering orders, products and inventory, receivings, returns and warehouses, with four HTTP webhook events for shipment, order, return and receiving status changes and a contract-only sandbox environment with warehouse simulation endpoints.
image: https://files.readme.io/742121760e9d1bfa2dd7dd9dc8fb20dba2f79207e8c192facb4681cdb2bb5c23-logo.svg
layout: provider
mcp_servers:
- description: ShipMonk serves a live MCP endpoint from its own developer-docs host. tools/list responds anonymously over streamable HTTP (SSE) with five spec-driven tools. These are ReadMe's documentation-MCP tools
  name: ShipMonk MCP Server
  slug: shipmonk-mcp-server
modified: '2026-08-02'
name: ShipMonk
nav: Providers
network: true
overview: 'ShipMonk publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Orders API, Products API, and 3 more. Tagged areas include Logistics, Fulfillment, 3PL, E-Commerce, and Warehousing.


  The ShipMonk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShipMonk''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 2
  name: Shipmonk Rate Limits
  slug: shipmonk-rate-limits
score:
  band: developing
  composite: 53.5
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 62.8
    developer_ergonomics: 41.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 56.6
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shipmonk/refs/heads/main/screenshots/shipmonk-2026-08-17T081833.png
security:
- kind: authentication
  name: Shipmonk Authentication
  slug: shipmonk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shipmonk Domain Security
  slug: shipmonk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shipmonk Vulnerability Disclosure
  slug: shipmonk-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Shipmonk Trust Center
  slug: shipmonk-trust-center
  summary_line: SOC 2 Type II
slug: shipmonk
tags:
- Logistics
- Fulfillment
- 3PL
- E-Commerce
- Warehousing
- Inventory
- Shipping
- Returns
- Supply Chain
- Direct to Consumer
- Order Management
website: https://www.shipmonk.com/
---
