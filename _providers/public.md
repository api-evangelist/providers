---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.7
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST API for programmatic trading on Public — manage brokerage accounts, pull portfolio and transaction history, retrieve market data (quotes, bars, option chains, greeks), and place, replace, and can
  name: Public Trading API
  slug: public-trading-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/public-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://public.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://public.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://public.com/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://public.com/api/docs/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/public-changelog.yml
- group: start
  title: ''
  type: SignUp
  url: https://public.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://public.com/disclosures/fee-schedule
- group: commercial
  title: ''
  type: TermsOfService
  url: https://public.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://public.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.public.com
- group: company
  title: ''
  type: Blog
  url: https://public.com/learn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PublicDotCom
- group: build
  title: ''
  type: Packages
  url: packages/public-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/public-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/public-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/public-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/public-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/public-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/public-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/public-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/public-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/public-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/public-lifecycle.yml
- group: build
  title: ''
  type: Postman
  url: https://github.com/PublicDotCom/postman-collection
created: '2026-07-17'
description: Public (Public Holdings, Inc.) is a multi-asset investing platform where people can trade stocks, ETFs, options, index options, crypto, bonds, and treasuries, and hold IRAs, direct indexing, high-yield cash, and margin in one account. Public positions itself as an "agentic brokerage" and ships a public Trading API (api.public.com) that lets developers programmatically manage accounts, pull market data, and place equity, crypto, and options orders with commission-free execution and options rebates. It also operates a hosted, OAuth-secured MCP server (mcp.public.com) so AI assistants like Claude and ChatGPT can query portfolios and trade on a user's behalf, alongside an official Python SDK, command-line interface, and Postman collection. Backed by Accel.
image: https://public.com/favicon.ico
layout: provider
mcp_servers:
- description: Public's hosted, remote MCP server — described by Public as part of "the world's first agentic brokerage." Lets AI assistants query portfolios and place trades on a connected Public account across sto
  name: Public MCP Server
  slug: public-mcp-server
modified: '2026-07-20'
name: Public
nav: Providers
network: true
overview: 'Public publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Investing, Brokerage, and Trading.


  Public''s developer surface includes documentation, getting-started guide, changelog, signup flow, pricing, support, engineering blog, and 18 more developer resources.'
random_paper: 9
scopes:
- name: Public Scopes
  scope_count: 4
  slug: public-scopes
  summary_line: 4 scopes
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 38.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/public/refs/heads/main/screenshots/public-2026-09-02T152315.png
security:
- kind: authentication
  name: Public Authentication
  slug: public-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Public Domain Security
  slug: public-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: public
tags:
- Company
- Consumer
- Investing
- Brokerage
- Trading
- Fintech
- Stocks
- Options
- Crypto
- Market Data
- Agentic
- MCP
website: https://public.com
---
