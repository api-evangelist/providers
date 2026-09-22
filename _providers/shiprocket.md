---
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.2
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://apiv2.shiprocket.in/v1/external
  baseurl_source: declared
  description: 'Public REST API (v1/external) for eCommerce shipping and order management: API-user login returning a 10-day JWT, order create/update/cancel/import, courier serviceability, AWB assignment and pickup s'
  name: Shiprocket API
  slug: shiprocket-api
artifact_total: 8
asyncapis:
- description: ''
  name: Shiprocket Tracking Webhooks
  slug: shiprocket-tracking-webhooks
collections:
- collection_type: postman
  name: Shiprocket API
  slug: postman-shiprocket-api
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/security/shiprocket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shiprocket-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/authentication/shiprocket-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/llms/shiprocket-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shiprocket-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/well-known/shiprocket-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shiprocket-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/mcp/shiprocket-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/shiprocket-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/mcp/shiprocket-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/shiprocket-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/packages/shiprocket-packages.yml
  title: ''
  type: Packages
  url: packages/shiprocket-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/components/shiprocket-components.yml
  title: ''
  type: Components
  url: components/shiprocket-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/asyncapi/shiprocket-tracking-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/shiprocket-tracking-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/conventions/shiprocket-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shiprocket-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/errors/shiprocket-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shiprocket-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/lifecycle/shiprocket-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shiprocket-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/conformance/shiprocket-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shiprocket-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/rate-limits/shiprocket-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shiprocket-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/plans/shiprocket-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shiprocket-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/overlays/shiprocket-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shiprocket-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shiprocket/refs/heads/main/data-model/shiprocket-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shiprocket-data-model.yml
created: '2026-09-18'
description: 'Shiprocket (BigFoot Retail Solutions Pvt Ltd, formerly KartRocket) is India''s largest eCommerce shipping and enablement platform, aggregating 25+ courier partners into one panel for D2C brands, SMEs and enterprise sellers: domestic and hyperlocal shipping, cross-border (ShipX/CargoX), warehouse fulfillment, returns and NDR management, COD reconciliation, checkout (fastrr), capital and the Sense address-intelligence and RTO-prediction APIs. The public Shiprocket API (apiv2.shiprocket.in/v1/external, JWT bearer from an API-user login) covers order create/update/cancel, courier serviceability and AWB assignment, pickup scheduling, labels/manifests/invoices, tracking, returns/exchanges, NDR actions, products, listings, channels, inventory, wallet and statements, and is published as a public Postman collection with tracking webhooks. An official open-source MCP server (bfrs/shiprocket-mcp) exposes ten of those flows to AI agents.'
image: https://sr-website.shiprocket.in/wp-content/uploads/2025/02/OG-Image-for-Shiprocket.png
layout: provider
mcp_servers:
- description: Official Shiprocket Model Context Protocol server. Wraps the public Shiprocket REST API (apiv2.shiprocket.in/v1/external + serviceability.shiprocket.in) as ten tools for rate shopping, EDD, order crea
  name: Shiprocket MCP
  slug: shiprocket-mcp
modified: '2026-09-18'
name: Shiprocket
nav: Providers
network: true
overview: 'Shiprocket publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Logistics, E-Commerce, and Fulfillment.


  The Shiprocket catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Shiprocket''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Shiprocket Plans Pricing
  plan_count: 4
  slug: shiprocket-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Shiprocket Rate Limits
  slug: shiprocket-rate-limits
score:
  band: strong
  composite: 54.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 67.1
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 54.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Shiprocket Authentication
  slug: shiprocket-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shiprocket Domain Security
  slug: shiprocket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
