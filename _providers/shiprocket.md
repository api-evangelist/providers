---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: The Account API from Shiprocket — 1 operation(s) for account.
  name: Shiprocket Account API
  slug: shiprocket-account-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: The authentication token is an alphanumeric code, unique to your Shiprocket account, can be used from any system to validate your API calls to access Shiprocket's resources. Shiprocket API uses JWT to
  name: Shiprocket Authentication API
  slug: shiprocket-authentication-api-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: Use this API to get details about all the integrated channels in your Shiprocket account, including channel id. This channel id can be used to select or specify a custom channel at the time of order c
  name: Shiprocket Channels API
  slug: shiprocket-channels-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: The following APIs provide details about the various country codes and their respective zone details along with the locality details.
  name: Shiprocket Countries API
  slug: shiprocket-countries-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: 'Use these APIs to assign AWB to your order, check for courier serviceability, and request for the pickup of your order. All available couriers, along with their codes, are mentioned below:'
  name: Shiprocket Couriers API
  slug: shiprocket-couriers-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: Using these APIs, you can create new orders in your Shiprocket account or update existing orders. You can also cancel an order, bulk import orders from a CSV file and update inventory for an ordered p
  name: Shiprocket Create Or Update Order API
  slug: shiprocket-create-or-update-order-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: Use this API to get the discrepancy details of your account.
  name: Shiprocket Discrepancy Details API
  slug: shiprocket-discrepancy-details-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: Check the status response of files that have been imported using the API.
  name: Shiprocket File Imports API
  slug: shiprocket-file-imports-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: The Hyperlocal API from Shiprocket — 12 operation(s) for hyperlocal.
  name: Shiprocket Hyperlocal API
  slug: shiprocket-hyperlocal-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: These endpoints are used for operations related to international orders and shipments.
  name: Shiprocket International API
  slug: shiprocket-international-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: Use this API to update and get Inventory details.
  name: Shiprocket Inventory API
  slug: shiprocket-inventory-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: These APIs are designed for the generation of manifests, invoices and labels for your shipment. You can also get manifest details and print a manifest using the respective API's.
  name: Shiprocket Labels | Manifests | Invoice API
  slug: shiprocket-labels-manifests-invoice-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: The Listings API from Shiprocket — 6 operation(s) for listings.
  name: Shiprocket Listings API
  slug: shiprocket-listings-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: These APIs can be used to get details about your shipments that are in NDR, as well as manage them, which includes fetching NDR shipments from your account (all or specific) and taking actions such as
  name: Shiprocket NDR API
  slug: shiprocket-ndr-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: These APIs can be used to get details about your created orders, as well as manage them, which include fetching orders from your channel, syncing their status, and exporting them to a CSV file. Filter
  name: Shiprocket Orders API
  slug: shiprocket-orders-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: Use these APIs to get a list of all available pickup locations in your account or add a new pickup location.
  name: Shiprocket Pickup Addresses API
  slug: shiprocket-pickup-addresses-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: Use these APIs to get information on your added products or update their details. You can also add a new product or import them in bulk.
  name: Shiprocket Products API
  slug: shiprocket-products-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: The Return & Exchange Orders API from Shiprocket — 6 operation(s) for return & exchange orders.
  name: Shiprocket Return & Exchange Orders API
  slug: shiprocket-return-exchange-orders-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: These APIs can be used to get shipment details. You can either get all shipment details at once or the details of a particular shipment. Below are some associated status codes related to the shipments
  name: Shiprocket Shipments API
  slug: shiprocket-shipments-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: The Statement Details API from Shiprocket — 1 operation(s) for statement details.
  name: Shiprocket Statement Details API
  slug: shiprocket-statement-details-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: 'Use these APIs to get the tracking details of your shipments through the AWB code or the Shipment ID. Shipment Status Codes:'
  name: Shiprocket Tracking API
  slug: shiprocket-tracking-api
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: This is an all-in-one API to create an order, ship the order, add a new pickup location and generate a label along with the manifest for the same.
  name: Shiprocket Wrapper API
  slug: shiprocket-wrapper-api-api
artifact_total: 33
asyncapis:
- description: ''
  name: Shiprocket Tracking Webhooks
  slug: shiprocket-tracking-webhooks
collections:
- collection_type: postman
  name: Shiprocket API
  slug: postman-shiprocket-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.shiprocket.in/feed/
- group: other
  href: https://artifacts.apis.io/shiprocket/capabilities/shiprocket-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/shiprocket-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/shiprocket/security/shiprocket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shiprocket-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/shiprocket/authentication/shiprocket-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shiprocket-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.shiprocket.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.shiprocket.in/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.shiprocket.in/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.shiprocket.in/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.shiprocket.in/developers/
- group: build
  title: ''
  type: Postman
  url: https://apidocs.shiprocket.in/
- group: company
  title: ''
  type: Blog
  url: https://www.shiprocket.in/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shiprocket.in/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.shiprocket.in/register
- group: start
  title: ''
  type: Login
  url: https://app.shiprocket.in/login
- group: operate
  title: ''
  type: Support
  url: https://support.shiprocket.in/support/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shiprocket.in/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shiprocket.in/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shiprocket.in/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bfrs
- group: agent
  href: https://artifacts.apis.io/shiprocket/llms/shiprocket-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shiprocket-llms.txt
- group: agent
  href: https://artifacts.apis.io/shiprocket/well-known/shiprocket-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shiprocket-well-known.yml
- group: agent
  href: https://artifacts.apis.io/shiprocket/mcp/shiprocket-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/shiprocket-mcp.yml
- group: build
  href: https://artifacts.apis.io/shiprocket/mcp/shiprocket-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/shiprocket-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/shiprocket/packages/shiprocket-packages.yml
  title: ''
  type: Packages
  url: packages/shiprocket-packages.yml
- group: design
  href: https://artifacts.apis.io/shiprocket/components/shiprocket-components.yml
  title: ''
  type: Components
  url: components/shiprocket-components.yml
- group: design
  href: https://artifacts.apis.io/shiprocket/asyncapi/shiprocket-tracking-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/shiprocket-tracking-webhooks.yml
- group: design
  href: https://artifacts.apis.io/shiprocket/conventions/shiprocket-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shiprocket-conventions.yml
- group: design
  href: https://artifacts.apis.io/shiprocket/errors/shiprocket-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shiprocket-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shiprocket/lifecycle/shiprocket-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shiprocket-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/shiprocket/conformance/shiprocket-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shiprocket-conformance.yml
- group: operate
  href: https://artifacts.apis.io/shiprocket/rate-limits/shiprocket-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shiprocket-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/shiprocket/plans/shiprocket-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shiprocket-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/shiprocket/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/shiprocket/overlays/shiprocket-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shiprocket-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/shiprocket/data-model/shiprocket-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shiprocket-data-model.yml
created: '2026-09-18'
description: 'Shiprocket (BigFoot Retail Solutions Pvt Ltd, formerly KartRocket) is India''s largest eCommerce shipping and enablement platform, aggregating 25+ courier partners into one panel for D2C brands, SMEs and enterprise sellers: domestic and hyperlocal shipping, cross-border (ShipX/CargoX), warehouse fulfillment, returns and NDR management, COD reconciliation, checkout (fastrr), capital and the Sense address-intelligence and RTO-prediction APIs. The public Shiprocket API (apiv2.shiprocket.in/v1/external, JWT bearer from an API-user login) covers order create/update/cancel, courier serviceability and AWB assignment, pickup scheduling, labels/manifests/invoices, tracking, returns/exchanges, NDR actions, products, listings, channels, inventory, wallet and statements, and is published as a public Postman collection with tracking webhooks. An official open-source MCP server (bfrs/shiprocket-mcp) exposes ten of those flows to AI agents.'
finops:
- has_sources: true
  method: derived
  name: Shiprocket Finops
  primary_unit: subscription
  service_category: ''
  slug: shiprocket-finops
  template: false
image: https://sr-website.shiprocket.in/wp-content/uploads/2025/02/OG-Image-for-Shiprocket.png
layout: provider
mcp_servers:
- description: Official Shiprocket Model Context Protocol server. Wraps the public Shiprocket REST API (apiv2.shiprocket.in/v1/external + serviceability.shiprocket.in) as ten tools for rate shopping, EDD, order crea
  name: Shiprocket MCP
  slug: shiprocket-mcp
modified: '2026-10-06'
name: Shiprocket
nav: Providers
network: true
overview: 'Shiprocket publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Authentication API, Channels API, and 19 more. Tagged areas include Company, Shipping, Logistics, E-Commerce, and Fulfillment.


  The Shiprocket catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Shiprocket''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Shiprocket Plans Pricing
  plan_count: 4
  slug: shiprocket-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Shiprocket Rate Limits
  slug: shiprocket-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Shiprocket API Rules
  rule_count: 62
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 13
  slug: shiprocket-rules
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 60.6
    developer_ergonomics: 63.7
    discoverability: 71.7
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 57.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/shiprocket/shiprocket-2026-10-11T125813.png
security:
- kind: authentication
  name: Shiprocket Authentication
  slug: shiprocket-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shiprocket Domain Security
  slug: shiprocket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: shiprocket-ship-an-order
  slug: shiprocket-ship-an-order
- name: shiprocket-track-and-handle-ndr
  slug: shiprocket-track-and-handle-ndr
slug: shiprocket
tags:
- Company
- Shipping
- Logistics
- E-Commerce
- Fulfillment
- Last Mile Delivery
- Order Management
- Courier Aggregation
- India
website: https://www.shiprocket.in/
---
