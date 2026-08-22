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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Primis Agentic Access
  operation_count: 42
  slug: primis-agentic-access
  summary_line: 42 operations · 25 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: The Auth API from PRIMIS — 6 operation(s) for auth.
  name: PRIMIS Auth API
  slug: primis-auth-api
- description: Billing API
  name: PRIMIS Billing API
  slug: primis-billing-api
- description: Campaign API
  name: PRIMIS Campaign API
  slug: primis-campaign-api
- description: Documents API
  name: PRIMIS Document API
  slug: primis-document-api
- description: FAQ API
  name: PRIMIS FAQ API
  slug: primis-faq-api
- description: Index API
  name: PRIMIS Index API
  slug: primis-index-api
- description: The Invitation API from PRIMIS — 3 operation(s) for invitation.
  name: PRIMIS Invitation API
  slug: primis-invitation-api
- description: Order API
  name: PRIMIS Order API
  slug: primis-order-api
- description: Product API
  name: PRIMIS Product API
  slug: primis-product-api
- description: Retailer API
  name: PRIMIS Retailer API
  slug: primis-retailer-api
- description: Tracking Context API
  name: PRIMIS Tracking API
  slug: primis-tracking-api
- description: User API
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
  name: primis-mcp.yml
  slug: primis-mcpyml
modified: '2026-07-20'
name: PRIMIS
nav: Providers
network: true
overview: 'PRIMIS publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Billing API, Campaign API, and 9 more. Tagged areas include Company, eCommerce, Logistics, Shipping, and Returns.


  PRIMIS''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, and 9 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 36.6
  delta: 0.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 44.3
    developer_ergonomics: 42.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
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
- eCommerce
- Logistics
- Shipping
- Returns
- Order Tracking
- Post-Purchase
- Customer Experience
- Fulfillment
website: https://primis.cx
---
