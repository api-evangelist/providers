---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Alcoven provides a collaborative project management platform with AI integration. Public API documentation is not publicly accessible and requires authentication.
  name: Alcoven API
  slug: alcoven-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/alcoven-co/plans/alcoven-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alcoven-co-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/alcoven-co/mcp/alcoven-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alcoven-co-mcp.yml
- group: agent
  href: https://artifacts.apis.io/alcoven-co/well-known/alcoven-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alcoven-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/alcoven-co/hosts/alcoven-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alcoven-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/alcoven-co/vendors/alcoven-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alcoven-co-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alcoven
- group: auth
  href: https://artifacts.apis.io/alcoven-co/security/alcoven-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alcoven-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alcoven.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://alcoven.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.alcoven.co/signup
- group: company
  title: ''
  type: Blog
  url: https://alcoven.co/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alcoven.co/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alcoven.co/terms
coverage:
  checked: '2026-11-01'
  detail: API documentation is behind a login page requiring authentication.
  evidence:
  - status: 200
    url: https://app.alcoven.co/
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Alcoven is a web‑based collaborative project management platform that lets teams store briefs, documents, and tasks in a single project and interact with AI assistants such as Claude, Codex, and ChatGPT. Users can open a project in any of the supported AI agents, capture generated content, and have it saved back to the project. The service offers a free tier for up to five users and paid Business, Enterprise and Education plans. It is operated by Deep Node Studios Yazılım ve Teknoloji Limited Şirketi, based in Kadıköy, Istanbul, Turkey.
image: https://alcoven.co/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.alcoven.co.
  name: Alcoven MCP Server
  slug: alcoven-co-mcp-yml
modified: '2026-11-01'
name: Alcoven
nav: Providers
network: true
overview: 'Alcoven is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Collaboration, Project Management, Team Collaboration, Productivity, and ChatGPT.


  Alcoven''s developer surface includes pricing, signup flow, engineering blog, and 10 more developer resources.'
plans:
- name: Alcoven Co Plans Pricing
  plan_count: 3
  slug: alcoven-co-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Alcoven Co Rate Limits
  slug: alcoven-co-rate-limits
scopes:
- name: Alcoven Co Scopes
  scope_count: 0
  slug: alcoven-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 56.7
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 24.2
  provenance:
    conformance: unknown
    mcp: derived
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
  name: Alcoven Co Authentication
  slug: alcoven-co-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Alcoven Co Domain Security
  slug: alcoven-co-domain-security
  summary_line: TLSv1.3 · HSTS
slug: alcoven-co
tags:
- AI Collaboration
- Project Management
- Team Collaboration
- Productivity
- ChatGPT
- Claude
website: https://alcoven.co/
---
