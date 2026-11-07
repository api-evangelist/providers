---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 8.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Optional JSON document store at api.demo.st - collections and records scoped to a site API key - that a static site published on demo.st can call from the browser. The homepage says to embed the key f
  name: demo.st Document API
  slug: document-api
- description: Remote MCP server (streamable HTTP, POST) for AI coding agents to check subdomain availability, reserve and release subdomains, upload or clear a static site, manage the site API key, and manage docum
  name: demo.st MCP Server
  slug: mcp-server
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/demo-st/conventions/demo-st-conventions.yml
  title: ''
  type: Conventions
  url: conventions/demo-st-conventions.yml
- group: auth
  href: https://artifacts.apis.io/demo-st/authentication/demo-st-authentication.yml
  title: ''
  type: Authentication
  url: authentication/demo-st-authentication.yml
- group: design
  href: https://artifacts.apis.io/demo-st/lifecycle/demo-st-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/demo-st-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/demo-st/mcp/demo-st-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/demo-st-mcp.yml
- group: other
  href: https://artifacts.apis.io/demo-st/hosts/demo-st-hosts.yml
  title: ''
  type: Hosts
  url: hosts/demo-st-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Reload
- group: auth
  href: https://artifacts.apis.io/demo-st/security/demo-st-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/demo-st-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://demo.st/
- group: docs
  title: ''
  type: Documentation
  url: https://demo.st/mcp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://demo.st/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://demo.st/privacy
created: '2026-11-05'
description: 'demo.st is a "demo stage for vibe-coded prototypes": a hosting service that lets people who build prototypes with AI coding agents (Cursor, Bolt, Claude Desktop and similar) reserve a subdomain such as project-name.demo.st and publish a static site (a zip of HTML, CSS and JS, up to 10MB) without DevOps. It is MCP-native - agents connect to its MCP endpoint with a bearer token to reserve subdomains and upload sites - and it offers an optional document API at api.demo.st/v1 that a published static site can call with a per-site API key (dk_...).'
image: https://demo.st/favicon.svg
layout: provider
mcp_servers:
- description: Official remote MCP server for demo.st. Tool list below is the verbatim result of a live tools/list call (JSON-RPC initialize + tools/list against the endpoint advertised at https://demo.st/.well-know
  name: demo.st MCP Server
  slug: demo-st
modified: '2026-11-05'
name: demo.st
nav: Providers
network: true
overview: 'demo.st is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hosting, Static Site Hosting, Prototyping, and MCP.


  demo.st''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Demo St Plans Pricing
  plan_count: 0
  slug: demo-st-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Demo St Rate Limits
  slug: demo-st-rate-limits
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Demo St Authentication
  slug: demo-st-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Demo St Domain Security
  slug: demo-st-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: demo-st
tags:
- Company
- Hosting
- Static Site Hosting
- Prototyping
- MCP
- AI Agents
- Developer Tools
- Document-Api
website: https://demo.st/
---
