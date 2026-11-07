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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API providing DeFi yield data and forecasts as documented on the MCP page.
  name: DeFi Garden API
  slug: defi-garden-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/defi-garden/llms/defi-garden-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/defi-garden-llms.txt
- group: agent
  href: https://artifacts.apis.io/defi-garden/mcp/defi-garden-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/defi-garden-mcp.yml
- group: agent
  href: https://artifacts.apis.io/defi-garden/well-known/defi-garden-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/defi-garden-well-known.yml
- group: other
  href: https://artifacts.apis.io/defi-garden/hosts/defi-garden-hosts.yml
  title: ''
  type: Hosts
  url: hosts/defi-garden-hosts.yml
- group: other
  href: https://artifacts.apis.io/defi-garden/vendors/defi-garden-vendors.yml
  title: ''
  type: Vendors
  url: vendors/defi-garden-vendors.yml
- group: auth
  href: https://artifacts.apis.io/defi-garden/security/defi-garden-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/defi-garden-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://defi.garden/
- group: docs
  title: ''
  type: Documentation
  url: https://www.defi.garden/
- group: docs
  title: ''
  type: APIReference
  url: https://www.defi.garden/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://www.defi.garden/plan.html
- group: other
  title: ''
  type: Methodology
  url: https://www.defi.garden/methodology
- group: other
  title: ''
  type: ForecastAccuracy
  url: https://www.defi.garden/forecast-accuracy
- group: other
  title: ''
  type: PoolsDirectory
  url: https://www.defi.garden/pools
- group: other
  title: ''
  type: Protocols
  url: https://www.defi.garden/protocols
coverage:
  checked: '2026-11-05'
  detail: Provider only offers markdown documentation on the MCP page with no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://www.defi.garden/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DeFi Garden provides live, curated DeFi yield data and forecasts across 30+ blockchain protocols. It aggregates pool information from DefiLlama, scoring yields by risk stability and projecting 14‑day APY outlooks. The platform offers a planner tool for goal‑based saving, educational resources, and a virtual yield‑funded card. All data is publicly accessible without authentication, aiming to help users compare and manage DeFi investments responsibly.
image: https://www.defi.garden/og-yield-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.defi.garden.
  name: DeFi Garden MCP Server
  slug: defi-garden-mcp-yml
modified: '2026-11-05'
name: DeFi Garden
nav: Providers
network: true
overview: 'DeFi Garden is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Crypto Data, Token Yields, and Chain Yields.


  DeFi Garden''s developer surface includes documentation, API reference, getting-started guide, and 11 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.3
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Defi Garden Domain Security
  slug: defi-garden-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: defi-garden
tags:
- DeFi
- Crypto Data
- Token Yields
- Chain Yields
website: https://defi.garden/
---
