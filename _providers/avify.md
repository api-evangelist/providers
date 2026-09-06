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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Avify's primary developer API. A GraphQL endpoint covering products, inventory, store locations, carts, orders and payment methods. Authenticated with the api-key header. A public GraphQL sandbox is a
  name: Avify GraphQL API
  slug: avify-graphql-api
- description: Avify's REST API (base path /api/v1). Includes a connectivity test endpoint and store/product media upload. Authenticated with the api-key header.
  name: Avify REST API v1
  slug: avify-rest-api-v1
artifact_total: 5
asyncapis:
- description: ''
  name: Avify Webhooks
  slug: avify-webhooks
common:
- group: auth
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
  title: ''
  type: GraphQL
  url: graphql/avify-graphql-operations.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/avify-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/avify-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/avify-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/avify-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/avify-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/avify-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/avify-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/avify-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avify-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/avify-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/avify-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/avify-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Avify is a WhatsApp-first commerce and CRM platform for small and medium-sized businesses (PYMEs) across Latin America. It centralizes conversations from WhatsApp, Instagram and Messenger and connects them to a real-time inventory system, an online store and catalog, a point-of-sale for physical stores, conversational marketing with AI agents, payment processing, shipping integrations and electronic invoicing. For developers, Avify exposes a GraphQL API and a REST API (base path /api/v1) authenticated with an api-key header, covering products, inventory, store locations, carts, orders and payment methods, plus order webhooks for create/update events. A public GraphQL sandbox is available for testing before going live.
image: https://avify.com/images/og.png
layout: provider
modified: '2026-07-18'
name: Avify
nav: Providers
network: true
overview: 'Avify publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, CRM, and WhatsApp.


  The Avify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Avify''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 22 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 43.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avify/refs/heads/main/screenshots/avify-2026-07-25T201935.png
security:
- kind: authentication
  name: Avify Authentication
  slug: avify-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Avify Domain Security
  slug: avify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- SMB
website: https://avify.com
---
