---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for BuildGets construction budgeting tools
  name: BuildGets API
  slug: buildgets-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/buildgets-com/llms/buildgets-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildgets-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/buildgets-com/mcp/buildgets-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buildgets-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/buildgets-com/well-known/buildgets-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buildgets-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/buildgets-com/hosts/buildgets-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildgets-com-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.buildgets.com/us/guides/
- group: company
  title: ''
  type: Blog
  url: https://www.buildgets.com/blog/
- group: auth
  href: https://artifacts.apis.io/buildgets-com/security/buildgets-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildgets-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildgets.com/
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.buildgets.com/us/guides/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: BuildGets offers AI-powered construction budgeting tools, allowing users to open and edit BC3 files, convert PDF and Excel estimates into BC3 format, and generate detailed work budgets using artificial intelligence. The platform is online, free to start, and integrates with popular engineering software like Presto and CYPE, targeting Spanish‑speaking construction professionals seeking efficient, automated cost planning.
image: https://www.buildgets.com/og-buildgets-2026.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.buildgets.com.
  name: BuildGets MCP Server
  slug: buildgets-com-mcp-yml
modified: '2026-11-03'
name: BuildGets
nav: Providers
network: true
overview: 'BuildGets is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Artificial Intelligence, Budgeting, Spanish, and Software.


  BuildGets'' developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buildgets Com Domain Security
  slug: buildgets-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buildgets-com
tags:
- Construction
- Artificial Intelligence
- Budgeting
- Spanish
- Software
website: https://buildgets.com/
---
