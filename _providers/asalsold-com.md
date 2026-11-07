---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Mortgage tools including rate hold deadline calculator.
  name: Mortgage Tools API
  slug: mortgage-tools-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/asalsold-com/llms/asalsold-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asalsold-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/asalsold-com/mcp/asalsold-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asalsold-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/asalsold-com/hosts/asalsold-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asalsold-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/asalsold-com/vendors/asalsold-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asalsold-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/asalsold-com/security/asalsold-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asalsold-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asalsold.com/
- group: company
  title: ''
  type: Blog
  url: https://asalsold.com/category/blog/
- group: start
  title: ''
  type: Login
  url: https://app.asalsold.com/login
- group: start
  title: ''
  type: SignUp
  url: https://app.asalsold.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.asalsold.com/privacy
created: '2026-11-01'
description: Asal Sold Team, led by Asal Matinsadeghy, provides real‑estate services in the Greater Toronto Area. With over thirteen years of experience, the brokerage (Royal LePage Signature Realty) offers in‑house tools for home valuation, net‑proceeds estimation, and pre‑construction closing assistance. Recognized with multiple Royal LePage awards, the team serves Richmond Hill, Markham, Vaughan, Thornhill, North York and Toronto, helping buyers and sellers navigate the market.
image: https://asalsold.com/_next/static/immutable/media/og-home.0zyr5kv5co_wm.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at app.asalsold.com.
  name: Asal Matinsadeghy MCP Server
  slug: asalsold-com-mcp-yml
modified: '2026-11-01'
name: Asal Matinsadeghy
nav: Providers
network: true
overview: 'Asal Matinsadeghy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Brokerage, Canada, GTA, and Residential.


  Asal Matinsadeghy''s developer surface includes engineering blog, signup flow, and 8 more developer resources.'
plans:
- name: Asalsold Com Plans Pricing
  plan_count: 0
  slug: asalsold-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Asalsold Com Rate Limits
  slug: asalsold-com-rate-limits
scopes:
- name: Asalsold Com Scopes
  scope_count: 0
  slug: asalsold-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.2
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 22.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asalsold Com Authentication
  slug: asalsold-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Asalsold Com Domain Security
  slug: asalsold-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asalsold-com
tags:
- Real Estate
- Brokerage
- Canada
- GTA
- Residential
website: https://asalsold.com/
---
