---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/a1-gallery/plans/a1-gallery-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/a1-gallery-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/a1-gallery/changelog/a1-gallery-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/a1-gallery-changelog.yml
- group: agent
  href: https://artifacts.apis.io/a1-gallery/llms/a1-gallery-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a1-gallery-llms.txt
- group: agent
  href: https://artifacts.apis.io/a1-gallery/mcp/a1-gallery-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/a1-gallery-mcp.yml
- group: agent
  href: https://artifacts.apis.io/a1-gallery/well-known/a1-gallery-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/a1-gallery-well-known.yml
- group: other
  href: https://artifacts.apis.io/a1-gallery/hosts/a1-gallery-hosts.yml
  title: ''
  type: Hosts
  url: hosts/a1-gallery-hosts.yml
- group: other
  href: https://artifacts.apis.io/a1-gallery/vendors/a1-gallery-vendors.yml
  title: ''
  type: Vendors
  url: vendors/a1-gallery-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.a1.gallery/terms
- group: auth
  title: ''
  type: Security
  url: https://www.a1.gallery/category/security
- group: start
  title: ''
  type: Sandbox
  url: https://www.a1.gallery/website/playground
- group: operate
  title: ''
  type: Roadmap
  url: https://www.a1.gallery/website/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.a1.gallery/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.a1.gallery/pricing
- group: start
  title: ''
  type: Login
  url: https://www.a1.gallery/login
- group: other
  title: ''
  type: Leadership
  url: https://www.a1.gallery/sections/team
- group: docs
  title: ''
  type: Documentation
  url: https://www.a1.gallery/pages/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.a1.gallery/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.a1.gallery/blog
- group: auth
  href: https://artifacts.apis.io/a1-gallery/security/a1-gallery-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a1-gallery-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a1.gallery/
coverage:
  checked: '2026-10-31'
  detail: MCP JSON-RPC endpoint requires Bearer token (401 Unauthorized)
  evidence:
  - status: 401
    url: https://www.a1.gallery/api/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: A1 Gallery is a curated collection of the best website designs found on the internet, offering hand‑picked inspiration for designers, developers, and creatives. Updated nearly every day, the gallery showcases diverse styles and trends to spark ideas and inform design decisions.
image: https://www.a1.gallery/images/a1-favicon-192.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.a1.gallery requiring OAuth.
  name: A1 Gallery MCP Server
  slug: a1-gallery-mcp-yml
modified: '2026-10-31'
name: A1 Gallery
nav: Providers
network: true
overview: 'A1 Gallery is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Design, Gallery, Web, and Creative.


  A1 Gallery''s developer surface includes changelog, sandbox, pricing, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: A1 Gallery Plans Pricing
  plan_count: 2
  slug: a1-gallery-plans-pricing
random_paper: 7
scopes:
- name: A1 Gallery Scopes
  scope_count: 0
  slug: a1-gallery-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 40.8
    operational_transparency: 15.8
  previous_composite: 28.2
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: A1 Gallery Authentication
  slug: a1-gallery-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: A1 Gallery Domain Security
  slug: a1-gallery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: a1-gallery
tags:
- Design
- Gallery
- Web
- Creative
website: https://a1.gallery/
---
