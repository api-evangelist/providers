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
  score: 19.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API providing stock market data, AI signals, and related endpoints.
  name: Algolab API
  slug: algolab-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/algolab-vn/llms/algolab-vn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algolab-vn-llms.txt
- group: agent
  href: https://artifacts.apis.io/algolab-vn/mcp/algolab-vn-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/algolab-vn-mcp.yml
- group: agent
  href: https://artifacts.apis.io/algolab-vn/well-known/algolab-vn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/algolab-vn-well-known.yml
- group: other
  href: https://artifacts.apis.io/algolab-vn/hosts/algolab-vn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/algolab-vn-hosts.yml
- group: other
  href: https://artifacts.apis.io/algolab-vn/vendors/algolab-vn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/algolab-vn-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://algolab.vn/signup
- group: build
  title: ''
  type: SDKs
  url: https://algolab.vn/ticker/SDK
- group: company
  title: ''
  type: Newsroom
  url: https://algolab.vn/news
- group: auth
  href: https://artifacts.apis.io/algolab-vn/security/algolab-vn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algolab-vn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://algolab.vn/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://algolab.vn/docs
- group: docs
  title: ''
  type: APIReference
  url: https://algolab.vn/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://algolab.vn/docs
- group: operate
  title: ''
  type: Support
  url: https://algolab.vn/support
- group: company
  title: ''
  type: Blog
  url: https://algolab.vn/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://algolab.vn/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://algolab.vn/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://algolab.vn/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://algolab.vn/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/algolab
coverage:
  checked: '2026-11-01'
  detail: The API reference page is a JavaScript‑rendered SPA, providing no machine‑readable spec.
  evidence:
  - status: 200
    url: https://algolab.vn/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Algolab provides Vietnamese stock market data, AI-driven investment signals, and analysis tools. It offers real-time prices, backtested buy/sell signals, VN-Index forecasts, analytical reports on 50 securities, and an AI assistant via MCP for Claude and ChatGPT. The platform serves investors with data, charts, and AI insights, operated by CTCP Tập đoàn Algospace.
image: https://algolab.vn/_next/image?url=%2Falgolab-logo.png&w=640&q=75
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.algolab.vn.
  name: Algolab MCP Server
  slug: algolab-vn-mcp-yml
modified: '2026-11-01'
name: Algolab
nav: Providers
network: true
overview: 'Algolab is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Data, Artificial Intelligence, Vietnam, and Stock Market.


  Algolab''s developer surface includes signup flow, API reference, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
random_paper: 11
scopes:
- name: Algolab Vn Scopes
  scope_count: 0
  slug: algolab-vn-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 65.8
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - vietnam
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 27.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Algolab Vn Authentication
  slug: algolab-vn-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Algolab Vn Domain Security
  slug: algolab-vn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: algolab-vn
tags:
- Finance
- Data
- Artificial Intelligence
- Vietnam
- Stock Market
website: https://algolab.vn/
---
