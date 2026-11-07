---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/livescoremcp-com/rate-limits/livescoremcp-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/livescoremcp-com-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/livescoremcp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/livescoremcp-com/mcp/livescoremcp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/livescoremcp-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/livescoremcp-com/hosts/livescoremcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/livescoremcp-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://livescoremcp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://livescoremcp.com/privacy
- group: auth
  href: https://artifacts.apis.io/livescoremcp-com/security/livescoremcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/livescoremcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://livescoremcp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://livescoremcp.com/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://livescoremcp.com/#steps-card
- group: commercial
  title: ''
  type: Pricing
  url: https://livescoremcp.com/#usage-policy
- group: operate
  title: ''
  type: Support
  url: mailto:gillis.haasnoot@gmail.com?subject=LiveScore%20MCP%20Support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/holoduke/livescore-mcp
- group: start
  title: ''
  type: SignUp
  url: https://livescoremcp.com/#steps-card
created: '2026-10-31'
description: MCP server for real-time football scores, fixtures, team stats and player data. Connect Claude, Cursor or any AI agent to 1000+ leagues worldwide. Free under fair use; full commercial access $100/month.
image: https://livescoremcp.com/static/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at livescoremcp.com.
  name: LiveScore MCP MCP Server
  slug: livescoremcp-com-mcp-yml
modified: '2026-10-31'
name: LiveScore MCP
nav: Providers
network: true
overview: 'LiveScore MCP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Football, Live Scores, MCP, Artificial Intelligence, and Sports Data.


  LiveScore MCP''s developer surface includes API reference, getting-started guide, pricing, support, signup flow, and 9 more developer resources.'
plans:
- name: Livescoremcp Com Plans Pricing
  plan_count: 0
  slug: livescoremcp-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Livescoremcp Com Rate Limits
  slug: livescoremcp-com-rate-limits
scopes:
- name: Livescoremcp Com Scopes
  scope_count: 0
  slug: livescoremcp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.7
    discoverability: 48.3
    operational_transparency: 23.7
  previous_composite: 24.2
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
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
screenshot: https://apis.io/screenshots/livescoremcp-com/livescoremcp-com-2026-11-03T134941.png
security:
- kind: authentication
  name: Livescoremcp Com Authentication
  slug: livescoremcp-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Livescoremcp Com Domain Security
  slug: livescoremcp-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: livescoremcp-com
tags:
- Football
- Live Scores
- MCP
- Artificial Intelligence
- Sports Data
website: https://livescoremcp.com/
---
