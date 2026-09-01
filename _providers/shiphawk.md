---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: ShipHawk's public REST API. Key-based authentication (X-Api-Key header or api_key query parameter), JSON request and response bodies, POST used for both create and update (no PUT/PATCH). Resources cov
  name: ShipHawk API v4
  slug: shiphawk-api-v4
artifact_total: 6
asyncapis:
- description: ''
  name: Shiphawk Webhooks
  slug: shiphawk-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://shiphawk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shiphawk.com/solutions/shipping-api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shiphawk.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shiphawk.com/#overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shiphawk.com/#api-integration
- group: operate
  title: ''
  type: Support
  url: https://shiphawk.atlassian.net/wiki/spaces/HELP
- group: company
  title: ''
  type: Blog
  url: https://blog.shiphawk.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ShipHawk
- group: start
  title: ''
  type: Login
  url: https://login.myshiphawk.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shiphawk.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shiphawk.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://shiphawk.statuspage.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shiphawk-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/shiphawk-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/shiphawk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shiphawk-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shiphawk-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shiphawk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shiphawk-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shiphawk-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shiphawk-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shiphawk-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shiphawk-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/shiphawk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shiphawk-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shiphawk-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shiphawk-domain-security.yml
created: '2026-08-27'
description: ShipHawk is a Santa Barbara, California shipping and warehouse automation platform for high-volume eCommerce, wholesale and manufacturing shippers. It combines a multi-carrier transportation management system (TMS), a warehouse management system (WMS), packing and rate optimization, and shipping business rules, and it plugs into ERPs including NetSuite, Acumatica, Infor, Microsoft Dynamics 365, Sage and SAP. ShipHawk publishes a public REST API (v4) covering rating, address validation, orders, proposed shipments, shipments, SKUs, handling units, material containers, warehouses, workstations, documents (labels, BOLs, commercial invoices, packing slips), tracking and webhooks, documented in a single Slate reference at docs.shiphawk.com and served from shiphawk.com/api/v4 with a shared sandbox at sandbox.shiphawk.com.
image: https://shiphawk.com/wp-content/uploads/2022/03/ShipHawk-favicon_2.png
layout: provider
modified: '2026-08-27'
name: ShipHawk
nav: Providers
network: true
overview: 'ShipHawk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Logistics, Transportation Management, and Warehouse Management.


  The ShipHawk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShipHawk''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 20 more developer resources.'
plans:
- name: Shiphawk Plans Pricing
  plan_count: 0
  slug: shiphawk-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Shiphawk Rate Limits
  slug: shiphawk-rate-limits
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Shiphawk Authentication
  slug: shiphawk-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Shiphawk Domain Security
  slug: shiphawk-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: shiphawk
tags:
- Company
- Shipping
- Logistics
- Transportation Management
- Warehouse Management
- Freight
- Parcel
- Fulfillment
- E-Commerce
- Supply Chain
- Carriers
- Rate Shopping
- Tracking
- Webhook
website: https://shiphawk.com/
---
