---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Arsaze provides an API via MCP for AI-driven video editing, referenced in the Skills documentation.
  name: Arsaze API
  slug: arsaze-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/arsaze-com/plans/arsaze-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arsaze-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/arsaze-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/arsaze-com/llms/arsaze-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arsaze-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/arsaze-com/mcp/arsaze-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arsaze-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/arsaze-com/well-known/arsaze-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arsaze-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/arsaze-com/hosts/arsaze-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arsaze-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arsaze-com/vendors/arsaze-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arsaze-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arsaze.com/tos
- group: start
  title: ''
  type: Login
  url: https://www.arsaze.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.arsaze.com/docs/skills
- group: auth
  href: https://artifacts.apis.io/arsaze-com/security/arsaze-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arsaze-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arsaze.com/
- group: company
  title: ''
  type: Blog
  url: https://www.arsaze.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.arsaze.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arsaze.com/privacy
coverage:
  checked: '2026-11-02'
  detail: The public documentation at https://www.arsaze.com/docs/skills provides human‑readable information but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable specification.
  evidence:
  - status: 200
    url: https://www.arsaze.com/docs/skills
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Arsaze is an AI-native video editor for agents and humans. It provides a cursor-like interface for video editing, enabling AI-driven multi-track timeline edits, versioned changes, and client review on exact frames.
image: https://www.arsaze.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.arsaze.com requiring OAuth.
  name: Arsaze MCP Server
  slug: arsaze-com-mcp-yml
modified: '2026-11-01'
name: Arsaze
nav: Providers
network: true
overview: 'Arsaze is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Video Editing, Automation, Productivity, and Media.


  Arsaze''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Arsaze Com Plans Pricing
  plan_count: 1
  slug: arsaze-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Arsaze Com Rate Limits
  slug: arsaze-com-rate-limits
scopes:
- name: Arsaze Com Scopes
  scope_count: 0
  slug: arsaze-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 12.4
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 24.3
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arsaze Com Authentication
  slug: arsaze-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arsaze Com Domain Security
  slug: arsaze-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arsaze-com
tags:
- Artificial Intelligence
- Video Editing
- Automation
- Productivity
- Media
website: https://www.arsaze.com/
---
