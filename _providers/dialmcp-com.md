---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted remote MCP server (Streamable HTTP, OAuth 2.1 with SMS verification) exposing four documented tools (place_call, get_call, end_call, list_calls) so AI agents can place and track real outbound p
  name: DialMCP MCP Server
  slug: dialmcp-mcp-server
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/dialmcp-com/rate-limits/dialmcp-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dialmcp-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dialmcp-com/plans/dialmcp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dialmcp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dialmcp-com/conventions/dialmcp-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dialmcp-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dialmcp-com/authentication/dialmcp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dialmcp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dialmcp-com/lifecycle/dialmcp-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dialmcp-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dialmcp-com/errors/dialmcp-com-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/dialmcp-com-error-codes.yml
- group: design
  href: https://artifacts.apis.io/dialmcp-com/conformance/dialmcp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dialmcp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dialmcp-com/llms/dialmcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dialmcp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dialmcp-com/mcp/dialmcp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dialmcp-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dialmcp-com/well-known/dialmcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dialmcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dialmcp-com/hosts/dialmcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dialmcp-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/dialmcp-com/integrations/dialmcp-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dialmcp-com-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/dialmcp-com/vendors/dialmcp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dialmcp-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/dialmcp-com/packages/dialmcp-com-packages.yml
  title: ''
  type: SDKs
  url: packages/dialmcp-com-packages.yml
- group: build
  href: https://artifacts.apis.io/dialmcp-com/packages/dialmcp-com-packages.yml
  title: ''
  type: Packages
  url: packages/dialmcp-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/dialmcp-com/security/dialmcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dialmcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dialmcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dialmcp.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dialmcp.com/docs/tools
- group: start
  title: ''
  type: GettingStarted
  url: https://dialmcp.com/docs/install
- group: commercial
  title: ''
  type: Pricing
  url: https://dialmcp.com/free
- group: company
  title: ''
  type: Blog
  url: https://dialmcp.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SkillfulAgents
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dialmcp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dialmcp.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: https://dialmcp.com/llms.txt
created: '2026-11-05'
description: DialMCP is a hosted remote Model Context Protocol (MCP) server that lets Claude, Codex, ChatGPT, Cursor and other MCP-enabled AI agents place real outbound phone calls to US and Canadian numbers on a user's behalf, from the user's own SMS-verified caller ID. Calls are asynchronous (place_call returns a call ID, get_call returns progress, transcript, recording link and a structured outcome) and the voice agent is disclosure-first with anti-abuse limits. It is reached at https://mcp.dialmcp.com/mcp over Streamable HTTP with OAuth 2.1, offers an MIT-licensed stdio bridge for local-only clients, and is built by Datawizz Inc., the makers of Gamut. It is free during launch.
image: https://dialmcp.com/og-preview.jpg
layout: provider
mcp_servers:
- description: Hosted remote MCP server that lets MCP-enabled AI agents place real outbound phone calls to US and Canadian numbers from the user's own SMS-verified caller ID. Calls are asynchronous; four tools are d
  name: DialMCP MCP Server
  slug: dialmcp-mcp-server
modified: '2026-11-05'
name: DialMCP
nav: Providers
network: true
overview: 'DialMCP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, AI Agents, Phone Calls, and Voice AI.


  DialMCP''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Dialmcp Com Plans Pricing
  plan_count: 1
  slug: dialmcp-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 7
  name: Dialmcp Com Rate Limits
  slug: dialmcp-com-rate-limits
scopes:
- name: Dialmcp Com Scopes
  scope_count: 0
  slug: dialmcp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 71.7
    operational_transparency: 36.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dialmcp Com Authentication
  slug: dialmcp-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dialmcp Com Domain Security
  slug: dialmcp-com-domain-security
  summary_line: TLSv1.3
slug: dialmcp-com
tags:
- Company
- MCP
- AI Agents
- Phone Calls
- Voice AI
- Telephony
website: https://dialmcp.com/
---
