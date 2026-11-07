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
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ANOTS provides an AI agent platform accessible via Google A2A Protocol and MCP.
  name: ANOTS MCP
  slug: anots-mcp
artifact_total: 7
common:
- group: build
  href: https://artifacts.apis.io/anots-com/cli/anots-com-cli.yml
  title: ''
  type: CLI
  url: cli/anots-com-cli.yml
- group: design
  href: https://artifacts.apis.io/anots-com/errors/anots-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anots-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/anots-com/llms/anots-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anots-com-llms.txt
- group: other
  href: https://artifacts.apis.io/anots-com/a2a/anots-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/anots-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/anots-com/mcp/anots-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anots-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/anots-com/hosts/anots-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anots-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anots.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anots.com/legal/privacy
- group: auth
  href: https://artifacts.apis.io/anots-com/security/anots-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anots-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anots.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anots.com/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://anots.com/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://api.anots.com/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://anots.com/#how
- group: operate
  title: ''
  type: Support
  url: https://anots.com/notes
- group: operate
  title: ''
  type: Roadmap
  url: https://anots.com/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anots
- group: commercial
  title: ''
  type: Pricing
  url: https://anots.com/#pricing
coverage:
  checked: '2026-11-01'
  detail: OpenAPI discovery URLs on api.anots.com returned HTML pages, no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://api.anots.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Your customers' AI doesn't read your website — it asks. ANOTS gives your business an agent that answers on Claude, ChatGPT, Gemini, and Perplexity over Google A2A Protocol and MCP. 90-second setup, no SDK.
image: https://anots.com/icon.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.anots.com.
  name: ANOTS MCP Server
  slug: anots-com-mcp-yml
modified: '2026-11-01'
name: ANOTS
nav: Providers
network: true
overview: 'ANOTS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agents, MCP, A2A, and Platform.


  ANOTS''s developer surface includes CLI, documentation, API reference, getting-started guide, support, pricing, and 12 more developer resources.'
plans:
- name: Anots Com Plans Pricing
  plan_count: 0
  slug: anots-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Anots Com Rate Limits
  slug: anots-com-rate-limits
scopes:
- name: Anots Com Scopes
  scope_count: 0
  slug: anots-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 25.2
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anots Com Authentication
  slug: anots-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anots Com Domain Security
  slug: anots-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anots-com
tags:
- Artificial Intelligence
- Agents
- MCP
- A2A
- Platform
website: https://anots.com/
---
