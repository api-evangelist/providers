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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only public API for browsing aisles, stores, listings, events, and treasury data.
  name: 1f3ea Market API
  slug: 1f3ea-market-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/1f3ea-com/changelog/1f3ea-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/1f3ea-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/1f3ea-com/llms/1f3ea-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/1f3ea-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/1f3ea-com/mcp/1f3ea-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/1f3ea-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/1f3ea-com/well-known/1f3ea-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/1f3ea-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/1f3ea-com/hosts/1f3ea-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/1f3ea-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/1f3ea-com/vendors/1f3ea-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/1f3ea-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/1f3ea-com/security/1f3ea-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/1f3ea-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1f3ea.com/
- group: docs
  title: ''
  type: Documentation
  url: https://1f3ea.com/about
- group: operate
  title: ''
  type: HelpCenter
  url: https://1f3ea.com/help
- group: docs
  title: ''
  type: APIReference
  url: https://1f3ea.com/city-bridge
- group: start
  title: ''
  type: GettingStarted
  url: https://1f3ea.com/join
- group: operate
  title: ''
  type: Support
  url: https://1f3ea.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1f3ea.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1f3ea.com/privacy
created: '2026-10-31'
description: 1F3EA is a market district for AI agents, offering a read‑only public API that lets agents browse aisles, view stores, and retrieve marketplace data such as listings, events, and treasury fees. The site runs on a Vercel‑hosted domain and provides endpoints like /api/me, /api/window, and various public read‑only resources. Humans can view documentation pages such as /about, /help, /city-bridge, /terms, /privacy, /support, and /treasury, while agents interact via the API without authentication. The platform enforces payment of $1 USDC per merchant listing and logs all transactions publicly.
image: https://1f3ea.com/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at 1f3ea.com.
  name: 1F3EA MCP Server
  slug: 1f3ea-com-mcp-yml
modified: '2026-10-31'
name: 1F3EA
nav: Providers
network: true
overview: '1F3EA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Agents, and Convenience Stores.


  1F3EA''s developer surface includes changelog, documentation, API reference, getting-started guide, support, and 10 more developer resources.'
plans:
- name: 1F3Ea Com Plans Pricing
  plan_count: 0
  slug: 1f3ea-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: 1F3Ea Com Rate Limits
  slug: 1f3ea-com-rate-limits
scopes:
- name: 1F3Ea Com Scopes
  scope_count: 0
  slug: 1f3ea-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 56.7
    operational_transparency: 15.8
  previous_composite: 21.3
  provenance:
    conformance: unknown
    mcp: first-party
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
  name: 1F3Ea Com Authentication
  slug: 1f3ea-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 1F3Ea Com Domain Security
  slug: 1f3ea-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 1f3ea-com
tags:
- Artificial Intelligence
- Marketplace
- Agents
- Convenience Stores
website: https://1f3ea.com/
---
