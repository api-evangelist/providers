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
  band: human-only
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Fishing venue data and booking tools via MCP JSON-RPC.
  name: Angling Lines API
  slug: angling-lines-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/anglinglines-com/llms/anglinglines-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anglinglines-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/anglinglines-com/mcp/anglinglines-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anglinglines-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/anglinglines-com/hosts/anglinglines-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anglinglines-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anglinglines-com/vendors/anglinglines-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anglinglines-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.anglinglines.com/press
- group: start
  title: ''
  type: Login
  url: https://www.anglinglines.com/login
- group: auth
  href: https://artifacts.apis.io/anglinglines-com/security/anglinglines-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anglinglines-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anglinglines.com/
- group: company
  title: ''
  type: Blog
  url: https://www.anglinglines.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anglinglines.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anglinglines.com/privacy
created: '2026-11-01'
description: Carp fishing holidays in France at 50+ personally vetted lakes, with carp to 83lb+. Rated Excellent on Trustpilot. Flexible payment plans. Trusted by over 47,000 UK anglers for 26 years. For anglers chasing a true personal best, these big carp lakes in France offer a genuine opportunity to land fish of 60lb, 70lb and beyond. Angling Lines works exclusively with proven venues where you have the very real chance of exceptional catches. Read authentic reviews from anglers who have already made their catch of a lifetime.
examples:
- key_count: 3
  name: Anglinglines Com Mcp
  slug: anglinglines-com-mcp
image: https://www.anglinglines.com/images/allogo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at www.anglinglines.com.
  name: Angling Lines MCP Server
  slug: anglinglines-com-mcp-yml
modified: '2026-11-01'
name: Angling Lines
nav: Providers
network: true
overview: 'Angling Lines is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fishing, carp, Holiday, France, and Angling.


  Angling Lines'' developer surface includes engineering blog and 10 more developer resources.'
random_paper: 7
scopes:
- name: Anglinglines Com Scopes
  scope_count: 0
  slug: anglinglines-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 65.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 15.3
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anglinglines Com Authentication
  slug: anglinglines-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anglinglines Com Domain Security
  slug: anglinglines-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anglinglines-com
tags:
- Fishing
- carp
- Holiday
- France
- Angling
website: https://www.anglinglines.com/
---
