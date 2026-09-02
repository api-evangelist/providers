---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'A valid JSON Web Token (JWT) is required to access API methods. A JWT access token must be included in the authorization header of each request in the following Bearer schema: ``` Authorization: Beare'
  name: PartsTech Auth API
  slug: partstech-auth-api
- description: Easy Registration & Auto-Connect API
  name: PartsTech Auto Connect API
  slug: partstech-auto-connect-api
- description: Brands
  name: PartsTech Brands API
  slug: partstech-brands-api
- description: Callback
  name: PartsTech Callback Cart API
  slug: partstech-callback-cart-api
- description: Custom Cart
  name: PartsTech Custom Cart API
  slug: partstech-custom-cart-api
- description: EX Permissions
  name: PartsTech Ex Permissions API
  slug: partstech-ex-permissions-api
- description: Jobs
  name: PartsTech Jobs API
  slug: partstech-jobs-api
- description: Local inventory
  name: PartsTech Local Inventory API
  slug: partstech-local-inventory-api
- description: Vehicles
  name: PartsTech Mitchell1 API
  slug: partstech-mitchell1-api
- description: Labor
  name: PartsTech Mitchell1 Labor API
  slug: partstech-mitchell1-labor-api
- description: Fluids
  name: PartsTech Motor Fluids API
  slug: partstech-motor-fluids-api
- description: Labor
  name: PartsTech Motor Labor API
  slug: partstech-motor-labor-api
- description: Maintenance Schedules
  name: PartsTech Motor Maintenance Schedules API
  slug: partstech-motor-maintenance-schedules-api
- description: Specifications
  name: PartsTech Motor Specifications API
  slug: partstech-motor-specifications-api
- description: Orders
  name: PartsTech Orders API
  slug: partstech-orders-api
- description: Orders methods
  name: PartsTech Partner Orders API
  slug: partstech-partner-orders-api
- description: Parts
  name: PartsTech Parts API
  slug: partstech-parts-api
- description: Product Characteristics Database
  name: PartsTech Pcdb API
  slug: partstech-pcdb-api
- description: Cart with Punchout
  name: PartsTech Punchout Cart API
  slug: partstech-punchout-cart-api
- description: Punchout Orders
  name: PartsTech Punchout Orders API
  slug: partstech-punchout-orders-api
- description: Quote Methods
  name: PartsTech Punchout Quote API
  slug: partstech-punchout-quote-api
- description: Quoting
  name: PartsTech Quoting API
  slug: partstech-quoting-api
- description: Search
  name: PartsTech Search API
  slug: partstech-search-api
- description: Cart by Session
  name: PartsTech Session Cart API
  slug: partstech-session-cart-api
- description: Shop
  name: PartsTech Shop API
  slug: partstech-shop-api
- description: Shop methods
  name: PartsTech Shops API
  slug: partstech-shops-api
- description: Supplier Preferences
  name: PartsTech Supplier Preferences API
  slug: partstech-supplier-preferences-api
- description: Supplier methods
  name: PartsTech Suppliers API
  slug: partstech-suppliers-api
- description: Tires
  name: PartsTech Tires API
  slug: partstech-tires-api
- description: User Methods
  name: PartsTech User API
  slug: partstech-user-api
- description: Users methods
  name: PartsTech Users API
  slug: partstech-users-api
- description: Vehicle Configuration Database
  name: PartsTech Vcdb API
  slug: partstech-vcdb-api
- description: VIN Methods
  name: PartsTech Vin API
  slug: partstech-vin-api
artifact_total: 39
asyncapis:
- description: ''
  name: Partstech Webhooks
  slug: partstech-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/partstech-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/partstech-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/partstech-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://partstech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.partstech.com/openapi.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.partstech.com/openapi.yaml
- group: operate
  title: ''
  type: Support
  url: https://partstech.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://partstech.my.site.com/help/s/
- group: start
  title: ''
  type: GettingStarted
  url: https://partstech.my.site.com/help/s/article/Getting-Started-With-Partstech
- group: company
  title: ''
  type: Blog
  url: https://partstech.com/resource/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/partstech
- group: commercial
  title: ''
  type: Pricing
  url: https://partstech.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.partstech.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.partstech.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://partstech.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://partstech.com/privacy-policy/
- group: commercial
  title: ''
  type: Plans
  url: plans/partstech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/partstech-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/partstech-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/partstech-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/partstech-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/partstech-sandbox.yml
created: '2026-08-26'
description: PartsTech is a web-based automotive parts and tire procurement platform for repair shops, tire shops and dealers, connecting more than 30,000 shops to 300+ aftermarket parts and tire suppliers across 30,000+ distribution locations through a single search, quote and ordering workflow. Founded by Greg Kirber and Erik St. Pierre and acquired by OEConnection (OEC) in 2025, PartsTech pairs its shop-facing web application with a partner-facing REST API — the PartsTech External API — used by 35+ shop management systems (SMS), point-of-sale and estimating vendors to embed parts search, VIN and license plate decoding, ACES/PCdb/VCdb taxonomy lookups, live wholesale pricing and availability, punchout carts, quoting, tire search, MOTOR and Mitchell 1 labor/maintenance content, order history and local inventory into their own software.
image: https://partstech.com/wp-content/uploads/2024/04/partstech-fb-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: PartsTech MCP Server
  slug: partstech-mcp-server
modified: '2026-08-26'
name: PartsTech
nav: Providers
network: true
overview: 'PartsTech publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Auto Connect API, Brands API, and 30 more. Tagged areas include Company, Automotive, Auto Parts, Parts Procurement, and Tires.


  The PartsTech catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PartsTech''s developer surface includes documentation, API reference, support, getting-started guide, engineering blog, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Partstech Plans Pricing
  plan_count: 3
  slug: partstech-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Partstech Rate Limits
  slug: partstech-rate-limits
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 61.1
    developer_ergonomics: 56.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 53.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Partstech Authentication
  slug: partstech-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Partstech Domain Security
  slug: partstech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: partstech
tags:
- Company
- Automotive
- Auto Parts
- Parts Procurement
- Tires
- E-Commerce
- Ordering
- Catalog
- Vehicle Data
- VIN Decoding
- Shop Management
- Punchout
- Marketplace
- Supply Chain
website: https://partstech.com/
---
