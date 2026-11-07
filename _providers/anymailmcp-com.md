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
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted email MCP server for any IMAP mailbox
  name: anymailmcp
  slug: anymailmcp
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/anymailmcp-com/rate-limits/anymailmcp-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anymailmcp-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/anymailmcp-com/plans/anymailmcp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anymailmcp-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/anymailmcp-com/llms/anymailmcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anymailmcp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/anymailmcp-com/mcp/anymailmcp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anymailmcp-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anymailmcp-com/well-known/anymailmcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anymailmcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anymailmcp-com/hosts/anymailmcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anymailmcp-com-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://anymailmcp.com/providers/register-it
- group: auth
  href: https://artifacts.apis.io/anymailmcp-com/security/anymailmcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anymailmcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anymailmcp.com/
- group: company
  title: ''
  type: Blog
  url: https://anymailmcp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://anymailmcp.com/#pricing
coverage:
  checked: '2026-11-01'
  detail: MCP endpoint requires authentication, returning 401 when accessed without credentials.
  evidence:
  - status: 405
    url: https://anymailmcp.com/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: anymailmcp provides a hosted email MCP (Model Context Protocol) server that connects any IMAP mailbox and CalDAV calendar to AI assistants like Claude, ChatGPT, Grok, and Vibe. It enables AI to read, draft, send emails, and manage calendars directly from chat, offering a free tier for a single mailbox with 150 calls per month and paid plans for higher usage. The service encrypts passwords, supports many IMAP providers, and integrates calendar via CalDAV, making AI‑driven email handling seamless and secure.
image: https://anymailmcp.com/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at anymailmcp.com.
  name: anymailmcp MCP Server
  slug: anymailmcp-com-mcp-yml
modified: '2026-11-01'
name: anymailmcp
nav: Providers
network: true
overview: 'anymailmcp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email, MCP, Artificial Intelligence, Hosted, and IMAP.


  anymailmcp''s developer surface includes signup flow, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Anymailmcp Com Plans Pricing
  plan_count: 3
  slug: anymailmcp-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Anymailmcp Com Rate Limits
  slug: anymailmcp-com-rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 20.2
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anymailmcp Com Domain Security
  slug: anymailmcp-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: anymailmcp-com
tags:
- Email
- MCP
- Artificial Intelligence
- Hosted
- IMAP
website: https://anymailmcp.com/
---
