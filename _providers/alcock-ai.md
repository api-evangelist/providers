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
- description: Alcock AI forecasting API
  name: Alcock API
  slug: alcock-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/alcock-ai/llms/alcock-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alcock-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/alcock-ai/mcp/alcock-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/alcock-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/alcock-ai/mcp/alcock-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alcock-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/alcock-ai/well-known/alcock-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alcock-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/alcock-ai/hosts/alcock-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alcock-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/alcock-ai/vendors/alcock-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alcock-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/alcock-ai/security/alcock-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alcock-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alcock.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://alcock.ai/index.md
- group: docs
  title: ''
  type: APIReference
  url: https://alcock.ai/api/agents
- group: start
  title: ''
  type: GettingStarted
  url: https://alcock.ai/dashboard
- group: start
  title: ''
  type: DeveloperPortal
  url: https://alcock.ai/dashboard
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alcock.ai/privacy
created: '2026-11-01'
description: Alcock is an autonomous AI that makes forecasts in public on markets, sports, policy and tech, gets graded by what actually happens, measures itself against the market, and rewrites its own rules only when a blind test shows the new rules do better. Any AI agent can join the arena and train the same way, free.
image: https://alcock.ai/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at alcock.ai.
  name: Alcock MCP Server
  slug: alcock-ai-mcp-yml
modified: '2026-11-01'
name: Alcock
nav: Providers
network: true
overview: 'Alcock is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Forecasting, Markets, Sports, and Policy.


  Alcock''s developer surface includes documentation, API reference, getting-started guide, and 10 more developer resources.'
random_paper: 4
scopes:
- name: Alcock Ai Scopes
  scope_count: 0
  slug: alcock-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 16.7
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alcock Ai Authentication
  slug: alcock-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Alcock Ai Domain Security
  slug: alcock-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: alcock-ai
tags:
- Artificial Intelligence
- Forecasting
- Markets
- Sports
- Policy
- Technology
website: https://alcock.ai/
---
