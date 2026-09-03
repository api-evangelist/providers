---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.7
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: RESTful enterprise API for real-time private market data across 6,000+ companies - Notice Price, verified trades and indications of interest - retrievable up to once per minute. Sold as a 12-month ent
  name: Notice API
  slug: notice-api
- description: Live remote Model Context Protocol server for Notice, discovered by probe. Anonymous JSON-RPC calls return an RFC 9728-linked 401 challenge; the tool list requires an authenticated Notice OAuth sessio
  name: Notice MCP Server
  slug: notice-mcp-server
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notice-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://notice.co
- group: docs
  title: ''
  type: Documentation
  url: https://learn.notice.co/en/
- group: operate
  title: ''
  type: Support
  url: https://learn.notice.co/en/articles/8590059-how-do-i-get-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/notice-co
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/notice-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/notice-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/notice-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/notice-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/notice-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/notice-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/notice-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/notice-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/notice-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/notice-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/notice-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/notice-components.yml
created: '2026-08-26'
description: Notice (notice.co) is a private-market data and investing platform founded in 2021 by Philip West and Tyson Hendricksen and headquartered in Wilmington, Delaware. It publishes Notice Price, a real-time evaluated price for private company stock recomputed every three seconds from private market transactions, indications of interest and public comparables, alongside company profiles, rankings, industry screeners and the Notice.co 50 Index (N50) covering 6,000+ private companies. Its commercial surface is a RESTful enterprise API that imports that same real-time data - Notice Price, verified trades and indications of interest - into a subscriber's own systems, plus a live OAuth-protected MCP server at api.notice.co/mcp and a free embeddable chart widget. Notice shares trade on secondary marketplaces including Forge and Nasdaq Private Market.
layout: provider
mcp_servers:
- description: ''
  name: Notice MCP Server
  slug: notice-mcp-server
modified: '2026-08-26'
name: Notice
nav: Providers
network: true
overview: 'Notice publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Private Markets, Market Data, Financial Data, and Investing.


  Notice''s developer surface includes documentation, support, authentication, changelog, and 13 more developer resources.'
plans:
- name: Notice Plans Pricing
  plan_count: 3
  slug: notice-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Notice Rate Limits
  slug: notice-rate-limits
scopes:
- name: Notice Scopes
  scope_count: 0
  slug: notice-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 60.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 29.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 55.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/notice/refs/heads/main/screenshots/notice-2026-09-02T150805.png
security:
- kind: authentication
  name: Notice Authentication
  slug: notice-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Notice Domain Security
  slug: notice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: notice
tags:
- Company
- Private Markets
- Market Data
- Financial Data
- Investing
- Pre-IPO
- Secondary Markets
- Valuations
- Fintech
- MCP
website: https://notice.co
---
