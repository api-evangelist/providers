---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 14.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Image hosting API for uploading and managing images.
  name: BeeIMG API
  slug: beeimg-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/beeimg-com/rate-limits/beeimg-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/beeimg-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/beeimg-com/plans/beeimg-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beeimg-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/beeimg-com/authentication/beeimg-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beeimg-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/beeimg-com/errors/beeimg-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beeimg-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/beeimg-com/mcp/beeimg-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/beeimg-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/beeimg-com/well-known/beeimg-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beeimg-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/beeimg-com/hosts/beeimg-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beeimg-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/beeimg-com/vendors/beeimg-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beeimg-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beeimg.com/tos
- group: start
  title: ''
  type: Login
  url: https://beeimg.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BeeIMG
- group: auth
  href: https://artifacts.apis.io/beeimg-com/security/beeimg-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beeimg-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beeimg.com/
- group: company
  title: ''
  type: Blog
  url: https://beeimg.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://beeimg.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://beeimg.com/api/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beeimg.com/privacy
coverage:
  checked: '2026-11-02'
  detail: API documentation page is a JavaScript‑rendered single‑page app with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://beeimg.com/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: BeeIMG is a simple, fast, free unlimited image hosting and sharing solution created to fill up your image sharing needs. with real time image views and bandwidth stats. Most image hosts stop counting the moment someone embeds your image elsewhere. BeeIMG does not. Our custom-built serving layer counts every view at the network edge — whether someone visits your link directly or embeds it on a forum, blog, or social site.
image: https://i.beeimg.com/resources/icons/favicon-96x96.png
layout: provider
mcp_servers:
- description: Remote MCP server at beeimg.com.
  name: BeeIMG MCP Server
  slug: beeimg-com-mcp-yml
modified: '2026-11-02'
name: BeeIMG
nav: Providers
network: true
overview: 'BeeIMG is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Image Hosting, Free, Unlimited, Sharing, and Sri Lanka.


  BeeIMG''s developer surface includes authentication, engineering blog, documentation, API reference, and 13 more developer resources.'
plans:
- name: Beeimg Com Plans Pricing
  plan_count: 3
  slug: beeimg-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Beeimg Com Rate Limits
  slug: beeimg-com-rate-limits
scopes:
- name: Beeimg Com Scopes
  scope_count: 0
  slug: beeimg-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 56.7
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sri-lanka
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Beeimg Com Authentication
  slug: beeimg-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Beeimg Com Domain Security
  slug: beeimg-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: beeimg-com
tags:
- Image Hosting
- Free
- Unlimited
- Sharing
- Sri Lanka
website: https://beeimg.com/
---
