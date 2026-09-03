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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Primis Agentic Access
  operation_count: 42
  slug: primis-agentic-access
  summary_line: 42 operations · 25 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: The Auth API from PRIMIS — 6 operation(s) for auth.
  name: PRIMIS Auth API
  slug: primis-auth-api
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: Billing API
  name: PRIMIS Billing API
  slug: primis-billing-api
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: Campaign API
  name: PRIMIS Campaign API
  slug: primis-campaign-api
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: Documents API
  name: PRIMIS Document API
  slug: primis-document-api
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: FAQ API
  name: PRIMIS FAQ API
  slug: primis-faq-api
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: Index API
  name: PRIMIS Index API
  slug: primis-index-api
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: The Invitation API from PRIMIS — 3 operation(s) for invitation.
  name: PRIMIS Invitation API
  slug: primis-invitation-api
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: Order API
  name: PRIMIS Order API
  slug: primis-order-api
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: Product API
  name: PRIMIS Product API
  slug: primis-product-api
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: Retailer API
  name: PRIMIS Retailer API
  slug: primis-retailer-api
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: Tracking Context API
  name: PRIMIS Tracking API
  slug: primis-tracking-api
- baseURL: https://api.primis.cx
  baseurl_source: declared
  description: User API
  name: PRIMIS User API
  slug: primis-user-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: REST Auth API
  slug: open-primis-auth-api
- collection_type: open
  name: REST Auth Billing API
  slug: open-primis-billing-api
- collection_type: open
  name: REST Auth Campaign API
  slug: open-primis-campaign-api
- collection_type: open
  name: REST Auth Document API
  slug: open-primis-document-api
- collection_type: open
  name: REST Auth FAQ API
  slug: open-primis-faq-api
- collection_type: open
  name: REST Auth Index API
  slug: open-primis-index-api
- collection_type: open
  name: REST Auth Invitation API
  slug: open-primis-invitation-api
- collection_type: open
  name: REST Auth Order API
  slug: open-primis-order-api
- collection_type: open
  name: REST Auth Product API
  slug: open-primis-product-api
- collection_type: open
  name: REST Auth Retailer API
  slug: open-primis-retailer-api
- collection_type: open
  name: REST Auth Tracking API
  slug: open-primis-tracking-api
- collection_type: open
  name: REST Auth User API
  slug: open-primis-user-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/primis-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/primis-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/primis-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/primis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/primis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/primis-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://primis.cx
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.primis.cx/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.primis.cx/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.primis.cx/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://primis.cx/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://retailer.primis.cx
- group: start
  title: ''
  type: Login
  url: https://retailer.primis.cx
- group: operate
  title: ''
  type: Support
  url: https://primis.cx/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://primis.cx/privacy-centre/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/primis-llms.txt
created: '2026-07-17'
description: Primis (Primis CX) is a post-purchase customer experience platform for eCommerce retailers, headquartered in the UK and backed by 500 Global. Its products — Primis Track (branded order tracking), Primis Ship (discounted multi-carrier shipping), Primis Returns (label-less returns processing), and Primis International (cross-border logistics across 120+ carriers) — reduce "where is my order?" support volume and drive repeat purchases. Primis exposes a REST API (OpenAPI 3.0.0, 42 operations) over HTTPS with bearer-token authentication, covering retailers, orders, shipments, products, campaigns, billing, users, tracking pages, FAQs, and documents, and integrates with Shopify, BigCommerce, Adobe Commerce/Magento, WooCommerce, and carriers such as DPD, DHL, USPS, Evri, UPS, and FedEx.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/primis.png
layout: provider
mcp_servers:
- description: ''
  name: PRIMIS MCP Server
  slug: primis-mcp-server
modified: '2026-07-20'
name: PRIMIS
nav: Providers
network: true
overview: 'PRIMIS publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Billing API, Campaign API, and 9 more. Tagged areas include Company, E-Commerce, Logistics, Shipping, and Returns.


  PRIMIS''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, and 10 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 43.1
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/primis/refs/heads/main/screenshots/primis-2026-09-02T152023.png
security:
- kind: authentication
  name: Primis Authentication
  slug: primis-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Primis Domain Security
  slug: primis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: primis
tags:
- Company
- E-Commerce
- Logistics
- Shipping
- Returns
- Order Tracking
- Post-Purchase
- Customer Experience
- Fulfillment
website: https://primis.cx
---
