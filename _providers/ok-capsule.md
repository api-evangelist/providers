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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: A production remote MCP server that exposes the OK Capsule platform — catalog, product intelligence, pack builder, recommendation validation, consumers, orders and fulfillments — as OAuth 2.1 scoped t
  name: OK Capsule MCP Server
  slug: ok-capsule-mcp-server
- description: Routes to manage assemblies (formerly packs)
  name: OK Capsule Assemblies API
  slug: ok-capsule-assemblies-api
- description: OK Capsule API uses **Oauth2.0 with OpenID Connect**. It issues **access**, **id**, and **refresh** tokens. **Access** tokens is used to authenticate API requests and are short lived (1 day). *Id toke
  name: OK Capsule Authentication API
  slug: ok-capsule-authentication-api
- description: Routes to manage batches
  name: OK Capsule Batches API
  slug: ok-capsule-batches-api
- description: Routes to manage billing
  name: OK Capsule Billings API
  slug: ok-capsule-billings-api
- description: The Categories API from OK Capsule — 4 operation(s) for categories.
  name: OK Capsule Categories API
  slug: ok-capsule-categories-api
- description: Routes to manage client addresses
  name: OK Capsule Client Addresses API
  slug: ok-capsule-client-addresses-api
- description: The Client Printer Settings API from OK Capsule — 4 operation(s) for client printer settings.
  name: OK Capsule Client Printer Settings API
  slug: ok-capsule-client-printer-settings-api
- description: Routes to manage clients
  name: OK Capsule Clients API
  slug: ok-capsule-clients-api
- description: Routes to manage consumer addresses
  name: OK Capsule Consumer Addresses API
  slug: ok-capsule-consumer-addresses-api
- description: Routes to manage consumers
  name: OK Capsule Consumers API
  slug: ok-capsule-consumers-api
- description: Routes to manage contact addresses
  name: OK Capsule Contact Addresses API
  slug: ok-capsule-contact-addresses-api
- description: Routes to manage contacts
  name: OK Capsule Contacts API
  slug: ok-capsule-contacts-api
- description: The Destination Products API from OK Capsule — 1 operation(s) for destination products.
  name: OK Capsule Destination Products API
  slug: ok-capsule-destination-products-api
- description: Routes to manage fulfillments
  name: OK Capsule Fulfillments API
  slug: ok-capsule-fulfillments-api
- description: The Integrations Orders API from OK Capsule — 2 operation(s) for integrations orders.
  name: OK Capsule Integrations Orders API
  slug: ok-capsule-integrations-orders-api
- description: Routes to manage OK Capsule products
  name: OK Capsule OKC Products API
  slug: ok-capsule-okc-products-api
- description: The Onboarding API from OK Capsule — 1 operation(s) for onboarding.
  name: OK Capsule Onboarding API
  slug: ok-capsule-onboarding-api
- description: The Onboarding (Public) API from OK Capsule — 3 operation(s) for onboarding (public).
  name: OK Capsule Onboarding (Public) API
  slug: ok-capsule-onboarding-public-api
- description: Routes to manage order lines
  name: OK Capsule Order Lines API
  slug: ok-capsule-order-lines-api
- description: The Order transaction logs API from OK Capsule — 2 operation(s) for order transaction logs.
  name: OK Capsule Order transaction logs API
  slug: ok-capsule-order-transaction-logs-api
- description: Routes to manage orders
  name: OK Capsule Orders API
  slug: ok-capsule-orders-api
- description: The Pack Builder API from OK Capsule — 6 operation(s) for pack builder.
  name: OK Capsule Pack Builder API
  slug: ok-capsule-pack-builder-api
- description: The Pack Builder Cart API from OK Capsule — 2 operation(s) for pack builder cart.
  name: OK Capsule Pack Builder Cart API
  slug: ok-capsule-pack-builder-cart-api
- description: The Pack Builder Categories API from OK Capsule — 2 operation(s) for pack builder categories.
  name: OK Capsule Pack Builder Categories API
  slug: ok-capsule-pack-builder-categories-api
- description: The Pack Builder Categories Products API from OK Capsule — 4 operation(s) for pack builder categories products.
  name: OK Capsule Pack Builder Categories Products API
  slug: ok-capsule-pack-builder-categories-products-api
- description: The Pack Builder Client Products API from OK Capsule — 3 operation(s) for pack builder client products.
  name: OK Capsule Pack Builder Client Products API
  slug: ok-capsule-pack-builder-client-products-api
- description: The Pack Builder Integration Settings (Private) API from OK Capsule — 3 operation(s) for pack builder integration settings (private).
  name: OK Capsule Pack Builder Integration Settings (Private) API
  slug: ok-capsule-pack-builder-integration-settings-private-api
- description: The Pack Builder mapped products API from OK Capsule — 2 operation(s) for pack builder mapped products.
  name: OK Capsule Pack Builder mapped products API
  slug: ok-capsule-pack-builder-mapped-products-api
- description: The Pack Builder Settings API from OK Capsule — 1 operation(s) for pack builder settings.
  name: OK Capsule Pack Builder Settings API
  slug: ok-capsule-pack-builder-settings-api
- description: The Pack Builder Shipping Profiles API from OK Capsule — 1 operation(s) for pack builder shipping profiles.
  name: OK Capsule Pack Builder Shipping Profiles API
  slug: ok-capsule-pack-builder-shipping-profiles-api
- description: The Pack Builder Types (Private) API from OK Capsule — 2 operation(s) for pack builder types (private).
  name: OK Capsule Pack Builder Types (Private) API
  slug: ok-capsule-pack-builder-types-private-api
- description: The Pack Builder Widget API from OK Capsule — 5 operation(s) for pack builder widget.
  name: OK Capsule Pack Builder Widget API
  slug: ok-capsule-pack-builder-widget-api
- description: The Packaging Asset Groups API from OK Capsule — 3 operation(s) for packaging asset groups.
  name: OK Capsule Packaging Asset Groups API
  slug: ok-capsule-packaging-asset-groups-api
- description: Routes to manage pamphlets
  name: OK Capsule Pamphlets API
  slug: ok-capsule-pamphlets-api
- description: Routes to manage product lines (formerly brands).
  name: OK Capsule Product Lines API
  slug: ok-capsule-product-lines-api
- description: Routes to manage client product sets (a set is a client product composed of other client products)
  name: OK Capsule Product Sets API
  slug: ok-capsule-product-sets-api
- description: Routes to manage client products
  name: OK Capsule Products API
  slug: ok-capsule-products-api
- description: List of statuses for resources
  name: OK Capsule Statuses API
  slug: ok-capsule-statuses-api
- description: The Sync Processes API from OK Capsule — 2 operation(s) for sync processes.
  name: OK Capsule Sync Processes API
  slug: ok-capsule-sync-processes-api
- description: The Telemetry API from OK Capsule — 2 operation(s) for telemetry.
  name: OK Capsule Telemetry API
  slug: ok-capsule-telemetry-api
- description: The UPC Codes API from OK Capsule — 3 operation(s) for upc codes.
  name: OK Capsule UPC Codes API
  slug: ok-capsule-upc-codes-api
- description: Routes to manage client users
  name: OK Capsule Users API
  slug: ok-capsule-users-api
artifact_total: 50
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ok-capsule-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ok-capsule-core-api-v2-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://okcapsule.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.okcapsule.app/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.okcapsule.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api2-docs.okcapsule.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.okcapsule.app/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/ok-capsule-918b959a076c/en
- group: company
  title: ''
  type: Blog
  url: https://okcapsule.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/okcapsule
- group: commercial
  title: ''
  type: Pricing
  url: https://okcapsule.com/pricing/plans
- group: start
  title: ''
  type: SignUp
  url: https://portal.okcapsule.app/
- group: start
  title: ''
  type: Login
  url: https://portal.okcapsule.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://okcapsule.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://okcapsule.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: https://storefront.okcapsule.app/mcp
- group: build
  title: ''
  type: Packages
  url: packages/ok-capsule-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ok-capsule-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ok-capsule-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ok-capsule-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/ok-capsule-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ok-capsule-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ok-capsule-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ok-capsule-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ok-capsule-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ok-capsule-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ok-capsule-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ok-capsule-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ok-capsule-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ok-capsule-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/ok-capsule-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ok-capsule-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ok-capsule-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: 'OK Capsule is an on-demand, private-label supplement manufacturing and fulfillment platform. Health brands, telehealth providers, clinics and retailers use it to launch personalized daily vitamin packs without minimum order quantities, inventory or upfront deposits. The platform exposes its whole supply chain programmatically: a REST Core API V2 (199 operations across clients, consumers, orders, order lines, fulfillments, assemblies, batches, billings, product lines, pack builders and UPC codes) and a production remote MCP server that publishes the same catalog, pack-building, order and fulfillment surface as OAuth 2.1 scoped tools for Claude, ChatGPT, Gemini and other MCP hosts. Supplements are manufactured in cGMP-certified, FDA-registered facilities and lot-tested by ISO 17025 accredited third-party labs.'
image: https://okcapsule.com/og-preview.png
layout: provider
mcp_servers:
- description: A production remote MCP server that exposes the OK Capsule supplement platform — brands and catalog, product intelligence, the pack builder, recommendation validation, consumers, orders and fulfillmen
  name: OK Capsule MCP Server
  slug: ok-capsule-mcp-server
- description: Production remote MCP server for catalog, pack building, consumers, orders and fulfillments, behind OAuth 2.1 + PKCE.
  name: OK Capsule MCP Server
  slug: ok-capsule-mcp-server-2
modified: '2026-08-26'
name: OK Capsule
nav: Providers
network: true
overview: 'OK Capsule publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Assemblies API, Authentication API, Batches API, and 39 more. Tagged areas include Supplements, Nutrition, Health, Manufacturing, and Fulfillment.


  OK Capsule''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Ok Capsule Plans Pricing
  plan_count: 3
  slug: ok-capsule-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Ok Capsule Rate Limits
  slug: ok-capsule-rate-limits
scopes:
- name: Ok Capsule Scopes
  scope_count: 0
  slug: ok-capsule-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 55.5
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 60.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 65.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Ok Capsule Authentication
  slug: ok-capsule-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Ok Capsule Domain Security
  slug: ok-capsule-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ok-capsule
tags:
- Supplements
- Nutrition
- Health
- Manufacturing
- Fulfillment
- E-Commerce
- Personalization
- Order
- Shipping
- Agents
- MCP
- Telehealth
website: https://okcapsule.com/
---
