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
    agent_skills: unknown
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
  score: 6.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Wash/sybil screening + the Real-Agent Index for Base agent wallets — is this wallet a real autonomous agent or a fake-volume sybil? Machine-payable via x402 (USDC on Base).
  name: AgentFlow API
  slug: agentflow-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/agentflow-watch/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/agentflow-watch/mcp/agentflow-watch-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentflow-watch-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentflow-watch/hosts/agentflow-watch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentflow-watch-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentflow-watch/vendors/agentflow-watch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentflow-watch-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentflow-watch/security/agentflow-watch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentflow-watch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentflow.watch/
- group: docs
  title: ''
  type: APIReference
  url: https://agentflow.watch/openapi.json
- group: docs
  title: ''
  type: Documentation
  url: https://agentflow.watch/openapi.json
created: '2026-10-31'
description: AgentFlow provides a live map of AI‑agent money on the Base blockchain, labeling autonomous AI‑agent wallets and tracking their USDC flow in real time. The platform scores each Base wallet based on activity patterns, distinguishing genuine AI agents from MEV bots and market makers. Users can monitor wallets via a free dashboard and obtain API access to receive real‑time updates or webhook notifications when a wallet goes silent. The service offers a free tier with rate‑limited calls and a paid tier for unlimited, machine‑payable usage.
image: https://agentflow.watch/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at agentflow.watch.
  name: AgentFlow MCP Server
  slug: agentflow-watch-mcp-yml
modified: '2026-10-31'
name: AgentFlow
nav: Providers
network: true
overview: 'AgentFlow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Finance, Blockchain, Base, and USDC.


  AgentFlow''s developer surface includes API reference, documentation, and 6 more developer resources.'
random_paper: 11
scopes:
- name: Agentflow Watch Scopes
  scope_count: 0
  slug: agentflow-watch-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.8
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 11.0
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentflow Watch Authentication
  slug: agentflow-watch-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentflow Watch Domain Security
  slug: agentflow-watch-domain-security
  summary_line: TLSv1.3
slug: agentflow-watch
tags:
- Artificial Intelligence
- Finance
- Blockchain
- Base
- USDC
- Monitoring
website: https://agentflow.watch/
---
