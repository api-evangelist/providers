---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.9
  scored_at: '2026-09-01'
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
- group: auth
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
  title: ''
  type: Plans
  url: plans/imvu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imvu-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/imvu-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/imvu-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/imvu-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/imvu-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/imvu-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/imvu-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/imvu-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/imvu-packages.yml
created: '2026-08-23'
description: 'Together Labs (Palo Alto, California) is the company behind IMVU, the 3D avatar-based social network and virtual-goods marketplace, alongside MetaJuice, its blockchain arm, and the VCOIN transferable digital currency. Its developer surface is unusual for a consumer platform: the public developer program that once issued API keys was retired, but api.imvu.com remains a live, publicly readable hypermedia REST API — a "denormalized" node envelope over users, products, rooms and derivation relationships — and Together Labs publishes a genuinely documented, first-party in-world scripting API for IMVU rooms in Lua/Luau on GitHub, complete with an event model, an imvu.* method surface, a persistent key/value data module and published resource limits. Neither surface ships an OpenAPI, an AsyncAPI, an MCP server, an agent card or an llms.txt.'
image: https://togetherlabs.com/wp-content/uploads/2021/01/together-labs-logo.png
layout: provider
modified: '2026-08-23'
name: Together Labs
nav: Providers
network: true
overview: 'Together Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Networking, Virtual Worlds, Metaverse, and Gaming.


  Together Labs'' developer surface includes documentation, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Imvu Plans Pricing
  plan_count: 5
  slug: imvu-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 7
  name: Imvu Rate Limits
  slug: imvu-rate-limits
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 6.7
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 30.3
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
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
- Social Networking
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
