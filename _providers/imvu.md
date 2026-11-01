---
access_model:
  confidence: high
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: First-party in-world scripting API for IMVU Live Rooms. Room scripts are single-file Lua programs executed server-side in a Luau sandbox; the engine calls event functions (event_start, event_begin_ite
  name: IMVU Room Scripting API
  slug: imvu-room-scripting-api
- description: 'Production hypermedia REST API serving IMVU''s own web and mobile clients. It is publicly reachable and a meaningful slice of it answers unauthenticated: GET /product/product-<id>, /user/user-<id> and '
  name: IMVU REST API
  slug: imvu-rest-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/imvu/lifecycle/imvu-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/imvu-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/imvu/hosts/imvu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/imvu-hosts.yml
- group: other
  href: https://artifacts.apis.io/imvu/vendors/imvu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/imvu-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://togetherlabs.com/press/
- group: company
  title: ''
  type: Blog
  url: https://togetherlabs.com/press/
- group: auth
  href: https://artifacts.apis.io/imvu/security/imvu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/imvu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://togetherlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/imvu/imvu-scripting-docs/blob/main/README.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/imvu
- group: operate
  title: ''
  type: Support
  url: https://support.imvu.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://blog.imvu.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://about.imvu.com/vip-club
- group: start
  title: ''
  type: SignUp
  url: https://secure.imvu.com/welcome/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.imvu.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imvu.com/next/policyhub/privacypolicy/
- group: commercial
  href: https://artifacts.apis.io/imvu/plans/imvu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/imvu-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/imvu/rate-limits/imvu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/imvu-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/imvu/lifecycle/imvu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/imvu-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/imvu/conventions/imvu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/imvu-conventions.yml
- group: design
  href: https://artifacts.apis.io/imvu/conventions/imvu-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/imvu-conventions.yml
- group: design
  href: https://artifacts.apis.io/imvu/data-model/imvu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/imvu-data-model.yml
- group: design
  href: https://artifacts.apis.io/imvu/conformance/imvu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/imvu-conformance.yml
coverage:
  checked: '2026-10-20'
  detail: api.imvu.com is a live but undocumented hypermedia API that answers REST_DISCOVER_003 404s for openapi.json, swagger.json and api-docs, and the only published docs are the Lua room-scripting README on GitHub, with no HTTP contract.
  evidence:
  - status: 404
    url: https://api.imvu.com/openapi.json
  - status: 404
    url: https://api.imvu.com/swagger.json
  - status: 200
    url: https://raw.githubusercontent.com/imvu/imvu-scripting-docs/main/README.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-23'
description: 'Together Labs (Palo Alto, California) is the company behind IMVU, the 3D avatar-based social network and virtual-goods marketplace, alongside MetaJuice, its blockchain arm, and the VCOIN transferable digital currency. Its developer surface is unusual for a consumer platform: the public developer program that once issued API keys was retired, but api.imvu.com remains a live, publicly readable hypermedia REST API — a "denormalized" node envelope over users, products, rooms and derivation relationships — and Together Labs publishes a genuinely documented, first-party in-world scripting API for IMVU rooms in Lua/Luau on GitHub, complete with an event model, an imvu.* method surface, a persistent key/value data module and published resource limits. Neither surface ships an OpenAPI, an AsyncAPI, an MCP server, an agent card or an llms.txt.'
image: https://togetherlabs.com/wp-content/uploads/2021/01/together-labs-logo.png
layout: provider
modified: '2026-10-06'
name: Together Labs
nav: Providers
network: true
overview: 'Together Labs is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Network, Virtual Worlds, Metaverse, and Gaming.


  Together Labs'' developer surface includes engineering blog, documentation, support, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Imvu Plans Pricing
  plan_count: 5
  slug: imvu-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 7
  name: Imvu Rate Limits
  slug: imvu-rate-limits
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 51.0
    catalog_earned_first_party: 24.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 44.7
  previous_composite: 32.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/imvu/imvu-2026-09-02T145854.png
security:
- kind: authentication
  name: Imvu Authentication
  slug: imvu-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Imvu Domain Security
  slug: imvu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: imvu
tags:
- Company
- Social Network
- Virtual Worlds
- Metaverse
- Gaming
- Avatars
- Virtual Goods
- Marketplace
- User Generated Content
- Scripting
- Digital Currency
- Blockchain
website: https://togetherlabs.com/
---
