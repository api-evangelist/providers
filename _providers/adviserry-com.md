---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 16.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Adviserry MCP API provides programmatic access to newsletter and YouTube panel data via a JSON-RPC interface.
  name: Adviserry MCP
  slug: adviserry-mcp
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/adviserry-com/rate-limits/adviserry-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adviserry-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/adviserry-com/plans/adviserry-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adviserry-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/adviserry-com/authentication/adviserry-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adviserry-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/adviserry-com/llms/adviserry-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adviserry-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/adviserry-com/mcp/adviserry-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adviserry-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adviserry-com/well-known/adviserry-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adviserry-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adviserry-com/hosts/adviserry-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adviserry-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adviserry-com/vendors/adviserry-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adviserry-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://adviserry.com/blog/tag/pricing
- group: auth
  href: https://artifacts.apis.io/adviserry-com/security/adviserry-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adviserry-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adviserry.com/
- group: docs
  title: ''
  type: Documentation
  url: https://adviserry.com/docs/mcp
- group: company
  title: ''
  type: Blog
  url: https://adviserry.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adviserry.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://adviserry.com/signup
- group: start
  title: ''
  type: Login
  url: https://adviserry.com/login
- group: operate
  title: ''
  type: Support
  url: mailto:support@adviserry.com
coverage:
  checked: '2026-11-01'
  detail: Public documentation exists but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://adviserry.com/docs/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Adviserry offers an AI‑powered advisory panel that turns the experts you follow into actionable insights. By aggregating newsletters, YouTube transcripts, and other expert content, Adviserry reads and summarizes the information, weighs it against your projects, and drafts weekly recommended actions. The service provides a free 14‑day trial and aims to help users make informed decisions without manual research.
image: https://adviserry.com/opengraph-image?691e35124db1eace
layout: provider
mcp_servers:
- description: Remote MCP server at adviserry.com requiring an API key.
  name: Adviserry MCP Server
  slug: adviserry-com-mcp-yml
modified: '2026-10-31'
name: Adviserry
nav: Providers
network: true
overview: 'Adviserry is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Advisory, Newsletters, Knowledge Base, and Productivity.


  Adviserry''s developer surface includes authentication, pricing, documentation, engineering blog, signup flow, support, and 11 more developer resources.'
plans:
- name: Adviserry Com Plans Pricing
  plan_count: 3
  slug: adviserry-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Adviserry Com Rate Limits
  slug: adviserry-com-rate-limits
scopes:
- name: Adviserry Com Scopes
  scope_count: 0
  slug: adviserry-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 29.4
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adviserry Com Authentication
  slug: adviserry-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adviserry Com Domain Security
  slug: adviserry-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adviserry-com
tags:
- Artificial Intelligence
- Advisory
- Newsletters
- Knowledge Base
- Productivity
- Automation
website: https://adviserry.com/
---
