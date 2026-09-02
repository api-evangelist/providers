---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.1
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: REST API for Lightspeed Retail R-Series (formerly Vend) providing access to sales, inventory, customers, products, and reporting data for retail point-of-sale systems.
  name: Lightspeed Retail R-Series API
  slug: retail-r-series
- description: REST API for Lightspeed eCom (C-Series) e-commerce platform providing endpoints for products, orders, customers, shipments, payments, and inventory management. Requires Advanced or Professional subscr
  name: Lightspeed eCom API
  slug: ecom-c-series
- description: REST API for Lightspeed eCom E-Series, the Ecwid storefront platform Lightspeed acquired in 2021 and now sells as eCom E-Series. Provides store profile, product catalog, categories, orders, customers,
  name: Lightspeed eCom E-Series (Ecwid) API
  slug: ecom-e-series
- description: REST API for Lightspeed Restaurant O-Series, the Kounta hospitality point-of-sale platform Lightspeed acquired in 2019 and sells as O-Series. Exposes sites, registers, products, categories, orders, cu
  name: Lightspeed Restaurant O-Series (Kounta) API
  slug: restaurant-o-series
- description: Partner REST API for Lightspeed Golf, the Chronogolf tee-sheet and golf course management platform Lightspeed acquired in 2019. Covers organizations, courses, tee times, green fees, reservations and c
  name: Lightspeed Golf (Chronogolf) Partner API
  slug: golf-g-series
- description: Audit and security operations
  name: Lightspeed Commerce Audit API
  slug: lightspeed-audit-api
- description: Brand operations
  name: Lightspeed Commerce Brands API
  slug: lightspeed-brands-api
- description: A log of requests and responses between Lightspeed and an integration channel.
  name: Lightspeed Commerce Channel Request Log API
  slug: lightspeed-channel-request-log-api
- description: Consignment Product operations
  name: Lightspeed Commerce Consignment Products API
  slug: lightspeed-consignment-products-api
- description: Stock control operations
  name: Lightspeed Commerce Consignments API
  slug: lightspeed-consignments-api
- description: Customer Address operations
  name: Lightspeed Commerce Customer Addresses API
  slug: lightspeed-customer-addresses-api
- description: Customer Group operations
  name: Lightspeed Commerce Customer Groups API
  slug: lightspeed-customer-groups-api
- description: Customer operations
  name: Lightspeed Commerce Customers API
  slug: lightspeed-customers-api
- description: 'V1 endpoints (`/f/finance/...`) for retrieving sales and financial data. For the newer V2 versions of these endpoints see FinancialV2 ### V1 behaviour - **Sorting**: No guaranteed sorting order; inter'
  name: Lightspeed Commerce Financial API
  slug: lightspeed-financial-api
- description: 'V2 endpoints (`/f/v2/...`) for retrieving sales and financial data. ### Endpoint Mapping | V1 Endpoint | V2 Endpoint | |-------------|-------------| | `getFinancials` (`/f/finance/{id}/financials/{fro'
  name: Lightspeed Commerce Financial V2 API
  slug: lightspeed-financialv2-api
- description: Fulfillment operations
  name: Lightspeed Commerce Fulfillments API
  slug: lightspeed-fulfillments-api
- description: Gift Card operations
  name: Lightspeed Commerce Gift Cards API
  slug: lightspeed-gift-cards-api
- description: The ID Cards API from Lightspeed Commerce — 2 operation(s) for id cards.
  name: Lightspeed Commerce ID Cards API
  slug: lightspeed-id-cards-api
- description: Inventory operations
  name: Lightspeed Commerce Inventory API
  slug: lightspeed-inventory-api
- description: The Items API from Lightspeed Commerce — 2 operation(s) for items.
  name: Lightspeed Commerce Items API
  slug: lightspeed-items-api
- description: The Loyalty Adjustments [BETA] API from Lightspeed Commerce — 1 operation(s) for loyalty adjustments [beta].
  name: Lightspeed Commerce Loyalty Adjustments [BETA] API
  slug: lightspeed-loyalty-adjustments-beta-api
- description: The Order and Pay API from Lightspeed Commerce — 19 operation(s) for order and pay.
  name: Lightspeed Commerce Order and Pay API
  slug: lightspeed-order-and-pay-api
- description: 'The Order and Pay: Webhook API from Lightspeed Commerce — 4 operation(s) for order and pay: webhook.'
  name: 'Lightspeed Commerce Order and Pay: Webhook API'
  slug: lightspeed-order-and-pay-webhook-api
- description: Outlet Product Tax operations
  name: Lightspeed Commerce Outlet Product Taxes API
  slug: lightspeed-outlet-product-taxes-api
- description: Outlet operations
  name: Lightspeed Commerce Outlets API
  slug: lightspeed-outlets-api
- description: Packing slip rendering operations
  name: Lightspeed Commerce Packing Slips API
  slug: lightspeed-packing-slips-api
- description: Partner Billing operations
  name: Lightspeed Commerce Partner Billing API
  slug: lightspeed-partner-billing-api
- description: Payment Type operations
  name: Lightspeed Commerce Payment Types API
  slug: lightspeed-payment-types-api
- description: The PMS API from Lightspeed Commerce — 3 operation(s) for pms.
  name: Lightspeed Commerce PMS API
  slug: lightspeed-pms-api
- description: The PMS Integration API from Lightspeed Commerce — 0 operation(s) for pms integration.
  name: Lightspeed Commerce PMS Integration API
  slug: lightspeed-pms-integration-api
- description: Price Book operations
  name: Lightspeed Commerce Price Books API
  slug: lightspeed-price-books-api
- description: Product Categories operations
  name: Lightspeed Commerce Product Categories API
  slug: lightspeed-product-categories-api
- description: Product Image operations
  name: Lightspeed Commerce Product Images API
  slug: lightspeed-product-images-api
- description: Product Type operations
  name: Lightspeed Commerce Product Types API
  slug: lightspeed-product-types-api
- description: Product operations
  name: Lightspeed Commerce Products API
  slug: lightspeed-products-api
- description: The Promo Code API from Lightspeed Commerce — 2 operation(s) for promo code.
  name: Lightspeed Commerce Promo Code API
  slug: lightspeed-promo-code-api
- description: Promotion operations
  name: Lightspeed Commerce Promotions API
  slug: lightspeed-promotions-api
- description: Purchase order operations
  name: Lightspeed Commerce Purchase Orders API
  slug: lightspeed-purchase-orders-api
- description: Quotes operations
  name: Lightspeed Commerce Quotes API
  slug: lightspeed-quotes-api
- description: Register operations
  name: Lightspeed Commerce Registers API
  slug: lightspeed-registers-api
- description: The Reservations for Platforms API from Lightspeed Commerce — 11 operation(s) for reservations for platforms.
  name: Lightspeed Commerce Reservations for Platforms API
  slug: lightspeed-reservations-for-platforms-api
- description: Retailer operations
  name: Lightspeed Commerce Retailers API
  slug: lightspeed-retailers-api
- description: The Rich Item API from Lightspeed Commerce — 6 operation(s) for rich item.
  name: Lightspeed Commerce Rich Item API
  slug: lightspeed-rich-item-api
- description: Sale operations
  name: Lightspeed Commerce Sales API
  slug: lightspeed-sales-api
- description: Search related operations
  name: Lightspeed Commerce Search API
  slug: lightspeed-search-api
- description: Serial number related operations
  name: Lightspeed Commerce Serial Numbers API
  slug: lightspeed-serial-numbers-api
- description: Service orders and Job management
  name: Lightspeed Commerce Service Orders API
  slug: lightspeed-service-orders-api
- description: The Shifts API from Lightspeed Commerce — 1 operation(s) for shifts.
  name: Lightspeed Commerce Shifts API
  slug: lightspeed-shifts-api
- description: Staff API. Authorisation Code grant type is required for this API with permission ROLE_CONFIG_USERS.
  name: Lightspeed Commerce Staff API
  slug: lightspeed-staff-api
- description: Store Credit operations
  name: Lightspeed Commerce Store Credits API
  slug: lightspeed-store-credits-api
- description: Supplier operations
  name: Lightspeed Commerce Suppliers API
  slug: lightspeed-suppliers-api
- description: Tag operations
  name: Lightspeed Commerce Tags API
  slug: lightspeed-tags-api
- description: The Tax Breakdown API from Lightspeed Commerce — 1 operation(s) for tax breakdown.
  name: Lightspeed Commerce Tax Breakdown API
  slug: lightspeed-tax-breakdown-api
- description: Tax operations
  name: Lightspeed Commerce Taxes API
  slug: lightspeed-taxes-api
- description: User operations
  name: Lightspeed Commerce Users API
  slug: lightspeed-users-api
- description: The Variant Attributes API from Lightspeed Commerce — 2 operation(s) for variant attributes.
  name: Lightspeed Commerce Variant Attributes API
  slug: lightspeed-variant-attributes-api
- description: Webhook operations
  name: Lightspeed Commerce Webhooks API
  slug: lightspeed-webhooks-api
- description: Workflow operations
  name: Lightspeed Commerce Workflows API
  slug: lightspeed-workflows-api
artifact_total: 68
asyncapis:
- description: ''
  name: Lightspeed Webhooks
  slug: lightspeed-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lightspeed-capability-edges.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lightspeed-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightspeed-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightspeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lightspeedhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lightspeedhq.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LightspeedHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightspeedcommerce
- group: company
  title: ''
  type: Blog
  url: https://www.lightspeedhq.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lightspeedhq.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lightspeedhq.com/
- group: other
  title: ''
  type: X
  url: https://x.com/LightspeedHQ
- group: commercial
  title: ''
  type: Plans
  url: plans/lightspeed-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lightspeed-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lightspeed-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.lightspeedhq.com/
- group: operate
  title: ''
  type: Support
  url: https://www.lightspeedhq.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lightspeedhq.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lightspeedhq.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.lightspeedhq.com/login/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.lightspeedhq.com/
- group: build
  title: ''
  type: Packages
  url: packages/lightspeed-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lightspeed-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lightspeed-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lightspeed-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightspeed-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/lightspeed-x-series-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lightspeed-k-series-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/lightspeed-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/lightspeed-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lightspeed-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lightspeed-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lightspeed-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/lightspeed-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lightspeed-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/lightspeed-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lightspeed-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lightspeed-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/lightspeed-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lightspeed-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/lightspeed-cli.yml
- group: design
  title: ''
  type: Components
  url: components/lightspeed-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lightspeed-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lightspeed-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/lightspeed-x-series-openapi.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/lightspeed-k-series-openapi.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/lightspeed.json
- group: docs
  title: ''
  type: APIReference
  url: https://x-series-api.lightspeedhq.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://x-series-api.lightspeedhq.com/docs/quick_start
- group: build
  title: ''
  type: Postman
  url: https://developers.lightspeedhq.com/ecom/introduction/images/Lightspeed_eCom.postman_collection.json
created: 2026-06-13
description: Omnichannel commerce platform with REST APIs for retail and restaurant POS, inventory management, loyalty programs, and e-commerce integrations. Lightspeed serves retailers and restaurateurs with cloud-based point-of-sale systems, enabling custom integrations through APIs for sales, inventory, customers, orders, payments, and loyalty programs across multiple product lines including Retail X-Series, Retail R-Series, Restaurant K-Series, and eCom.
finops:
- name: Lightspeed Finops
  service_category: ''
  slug: lightspeed-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightspeed.png
layout: provider
mcp_servers:
- description: 'Lightspeed runs two hosted, anonymous MCP servers — one per documentation platform. Both are documentation-plane servers: they let an agent read and search the API contract. Only the X-Series server c'
  name: Lightspeed Commerce MCP Servers
  slug: lightspeed-commerce-mcp-servers
modified: '2026-08-27'
name: Lightspeed Commerce
nav: Providers
network: true
overview: 'Lightspeed Commerce publishes 54 APIs on the [APIs.io](https://apis.io/) network, including Lightspeed eCom API, Audit API, Brands API, and 51 more. Tagged areas include Commerce, Point-of-Sale, Retail, Restaurant, and Inventory.


  The Lightspeed Commerce catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lightspeed Commerce''s developer surface includes authentication, documentation, engineering blog, pricing, support, signup flow, sandbox, and 44 more developer resources.'
plans:
- name: Lightspeed Plans Pricing
  plan_count: 6
  slug: lightspeed-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 6
  name: Lightspeed Rate Limits
  slug: lightspeed-rate-limits
scopes:
- name: Lightspeed Scopes
  scope_count: 90
  slug: lightspeed-scopes
  summary_line: 90 scopes · authorizationCode
score:
  band: exemplar
  composite: 80.4
  coverage:
    artifact_dirs: 27
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -2.1
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 64.1
    developer_ergonomics: 85.1
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 92.1
  previous_composite: 82.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 53
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 84.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightspeed/refs/heads/main/screenshots/lightspeed-2026-06-20T184527.png
security:
- kind: authentication
  name: Lightspeed Authentication
  slug: lightspeed-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lightspeed Domain Security
  slug: lightspeed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lightspeed Vulnerability Disclosure
  slug: lightspeed-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Lightspeed Trust Center
  slug: lightspeed-trust-center
  summary_line: PCI DSS, SOC 2, SOC 3, GDPR
slug: lightspeed
tags:
- Commerce
- Point-of-Sale
- Retail
- Restaurant
- Inventory
- Loyalty
- Payments
- E-Commerce
- Omnichannel
website: https://www.lightspeedhq.com/
---
