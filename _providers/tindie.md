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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://www.tindie.com/api/v1
  baseurl_source: declared
  description: A seller's orders (authenticated).
  name: Tindie Order API
  slug: tindie-order-api
- baseURL: https://www.tindie.com/api/v1
  baseurl_source: declared
  description: Line items within a seller's orders (authenticated).
  name: Tindie Orderitem API
  slug: tindie-orderitem-api
- baseURL: https://www.tindie.com/api/v1
  baseurl_source: declared
  description: Store product listings (public read).
  name: Tindie Product API
  slug: tindie-product-api
artifact_total: 11
collections:
- collection_type: open
  name: Tindie order API
  slug: open-tindie-order-api
- collection_type: open
  name: Tindie order orderitem API
  slug: open-tindie-orderitem-api
- collection_type: open
  name: Tindie order product API
  slug: open-tindie-product-api
- collection_type: open
  name: API Collection
  slug: open-tindie-product-schema
common:
- group: auth
  href: https://artifacts.apis.io/tindie/security/tindie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tindie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tindie.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.tindie.com/api/v1/
- group: operate
  title: ''
  type: Support
  url: https://www.tindie.com/help/
- group: company
  title: ''
  type: Blog
  url: https://www.tindie.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tindie.com/about/terms/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tindie
- group: auth
  href: https://artifacts.apis.io/tindie/authentication/tindie-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tindie-authentication.yml
- group: design
  href: https://artifacts.apis.io/tindie/conventions/tindie-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tindie-conventions.yml
- group: design
  href: https://artifacts.apis.io/tindie/errors/tindie-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tindie-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tindie/data-model/tindie-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tindie-data-model.yml
- group: design
  href: https://artifacts.apis.io/tindie/lifecycle/tindie-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tindie-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/tindie/well-known/tindie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tindie-well-known.yml
- group: agent
  href: https://artifacts.apis.io/tindie/mcp/tindie-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tindie-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tindie/llms/tindie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tindie-llms.txt
- group: design
  href: https://artifacts.apis.io/tindie/conformance/tindie-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tindie-conformance.yml
- group: other
  href: https://artifacts.apis.io/tindie/overlays/tindie-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tindie-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/tindie/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tindie is an online marketplace for indie electronics and maker hardware — DIY kits, robotics, 3D-printing gear, IoT boards, and open-source hardware sold directly by independent creators worldwide. Tindie publishes a small public REST API built on Django Tastypie that exposes product listings and, for authenticated sellers, their orders and order line items, using API-key authentication (ApiKey) and standard Tastypie limit/offset pagination with a self-describing per-resource schema surface.
image: https://avatars.githubusercontent.com/u/2267159
layout: provider
modified: '2026-07-21'
name: Tindie
nav: Providers
network: true
overview: 'Tindie publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Order API, Orderitem API, and Product API. Tagged areas include Company, Marketplace, Hardware, Electronics, and Maker.


  Tindie''s developer surface includes API reference, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 47.8
    developer_ergonomics: 28.0
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 28.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tindie Authentication
  slug: tindie-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Tindie Domain Security
  slug: tindie-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Browse Tindie products
  slug: tindie-browse-products
- name: Fetch Tindie seller orders
  slug: tindie-fetch-orders
slug: tindie
tags:
- Company
- Marketplace
- Hardware
- Electronics
- Maker
- E-Commerce
- Open Source Hardware
- Order
website: https://www.tindie.com
---
