---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - finops
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Shipbob Agentic Access
  operation_count: 72
  slug: shipbob-agentic-access
  summary_line: 72 operations · 28 acting
api_count: 1
apis:
- baseURL: https://api.shipbob.com
  baseurl_source: declared
  description: The subpackage_billing API from ShipBob — 4 operation(s) for subpackage_billing.
  name: ShipBob Subpackage Billing API
  slug: shipbob-subpackage-billing-api
- baseURL: https://api.shipbob.com
  baseurl_source: declared
  description: The subpackage_channels API from ShipBob — 1 operation(s) for subpackage_channels.
  name: ShipBob Subpackage Channels API
  slug: shipbob-subpackage-channels-api
- baseURL: https://api.shipbob.com
  baseurl_source: declared
  description: The subpackage_inventory API from ShipBob — 9 operation(s) for subpackage_inventory.
  name: ShipBob Subpackage Inventory API
  slug: shipbob-subpackage-inventory-api
- baseURL: https://api.shipbob.com
  baseurl_source: declared
  description: The subpackage_locations API from ShipBob — 1 operation(s) for subpackage_locations.
  name: ShipBob Subpackage Locations API
  slug: shipbob-subpackage-locations-api
- baseURL: https://api.shipbob.com
  baseurl_source: declared
  description: The subpackage_orders API from ShipBob — 21 operation(s) for subpackage_orders.
  name: ShipBob Subpackage Orders API
  slug: shipbob-subpackage-orders-api
- baseURL: https://api.shipbob.com
  baseurl_source: declared
  description: The subpackage_products API from ShipBob — 11 operation(s) for subpackage_products.
  name: ShipBob Subpackage Products API
  slug: shipbob-subpackage-products-api
- baseURL: https://api.shipbob.com
  baseurl_source: declared
  description: The subpackage_receiving API from ShipBob — 8 operation(s) for subpackage_receiving.
  name: ShipBob Subpackage Receiving API
  slug: shipbob-subpackage-receiving-api
- baseURL: https://api.shipbob.com
  baseurl_source: declared
  description: The subpackage_returns API from ShipBob — 3 operation(s) for subpackage_returns.
  name: ShipBob Subpackage Returns API
  slug: shipbob-subpackage-returns-api
- baseURL: https://api.shipbob.com
  baseurl_source: declared
  description: The subpackage_simulations API from ShipBob — 2 operation(s) for subpackage_simulations.
  name: ShipBob Subpackage Simulations API
  slug: shipbob-subpackage-simulations-api
- baseURL: https://api.shipbob.com
  baseurl_source: declared
  description: The subpackage_webhooks API from ShipBob — 2 operation(s) for subpackage_webhooks.
  name: ShipBob Subpackage Webhooks API
  slug: shipbob-subpackage-webhooks-api
artifact_total: 31
asyncapis:
- description: AsyncAPI 2.6 specification modeling the ShipBob webhook event surface. ShipBob webhooks allow applications to subscribe to events that occur in a ShipBob merchant account (order shipments, returns, wa
  name: ShipBob Webhooks
  slug: shipbob-webhooks-asyncapi
collections:
- collection_type: open
  name: API Reference subpackage_billing API
  slug: open-shipbob-subpackage-billing-api
- collection_type: open
  name: API Reference subpackage_billing subpackage_channels API
  slug: open-shipbob-subpackage-channels-api
- collection_type: open
  name: API Reference subpackage_billing subpackage_inventory API
  slug: open-shipbob-subpackage-inventory-api
- collection_type: open
  name: API Reference subpackage_billing subpackage_locations API
  slug: open-shipbob-subpackage-locations-api
- collection_type: open
  name: API Reference subpackage_billing subpackage_orders API
  slug: open-shipbob-subpackage-orders-api
- collection_type: open
  name: API Reference subpackage_billing subpackage_products API
  slug: open-shipbob-subpackage-products-api
- collection_type: open
  name: API Reference subpackage_billing subpackage_receiving API
  slug: open-shipbob-subpackage-receiving-api
- collection_type: open
  name: API Reference subpackage_billing subpackage_returns API
  slug: open-shipbob-subpackage-returns-api
- collection_type: open
  name: API Reference subpackage_billing subpackage_simulations API
  slug: open-shipbob-subpackage-simulations-api
- collection_type: open
  name: API Reference subpackage_billing subpackage_webhooks API
  slug: open-shipbob-subpackage-webhooks-api
- collection_type: open
  name: API Reference
  slug: open-shipbob
common:
- group: other
  href: https://artifacts.apis.io/shipbob/capabilities/shipbob-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/shipbob-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/shipbob/agentic-access/shipbob-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shipbob-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/shipbob/security/shipbob-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/shipbob-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/shipbob/security/shipbob-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shipbob-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/shipbob/authentication/shipbob-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shipbob-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.shipbob.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shipbob.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shipbob.com/pricing/
- group: other
  title: ''
  type: AppStore
  url: https://www.shipbob.com/integrations/
- group: start
  title: ''
  type: SupportPortal
  url: https://support.shipbob.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ShipBob
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shipbob
- group: commercial
  href: https://artifacts.apis.io/shipbob/plans/shipbob-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shipbob-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/shipbob/rate-limits/shipbob-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shipbob-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/shipbob/finops/shipbob-finops.yml
  title: ''
  type: FinOps
  url: finops/shipbob-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.shipbob.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.shipbob.com/blog/feed/
created: '2026-05-08'
description: ShipBob is a Chicago-based global ecommerce fulfillment network and 3PL operating 60+ fulfillment centers, providing distributed warehousing, inventory, B2B/EDI, and shipping operations for direct-to-consumer brands with a developer-friendly REST API.
finops:
- has_sources: true
  method: generated
  name: Shipbob Finops
  primary_unit: ''
  service_category: Logistics
  slug: shipbob-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shipbob.png
layout: provider
mcp_servers:
- description: Remote MCP server at sandbox-api.shipbob.com over HTTP.
  name: ShipBob MCP Server
  slug: shipbob
modified: '2026-05-30'
name: ShipBob
nav: Providers
network: true
overview: 'ShipBob publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Subpackage Billing API, Subpackage Channels API, Subpackage Inventory API, and 7 more. Tagged areas include Logistics, Fulfillment, 3PL, E-Commerce, and Inventory.


  The ShipBob catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  ShipBob''s developer surface includes authentication, documentation, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Shipbob Plans Pricing
  plan_count: 0
  slug: shipbob-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Shipbob Rate Limits
  slug: shipbob-rate-limits
rules:
- authorship: generated
  effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: ShipBob — asyncapi rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: shipbob-asyncapi-spectral-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 11.4
    contract_quality: 56.7
    developer_ergonomics: 35.7
    discoverability: 75.0
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/shipbob/shipbob-2026-06-20T193812.png
security:
- kind: authentication
  name: Shipbob Authentication
  slug: shipbob-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shipbob Domain Security
  slug: shipbob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Shipbob Trust Center
  slug: shipbob-trust-center
  summary_line: SOC 2, ISO 27001
slug: shipbob
tags:
- Logistics
- Fulfillment
- 3PL
- E-Commerce
- Inventory
- Warehousing
- Shipping
- Direct to Consumer
website: https://www.shipbob.com/
---
