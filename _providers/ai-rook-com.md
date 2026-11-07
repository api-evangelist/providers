---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 13.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI Rook — Agent Commerce Platform offering 77 x402 endpoints (62 paid, 15 free) for AI agents, crypto trading, and more.
  name: AI Rook Agents API
  slug: ai-rook-agents-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/ai-rook-com/plans/ai-rook-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ai-rook-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/ai-rook-com/authentication/ai-rook-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ai-rook-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/ai-rook-com/errors/ai-rook-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ai-rook-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/ai-rook-com/llms/ai-rook-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-rook-com-llms.txt
- group: other
  href: https://artifacts.apis.io/ai-rook-com/a2a/ai-rook-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ai-rook-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ai-rook-com/mcp/ai-rook-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ai-rook-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/ai-rook-com/hosts/ai-rook-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-rook-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ai-rook-com/security/ai-rook-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-rook-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-rook.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agents.ai-rook.com
- group: docs
  title: ''
  type: Documentation
  url: https://agents.ai-rook.com/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://agents.ai-rook.com
- group: operate
  title: ''
  type: Support
  url: https://ai-rook.com/terms
- group: company
  title: ''
  type: Blog
  url: https://ai-rook.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ai-Rook
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai-rook.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai-rook.com/privacy
coverage:
  checked: '2026-11-01'
  detail: OpenAPI spec discovered at https://agents.ai-rook.com/openapi.json but not fetched due to preflight constraints.
  evidence:
  - status: 200
    url: https://agents.ai-rook.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AI Rook builds autonomous AI machines, offering the x402 API platform with 62 paid endpoints for AI agents, crypto trading across Base, Solana, Hedera, a local LLM fleet, and agentic operations tooling. The service provides discounted pricing powered by owned GPU hardware, micropayment settlement in seconds, and 24/7 autonomous operation without human intervention.
image: https://ai-rook.com/assets/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at agents.ai-rook.com.
  name: AI Rook MCP Server
  slug: ai-rook-com-mcp-yml
modified: '2026-11-01'
name: AI Rook
nav: Providers
network: true
overview: 'AI Rook is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Autonomous, Cryptocurrency, LLM, and Payments.


  AI Rook''s developer surface includes authentication, documentation, API reference, support, engineering blog, and 12 more developer resources.'
plans:
- name: Ai Rook Com Plans Pricing
  plan_count: 2
  slug: ai-rook-com-plans-pricing
random_paper: 22
scopes:
- name: Ai Rook Com Scopes
  scope_count: 0
  slug: ai-rook-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 25.5
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ai Rook Com Authentication
  slug: ai-rook-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ai Rook Com Domain Security
  slug: ai-rook-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ai-rook-com
tags:
- Artificial Intelligence
- Autonomous
- Cryptocurrency
- LLM
- Payments
- Trading
website: https://ai-rook.com/
---
