---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
- description: Runlane provides an API accessible via its MCP endpoint; documentation is not publicly available.
  name: Runlane API
  slug: runlane-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/runlane-run/plans/runlane-run-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/runlane-run-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/runlane-run/llms/runlane-run-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/runlane-run-llms.txt
- group: agent
  href: https://artifacts.apis.io/runlane-run/mcp/runlane-run-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/runlane-run-mcp.yml
- group: other
  href: https://artifacts.apis.io/runlane-run/hosts/runlane-run-hosts.yml
  title: ''
  type: Hosts
  url: hosts/runlane-run-hosts.yml
- group: other
  href: https://artifacts.apis.io/runlane-run/vendors/runlane-run-vendors.yml
  title: ''
  type: Vendors
  url: vendors/runlane-run-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://runlane.run/login
- group: auth
  href: https://artifacts.apis.io/runlane-run/security/runlane-run-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/runlane-run-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://runlane.run/
- group: commercial
  title: ''
  type: Pricing
  url: https://runlane.run/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runlane.run/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runlane.run/privacy
coverage:
  checked: '2026-10-31'
  detail: The API is gated behind authentication; the MCP endpoint returns 401 and the GraphQL endpoint redirects to a login page.
  evidence:
  - status: 401
    url: https://runlane.run/api/mcp
  - status: 307
    url: https://runlane.run/api/graphql
  reason: auth-required
  state: gated
created: '2026-10-31'
description: Runlane is a web‑based task tracker designed for solo developers and AI‑assisted coding agents. It lets developers capture ideas, create project backlogs, and delegate work to Claude Code or other agents. The platform offers a free tier with AI credits, supports multiple languages, and provides a clean, minimalist UI for managing many projects in one place.
image: https://runlane.run/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at runlane.run.
  name: runlane-run MCP Server
  slug: runlane-run-mcp-yml
modified: '2026-10-31'
name: runlane-run
nav: Providers
network: true
overview: 'runlane-run is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Productivity, Task Management, Solo Developers, and AI Integration.


  runlane-run''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Runlane Run Plans Pricing
  plan_count: 5
  slug: runlane-run-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Runlane Run Rate Limits
  slug: runlane-run-rate-limits
scopes:
- name: Runlane Run Scopes
  scope_count: 0
  slug: runlane-run-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 22.2
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/runlane-run/runlane-run-2026-11-03T142537.png
security:
- kind: authentication
  name: Runlane Run Authentication
  slug: runlane-run-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Runlane Run Domain Security
  slug: runlane-run-domain-security
  summary_line: TLSv1.3 · DMARC
slug: runlane-run
tags:
- Company
- Productivity
- Task Management
- Solo Developers
- AI Integration
- Project Management
website: https://runlane.run/
---
