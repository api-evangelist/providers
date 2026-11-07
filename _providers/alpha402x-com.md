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
- description: Equity research data API providing quantitative and qualitative analysis, WACC builds, 10‑Q highlights, line‑item trajectory, and SEC filing bundles. Free sample cards available, paid usage via USDC.
  name: Alpha402X API
  slug: alpha402x-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/alpha402x-com/mcp/alpha402x-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alpha402x-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/alpha402x-com/hosts/alpha402x-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alpha402x-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/alpha402x-com/vendors/alpha402x-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alpha402x-com-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://alpha402x.com/api-key/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://alpha402x.com/blog/pricing-power
- group: company
  title: ''
  type: Blog
  url: https://alpha402x.com/blog
- group: auth
  href: https://artifacts.apis.io/alpha402x-com/security/alpha402x-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpha402x-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alpha402x.com/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing known hosts.
  evidence:
  - status: 0
    url: https://api.alpha402x.com/openapi.json
  - status: 200
    url: https://alpha402x.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Alpha402X provides equity research data for humans and AI agents, offering quantitative and qualitative analysis, WACC builds, 10‑Q highlights, line‑item trajectory, and SEC filing bundles. Users can access free sample cards and purchase detailed reports via USDC on Base. The platform aggregates SEC filings into actionable research cards, with pricing at $0.25 per call. No account is required for free samples, and API keys are available for paid usage.
image: https://alpha402x.com/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at alpha402x.com.
  name: Alpha402X MCP Server
  slug: alpha402x-com-mcp-yml
modified: '2026-11-01'
name: Alpha402X
nav: Providers
network: true
overview: 'Alpha402X is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Equity Research, Data API, AI Agents, and Quantitative Analysis.


  Alpha402X''s developer surface includes sandbox, pricing, engineering blog, and 5 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 8.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alpha402X Com Domain Security
  slug: alpha402x-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alpha402x-com
tags:
- Finance
- Equity Research
- Data API
- AI Agents
- Quantitative Analysis
website: https://alpha402x.com/
---
