---
access_model:
  confidence: high
  label: Public, self-service with a free tier; API access begins on the Premium tier
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://www.aftership.com/pricing
  - plans/aftership-plans-pricing.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 85
  human_in_the_loop: 0
  name: Aftership Agentic Access
  operation_count: 131
  slug: aftership-agentic-access
  summary_line: 131 operations · 85 acting
api_count: 7
apis:
- baseURL: https://api.aftership.com/address/2024-07/
  baseurl_source: declared
  description: Address validation and correction so packages are delivered to a deliverable, normalized address.
  name: AfterShip Address API
  slug: aftership-address-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Address Validations (Beta) API from AfterShip — 1 operation(s) for address validations (beta).
  name: AfterShip Address Validations (Beta) API
  slug: aftership-address-validations-beta-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Cancel Labels API from AfterShip — 2 operation(s) for cancel labels.
  name: AfterShip Cancel Labels API
  slug: aftership-cancel-labels-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Cancel Pickups API from AfterShip — 2 operation(s) for cancel pickups.
  name: AfterShip Cancel Pickups API
  slug: aftership-cancel-pickups-api
- baseURL: https://api.aftership.com/warranty/2026-07
  baseurl_source: declared
  description: Public endpoints for updating item-level claim data.
  name: AfterShip Claim Items API
  slug: aftership-claim-items-api
- baseURL: https://api.aftership.com/warranty/2026-07
  baseurl_source: declared
  description: Public endpoints for creating and polling claim shipment resources.
  name: AfterShip Claim Shipments API
  slug: aftership-claim-shipments-api
- baseURL: https://api.aftership.com/admin/2022-01
  baseurl_source: declared
  description: The Claims API from AfterShip — 10 operation(s) for claims.
  name: AfterShip Claims API
  slug: aftership-claims-api
- baseURL: https://api.aftership.com/tracking/2026-07
  baseurl_source: declared
  description: The Courier API from AfterShip — 2 operation(s) for courier.
  name: AfterShip Courier API
  slug: aftership-courier-api
- baseURL: https://api.aftership.com/tracking/2026-07
  baseurl_source: declared
  description: The Courier connection API from AfterShip — 2 operation(s) for courier connection.
  name: AfterShip Courier connection API
  slug: aftership-courier-connection-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Couriers API from AfterShip — 1 operation(s) for couriers.
  name: AfterShip Couriers API
  slug: aftership-couriers-api
- baseURL: https://api.aftership.com/admin/2022-01
  baseurl_source: declared
  description: The Coverages API from AfterShip — 5 operation(s) for coverages.
  name: AfterShip Coverages API
  slug: aftership-coverages-api
- baseURL: https://api.aftership.com/personalization/2025-01
  baseurl_source: declared
  description: The Discoveries API from AfterShip — 4 operation(s) for discoveries.
  name: AfterShip Discoveries API
  slug: aftership-discoveries-api
- baseURL: https://api.aftership.com/admin/2022-01
  baseurl_source: declared
  description: The Email Parses API from AfterShip — 2 operation(s) for email parses.
  name: AfterShip Email Parses API
  slug: aftership-email-parses-api
- baseURL: https://api.aftership.com/tracking/2026-07
  baseurl_source: declared
  description: The Estimated delivery date API from AfterShip — 2 operation(s) for estimated delivery date.
  name: AfterShip Estimated delivery date API
  slug: aftership-estimated-delivery-date-api
- baseURL: https://api.aftership.com/commerce/2026-07
  baseurl_source: declared
  description: The Fulfillments API from AfterShip — 3 operation(s) for fulfillments.
  name: AfterShip Fulfillments API
  slug: aftership-fulfillments-api
- baseURL: https://api.aftership.com/returns/2026-07
  baseurl_source: declared
  description: The Item tags API from AfterShip — 1 operation(s) for item tags.
  name: AfterShip Item tags API
  slug: aftership-item-tags-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Labels API from AfterShip — 2 operation(s) for labels.
  name: AfterShip Labels API
  slug: aftership-labels-api
- baseURL: https://api.aftership.com/commerce/2026-07
  baseurl_source: declared
  description: The Locations API from AfterShip — 2 operation(s) for locations.
  name: AfterShip Locations API
  slug: aftership-locations-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Manifests API from AfterShip — 2 operation(s) for manifests.
  name: AfterShip Manifests API
  slug: aftership-manifests-api
- baseURL: https://api.aftership.com/admin/2022-01
  baseurl_source: declared
  description: The Memberships API from AfterShip — 2 operation(s) for memberships.
  name: AfterShip Memberships API
  slug: aftership-memberships-api
- baseURL: https://api.aftership.com/commerce/2026-07
  baseurl_source: declared
  description: The Orders API from AfterShip — 4 operation(s) for orders.
  name: AfterShip Orders API
  slug: aftership-orders-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Pickups API from AfterShip — 2 operation(s) for pickups.
  name: AfterShip Pickups API
  slug: aftership-pickups-api
- baseURL: https://api.aftership.com/commerce/2026-07
  baseurl_source: declared
  description: The Products API from AfterShip — 4 operation(s) for products.
  name: AfterShip Products API
  slug: aftership-products-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Rates API from AfterShip — 2 operation(s) for rates.
  name: AfterShip Rates API
  slug: aftership-rates-api
- baseURL: https://api.aftership.com/returns/2026-07
  baseurl_source: declared
  description: The Return Dropoffs API from AfterShip — 1 operation(s) for return dropoffs.
  name: AfterShip Return Dropoffs API
  slug: aftership-return-dropoffs-api
- baseURL: https://api.aftership.com/returns/2026-07
  baseurl_source: declared
  description: The Return items API from AfterShip — 2 operation(s) for return items.
  name: AfterShip Return items API
  slug: aftership-return-items-api
- baseURL: https://api.aftership.com/returns/2026-07
  baseurl_source: declared
  description: Create, approve, reject, resolve and receive returns by return ID or RMA number, manage return items, item tags and returns-page deep links.
  name: AfterShip Returns API
  slug: aftership-returns-api
- baseURL: https://api.aftership.com/returns/2026-07
  baseurl_source: declared
  description: The Returns Page API from AfterShip — 1 operation(s) for returns page.
  name: AfterShip Returns Page API
  slug: aftership-returns-page-api
- baseURL: https://api.aftership.com/admin/2022-01
  baseurl_source: declared
  description: The Roles API from AfterShip — 1 operation(s) for roles.
  name: AfterShip Roles API
  slug: aftership-roles-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Shipper Accounts API from AfterShip — 5 operation(s) for shipper accounts.
  name: AfterShip Shipper Accounts API
  slug: aftership-shipper-accounts-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Specific Shipper Accounts API from AfterShip — 2 operation(s) for specific shipper accounts.
  name: AfterShip Specific Shipper Accounts API
  slug: aftership-specific-shipper-accounts-api
- baseURL: https://api.aftership.com/commerce/2026-07
  baseurl_source: declared
  description: The Stores API from AfterShip — 2 operation(s) for stores.
  name: AfterShip Stores API
  slug: aftership-stores-api
- baseURL: https://api.aftership.com/tracking/2026-07
  baseurl_source: declared
  description: 'Shipment tracking across 1,400+ carriers: create and query trackings, detect couriers, manage courier connections, and predict estimated delivery dates.'
  name: AfterShip Tracking API
  slug: aftership-tracking-api
- baseURL: https://api.aftership.com/warranty/2026-07
  baseurl_source: declared
  description: Public endpoints for querying and correcting warranty registration data.
  name: AfterShip Warranty Registrations API
  slug: aftership-warranty-registrations-api
artifact_total: 45
asyncapis:
- description: ''
  name: Aftership Webhooks
  slug: aftership-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/aftership-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aftership-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aftership-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aftership-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aftership-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aftership-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AfterShip
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aftership
- group: company
  title: ''
  type: Website
  url: https://www.aftership.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/aftership-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aftership-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aftership-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/aftership-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aftership-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aftership-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aftership-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aftership-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aftership-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/aftership-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/aftership-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aftership-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aftership-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.aftershipstatus.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/aftership-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aftership-scopes.yml
- group: auth
  title: ''
  type: Security
  url: security/aftership-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aftership-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aftership-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aftership-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/aftership-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aftership-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aftership-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aftership-tracking-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aftership.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.aftership.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.aftership.com/docs/tracking/reference/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aftership.com/docs/tracking/quickstart/api-quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.aftership.com/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.aftership.com/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.aftership.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aftership.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.aftership.com/sso/authorize?continue=register&pd=tracking
- group: start
  title: ''
  type: Login
  url: https://accounts.aftership.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aftership.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aftership.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/aftership/workspace/api-aftership-com
created: '2026-05-08'
description: AfterShip is a post-purchase experience platform for ecommerce brands, retailers, marketplaces and 3PLs, founded in 2012 and headquartered in Hong Kong. Its products cover shipment tracking across 1,400+ carriers, branded tracking pages, AI-predicted estimated delivery dates, automated returns and exchanges, warranty and claims management, shipping-label generation and rate shopping (Postmen), shipment protection, address validation, AI email parsing, product personalization and discovery, and marketplace feed management. AfterShip publishes ten versioned, date-based REST APIs on api.aftership.com, each with a downloadable OpenAPI 3.1 description, seven first-party SDKs, webhooks, an OAuth 2.0 authorization server, and public and OAuth-gated MCP servers for AI agents.
finops:
- name: Aftership Finops
  service_category: Shipping
  slug: aftership-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aftership.png
layout: provider
mcp_servers:
- description: AfterShip publishes an anonymous, no-auth remote MCP server for real-time package tracking and a Returns Center demo, plus two OAuth-gated remote MCP servers (Post-purchase and Channels) documented on
  name: AfterShip Tracking & Returns MCP Server
  slug: aftership-tracking-returns-mcp-server
modified: '2026-08-27'
name: AfterShip
nav: Providers
network: true
overview: 'AfterShip publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Address API, Address Validations (Beta) API, Cancel Labels API, and 31 more. Tagged areas include Shipping, Tracking, E-Commerce, Post-Purchase, and Notification.


  The AfterShip catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AfterShip''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 40 more developer resources.'
plans:
- name: Aftership Plans Pricing
  plan_count: 4
  slug: aftership-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 20
  name: Aftership Rate Limits
  slug: aftership-rate-limits
scopes:
- name: Aftership Scopes
  scope_count: 7
  slug: aftership-scopes
  summary_line: 7 scopes
score:
  band: exemplar
  composite: 81.2
  coverage:
    artifact_dirs: 26
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.2
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 66.3
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 92.1
  previous_composite: 81.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/screenshots/aftership-2026-06-20T165736.png
security:
- kind: authentication
  name: Aftership Authentication
  slug: aftership-authentication
  summary_line: apiKey/hmac-signature/oauth2 · 3 schemes
- kind: domain-security
  name: Aftership Domain Security
  slug: aftership-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aftership Vulnerability Disclosure
  slug: aftership-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Aftership Trust Center
  slug: aftership-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: aftership
tags:
- Shipping
- Tracking
- E-Commerce
- Post-Purchase
- Notification
- Logistics
- Returns
- Warranty
- Address Validation
- Fulfillment
- Carriers
- Webhook
- MCP
- Retail
website: https://www.aftership.com/
---
