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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Avify's primary developer API. A GraphQL endpoint covering products, inventory, store locations, carts, orders and payment methods. Authenticated with the api-key header. A public GraphQL sandbox is a
  name: Avify GraphQL API
  slug: avify-graphql-api
- description: Avify's REST API (base path /api/v1). Includes a connectivity test endpoint and store/product media upload. Authenticated with the api-key header.
  name: Avify REST API v1
  slug: avify-rest-api-v1
artifact_total: 10
asyncapis:
- description: ''
  name: Avify Webhooks
  slug: avify-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/avify/plans/avify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avify-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/avify/security/avify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avify.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://avify.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://avify.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://avify.com/docs/introduccion-api
- group: start
  title: ''
  type: GettingStarted
  url: https://avify.com/docs/guia-inicio-rapido
- group: auth
  title: ''
  type: Authentication
  url: https://avify.com/docs/autenticacion-api
- group: operate
  title: ''
  type: Support
  url: https://avify.com/docs/soporte-y-recursos-adicionales
- group: company
  title: ''
  type: Blog
  url: https://avify.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avify-com
- group: commercial
  title: ''
  type: Pricing
  url: https://avify.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.avify.com/auth/register
- group: start
  title: ''
  type: Login
  url: https://app.avify.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avify.com/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avify.com/politica-de-privacidad
- group: docs
  href: https://artifacts.apis.io/avify/graphql/avify-graphql-operations.yml
  title: ''
  type: GraphQL
  url: graphql/avify-graphql-operations.yml
- group: auth
  href: https://artifacts.apis.io/avify/authentication/avify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avify-authentication.yml
- group: design
  href: https://artifacts.apis.io/avify/conventions/avify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/avify-conventions.yml
- group: design
  href: https://artifacts.apis.io/avify/errors/avify-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/avify-error-codes.yml
- group: design
  href: https://artifacts.apis.io/avify/asyncapi/avify-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/avify-webhooks.yml
- group: start
  href: https://artifacts.apis.io/avify/sandbox/avify-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/avify-sandbox.yml
- group: design
  href: https://artifacts.apis.io/avify/data-model/avify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avify-data-model.yml
- group: build
  href: https://artifacts.apis.io/avify/packages/avify-packages.yml
  title: ''
  type: Packages
  url: packages/avify-packages.yml
- group: agent
  href: https://artifacts.apis.io/avify/mcp/avify-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/avify-mcp.yml
- group: agent
  href: https://artifacts.apis.io/avify/llms/avify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avify-llms.txt
- group: agent
  href: https://artifacts.apis.io/avify/well-known/avify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avify-well-known.yml
- group: design
  href: https://artifacts.apis.io/avify/lifecycle/avify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/avify-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/avify/conformance/avify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avify-conformance.yml
- group: agent
  href: https://artifacts.apis.io/avify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Avify is a WhatsApp-first commerce and CRM platform for small and medium-sized businesses (PYMEs) across Latin America. It centralizes conversations from WhatsApp, Instagram and Messenger and connects them to a real-time inventory system, an online store and catalog, a point-of-sale for physical stores, conversational marketing with AI agents, payment processing, shipping integrations and electronic invoicing. For developers, Avify exposes a GraphQL API and a REST API (base path /api/v1) authenticated with an api-key header, covering products, inventory, store locations, carts, orders and payment methods, plus order webhooks for create/update events. A public GraphQL sandbox is available for testing before going live.
finops:
- has_sources: true
  method: derived
  name: Avify Finops
  primary_unit: instalación
  service_category: ''
  slug: avify-finops
  template: false
image: https://avify.com/images/og.png
layout: provider
modified: '2026-07-18'
name: Avify
nav: Providers
network: true
overview: 'Avify is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, CRM, and WhatsApp.


  The Avify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Avify''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Avify Plans Pricing
  plan_count: 12
  slug: avify-plans-pricing
- name: Avify Price Estimates
  plan_count: 0
  slug: avify-price-estimates
random_paper: 15
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 41.2
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/avify/avify-2026-07-25T201935.png
security:
- kind: authentication
  name: Avify Authentication
  slug: avify-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Avify Domain Security
  slug: avify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Create an Avify order from a cart
  slug: avify-create-order
- name: Manage Avify products and inventory
  slug: avify-manage-inventory
slug: avify
tags:
- Company
- Commerce
- E-Commerce
- CRM
- WhatsApp
- Conversational Commerce
- Inventory
- Point-of-Sale
- Payments
- Order
- GraphQL
- Latin America
- Small Business
website: https://avify.com
---
