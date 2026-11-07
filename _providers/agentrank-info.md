---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    agent_card: conformant
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
  score: 11.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://agentrank.info/
- group: docs
  title: ''
  type: Documentation
  url: https://agentrank.info/whitepaper
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/andysalvo/agentrank/blob/main/METHODOLOGY.md
- group: docs
  title: ''
  type: Documentation
  url: https://agentrank.info/research
- group: other
  title: ''
  type: Leadership
  url: https://agentrank.info/about
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/andysalvo/agentrank
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/andysalvo
- group: agent
  href: https://artifacts.apis.io/agentrank-info/llms/agentrank-info-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentrank-info-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://agentrank.info/llms.txt
- group: other
  href: https://artifacts.apis.io/agentrank-info/a2a/agentrank-info-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentrank-info-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentrank-info/well-known/agentrank-info-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentrank-info-well-known.yml
- group: build
  href: https://artifacts.apis.io/agentrank-info/packages/agentrank-info-packages.yml
  title: ''
  type: Packages
  url: packages/agentrank-info-packages.yml
- group: build
  href: https://artifacts.apis.io/agentrank-info/packages/agentrank-info-packages.yml
  title: ''
  type: SDKs
  url: packages/agentrank-info-packages.yml
- group: agent
  href: https://artifacts.apis.io/agentrank-info/mcp/agentrank-info-mcp.yml
  title: ''
  type: X-MCPServerRetired
  url: mcp/agentrank-info-mcp.yml
- group: design
  href: https://artifacts.apis.io/agentrank-info/lifecycle/agentrank-info-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentrank-info-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/agentrank-info/plans/agentrank-info-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentrank-info-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/agentrank-info/rate-limits/agentrank-info-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentrank-info-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/agentrank-info/conformance/agentrank-info-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentrank-info-conformance.yml
- group: other
  href: https://artifacts.apis.io/agentrank-info/regulatory/agentrank-info-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/agentrank-info-regulatory-posture.yml
- group: auth
  href: https://artifacts.apis.io/agentrank-info/security/agentrank-info-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentrank-info-domain-security.yml
coverage:
  checked: '2026-09-19'
  detail: AgentRank's entire machine surface (REST, MCP and A2A) lived on api.agentrank.info, which resolves to 167.71.254.98 but refuses TCP connections on 443 and 80, and the company's source repository is archived as "Retired ... The hosted service no longer runs"; agentrank.info still serves the agent card and llms.txt that advertise the dead endpoints while its index pages return HTTP 500 — a product retirement (Crest Deployment Systems LLC is still active on GitHub), not a company closure, and no OpenAPI was ever published.
  evidence:
  - status: 0
    url: https://api.agentrank.info/
  - status: 200
    url: https://api.github.com/repos/andysalvo/agentrank
  - status: 500
    url: https://agentrank.info/agents
  - status: 200
    url: https://agentrank.info/.well-known/agent-card.json
  reason: defunct
  state: none
created: '2026-09-19'
description: 'Crest Deployment Systems LLC built AgentRank, a settlement-grounded reputation index for AI agents that scored x402 counterparties 0-1000 from real on-chain USDC settlement on Base, weighted by payer standing, and served it as a free read-only REST API, a hosted MCP server and an A2A agent on api.agentrank.info. The service is retired: the source repository is archived with the note "The hosted service no longer runs", the API host refuses connections, and the website''s index pages fail, while the whitepaper, research papers, A2A agent card, llms.txt and four npm client packages remain published. Founded by Andy Salvo and Jameson Ackerman.'
image: https://agentrank.info/apple-touch-icon.png
layout: provider
modified: '2026-09-19'
name: Crest Deployment Systems LLC
nav: Providers
network: true
overview: 'Crest Deployment Systems LLC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Agent Reputation, Trust and Safety, and x402.


  Crest Deployment Systems LLC''s developer surface includes documentation and 19 more developer resources.'
plans:
- name: Agentrank Info Plans Pricing
  plan_count: 1
  slug: agentrank-info-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Agentrank Info Rate Limits
  slug: agentrank-info-rate-limits
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 60.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentrank Info Domain Security
  slug: agentrank-info-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentrank-info
tags:
- Company
- AI Agents
- Agent Reputation
- Trust and Safety
- x402
- Agentic Payments
- Blockchain
- A2A
- MCP
website: https://agentrank.info/
---
