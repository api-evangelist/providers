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
    agent_card: flavored
    agent_skills: derived
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
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Deterministic pre‑execution audit services for autonomous trading agents.
  name: DJZS Protocol
  slug: djzs-protocol
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/djzs-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/djzs-ai/conformance/djzs-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/djzs-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/djzs-ai/llms/djzs-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/djzs-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/djzs-ai/a2a/djzs-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/djzs-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/djzs-ai/mcp/djzs-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/djzs-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/djzs-ai/hosts/djzs-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/djzs-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/djzs-ai/vendors/djzs-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/djzs-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/djzs-ai/security/djzs-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/djzs-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://djzs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://djzs.ai/guide
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.djzs.ai/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://djzs.ai/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SIFR0-dev/djzs-AI
created: '2026-11-05'
description: DJZS AI, LLC provides deterministic pre‑execution audit services for autonomous trading agents. It reads the reasoning behind a trade and refuses it when the reason does not hold up, protecting bots from bad trades. The platform offers five free verdicts per day and charges 2.00 USDC per receipt on Base mainnet, with on‑chain proof of audit. It serves markets like Kalshi, Polymarket, Hyperliquid perps, and treasury bots, aiming to prevent erroneous orders before they fire.
image: https://djzs.ai/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.djzs.ai.
  name: DJZS MCP Server
  slug: djzs-ai-mcp-yml
modified: '2026-11-05'
name: DJZS
nav: Providers
network: true
overview: 'DJZS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Trading, Auditing, Autonomous Agents, and Finance.


  DJZS''s developer surface includes documentation, API reference, and 11 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 18.5
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 12.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Djzs Ai Domain Security
  slug: djzs-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: audit
  slug: djzs-ai-audit
slug: djzs-ai
tags:
- Artificial Intelligence
- Trading
- Auditing
- Autonomous Agents
- Finance
website: https://djzs.ai/
---
