---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - '{''url'': ''https://shopgo.me'', ''status'': 302, ''note'': ''declared website redirects to sa-https://makane.com/ar/ — a different registrable domain (shopgo.me -> makane.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.shopgo.me/v1/management
  baseurl_source: declared
  description: Obtain and test API keys
  name: ShopGo Authentication API
  slug: shopgo-authentication-api
- baseURL: https://api.shopgo.me/v1/management
  baseurl_source: declared
  description: Order, payment and shipment management
  name: ShopGo Orders API
  slug: shopgo-orders-api
- baseURL: https://api.shopgo.me/v1/management
  baseurl_source: declared
  description: Store availability, legal and webhook settings
  name: ShopGo Store API
  slug: shopgo-store-api
- baseURL: https://api.shopgo.me/v1/management
  baseurl_source: declared
  description: The Tenants API from ShopGo — 2 operation(s) for tenants.
  name: ShopGo Tenants API
  slug: shopgo-tenants-api
- baseURL: https://api.shopgo.me/v1/management
  baseurl_source: declared
  description: Dashboard user and tenant information
  name: ShopGo Users API
  slug: shopgo-users-api
artifact_total: 16
asyncapis:
- description: ''
  name: Shopgo Webhooks
  slug: shopgo-webhooks
collections:
- collection_type: open
  name: ShopGo Management Authentication API
  slug: open-shopgo-authentication-api
- collection_type: open
  name: ShopGo Management Authentication Orders API
  slug: open-shopgo-orders-api
- collection_type: open
  name: ShopGo Management Authentication Store API
  slug: open-shopgo-store-api
- collection_type: open
  name: ShopGo Management Authentication Tenants API
  slug: open-shopgo-tenants-api
- collection_type: open
  name: ShopGo Management Authentication Users API
  slug: open-shopgo-users-api
common:
- group: company
  title: ''
  type: Website
  url: https://shopgo.me
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.shopgo.me
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shopgo.me
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shopgo.me/management-api/orders
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shopgo
- group: auth
  href: https://artifacts.apis.io/shopgo/authentication/shopgo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shopgo-authentication.yml
- group: design
  href: https://artifacts.apis.io/shopgo/conventions/shopgo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shopgo-conventions.yml
- group: design
  href: https://artifacts.apis.io/shopgo/errors/shopgo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shopgo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shopgo/data-model/shopgo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shopgo-data-model.yml
- group: design
  href: https://artifacts.apis.io/shopgo/conformance/shopgo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shopgo-conformance.yml
- group: design
  href: https://artifacts.apis.io/shopgo/lifecycle/shopgo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shopgo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/shopgo/asyncapi/shopgo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/shopgo-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/shopgo/mcp/shopgo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/shopgo-mcp.yml
- group: agent
  href: https://artifacts.apis.io/shopgo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/shopgo/llms/shopgo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shopgo-llms.txt
- group: agent
  href: https://artifacts.apis.io/shopgo/well-known/shopgo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shopgo-well-known.yml
- group: other
  href: https://artifacts.apis.io/shopgo/overlays/shopgo-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shopgo-management-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/shopgo/security/shopgo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shopgo-domain-security.yml
created: '2026-07-17'
description: 'ShopGo (now branded Makane) is a MENA-focused eCommerce SaaS platform based in Amman, Jordan and founded in 2012, backed by 500 Global. It lets merchants build and run online stores with integrated payment and shipment options across the Middle East and North Africa. For developers, ShopGo publishes a GitBook developer portal (docs.shopgo.me) documenting two REST APIs served from api.shopgo.me: a Management API for store, order, payment and shipment administration, and an internal Platform API for SaaS tenant control. Both use API-key authentication and a JSON result/payload envelope, and the platform supports configurable checkout webhooks (custom shipping rates, order confirmation).'
image: https://github.com/shopgo.png
layout: provider
modified: '2026-07-21'
name: ShopGo
nav: Providers
network: true
overview: 'ShopGo publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Orders API, Store API, and 2 more. Tagged areas include Company, E-Commerce, Online Store, Payments, and Shipping.


  The ShopGo catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  ShopGo''s developer surface includes documentation, API reference, authentication, and 15 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: ShopGo API Rules
  rule_count: 57
  severity_counts:
    error: 53
    hint: 0
    info: 3
    warn: 1
  slug: shopgo-rules
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 54.6
    developer_ergonomics: 39.9
    discoverability: 73.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - jordan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 31.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/shopgo/shopgo-2026-09-02T155259.png
security:
- kind: authentication
  name: Shopgo Authentication
  slug: shopgo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Shopgo Domain Security
  slug: shopgo-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: Provide custom ShopGo shipping rates via webhook
  slug: shopgo-custom-shipping-rates
- name: Process a ShopGo order (payment, authorization, fulfillment)
  slug: shopgo-process-order
slug: shopgo
tags:
- Company
- E-Commerce
- Online Store
- Payments
- Shipping
- Software-as-a-Service
- MENA
- Order
website: https://shopgo.me
---
