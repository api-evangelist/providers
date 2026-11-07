---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
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
- description: Public API for AgentRank providing search, lookup, and ranking of MCP servers and tools. Documentation at https://agentrank-ai.com/docs/api.
  name: AgentRank API
  slug: agentrank-api
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/agentrank-ai-com/rate-limits/agentrank-ai-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentrank-ai-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agentrank-ai-com/plans/agentrank-ai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentrank-ai-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/agentrank-ai-com/changelog/agentrank-ai-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentrank-ai-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/agentrank-ai-com/conventions/agentrank-ai-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentrank-ai-com-conventions.yml
- group: agent
  href: https://artifacts.apis.io/agentrank-ai-com/llms/agentrank-ai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentrank-ai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentrank-ai-com/mcp/agentrank-ai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentrank-ai-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentrank-ai-com/well-known/agentrank-ai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentrank-ai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentrank-ai-com/hosts/agentrank-ai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentrank-ai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentrank-ai-com/vendors/agentrank-ai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentrank-ai-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://agentrank-ai.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://agentrank-ai.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://agentrank-ai.com/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://agentrank-ai.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://agentrank-ai.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://agentrank-ai.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/agentrank-ai-com/security/agentrank-ai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentrank-ai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentrank-ai.com/
coverage:
  checked: '2026-11-01'
  detail: API documentation is served as HTML with no machine‑readable OpenAPI/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://agentrank-ai.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AgentRank provides a leaderboard and ranking of MCP (Machine-Callable-Protocol) servers, tools, and agents. It aggregates popularity signals, usage metrics, and community contributions to help developers discover and integrate top AI agents and tools. The platform offers daily updates, detailed tool profiles, pricing information, and a blog covering ecosystem trends and news.
image: https://agentrank-ai.com/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at agentrank-ai.com.
  name: AgentRank MCP Server
  slug: agentrank-ai-com-mcp-yml
modified: '2026-11-01'
name: AgentRank
nav: Providers
network: true
overview: 'AgentRank is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Rankings, Tools, Marketplace, and Analytics.


  AgentRank''s developer surface includes changelog, pricing, documentation, engineering blog, getting-started guide, and 12 more developer resources.'
plans:
- name: Agentrank Ai Com Plans Pricing
  plan_count: 4
  slug: agentrank-ai-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Agentrank Ai Com Rate Limits
  slug: agentrank-ai-com-rate-limits
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.5
    operational_transparency: 28.9
  previous_composite: 22.4
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentrank Ai Com Domain Security
  slug: agentrank-ai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentrank-ai-com
tags:
- Artificial Intelligence
- Rankings
- Tools
- Marketplace
- Analytics
website: https://agentrank-ai.com/
---
