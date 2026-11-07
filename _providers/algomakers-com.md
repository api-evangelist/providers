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
- description: MCP endpoint providing tool list for AlgoMaker platform.
  name: AlgoMaker MCP API
  slug: algomaker-mcp-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/algomakers-com/llms/algomakers-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algomakers-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/algomakers-com/mcp/algomakers-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/algomakers-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/algomakers-com/hosts/algomakers-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/algomakers-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/algomakers-com/vendors/algomakers-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/algomakers-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/algomakers-com/security/algomakers-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algomakers-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://algomakers.com/
- group: operate
  title: ''
  type: Support
  url: https://algomakers.com/contato
- group: commercial
  title: ''
  type: TermsOfService
  url: https://algomakers.com/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://algomakers.com/privacidade
created: '2026-11-01'
description: AlgoMaker provides a Model Context Protocol (MCP) server for quantitative trading, enabling AI agents to mine, validate, and paper‑trade strategies. The platform runs on the operator’s own infrastructure, offering out‑of‑sample gates, cost measurement per instrument, and live execution that records decisions with full auditability. It includes a local API for non‑agent systems, a research pipeline with Monte Carlo resampling, portfolio composition, and detailed execution analytics. Designed for institutional desks, AlgoMaker emphasizes transparency, human‑in‑the‑loop controls, and privacy‑preserving data handling.
image: https://algomakers.com/marca.png
layout: provider
mcp_servers:
- description: Remote MCP server at algomakers.com.
  name: AlgoMaker MCP Server
  slug: algomakers-com-mcp-yml
modified: '2026-11-01'
name: AlgoMaker
nav: Providers
network: true
overview: 'AlgoMaker is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Quantitative Trading, AI Agents, MCP, Finance, and Institutional.


  AlgoMaker''s developer surface includes support and 8 more developer resources.'
plans:
- name: Algomakers Com Plans Pricing
  plan_count: 0
  slug: algomakers-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Algomakers Com Rate Limits
  slug: algomakers-com-rate-limits
scopes:
- name: Algomakers Com Scopes
  scope_count: 0
  slug: algomakers-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 12.9
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
  name: Algomakers Com Authentication
  slug: algomakers-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Algomakers Com Domain Security
  slug: algomakers-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: algomakers-com
tags:
- Quantitative Trading
- AI Agents
- MCP
- Finance
- Institutional
website: https://algomakers.com/
---
