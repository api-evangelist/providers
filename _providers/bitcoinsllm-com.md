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
    agentic_access: derived
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
  score: 5.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bitcoinsllm Com Agentic Access
  operation_count: 9
  slug: bitcoinsllm-com-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- description: Autotrade Agent API providing LLM-powered trading agent operations.
  name: Autotrade Agent API
  slug: autotrade-agent-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/bitcoinsllm-com/agentic-access/bitcoinsllm-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bitcoinsllm-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bitcoinsllm-com/rules/bitcoinsllm-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bitcoinsllm-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bitcoinsllm-com/conformance/bitcoinsllm-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitcoinsllm-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bitcoinsllm-com/mcp/bitcoinsllm-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bitcoinsllm-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bitcoinsllm-com/well-known/bitcoinsllm-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitcoinsllm-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitcoinsllm-com/hosts/bitcoinsllm-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitcoinsllm-com-hosts.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.bitcoinsllm.com/docs
- group: auth
  href: https://artifacts.apis.io/bitcoinsllm-com/security/bitcoinsllm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitcoinsllm-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitcoinsllm.com/
created: '2026-11-02'
description: Autotrade provides autonomous LLM-powered trading agents that connect over the MCP (Machine Communication Protocol). Users can deploy an LLM agent, configure trading strategies, and let the system execute trades continuously on their behalf. The platform emphasizes secure key exchange, real‑time market data integration, and 24/7 operation for crypto and traditional assets.
layout: provider
mcp_servers:
- description: Remote MCP server at api.bitcoinsllm.com.
  name: Autotrade MCP Server
  slug: bitcoinsllm-com-mcp-yml
modified: '2026-11-02'
name: Autotrade
nav: Providers
network: true
overview: 'Autotrade is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LLM, Trading, Autonomous Agents, and Cryptocurrency.


  The Autotrade catalog on APIs.io includes 1 Spectral governance ruleset.


  Autotrade''s developer surface includes API reference and 8 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Autotrade API Rules
  rule_count: 19
  severity_counts:
    error: 16
    hint: 0
    info: 2
    warn: 1
  slug: bitcoinsllm-com-rules
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 61.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 9.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitcoinsllm Com Domain Security
  slug: bitcoinsllm-com-domain-security
  summary_line: TLSv1.3
slug: bitcoinsllm-com
tags:
- Company
- LLM
- Trading
- Autonomous Agents
- Cryptocurrency
website: https://bitcoinsllm.com/
---
