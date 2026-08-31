---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The auth API from Platzi — 3 operation(s) for auth.
  name: Platzi auth API
  slug: platzi-auth-api
- description: The categories API from Platzi — 4 operation(s) for categories.
  name: Platzi categories API
  slug: platzi-categories-api
- description: The files API from Platzi — 2 operation(s) for files.
  name: Platzi files API
  slug: platzi-files-api
- description: The Locations API from Platzi — 1 operation(s) for locations.
  name: Platzi Locations API
  slug: platzi-locations-api
- description: The products API from Platzi — 5 operation(s) for products.
  name: Platzi products API
  slug: platzi-products-api
- description: The users API from Platzi — 3 operation(s) for users.
  name: Platzi users API
  slug: platzi-users-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Platzi Fake Store auth API
  slug: open-platzi-auth-api
- collection_type: open
  name: Platzi Fake Store auth categories API
  slug: open-platzi-categories-api
- collection_type: open
  name: Platzi Fake Store auth files API
  slug: open-platzi-files-api
- collection_type: open
  name: Platzi Fake Store auth Locations API
  slug: open-platzi-locations-api
- collection_type: open
  name: Platzi Fake Store auth products API
  slug: open-platzi-products-api
- collection_type: open
  name: Platzi Fake Store auth users API
  slug: open-platzi-users-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fakeapi.platzi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fakeapi.platzi.com/en/about/introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://api.escuelajs.co/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://fakeapi.platzi.com/en/rest/auth-jwt/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PlatziLabs
- group: company
  title: ''
  type: Blog
  url: https://platzi.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://platzi.com/precios/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://platzi.com/terminos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platzi.com/privacidad/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.platzi.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/platzi-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/platzi-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/platzi-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/platzi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/platzi-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/platzi-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/platzi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/platzi-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/platzi-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/platzi-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/platzi-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/platzi-fake-store-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Platzi is the leading online learning platform in Latin America, offering thousands of technology, business, and marketing courses. For developers, Platzi (via PlatziLabs) publishes the free, public "Platzi Fake Store API" — a fully functional REST and GraphQL backend that provides mock e-commerce data (products, categories, users) with complete CRUD operations, JWT authentication, pagination, filtering, file upload, and AI-generated product imagery. It is a zero-signup prototyping API used worldwide to learn and practice building shopping and front-end applications, backed by an open source NestJS project.
image: https://static.platzi.com/media/og/platzi.png
layout: provider
mcp_servers:
- description: ''
  name: Platzi MCP Server
  slug: platzi-mcp-server
modified: '2026-07-20'
name: Platzi
nav: Providers
network: true
overview: 'Platzi publishes 6 APIs on the [APIs.io](https://apis.io/) network, including auth API, categories API, files API, and 3 more. Tagged areas include Company, Education, E-Commerce, Product, and Mock API.


  Platzi''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, authentication, sandbox, and 16 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 35.4
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 41.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Platzi Authentication
  slug: platzi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Platzi Domain Security
  slug: platzi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: platzi
tags:
- Company
- Education
- E-Commerce
- Product
- Mock API
- Prototyping
- REST
- GraphQL
- Fake Store
- Developer Tools
website: https://fakeapi.platzi.com/
---
