---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Optoro Agentic Access
  operation_count: 32
  slug: optoro-agentic-access
  summary_line: 32 operations · 23 acting
api_count: 17
apis:
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Catalog Entry Updates API from Optoro — 1 operation(s) for catalog entry updates.
  name: Optoro Catalog Entry Updates API
  slug: optoro-catalog-entry-updates-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Dispositions API from Optoro — 1 operation(s) for dispositions.
  name: Optoro Dispositions API
  slug: optoro-dispositions-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Drop Shipment Cancellation API from Optoro — 1 operation(s) for drop shipment cancellation.
  name: Optoro Drop Shipment Cancellation API
  slug: optoro-drop-shipment-cancellation-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Drop Shipment Confirmation API from Optoro — 1 operation(s) for drop shipment confirmation.
  name: Optoro Drop Shipment Confirmation API
  slug: optoro-drop-shipment-confirmation-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Drop Shipment Partial Cancellation API from Optoro — 1 operation(s) for drop shipment partial cancellation.
  name: Optoro Drop Shipment Partial Cancellation API
  slug: optoro-drop-shipment-partial-cancellation-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Exchange Orders API from Optoro — 1 operation(s) for exchange orders.
  name: Optoro Exchange Orders API
  slug: optoro-exchange-orders-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The External Bin Changes API from Optoro — 2 operation(s) for external bin changes.
  name: Optoro External Bin Changes API
  slug: optoro-external-bin-changes-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Facilities API from Optoro — 1 operation(s) for facilities.
  name: Optoro Facilities API
  slug: optoro-facilities-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Final Dispositions API from Optoro — 1 operation(s) for final dispositions.
  name: Optoro Final Dispositions API
  slug: optoro-final-dispositions-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Forward Orders API from Optoro — 1 operation(s) for forward orders.
  name: Optoro Forward Orders API
  slug: optoro-forward-orders-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Inventory Receipt API from Optoro — 1 operation(s) for inventory receipt.
  name: Optoro Inventory Receipt API
  slug: optoro-inventory-receipt-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Listings API from Optoro — 2 operation(s) for listings.
  name: Optoro Listings API
  slug: optoro-listings-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Orders API from Optoro — 3 operation(s) for orders.
  name: Optoro Orders API
  slug: optoro-orders-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Outbound Asn API from Optoro — 1 operation(s) for outbound asn.
  name: Optoro Outbound Asn API
  slug: optoro-outbound-asn-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Returns Portal Orders API from Optoro — 1 operation(s) for returns portal orders.
  name: Optoro Returns Portal Orders API
  slug: optoro-returns-portal-orders-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Rmas API from Optoro — 1 operation(s) for rmas.
  name: Optoro Rmas API
  slug: optoro-rmas-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Shipments API from Optoro — 3 operation(s) for shipments.
  name: Optoro Shipments API
  slug: optoro-shipments-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Sku API from Optoro — 1 operation(s) for sku.
  name: Optoro Sku API
  slug: optoro-sku-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Vendor Updates API from Optoro — 1 operation(s) for vendor updates.
  name: Optoro Vendor Updates API
  slug: optoro-vendor-updates-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Asns API from Optoro — 2 operation(s) for asns.
  name: Optoro Asns API
  slug: optoro-asns-api
- baseURL: https://auth.optiturn.com
  baseurl_source: declared
  description: The Oauth API from Optoro — 1 operation(s) for oauth.
  name: Optoro OAUTH API
  slug: optoro-oauth-api
artifact_total: 35
asyncapis:
- description: ''
  name: Optoro Webhooks
  slug: optoro-webhooks
common:
- group: other
  href: https://artifacts.apis.io/optoro/capabilities/optoro-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/optoro-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/optoro/overlays/optoro-auth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optoro-auth-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optoro/overlays/optoro-catalogs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optoro-catalogs-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optoro/overlays/optoro-facilities-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optoro-facilities-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optoro/overlays/optoro-rtv-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optoro-rtv-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optoro/overlays/optoro-asn-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optoro-asn-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optoro/overlays/optoro-external-bin-changes-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optoro-external-bin-changes-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/optoro/skills/optoro-drop-ship-order.md
  title: ''
  type: AgentSkill
  url: skills/optoro-drop-ship-order.md
- group: agent
  href: https://artifacts.apis.io/optoro/skills/optoro-returns-experience.md
  title: ''
  type: AgentSkill
  url: skills/optoro-returns-experience.md
- group: other
  href: https://artifacts.apis.io/optoro/overlays/optoro-returns-portal-orders-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optoro-returns-portal-orders-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optoro/overlays/optoro-rmas-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optoro-rmas-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/optoro/agentic-access/optoro-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/optoro-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/optoro/security/optoro-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/optoro-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/optoro/security/optoro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/optoro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.optoro.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.optoro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.optoro.com/content/api_overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.optoro.com/openapi/rmas/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.optoro.com/content/rx_integration_guide
- group: company
  title: ''
  type: Blog
  url: https://www.optoro.com/returns-blog/
- group: operate
  title: ''
  type: Support
  url: https://help.optoro.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optoro.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optoro.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://optiturn.com/session/new
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/optoro
- group: operate
  title: ''
  type: StatusPage
  url: https://status.optiturn.com/
- group: agent
  href: https://artifacts.apis.io/optoro/llms/optoro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optoro-llms.txt
- group: design
  href: https://artifacts.apis.io/optoro/asyncapi/optoro-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/optoro-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/optoro/authentication/optoro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/optoro-authentication.yml
- group: auth
  href: https://artifacts.apis.io/optoro/scopes/optoro-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/optoro-scopes.yml
- group: design
  href: https://artifacts.apis.io/optoro/conventions/optoro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/optoro-conventions.yml
- group: design
  href: https://artifacts.apis.io/optoro/errors/optoro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/optoro-problem-types.yml
- group: design
  href: https://artifacts.apis.io/optoro/lifecycle/optoro-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/optoro-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/optoro/conformance/optoro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/optoro-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.optoro.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.optoro.com/security/
- group: design
  href: https://artifacts.apis.io/optoro/data-model/optoro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/optoro-data-model.yml
- group: start
  href: https://artifacts.apis.io/optoro/sandbox/optoro-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/optoro-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/optoro/changelog/optoro-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/optoro-changelog.yml
- group: operate
  href: https://artifacts.apis.io/optoro/rate-limits/optoro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/optoro-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/optoro/plans/optoro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/optoro-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/optoro/packages/optoro-packages.yml
  title: ''
  type: Packages
  url: packages/optoro-packages.yml
- group: agent
  href: https://artifacts.apis.io/optoro/mcp/optoro-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/optoro-mcp.yml
- group: agent
  href: https://artifacts.apis.io/optoro/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/optoro/overlays/optoro-drop-ship-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optoro-drop-ship-overlay.yaml
- group: auth
  title: ''
  type: Security
  url: https://www.optoro.com/security/
created: '2026-08-26'
description: 'Optoro is a returns management and reverse-logistics software company (Washington, DC; acquired by Blue Yonder in August 2025) whose OptiTurn platform powers the full returns lifecycle for retailers, brands and 3PLs — a shopper-facing returns portal and RMA workflow, in-store and warehouse returns processing, disposition and routing decisions, drop-ship fulfillment of returned and excess inventory, return-to-vendor agreements, and resale across secondary channels. Optoro publishes a public, API-first developer portal at developer.optoro.com covering seventeen OpenAPI 3.0/3.1 definitions across two directions: inbound APIs the retailer calls (Catalogs, Facilities, Drop Ship, RTV Vendor, ASN, External Bin Changes, Auth) and outbound webhooks/customer endpoints Optoro calls (RMAs, Disposition Update, Final Disposition, Outbound ASN, Exchange Orders, Exchange Variants, Drop Ship confirmation/cancellation). Authentication is OAuth 2.0 client credentials against auth.optiturn.com
  with 25-hour bearer tokens, and a full sandbox estate is published on *.sandbox.optiturn.com.'
finops:
- has_sources: true
  method: derived
  name: Optoro Finops
  primary_unit: ''
  service_category: ''
  slug: optoro-finops
  template: true
image: https://www.optoro.com/wp-content/uploads/2024/03/optoro-home-hero-lg.png
layout: provider
modified: '2026-08-26'
name: Optoro
nav: Providers
network: true
overview: 'Optoro publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog Entry Updates API, Dispositions API, Drop Shipment Cancellation API, and 18 more. Tagged areas include Returns Management, Reverse Logistics, Retail, Supply Chain, and E-Commerce.


  The Optoro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Optoro''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 39 more developer resources.'
plans:
- name: Optoro Plans Pricing
  plan_count: 0
  slug: optoro-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Optoro Rate Limits
  slug: optoro-rate-limits
scopes:
- name: Optoro Scopes
  scope_count: 0
  slug: optoro-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 56.2
    developer_ergonomics: 66.1
    discoverability: 71.4
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 76.2
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/optoro/optoro-2026-09-02T150853.png
security:
- kind: authentication
  name: Optoro Authentication
  slug: optoro-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Optoro Domain Security
  slug: optoro-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Optoro Vulnerability Disclosure
  slug: optoro-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 5
skills:
- name: optoro-authenticate
  slug: optoro-authenticate
- name: optoro-drop-ship-order
  slug: optoro-drop-ship-order
- name: optoro-returns-experience
  slug: optoro-returns-experience
- name: optoro-sync-catalog
  slug: optoro-sync-catalog
- name: optoro-warehouse-events
  slug: optoro-warehouse-events
slug: optoro
tags:
- Returns Management
- Reverse Logistics
- Retail
- Supply Chain
- E-Commerce
- Fulfillment
- Dropship
- Inventory
- Webhook
- Order Management
website: https://www.optoro.com/
---
